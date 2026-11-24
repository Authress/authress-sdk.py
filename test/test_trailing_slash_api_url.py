from __future__ import absolute_import

import unittest.mock

import jwt
import pytest

from authress.api import token_verifier
from authress.http_client import HttpClient
from authress.utils.service_client_token_provider import ServiceClientTokenProvider

custom_domain = 'authress.token-validation.test'
access_key = 'CLIENT.KEY.ACCOUNT.MC4CAQAwBQYDK2VwBCIEIDVjjrIVCH3dVRq4ixRzBwjVHSoB2QzZ2iJuHq1Wshwp'
public_key = { 'alg': 'EdDSA', 'kty': 'OKP', 'crv': 'Ed25519', 'x': 'JxtSC5tZZJuaW7Aeu5Kh_3tgCpPZRkHaaFyTj5sQ3KU' }

api_urls_with_trailing_slashes = [
  pytest.param(f'https://{custom_domain}/', id='one trailing slash'),
  pytest.param(f'https://{custom_domain}//', id='multiple trailing slashes'),
]

@pytest.mark.parametrize('api_url', api_urls_with_trailing_slashes)
def test_verifier_with_access_key_uses_an_issuer_without_empty_path_segments(api_url):
  verifier = token_verifier.TokenVerifier()
  verifier.get_key_uncached = unittest.mock.MagicMock(return_value=public_key)

  identity = verifier.verify_token(api_url, access_key)

  assert identity['iss'] == f'https://{custom_domain}/v1/clients/CLIENT'
  verifier.get_key_uncached.assert_called_once_with(f'https://{custom_domain}/v1/clients/CLIENT/.well-known/openid-configuration/jwks?kid=KEY&iss={custom_domain}', 'KEY')

@pytest.mark.parametrize('api_url', api_urls_with_trailing_slashes)
def test_service_client_token_provider_issuer_has_no_trailing_slash_from_the_api_url(api_url):
  token = ServiceClientTokenProvider(access_key, api_url).get_client_token()

  assert jwt.decode(token, options={ 'verify_signature': False })['iss'] == f'https://{custom_domain}/v1/clients/CLIENT'

@pytest.mark.parametrize('api_url', api_urls_with_trailing_slashes)
def test_http_client_host_has_no_trailing_slash(api_url):
  assert HttpClient(host=api_url).host == f'https://{custom_domain}'
