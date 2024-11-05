# coding: utf-8
from __future__ import absolute_import

import json
import re

from authress.api.applications_api import ApplicationsApi
from authress.api.connections_api import ConnectionsApi
from authress.api.extensions_api import ExtensionsApi
from authress.api.groups_api import GroupsApi
from authress.api.invites_api import InvitesApi
from authress.api.roles_api import RolesApi
from authress.api.tenants_api import TenantsApi
from authress.api.users_api import UsersApi

# python 2 and python 3 compatibility library
from authress.http_client import HttpClient
from authress.api.access_records_api import AccessRecordsApi
from authress.api.accounts_api import AccountsApi
from authress.api.resource_permissions_api import ResourcePermissionsApi
from authress.api.service_clients_api import ServiceClientsApi
from authress.api.user_permissions_api import UserPermissionsApi
from authress.api import token_verifier

class AuthressClient(object):
    def __init__(self, authress_api_url=None, service_client_access_key=None, user_agent=None):
        self._host = authress_api_url if authress_api_url.startswith('http') else f"https://{authress_api_url}"
        self._host = re.sub(r'/+$', '', self._host)
        self._service_client_access_key = service_client_access_key
        
        self._http_client = HttpClient(host=self._host, access_key=service_client_access_key, user_agent=user_agent)
        self._token_verifier = token_verifier.TokenVerifier(http_client=self._http_client)

    def set_token(self, token: str):
        if self._service_client_access_key is None:
            self._http_client.set_token(token)
            return
        
        raise Exception("An AuthressClient cannot use set_token, when the client has been instantiated with a service client access key. It must either be used for User tokens or with Service Client Access Keys, but not both.")

    def get_client_token(self) -> str:
        """Generates a Service Client Machine JWT to be used for securing machine to machine requests."""
        return self._http_client._get_client_token()

    def verify_token(self, token: str) -> object:
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
    def user_permissions(self) -> UserPermissionsApi:
        """Gets the User permissions API to make HTTP Requests with."""
        return UserPermissionsApi(api_client=self._http_client)

    @property
    def users(self) -> UsersApi:
        """Gets the Users API to make HTTP Requests with."""
        return UsersApi(api_client=self._http_client)

    @property
    def access_records(self) -> AccessRecordsApi:
        """Gets the Access Records API to make HTTP Requests with."""
        return AccessRecordsApi(api_client=self._http_client)

    @property
    def accounts(self) -> AccountsApi:
        """Gets the Authress Admin API to make HTTP Requests with."""
        return AccountsApi(api_client=self._http_client)

    @property
    def applications(self) -> ApplicationsApi:
        """Gets the Applications API to make HTTP Requests with."""
        return ApplicationsApi(api_client=self._http_client)

    @property
    def connections(self) -> ConnectionsApi:
        """Gets the Connections API to make HTTP Requests with."""
        return ConnectionsApi(api_client=self._http_client)

    @property
    def extensions(self) -> ExtensionsApi:
        """Gets the Extensions API to make HTTP Requests with."""
        return ExtensionsApi(api_client=self._http_client)

    @property
    def groups(self) -> GroupsApi:
        """Gets the Groups API to make HTTP Requests with."""
        return GroupsApi(api_client=self._http_client)

    @property
    def invites(self) -> InvitesApi:
        """Gets the Invites API to make HTTP Requests with."""
        return InvitesApi(api_client=self._http_client)

    @property
    def resource_permissions(self) -> ResourcePermissionsApi:
        """Gets the ResourcePermissions API to make HTTP Requests with."""
        return ResourcePermissionsApi(api_client=self._http_client)

    @property
    def roles(self) -> RolesApi:
        """Gets the Roles API to make HTTP Requests with."""
        return RolesApi(api_client=self._http_client)

    @property
    def tenants(self) -> TenantsApi:
        """Gets the Tenants API to make HTTP Requests with."""
        return TenantsApi(api_client=self._http_client)

    @property
    def service_clients(self) -> ServiceClientsApi:
        """Gets the Service Clients API to make HTTP Requests with."""
        return ServiceClientsApi(api_client=self._http_client)