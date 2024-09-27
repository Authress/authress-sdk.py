from __future__ import absolute_import

import unittest
import time

from authress.models import *
from authress.utils import ServiceClientTokenProvider, JwtManager
from authress import AuthressClient

import unittest
from unittest.mock import patch
from urllib.parse import urlparse, parse_qs

class ServiceClientTokenProviderTest(unittest.TestCase):
  def setUp(self):
    pass

  def tearDown(self):
    pass

  def test_get_token(self):
    """Test case for get_token

    Get the token for a client registered as the token provider
    """

    access_key = 'eyJrZXlJZCI6ImNjYjFjZGJmLTM0NzYtNGNiNy05Njc1LTVlMzNmYjI5NTNjMyIsInByaXZhdGVLZXkiOiItLS0tLUJFR0lOIFBSSVZBVEUgS0VZLS0tLS1cbk1JSUV2Z0lCQURBTkJna3Foa2lHOXcwQkFRRUZBQVNDQktnd2dnU2tBZ0VBQW9JQkFRRFFidWFBd0V6VkJHZnZcbjBEL2JKSjRHa2JoV2oyRy9lYTF3UUZNeWxiK0ZzTDM1dGJvVHNIUGdvbUtGMDNNQkphWmRBVHhwcnhYa2xvYWNcblFhYkE4eXcyQ2lFbitHNjlMcUFnUVlLSmZzL1psWEo4MVJ0TkR0TkZRUTdPS0xpSGJrU1I1cFU3R0lKNENQZTZcbkxHM3UzUkVUbFFndmlhV2M2bzVOUkRMWTBIbzhya2w0Yk8rZjMycXg2SGV6dzBsUnZOK1I4L24vZUxLbCtGVlpcbk1yYzFkcmh5NDdtVU80ZnJKWW1LSzg2ZGZacVk4RVh2aGpjaFZzdHhSTXdtMlRDbUtWT2xsQWUrandmNTR5Q2NcbnUzcTNsRUxzcnhXTlRsVC9mRHBQQSt6MDh2MFdDa2ozdWo5SEh3REE1VjhZaUtJOEFheWRLSG9nYnA5eHp1amdcbnZwQmVacnRuQWdNQkFBRUNnZ0VBZnRpL0Z1UHcza0tNTG5vQ0lvK3FURDBxZmlOTVRZYnpjamp6YVBtUlVQODZcbjNsa21JUTFsdC9PYkdlNlJNc1dDOVY3bk1Ub0lqTkMrb3lHaEpoUFhlQnU2Q2VVN0g0N2NqRVRSK0hOZ2N2NXNcbmFtUVc5VkpzYU4wcThYUCt1UXoyVmdTS0ZTalpYY3UzVjJucWpVK2tNTktsNUtoVVRhYkJhMnh4dFZsS3l0bjlcbld6QnIzZExLVXBwYzdoZXFaa2diSHE2amZXd3h2Vk56cmhkNUZ1Tm5EeWI2R3QrUXhzYi83dmdhdnRsNmtXM0hcbnU5ZUtGcjJhdER4VHhaTDArRVIxWjVyV21MNzdUK3owQitYVkZJZ05ia2FlSURBZjEzRjBPSzE3YjJ4NmlSSjVcbnJCRTdCc0ZhMGVuOXBjSWN2UUxhbGFMREVOL1d2YWd4dnowSWZ4M1R3UUtCZ1FEbjVMSGhFczBzeWxYVUdrVlFcbmhFU1ZacGh5QzdFRHBZYm44UW5DNkI3ZDFtWkR1d1JuSkMyZXVxT1lNMFlVcWlGT3Q5RW9UMllNQy9jT2pUVTFcbndnMm9GQ0hqWUI4cGptNHVkb3B3MHRHcGRyb1piQVNkOHkzR1RuNitMK25tVGVzNjYxTGN6ekhSekhrTnh5OUJcbkNVNTRzWXhnK1M5bnhSTjdEVERxeTE2M1dRS0JnUURtR2Q1Snl4VnNyS3ZVSmFVbDM5ekZRcTh3cnpTZ0xZVVBcbjF0a1dHYWhIanFvRjYvSnM2YUZnZlYraXl5THk1dm03WEN0dUw2RGtEQW93NnVpS1NiRlhicnVCYW5GSDBnWktcbkRaVmVQcU9mbTVIYWJWalB1VmdPdW5HWHBOMnZ4QTdwNkg0SkMxOVkvUkg0MkY5bHE4aUtkejZXWHJYMjNPRHFcbjQrcHZtdzF3dndLQmdRQ0YyajlHNExobjR6OFptRFJzWG56TUZCVm90eER0UHUyWkVrd0ZJa0UyNFp2VCtxNTJcbjdxNGFramIrRXBLZ09QZlMzVTJ3eSt2bWhqMk1PN3Y4Rk5BWE5jKzkxRzBJYXJ0MHZGMzY4K1dyd09sNDVSM2hcbklrNUl5bVJrV1huVXd5TkZ0akgxWE8rdjN5djg1UDJFdDkrQTBWTnJZa3FYeG0wUk9UTUVSSEdldVFLQmdEZmdcbnNrMkRSc21rU1BuMHhsMGpOdTZrV2Z6ZG4wOENudHlRMVJqNzFCVEVmVitBdzlkVkNQNXdrOGZwd3F2d0VWZEJcbmM3NkhURy8weUlqR2t2LzZFMW5qSngrdlpLRUhUTVd3OU1QMVBERG5TNDBhbnNXYkFkcFp4bm9IN0ZuaHA2bC9cbjd4TnRNcE5lcVgyZnRkTHYyM3hjcHROSFhyTDdRcGRvRDZkWXBQUHJBb0dCQU5CN2QyME5kY1EzaTBmWGJ6dGhcbk1RUFIwK3NEVkViMUZjSUdXbDdPeXNvYy9UZ2prT3NhVDRTL2hXODg1RGR5ZnZHbjdpRmpyMDBPQVVyVjE5NlRcbmFwdDJNS0EvWVdWeG9Ud2kwZCs0UHZ5Mnk3SXBnMk9tcEE0bVliYnBXQ0NPS3dtczlEQ0E4MVVGeEJiMHdUbTdcbjlXVStVbGZMWDAvcGNkSFNEZkExbXVjZVxuLS0tLS1FTkQgUFJJVkFURSBLRVktLS0tLVxuIiwiYXVkaWVuY2UiOiIyMmJiYzUwMi0zYjdhLTRjNTQtOGE2ZS1jMDRhM2NhNGRmNWYuYWNjb3VudHMuYXV0aHJlc3MuaW8iLCJjbGllbnRJZCI6IjIzYjRiY2Q1LWMwYzEtNDYwMi05NGU1LThkYTgyNzNkMGRiMCJ9'

    service_client_token_provider = ServiceClientTokenProvider(access_key, "")
    token1 = service_client_token_provider.get_client_token()
    time.sleep(2)
    token2 = service_client_token_provider.get_client_token()
    assert token1 == token2
    pass

  def test_get_token_for_eddsa(self):
    """Test case for get_token for EdDsa

    Get the token for a client registered as the token provider
    """

    access_key = 'CLIENT.KEY.ACCOUNT.MC4CAQAwBQYDK2VwBCIEIIM7npIckfT431rYzEeF+hCqvHogpOllmVSgINwqQv+g'

    service_client_token_provider = ServiceClientTokenProvider(access_key, "")
    token1 = service_client_token_provider.get_client_token()
    time.sleep(2)
    token2 = service_client_token_provider.get_client_token()
    assert token1 == token2
    pass

  def test_get_token_without_access_key(self):
    """Test case for get_token with no access key

    Ignores access keys that are None
    """

    service_client_token_provider = ServiceClientTokenProvider("")
    token1 = service_client_token_provider.get_client_token()
    assert token1 == None
    pass

  def test_should_correctly_parse_parameters_from_authentication_url_object(self):
      access_key = 'clientId.uDeF.a43706ca-9647-40e4-aeae-7dcaa54bbab3.MC4CAQAwBQYDK2VwBCIEIE99LFw2c3DCiYwrY/Qkg1nIDiagoHtdCwb88RxarVYA'
      token_provider = ServiceClientTokenProvider(access_key)

      url = token_provider.generate_user_login_url({'authentication_url': 'https://login.redirect-url.com?client_id=clientId&state=state'}, 'user1')
      parsed_url = urlparse(url)
      query_params = parse_qs(parsed_url.query)
      self.assertEqual(query_params['iss'][0], 'https://login.redirect-url.com/v1/clients/clientId')
      self.assertEqual(query_params['state'][0], 'state')

  def test_should_throw_error_if_state_not_provided(self):
      access_key = 'clientId.uDeF.a43706ca-9647-40e4-aeae-7dcaa54bbab3.MC4CAQAwBQYDK2VwBCIEIE99LFw2c3DCiYwrY/Qkg1nIDiagoHtdCwb88RxarVYA'
      token_provider = ServiceClientTokenProvider(access_key)

      with self.assertRaises(ValueError) as context:
          token_provider.generate_user_login_url({'authentication_url': 'https://login.redirect-url.com?client_id=clientId'}, 'user1')
      self.assertEqual(str(context.exception), 'The state is required to generate a authorization code redirect for is required, and should be present in the authentication_url.')

  def test_should_throw_error_if_client_id_does_not_match(self):
      access_key = 'clientId.uDeF.a43706ca-9647-40e4-aeae-7dcaa54bbab3.MC4CAQAwBQYDK2VwBCIEIE99LFw2c3DCiYwrY/Qkg1nIDiagoHtdCwb88RxarVYA'
      token_provider = ServiceClientTokenProvider(access_key)

      with self.assertRaises(ValueError) as context:
          token_provider.generate_user_login_url({'authentication_url': 'https://login.redirect-url.com?client_id=wrongClientId&state=state'}, 'user1')
      self.assertEqual(str(context.exception), 'The client_id should be specified in the authentication_url. It should match the service client ID.')

  def test_should_throw_error_if_user_id_not_provided(self):
      access_key = 'clientId.uDeF.a43706ca-9647-40e4-aeae-7dcaa54bbab3.MC4CAQAwBQYDK2VwBCIEIE99LFw2c3DCiYwrY/Qkg1nIDiagoHtdCwb88RxarVYA'
      token_provider = ServiceClientTokenProvider(access_key)

      with self.assertRaises(ValueError) as context:
          token_provider.generate_user_login_url({'authentication_url': 'https://login.redirect-url.com?client_id=wrongClientId&state=state'}, None)
      self.assertEqual(str(context.exception), 'The user to generate an authorization code redirect for is required.')

  def test_should_generate_url_with_correct_authorization_code_and_parameters(self):
      access_key = 'clientId.uDeF.a43706ca-9647-40e4-aeae-7dcaa54bbab3.MC4CAQAwBQYDK2VwBCIEIE99LFw2c3DCiYwrY/Qkg1nIDiagoHtdCwb88RxarVYA'
      token_provider = ServiceClientTokenProvider(access_key)

      url = token_provider.generate_user_login_url({'authentication_url': 'https://login.redirect-url.com?client_id=clientId&state=state'}, 'user1')
      parsed_url = urlparse(url)
      query_params = parse_qs(parsed_url.query)

      code = query_params['code'][0]
      self.assertIsNotNone(code)

      jwt_payload = JwtManager().decode(code)
      self.assertEqual(jwt_payload['aud'], 'a43706ca-9647-40e4-aeae-7dcaa54bbab3.accounts.authress.io')
      self.assertEqual(jwt_payload['iss'], 'https://login.redirect-url.com/v1/clients/clientId')
      self.assertEqual(jwt_payload['sub'], 'user1')
      self.assertEqual(jwt_payload['client_id'], 'clientId')
      self.assertIsInstance(jwt_payload['iat'], int)
      self.assertIsInstance(jwt_payload['exp'], int)
      self.assertEqual(jwt_payload['scope'], 'openid')

      self.assertEqual(query_params['iss'][0], 'https://login.redirect-url.com/v1/clients/clientId')
      self.assertEqual(query_params['state'][0], 'state')