# coding: utf-8


from __future__ import absolute_import

import datetime
import json
from urllib.parse import quote, urlencode
import jwt
import base64
import json

class ServiceClientTokenProvider(object):
  def __init__(self):
    self.token = None

  def get_client_token(self, access_key, host=None) -> str:
    if access_key is None:
      return None

    current_token_is_valid = False
    try:
      current_token_is_valid = self.token is not None and jwt.decode(
        self.token, options={"verify_signature": False})['exp'] > (datetime.datetime.utcnow() + datetime.timedelta(seconds=3600)).timestamp()
    except jwt.ExpiredSignatureError:
      current_token_is_valid = False

    if current_token_is_valid is not False:
      return self.token

    try:
      decoded_access_key = json.loads(base64.b64decode(access_key))
      account_id = decoded_access_key['audience'].split('.')[0]
      algorithm = 'RS256'
    except:
      account_id = access_key.split('.')[2]
      decoded_access_key = {
        'clientId': access_key.split('.')[0],
        'keyId': access_key.split('.')[1],
        'audience': f"{account_id}.accounts.authress.io",
        'privateKey': f"-----BEGIN PRIVATE KEY-----\n{access_key.split('.')[3]}\n-----END PRIVATE KEY-----"
      }
      algorithm = 'EdDSA'

    issuer_origin = f"https://{account_id}.api.authress.io" if (host == None or host == '' or '.authress.io' in host) else host

    payload = {
      'iss': f"{issuer_origin}/v1/clients/{quote(decoded_access_key['clientId'], safe='')}",
      'aud': decoded_access_key['audience'],
      'iat': datetime.datetime.utcnow(),
      'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=86400),
      'sub': decoded_access_key['clientId'],
      'scopes': 'openId'
    }

    jwt_token = jwt.encode(payload, decoded_access_key['privateKey'], algorithm=algorithm, headers={'kid': decoded_access_key['keyId'] })
    self.token = jwt_token if isinstance(jwt_token, str) else jwt_token.decode("utf-8")
    return self.token
