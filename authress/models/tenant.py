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

from datetime import datetime
from typing import List, Optional
try:
    from pydantic.v1 import BaseModel, Field, conlist, constr, validator
except ImportError:
    from pydantic import BaseModel, Field, conlist, constr, validator
from authress.models.authentication_token_configuration import AuthenticationTokenConfiguration
from authress.models.tenant_connection import TenantConnection
from authress.models.tenant_data import TenantData
from authress.models.tenant_domain import TenantDomain

class Tenant(BaseModel):
    """
    Tenant
    """
    tenant_id: Optional[constr(strict=True, max_length=128, min_length=0)] = Field(default=None, alias="tenantId")
    tenant_lookup_identifier: Optional[constr(strict=True, max_length=64, min_length=0)] = Field(default=None, alias="tenantLookupIdentifier")
    data: Optional[TenantData] = None
    domains: Optional[conlist(TenantDomain, max_items=10, min_items=0)] = Field(default=None, description="The associated user email domains that are mapped to this tenant. When a user starts the authentication process, if they are using SSO, Authress will use their specified email address to identify which Authress Tenant to log the user in with.")
    connection: Optional[TenantConnection] = None
    token_configuration: Optional[AuthenticationTokenConfiguration] = Field(default=None, alias="tokenConfiguration")
    created_time: Optional[datetime] = Field(default=None, alias="createdTime")
    __properties = ["tenantId", "tenantLookupIdentifier", "data", "domains", "connection", "tokenConfiguration", "createdTime"]

    @validator('tenant_id')
    def tenant_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9-_.:]*$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9-_.:]*$/")
        return value

    @validator('tenant_lookup_identifier')
    def tenant_lookup_identifier_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9-_.:]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9-_.:]+$/")
        return value

    class Config:
        """Pydantic configuration"""
        extra = 'forbid'
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Tenant:
        """Create an instance of Tenant from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "created_time",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of data
        if self.data:
            _dict['data'] = self.data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in domains (list)
        _items = []
        if self.domains:
            for _item in self.domains:
                if _item:
                    _items.append(_item.to_dict())
            _dict['domains'] = _items
        # override the default output from pydantic by calling `to_dict()` of connection
        if self.connection:
            _dict['connection'] = self.connection.to_dict()
        # override the default output from pydantic by calling `to_dict()` of token_configuration
        if self.token_configuration:
            _dict['tokenConfiguration'] = self.token_configuration.to_dict()
        # set to None if tenant_id (nullable) is None
        # and __fields_set__ contains the field
        if self.tenant_id is None and "tenant_id" in self.__fields_set__:
            _dict['tenantId'] = None

        # set to None if tenant_lookup_identifier (nullable) is None
        # and __fields_set__ contains the field
        if self.tenant_lookup_identifier is None and "tenant_lookup_identifier" in self.__fields_set__:
            _dict['tenantLookupIdentifier'] = None

        # set to None if domains (nullable) is None
        # and __fields_set__ contains the field
        if self.domains is None and "domains" in self.__fields_set__:
            _dict['domains'] = None

        # set to None if connection (nullable) is None
        # and __fields_set__ contains the field
        if self.connection is None and "connection" in self.__fields_set__:
            _dict['connection'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Tenant:
        """Create an instance of Tenant from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Tenant.parse_obj(obj)

        _obj = Tenant.parse_obj({
            "tenant_id": obj.get("tenantId"),
            "tenant_lookup_identifier": obj.get("tenantLookupIdentifier"),
            "data": TenantData.from_dict(obj.get("data")) if obj.get("data") is not None else None,
            "domains": [TenantDomain.from_dict(_item) for _item in obj.get("domains")] if obj.get("domains") is not None else None,
            "connection": TenantConnection.from_dict(obj.get("connection")) if obj.get("connection") is not None else None,
            "token_configuration": AuthenticationTokenConfiguration.from_dict(obj.get("tokenConfiguration")) if obj.get("tokenConfiguration") is not None else None,
            "created_time": obj.get("createdTime")
        })
        return _obj


