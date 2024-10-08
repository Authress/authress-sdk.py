# coding: utf-8

"""
    Authress

    <p> <h2>Introduction</h2> <p>Welcome to the Authress Authorization API. <br>The Authress REST API provides the operations and resources necessary to create records, assign permissions, and verify any user in your platform.</p> <p><ul>   <li>Manage multitenant platforms and create user tenants for SSO connections.</li>   <li>Create records to assign roles and resources to grant access for users.</li>   <li>Check user access control by calling the authorization API at the right time.</li>   <li>Configure service clients to securely access services in your platform.</li> </ul></p> <p>For more in-depth scenarios check out the <a href=\"https://authress.io/knowledge-base\" target=\"_blank\">Authress knowledge base</a>.</p> </p>

    The version of the OpenAPI document: v1
    Contact: support@authress.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from authress.api.connections_api import ConnectionsApi  # noqa: E501


class TestConnectionsApi(unittest.TestCase):
    """ConnectionsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ConnectionsApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_create_connection(self) -> None:
        """Test case for create_connection

        Create SSO connection  # noqa: E501
        """
        pass

    def test_delete_connection(self) -> None:
        """Test case for delete_connection

        Delete SSO connection  # noqa: E501
        """
        pass

    def test_get_connection(self) -> None:
        """Test case for get_connection

        Retrieve SSO connection  # noqa: E501
        """
        pass

    def test_get_connection_credentials(self) -> None:
        """Test case for get_connection_credentials

        Retrieve user connection credentials  # noqa: E501
        """
        pass

    def test_get_connections(self) -> None:
        """Test case for get_connections

        List SSO connections  # noqa: E501
        """
        pass

    def test_update_connection(self) -> None:
        """Test case for update_connection

        Update SSO connection  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
