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

from authress.api.extensions_api import ExtensionsApi  # noqa: E501


class TestExtensionsApi(unittest.TestCase):
    """ExtensionsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ExtensionsApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_create_extension(self) -> None:
        """Test case for create_extension

        Create extension  # noqa: E501
        """
        pass

    def test_delete_extension(self) -> None:
        """Test case for delete_extension

        Delete extension  # noqa: E501
        """
        pass

    def test_get_extension(self) -> None:
        """Test case for get_extension

        Retrieve extension  # noqa: E501
        """
        pass

    def test_get_extensions(self) -> None:
        """Test case for get_extensions

        List extensions  # noqa: E501
        """
        pass

    def test_login(self) -> None:
        """Test case for login

        OAuth Authorize  # noqa: E501
        """
        pass

    def test_request_token(self) -> None:
        """Test case for request_token

        OAuth Token  # noqa: E501
        """
        pass

    def test_update_extension(self) -> None:
        """Test case for update_extension

        Update extension  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
