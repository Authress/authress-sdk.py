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


from typing import List, Optional
try:
    from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr, validator
except ImportError:
    from pydantic import BaseModel, Field, StrictStr, conlist, constr, validator
from authress.models.resource import Resource

class InviteStatement(BaseModel):
    """
    InviteStatement
    """
    roles: conlist(constr(strict=True, max_length=64, min_length=1), max_items=100, min_items=1) = Field(...)
    resources: conlist(Resource, max_items=100, min_items=1) = Field(...)
    users: Optional[conlist(StrictStr, max_items=0)] = None
    groups: Optional[conlist(StrictStr, max_items=0)] = None
    __properties = ["roles", "resources", "users", "groups"]

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
    def from_json(cls, json_str: str) -> InviteStatement:
        """Create an instance of InviteStatement from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in resources (list)
        _items = []
        if self.resources:
            for _item in self.resources:
                if _item:
                    _items.append(_item.to_dict())
            _dict['resources'] = _items
        # set to None if users (nullable) is None
        # and __fields_set__ contains the field
        if self.users is None and "users" in self.__fields_set__:
            _dict['users'] = None

        # set to None if groups (nullable) is None
        # and __fields_set__ contains the field
        if self.groups is None and "groups" in self.__fields_set__:
            _dict['groups'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> InviteStatement:
        """Create an instance of InviteStatement from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InviteStatement.parse_obj(obj)

        _obj = InviteStatement.parse_obj({
            "roles": obj.get("roles"),
            "resources": [Resource.from_dict(_item) for _item in obj.get("resources")] if obj.get("resources") is not None else None,
            "users": obj.get("users"),
            "groups": obj.get("groups")
        })
        return _obj


