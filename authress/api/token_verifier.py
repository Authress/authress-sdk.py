# coding: utf-8

from __future__ import absolute_import
import json

import jwt
import re
from urllib.parse import urlparse

from authress import rest
from authress.api import service_client_token_provider

class TokenVerifier(object):
  def __init__(self):
    self.keyMap = dict()

  def verify_token(self, authressCustomDomain, token, options=None):
    sanitized_domain = re.sub(r"https?://", "", authressCustomDomain)
    completeIssuerUrl = f"https://{sanitized_domain}"
    if token is None:
      raise Exception("Unauthorized")

    try:
      authenticationToken = token
      unverifiedPayload = jwt.decode(authenticationToken, options={"verify_signature": False})
      headers = jwt.get_unverified_header(authenticationToken)
    except jwt.DecodeError:
      try:
        authenticationToken = service_client_token_provider.ServiceClientTokenProvider().get_client_token(token, completeIssuerUrl)
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

    if (urlparse(issuer).netloc != urlparse(completeIssuerUrl).netloc):
      raise Exception("Unauthorized", "Issuer does not match")

    # Handle service client checking
    clientIdMatcher = re.match(r"^/v\d/clients/([^/]+)$", urlparse(issuer).path)
    if (clientIdMatcher is not None and clientIdMatcher.group(1) != unverifiedPayload['sub']):
      raise Exception("Unauthorized", "Service ID does not match token sub claim")

    jwk = options['expectedPublicKey'] if options is not None and 'expectedPublicKey' in options else self.get_public_key(f"{issuer}/.well-known/openid-configuration/jwks", kid)

    try:
      return jwt.decode(authenticationToken, jwt.api_jwk.PyJWK.from_dict(jwk).key, algorithms=['EdDSA'], options = { 'verify_aud': False })
    except jwt.ExpiredSignatureError:
      raise Exception("Unauthorized", "Token is invalid")

  def get_public_key(self, jwkKeyListUrl, kid):
    hashKey = f"{jwkKeyListUrl}|{kid}"

    if hashKey in self.keyMap is not None:
      self.keyMap[hashKey] = self.get_key_uncached(jwkKeyListUrl, kid)

    try:
      key = self.keyMap[hashKey]
      return key
    except:
      self.keyMap[hashKey] = self.get_key_uncached(jwkKeyListUrl, kid)
      return self.keyMap[hashKey]

  def get_key_uncached(self, jwkKeyListUrl, kid):
    rest_client = rest.RESTClientObject()
    result = rest_client.GET(jwkKeyListUrl)

    for index, key in enumerate(json.loads(result.data)['keys']):
      if key['kid'] == kid:
          return key

    raise Exception("Unauthorized", "KID is not valid")
