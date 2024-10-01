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


from typing import List
try:
    from pydantic.v1 import BaseModel, Field, conlist, constr, validator
except ImportError:
    from pydantic import BaseModel, Field, conlist, constr, validator
from authress.models.user_role import UserRole

class UserRoleCollection(BaseModel):
    """
    A collect of roles that the user has to a resource.  # noqa: E501
    """
    user_id: constr(strict=True, max_length=128, min_length=1) = Field(default=..., alias="userId")
    roles: conlist(UserRole) = Field(default=..., description="A list of the roles")
    __properties = ["userId", "roles"]

    @validator('user_id')
    def user_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-zA-Z0-9+._|\/~:@\s-]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9+._|\/~:@\s-]+$/")
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
    def from_json(cls, json_str: str) -> UserRoleCollection:
        """Create an instance of UserRoleCollection from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in roles (list)
        _items = []
        if self.roles:
            for _item in self.roles:
                if _item:
                    _items.append(_item.to_dict())
            _dict['roles'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UserRoleCollection:
        """Create an instance of UserRoleCollection from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UserRoleCollection.parse_obj(obj)

        _obj = UserRoleCollection.parse_obj({
            "user_id": obj.get("userId"),
            "roles": [UserRole.from_dict(_item) for _item in obj.get("roles")] if obj.get("roles") is not None else None
        })
        return _obj


