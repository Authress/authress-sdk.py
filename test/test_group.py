# coding: utf-8

"""
    Authress

    <p> <h2>Introduction</h2> <p>Welcome to the Authress Authorization API. <br>The Authress REST API provides the operations and resources necessary to create records, assign permissions, and verify any user in your platform.</p> <p><ul>   <li>Manage multitenant platforms and create user tenants for SSO connections.</li>   <li>Create records to assign roles and resources to grant access for users.</li>   <li>Check user access control by calling the authorization API at the right time.</li>   <li>Configure service clients to securely access services in your platform.</li> </ul></p> <p>For more in-depth scenarios check out the <a href=\"https://authress.io/knowledge-base\" target=\"_blank\">Authress knowledge base</a>.</p> </p>  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: support@authress.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import authress
from authress.models.group import Group  # noqa: E501
from authress.rest import ApiException

class TestGroup(unittest.TestCase):
    """Group unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Group
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Group`
        """
        model = authress.models.group.Group()  # noqa: E501
        if include_optional :
            return Group(
                group_id = 'grp_user_group_001', 
                name = '0', 
                last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                users = [
                    authress.models.user.User(
                        user_id = 'oauth|userId', )
                    ], 
                admins = [
                    authress.models.user.User(
                        user_id = 'oauth|userId', )
                    ], 
                links = authress.models.account_links.Account_links(
                    self = authress.models.link.Link(
                        href = '', 
                        rel = '', ), ), 
                tags = {"environment":"production"}
            )
        else :
            return Group(
                name = '0',
                users = [
                    authress.models.user.User(
                        user_id = 'oauth|userId', )
                    ],
                admins = [
                    authress.models.user.User(
                        user_id = 'oauth|userId', )
                    ],
                links = authress.models.account_links.Account_links(
                    self = authress.models.link.Link(
                        href = '', 
                        rel = '', ), ),
        )
        """

    def testGroup(self):
        """Test Group"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()