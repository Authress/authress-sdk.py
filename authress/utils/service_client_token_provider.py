# coding: utf-8


from __future__ import absolute_import

import datetime
import json
from urllib.parse import quote, urlencode, urlparse, parse_qs, urlunparse
import jwt
import base64
import json

class ServiceClientTokenProvider(object):
  def __init__(self, access_key, authress_api_url=None):
    self.token = None
    self.decoded_access_key = None
    self.account_id = None
    self.authress_api_url = authress_api_url
    
    if access_key:
      try:
        self.decoded_access_key = json.loads(base64.b64decode(access_key))
        self.account_id = self.decoded_access_key['audience'].split('.')[0]
        self.algorithm = 'RS256'
      except:
        self.account_id = access_key.split('.')[2]
        self.decoded_access_key = {
          'clientId': access_key.split('.')[0],
          'keyId': access_key.split('.')[1],
          'audience': f"{self.account_id}.accounts.authress.io",
          'privateKey': f"-----BEGIN PRIVATE KEY-----\n{access_key.split('.')[3]}\n-----END PRIVATE KEY-----"
        }
        self.algorithm = 'EdDSA'


  def get_client_token(self) -> str:
    if self.decoded_access_key is None:
      return None

    current_token_is_valid = False
    try:
      current_token_is_valid = self.token is not None and jwt.decode(
        self.token, options={"verify_signature": False})['exp'] > (datetime.datetime.utcnow() + datetime.timedelta(seconds=3600)).timestamp()
    except jwt.ExpiredSignatureError:
      current_token_is_valid = False

    if current_token_is_valid is not False:
      return self.token

    issuer_origin = f"https://{self.account_id}.api.authress.io" if (self.authress_api_url == None or self.authress_api_url == '' or '.authress.io' in self.authress_api_url) else self.authress_api_url

    payload = {
      'iss': f"{issuer_origin}/v1/clients/{quote(self.decoded_access_key['clientId'], safe='')}",
      'aud': self.decoded_access_key['audience'],
      'iat': datetime.datetime.utcnow(),
      'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=86400),
      'sub': self.decoded_access_key['clientId'],
      'client_id': self.decoded_access_key['clientId'],
      'scopes': 'openId'
    }

    jwt_token = jwt.encode(payload, self.decoded_access_key['privateKey'], algorithm=self.algorithm, headers={'kid': self.decoded_access_key['keyId'] })
    self.token = jwt_token if isinstance(jwt_token, str) else jwt_token.decode("utf-8")
    return self.token

  def generate_user_login_url(self, authenticate_response, user_id):
    if not authenticate_response:
        raise ValueError('The authenticate_response is specified in the incoming login request, this should include the configured Authress custom domain.')
    
    parsed_url = urlparse(authenticate_response['authentication_url'])
    parameters = dict(parse_qs(parsed_url.query))
    authress_custom_domain_login_url = authenticate_response['authentication_url']
    client_id = parameters.get('client_id', [None])[0]
    state = parameters.get('state', [None])[0]

    if not state:
        raise ValueError('The state is required to generate a authorization code redirect for is required, and should be present in the authentication_url.')
    if not user_id:
        raise ValueError('The user to generate an authorization code redirect for is required.')
    if not client_id or client_id != self.decoded_access_key['clientId']:
        raise ValueError('The client_id should be specified in the authentication_url. It should match the service client ID.')

    custom_domain_fallback = urlparse(authress_custom_domain_login_url).scheme + "://" + urlparse(authress_custom_domain_login_url).netloc
    issuer = get_issuer(self.authress_api_url or custom_domain_fallback, self.decoded_access_key)

    now = datetime.datetime.utcnow()
    payload = {
        'aud': self.decoded_access_key['audience'],
        'iss': issuer,
        'sub': user_id,
        'client_id': self.decoded_access_key['clientId'],
        'iat': int(now.timestamp()),
        'exp': int((now + datetime.timedelta(seconds=60)).timestamp()),
        'max_age': 60,
        'scope': 'openid'
    }

    if '@' in user_id:
        payload['email'] = user_id
        payload['email_verified'] = True

    code = jwt.encode(payload, self.decoded_access_key['privateKey'], algorithm=self.algorithm, headers={'kid': self.decoded_access_key['keyId'], 'typ': 'oauth-authz-req+jwt'})

    parsed_url = urlparse(authress_custom_domain_login_url)
    query_params = dict(parse_qs(parsed_url.query))
    query_params['code'] = code
    query_params['iss'] = issuer
    query_params['state'] = state

    new_query_string = urlencode(query_params, doseq=True)
    new_url = urlunparse(parsed_url._replace(query=new_query_string))
    return new_url

def get_issuer(domain, decoded_access_key):
    return f"{domain}/v1/clients/{decoded_access_key['clientId']}"