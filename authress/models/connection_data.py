# coding: utf-8

"""
    Authress

    <p> <h2>Introduction</h2> <p>Welcome to the Authress Authorization API. <br>The Authress REST API provides the operations and resources necessary to create records, assign permissions, and verify any user in your platform.</p> <p><ul>   <li>Manage multitenant platforms and create user tenants for SSO connections.</li>   <li>Create records to assign roles and resources to grant access for users.</li>   <li>Check user access control by calling the authorization API at the right time.</li>   <li>Configure service clients to securely access services in your platform.</li> </ul></p> <p>For more in-depth scenarios check out the <a href=\"https://authress.io/knowledge-base\" target=\"_blank\">Authress knowledge base</a>.</p> </p>

    The version of the OpenAPI document: v1
    Contact: support@authress.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
try:
    from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr, constr, validator
except ImportError:
    from pydantic import BaseModel, Field, StrictBool, StrictStr, constr, validator

class ConnectionData(BaseModel):
    """
    ConnectionData
    """
    tenant_id: Optional[constr(strict=True, max_length=128, min_length=0)] = Field(default=None, alias="tenantId")
    developer_account_id: Optional[constr(strict=True, max_length=32, min_length=0)] = Field(default=None, alias="developerAccountId", description="The Developer Account ID associated with the credentials. This is necessary for some providers, such as Apple Login.")
    name: Optional[constr(strict=True, max_length=64, min_length=0)] = Field(default=None, description="The name of this connection when displayed in the Authress management portal")
    supported_content_type: Optional[StrictStr] = Field(default='application/json', alias="supportedContentType", description="URL encode OAuth token parameters - Some authentication APIs don't support JSON, in these cases enable the url encoded form data parameters.")
    oidc_user_endpoint_url: Optional[constr(strict=True, max_length=128, min_length=0)] = Field(default=None, alias="oidcUserEndpointUrl", description="By default, the **sub** claim of the JWT is used to identify the user from this provider. However, not all providers are OpenID compliant. Here you can provide an optional user data endpoint to fetch additional user profile information and an expression to identify a new user ID from available properties.")
    user_id_expression: Optional[constr(strict=True, max_length=128, min_length=0)] = Field(default='{sub}', alias="userIdExpression", description="By default, the **sub** claim of the JWT is used to identify the user from this provider. However, not all providers are OpenID compliant. Here you can provide an optional user expression to identify a new user ID from available properties found from the oidcUserEndpointUrl. (The default is **{sub}**, any claims may be used.)")
    trust_identity_user_id: Optional[StrictBool] = Field(default=False, alias="trustIdentityUserId", description="Authress generates unique user IDs for every user, however if you trust your identity provider to handle unique ID generate across **ALL customers**, then it is safe to reuse the user ID from the provider.")
    __properties = ["tenantId", "developerAccountId", "name", "supportedContentType", "oidcUserEndpointUrl", "userIdExpression", "trustIdentityUserId"]

    @validator('tenant_id')
    def tenant_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9-_.:]*$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9-_.:]*$/")
        return value

    @validator('supported_content_type')
    def supported_content_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('application/json', 'application/x-www-form-urlencoded'):
            raise ValueError("must be one of enum values ('application/json', 'application/x-www-form-urlencoded')")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ConnectionData:
        """Create an instance of ConnectionData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if tenant_id (nullable) is None
        # and __fields_set__ contains the field
        if self.tenant_id is None and "tenant_id" in self.__fields_set__:
            _dict['tenantId'] = None

        # set to None if developer_account_id (nullable) is None
        # and __fields_set__ contains the field
        if self.developer_account_id is None and "developer_account_id" in self.__fields_set__:
            _dict['developerAccountId'] = None

        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        # set to None if supported_content_type (nullable) is None
        # and __fields_set__ contains the field
        if self.supported_content_type is None and "supported_content_type" in self.__fields_set__:
            _dict['supportedContentType'] = None

        # set to None if oidc_user_endpoint_url (nullable) is None
        # and __fields_set__ contains the field
        if self.oidc_user_endpoint_url is None and "oidc_user_endpoint_url" in self.__fields_set__:
            _dict['oidcUserEndpointUrl'] = None

        # set to None if user_id_expression (nullable) is None
        # and __fields_set__ contains the field
        if self.user_id_expression is None and "user_id_expression" in self.__fields_set__:
            _dict['userIdExpression'] = None

        # set to None if trust_identity_user_id (nullable) is None
        # and __fields_set__ contains the field
        if self.trust_identity_user_id is None and "trust_identity_user_id" in self.__fields_set__:
            _dict['trustIdentityUserId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ConnectionData:
        """Create an instance of ConnectionData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ConnectionData.parse_obj(obj)

        _obj = ConnectionData.parse_obj({
            "tenant_id": obj.get("tenantId"),
            "developer_account_id": obj.get("developerAccountId"),
            "name": obj.get("name"),
            "supported_content_type": obj.get("supportedContentType") if obj.get("supportedContentType") is not None else 'application/json',
            "oidc_user_endpoint_url": obj.get("oidcUserEndpointUrl"),
            "user_id_expression": obj.get("userIdExpression") if obj.get("userIdExpression") is not None else '{sub}',
            "trust_identity_user_id": obj.get("trustIdentityUserId") if obj.get("trustIdentityUserId") is not None else False
        })
        return _obj


