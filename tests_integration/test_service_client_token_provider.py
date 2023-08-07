from __future__ import absolute_import

import unittest
import time

from authress import AuthressClient

class ServiceClientTokenProviderTest(unittest.TestCase):
  def setUp(self):
    pass

  def tearDown(self):
    pass

  def test_integration_test(self):
    authress_client = AuthressClient(authress_api_url="https://TEST_AUTHRESS_DOMAIN")
    authress_client.set_token('TEST_TOKEN')
    authress_client.user_permissions.authorize_user(user_id="Authress|google-oauth2|TestUserId", resource_uri="Authress:UserPermissionss/", permission="something")