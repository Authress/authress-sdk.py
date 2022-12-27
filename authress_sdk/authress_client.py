# coding: utf-8
from __future__ import absolute_import

import json

# python 2 and python 3 compatibility library
from authress_sdk.http_client import HttpClient
from authress_sdk.api.access_records_api import AccessRecordsApi
from authress_sdk.api.accounts_api import AccountsApi
from authress_sdk.api.resource_permissions_api import ResourcePermissionsApi
from authress_sdk.api.service_clients_api import ServiceClientsApi
from authress_sdk.api.user_permissions_api import UserPermissionsApi
from authress_sdk.api import token_verifier

class AuthressClient(object):
    def __init__(self, host=None, access_key=None):
        self._host = host if host.startswith('http') else f"https://{host}"
        self._token_verifier = token_verifier.TokenVerifier()
        self._http_client = HttpClient(host=self._host, access_key=access_key)

    def set_token(self, token):
        self._http_client.set_token(token)

    def get_client_token(self) -> str:
        self._http_client._get_client_token()

    def verify_token(self, token):
      """Verify a user access token

        On successful verification the response is the decoded user identity JWT.
        On failure this raises an exception

        Note: This method makes HTTP calls to fetch public keys for token signature verification

        :param string token: (required) The user's access token to verify
        :raises: :class:`Exception`: Unauthorized

        :return: UserIdentityJWT
        """
      return self._token_verifier.verify_token(self._host, token)

    @property
    def users(self) -> UserPermissionsApi:
        """Gets the User permissions API to make HTTP Requests with."""
        return UserPermissionsApi(api_client=self._http_client)

    @property
    def records(self) -> AccessRecordsApi:
        """Gets the Access Records API to make HTTP Requests with."""
        return AccessRecordsApi(api_client=self._http_client)

    @property
    def accounts(self) -> AccountsApi:
        """Gets the Authress Accounts API to make HTTP Requests with."""
        return AccountsApi(api_client=self._http_client)

    @property
    def resources(self) -> ResourcePermissionsApi:
        """Gets the Resources API to make HTTP Requests with."""
        return ResourcePermissionsApi(api_client=self._http_client)

    @property
    def clients(self) -> ServiceClientsApi:
        """Gets the Service Clients API to make HTTP Requests with."""
        return ServiceClientsApi(api_client=self._http_client)