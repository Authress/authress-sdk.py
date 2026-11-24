from __future__ import absolute_import

import base64
import time
import unittest.mock

import jwt
import pytest
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from urllib3.util import parse_url

from authress.api import token_verifier

custom_domain = 'authress.token-validation.test'
client_id = 'client_abc'

signing_key = Ed25519PrivateKey.generate()
public_key_bytes = signing_key.public_key().public_bytes(serialization.Encoding.Raw, serialization.PublicFormat.Raw)
public_jwk = {
  'alg': 'EdDSA', 'kty': 'OKP', 'crv': 'Ed25519',
  'x': base64.urlsafe_b64encode(public_key_bytes).rstrip(b'=').decode()
}

def verify_outcome(issuer_path, sub, kid, userinfo=''):
  issuer = f'https://{userinfo}{custom_domain}{issuer_path}'
  token = jwt.encode({ 'iss': issuer, 'sub': sub, 'exp': int(time.time()) + 3600 }, signing_key, algorithm='EdDSA', headers={ 'kid': kid })

  verifier = token_verifier.TokenVerifier()
  verifier.get_key_uncached = unittest.mock.MagicMock(return_value={ **public_jwk, 'kid': kid })
  try:
    return 'accepted', verifier.verify_token(f'https://{custom_domain}', token), verifier.get_key_uncached
  except Exception as error:
    return 'rejected', error, verifier.get_key_uncached

cases = [
  pytest.param(f'/v1/clients/{client_id}', client_id, 'accepted', id='service client token with its own sub'),
  pytest.param(f'/v1/clients/{client_id}', 'user_alice', 'rejected', id='service client token claiming another sub'),
  pytest.param('', 'user_alice', 'accepted', id='issuer with no path'),
  pytest.param('/tenant/custom', 'user_alice', 'accepted', id='issuer with an arbitrary non-client path'),
  pytest.param(f'/v1/clients/{client_id}/', client_id, 'accepted', id='service client with trailing slash and its own sub'),
  pytest.param(f'/v1/clients/{client_id}/', 'user_alice', 'rejected', id='service client with trailing slash claiming another sub'),
  pytest.param(f'/v1/clients/{client_id}/.', 'user_alice', 'rejected', id='trailing dot segment hides the client id'),
  pytest.param(f'/v1/./clients/{client_id}', client_id, 'rejected', id='dot segment inside the path'),
  pytest.param(f'/v1/clients/user_alice/../{client_id}', 'user_alice', 'rejected', id='parent segment redirects the client id after the sub match'),
  pytest.param(f'/v1/x/../clients/{client_id}', 'user_alice', 'rejected', id='parent segment moves the path out of the clients prefix'),
  pytest.param(f'/v1/clients/{client_id}/%2e', 'user_alice', 'rejected', id='percent-encoded dot segment'),
  pytest.param(f'/v1/clients/{client_id}\\.', 'user_alice', 'rejected', id='backslash treated as a path separator'),
  pytest.param('/v1/clients/user_alice?', 'user_alice', 'rejected', id='query appended to the issuer swallows the jwks path'),
  pytest.param(f'/v1/clients/{client_id}#', client_id, 'rejected', id='fragment appended to the issuer swallows the jwks path'),
  pytest.param('/a/b/c/d', 'user_alice', 'accepted', id='issuer with a deep non-client path'),
  pytest.param('/v1.0/tenants/acme', 'user_alice', 'accepted', id='issuer with a version-like dotted segment'),
  pytest.param('/a/b/c/', 'user_alice', 'accepted', id='issuer with deep path and trailing slash'),
  pytest.param(f'/tenant/v1/clients/{client_id}', 'user_alice', 'accepted', id='client path nested below another prefix is not a service client issuer'),
  pytest.param(f'/v1/clients/{client_id}/extra', 'user_alice', 'accepted', id='client path with extra segment is not a service client issuer'),
  pytest.param('/tenant//custom', 'user_alice', 'rejected', id='empty segment in a non-client path'),
  pytest.param(f'/v1/clients/{client_id}//', 'user_alice', 'rejected', id='double trailing slash'),
  pytest.param(f'/v1/clients/{client_id}\n', 'user_alice', 'rejected', id='trailing newline'),
  pytest.param('/tenant/a%2Fb', 'user_alice', 'rejected', id='percent-encoded slash in a segment'),
  pytest.param('/tenant/a%5cb', 'user_alice', 'rejected', id='percent-encoded backslash in a segment'),
  pytest.param('/a/b/../c', 'user_alice', 'rejected', id='parent segment in a non-client path'),
]

@pytest.mark.parametrize('issuer_path,sub,expected', cases)
def test_issuer_canonical_form(issuer_path, sub, expected):
  outcome, _, get_key_uncached = verify_outcome(issuer_path, sub, 'kid-case')
  assert outcome == expected
  if expected == 'rejected':
    get_key_uncached.assert_not_called()

def test_issuer_with_userinfo_is_rejected_without_fetching_keys():
  outcome, _, get_key_uncached = verify_outcome(f'/v1/clients/{client_id}', client_id, 'kid-userinfo', userinfo='user@')
  assert outcome == 'rejected'
  get_key_uncached.assert_not_called()

def test_jwks_is_fetched_from_the_client_path_for_a_trailing_slash_issuer_with_its_own_sub():
  outcome, _, get_key_uncached = verify_outcome(f'/v1/clients/{client_id}/', client_id, 'kid-mechanism')
  assert outcome == 'accepted'
  fetched_url = get_key_uncached.call_args[0][0]
  assert parse_url(fetched_url).path == f'/v1/clients/{client_id}/.well-known/openid-configuration/jwks'
