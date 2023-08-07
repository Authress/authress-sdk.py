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


from typing import List, Optional
from pydantic import BaseModel, Field, conlist, constr, validator
from authress.models.permission_object import PermissionObject

class Role(BaseModel):
    """
    The role which contains a list of permissions.
    """
    role_id: constr(strict=True, max_length=64, min_length=1) = Field(..., alias="roleId", description="Unique identifier for the role, can be specified on creation, and used by records to map to permissions.")
    name: constr(strict=True, max_length=128, min_length=1) = Field(..., description="A helpful name for this role")
    description: Optional[constr(strict=True, max_length=1024, min_length=0)] = Field(None, description="A description for when to the user as well as additional information.")
    permissions: conlist(PermissionObject) = Field(..., description="A list of the permissions")
    __properties = ["roleId", "name", "description", "permissions"]

    @validator('role_id')
    def role_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-zA-Z0-9-._:@]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9-._:@]+$/")
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
    def from_json(cls, json_str: str) -> Role:
        """Create an instance of Role from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in permissions (list)
        _items = []
        if self.permissions:
            for _item in self.permissions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['permissions'] = _items
        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Role:
        """Create an instance of Role from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Role.parse_obj(obj)

        _obj = Role.parse_obj({
            "role_id": obj.get("roleId"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "permissions": [PermissionObject.from_dict(_item) for _item in obj.get("permissions")] if obj.get("permissions") is not None else None
        })
        return _obj

