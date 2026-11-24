# coding: utf-8

from __future__ import absolute_import
from datetime import datetime, timedelta
import json

import jwt
import re
from urllib.parse import urlparse

from authress import rest
from authress.utils import service_client_token_provider, PackageVersionProvider

class TokenVerifier(object):
  def __init__(self, http_client=None):
    self.http_client = http_client
    if http_client is None:
      self.http_client = rest.RESTClientObject()

    self.keyMap = dict()
    self.package_version_provider = PackageVersionProvider()

  def verify_token(self, authressCustomDomain, token, options=None):
    sanitized_domain = re.sub(r"https?://", "", authressCustomDomain).rstrip('/')
    completeIssuerUrl = f"https://{sanitized_domain}"
    if token is None:
      raise Exception("Unauthorized")

    try:
      authenticationToken = token
      unverifiedPayload = jwt.decode(authenticationToken, options={"verify_signature": False})
      headers = jwt.get_unverified_header(authenticationToken)
    except jwt.DecodeError:
      try:
        authenticationToken = service_client_token_provider.ServiceClientTokenProvider(token, completeIssuerUrl).get_client_token()
        unverifiedPayload = jwt.decode(authenticationToken, options={"verify_signature": False})
        headers = jwt.get_unverified_header(authenticationToken)
      except Exception as e:
        raise Exception("Unauthorized", f"Invalid Token format: {e}")

    if (unverifiedPayload is None):
      raise Exception("Unauthorized", "Invalid Token or Token not found")

    if (headers is None or 'kid' not in headers):
      raise Exception("Unauthorized", "No KID found in token")
    kid = headers['kid']

    if ('iss' not in unverifiedPayload['iss'] is None):
      raise Exception("Unauthorized", "No Issuer in token")
    issuer = unverifiedPayload['iss']

    canonicalIssuer = self.get_canonical_issuer(issuer)
    if canonicalIssuer is None:
      raise Exception("Unauthorized", "Issuer is not in canonical form")

    if (urlparse(issuer).netloc != urlparse(completeIssuerUrl).netloc):
      raise Exception("Unauthorized", "Issuer does not match")

    # Handle service client checking
    clientIdMatcher = re.match(r"^/v\d/clients/([^/]+)/?$", canonicalIssuer['path'])
    if (clientIdMatcher is not None and clientIdMatcher.group(1) != unverifiedPayload['sub']):
      raise Exception("Unauthorized", "Service ID does not match token sub claim")

    jwk = self.get_public_key(f"{canonicalIssuer['url']}/.well-known/openid-configuration/jwks?kid={kid}&iss={urlparse(issuer).netloc}", kid)

    try:
      return jwt.decode(authenticationToken, jwt.api_jwk.PyJWK.from_dict(jwk).key, algorithms=['EdDSA'], options = { 'verify_aud': False })
    except:
      raise Exception("Unauthorized", "Token is invalid")

  @staticmethod
  def get_canonical_issuer(issuer):
    """The service client check and the JWKS fetch must read the same issuer value. Any issuer that a runtime could normalise differently is rejected."""
    issuerMatch = None if re.search(r"[?#\\]", issuer) else re.fullmatch(r"([a-z][a-z0-9+.-]*://[^/@]+)(/.*)?", issuer, re.IGNORECASE)
    if issuerMatch is None:
      return None

    path = issuerMatch.group(2) or ""
    path = path[:-1] if path.endswith("/") else path
    segments = path[1:].split("/") if path else []
    if any(not segment or segment in (".", "..") or re.search(r"%(2e|2f|5c)", segment, re.IGNORECASE) for segment in segments):
      return None

    return { 'url': f"{issuerMatch.group(1)}{path}", 'path': path }

  def get_public_key(self, jwkKeyListUrl, kid):
    hashKey = f"{jwkKeyListUrl}|{kid}"
    
    if hashKey in self.keyMap is not None:
      try:
        keyData = self.keyMap[hashKey]
        if datetime.now() < keyData["expiry"]:
          return keyData["key"]
      except:
        self.keyMap[hashKey] = None
  
    self.keyMap[hashKey] = {
      "key": self.get_key_uncached(jwkKeyListUrl, kid),
      "expiry": datetime.now() + timedelta(hours=1)
    }
    return self.keyMap[hashKey]["key"]

  def get_key_uncached(self, jwkKeyListUrl, kid):    
    version = self.package_version_provider.get_version()
    headers = {
      'User-Agent': f'Authress SDK; Python; {version};'
    }
    result = self.http_client.request_with_retries('GET', jwkKeyListUrl, headers=headers)

    for index, key in enumerate(json.loads(result.data)['keys']):
      if key['kid'] == kid:
          return key

    raise Exception("Unauthorized", "The Service Client Access Key is not valid yet or has been deleted. For new Access Keys just created, key validation is cached and can take up to 5 minutes before new keys can be used.")
