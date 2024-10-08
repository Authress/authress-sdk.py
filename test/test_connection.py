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
import datetime

from authress.models.connection import Connection  # noqa: E501

class TestConnection(unittest.TestCase):
    """Connection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Connection:
        """Test Connection
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Connection`
        """
        model = Connection()  # noqa: E501
        if include_optional:
            return Connection(
                type = 'OAUTH2',
                connection_id = '',
                authentication_url = '0',
                token_url = '',
                issuer_url = '',
                provider_certificate = '',
                client_id = '',
                client_secret_id = '',
                client_secret = '',
                user_data_configuration = authress.models.connection_user_data_configuration.ConnectionUserDataConfiguration(
                    location = 'ZAF', ),
                data = authress.models.connection_data.Connection_data(
                    tenant_id = None, 
                    developer_account_id = '', 
                    name = '', 
                    supported_content_type = 'application/json', 
                    oidc_user_endpoint_url = '', 
                    user_id_expression = '{sub}', 
                    trust_identity_user_id = True, ),
                default_connection_properties = {
                    'key' : ''
                    },
                conditions = authress.models.connection_conditions.Connection_conditions(
                    require_business_account = False, ),
                linking_configuration = authress.models.connection_linking_configuration.Connection_linkingConfiguration(
                    type = 'EXPLICIT', ),
                created_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                is_active_connection = True,
                tags = {"environment":"production"}
            )
        else:
            return Connection(
        )
        """

    def testConnection(self):
        """Test Connection"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
