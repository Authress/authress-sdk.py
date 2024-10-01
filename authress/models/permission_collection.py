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
    from pydantic.v1 import BaseModel, Field, conlist, constr, validator
except ImportError:
    from pydantic import BaseModel, Field, conlist, constr, validator
from authress.models.permission_collection_account import PermissionCollectionAccount
from authress.models.permission_object import PermissionObject

class PermissionCollection(BaseModel):
    """
    A collect of permissions that the user has to a resource.  # noqa: E501
    """
    account: Optional[PermissionCollectionAccount] = None
    user_id: constr(strict=True, max_length=128, min_length=1) = Field(default=..., alias="userId")
    permissions: conlist(PermissionObject) = Field(default=..., description="A list of the permissions")
    __properties = ["account", "userId", "permissions"]

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
    def from_json(cls, json_str: str) -> PermissionCollection:
        """Create an instance of PermissionCollection from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of account
        if self.account:
            _dict['account'] = self.account.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in permissions (list)
        _items = []
        if self.permissions:
            for _item in self.permissions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['permissions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PermissionCollection:
        """Create an instance of PermissionCollection from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PermissionCollection.parse_obj(obj)

        _obj = PermissionCollection.parse_obj({
            "account": PermissionCollectionAccount.from_dict(obj.get("account")) if obj.get("account") is not None else None,
            "user_id": obj.get("userId"),
            "permissions": [PermissionObject.from_dict(_item) for _item in obj.get("permissions")] if obj.get("permissions") is not None else None
        })
        return _obj


