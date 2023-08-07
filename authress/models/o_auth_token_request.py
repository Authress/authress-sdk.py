# coding: utf-8

"""
    Authress

    <p> <h2>Introduction</h2> <p>Welcome to the Authress Authorization API. <br>The Authress REST API provides the operations and resources necessary to create records, assign permissions, and verify any user in your platform.</p> <p><ul>   <li>Manage multitenant platforms and create user tenants for SSO connections.</li>   <li>Create records to assign roles and resources to grant access for users.</li>   <li>Check user access control by calling the authorization API at the right time.</li>   <li>Configure service clients to securely access services in your platform.</li> </ul></p> <p>For more in-depth scenarios check out the <a href=\"https://authress.io/knowledge-base\" target=\"_blank\">Authress knowledge base</a>.</p> </p>  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: support@authress.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr, validator

class OAuthTokenRequest(BaseModel):
    """
    The OAuth 2.1 token request that follows [RFC 6749](https://www.rfc-editor.org/rfc/rfc6749). The properties in the request must be snake_case to follow the standard.
    """
    client_id: StrictStr = Field(..., description="The client identifier to constrain the token to.")
    client_secret: Optional[StrictStr] = Field(None, description="The secret associated with the client that authorizes the generation of token it's behalf. (Either the `client_secret` or the `code_verifier` is required)")
    code_verifier: Optional[StrictStr] = Field(None, description="The code verifier is the the value used in the generation of the OAuth authorization request `code_challenge` property. (Either the `client_secret` or the `code_verifier` is required)")
    grant_type: Optional[StrictStr] = Field(None, description="A suggestion to the token generation which type of credentials are being provided.")
    username: Optional[StrictStr] = Field(None, description="When using the user password grant_type, specify the username. Authress recommends this should always be an email address.")
    password: Optional[StrictStr] = Field(None, description="When using the user password grant_type, specify the user's password.")
    type: Optional[StrictStr] = Field(None, description="Enables additional configuration of the grant_type. In the case of user password grant_type, set this to **signup**, to enable the creation of users. Set this to **update**, force update the password associated with the user.")
    __properties = ["client_id", "client_secret", "code_verifier", "grant_type", "username", "password", "type"]

    @validator('grant_type')
    def grant_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('client_credentials', 'authorization_code', 'password'):
            raise ValueError("must be one of enum values ('client_credentials', 'authorization_code', 'password')")
        return value

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('signup', 'update'):
            raise ValueError("must be one of enum values ('signup', 'update')")
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
    def from_json(cls, json_str: str) -> OAuthTokenRequest:
        """Create an instance of OAuthTokenRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if client_secret (nullable) is None
        # and __fields_set__ contains the field
        if self.client_secret is None and "client_secret" in self.__fields_set__:
            _dict['client_secret'] = None

        # set to None if username (nullable) is None
        # and __fields_set__ contains the field
        if self.username is None and "username" in self.__fields_set__:
            _dict['username'] = None

        # set to None if password (nullable) is None
        # and __fields_set__ contains the field
        if self.password is None and "password" in self.__fields_set__:
            _dict['password'] = None

        # set to None if type (nullable) is None
        # and __fields_set__ contains the field
        if self.type is None and "type" in self.__fields_set__:
            _dict['type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OAuthTokenRequest:
        """Create an instance of OAuthTokenRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OAuthTokenRequest.parse_obj(obj)

        _obj = OAuthTokenRequest.parse_obj({
            "client_id": obj.get("client_id"),
            "client_secret": obj.get("client_secret"),
            "code_verifier": obj.get("code_verifier"),
            "grant_type": obj.get("grant_type"),
            "username": obj.get("username"),
            "password": obj.get("password"),
            "type": obj.get("type")
        })
        return _obj

