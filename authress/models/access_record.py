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

from datetime import datetime
from typing import Dict, List, Optional, Union
from pydantic import BaseModel, Field, StrictStr, confloat, conint, conlist, constr, validator
from authress.models.access_record_account import AccessRecordAccount
from authress.models.account_links import AccountLinks
from authress.models.linked_group import LinkedGroup
from authress.models.statement import Statement
from authress.models.user import User

class AccessRecord(BaseModel):
    """
    The access record which links users to roles.
    """
    record_id: Optional[constr(strict=True, max_length=100, min_length=1)] = Field(None, alias="recordId", description="Unique identifier for the record, can be specified on record creation.")
    name: constr(strict=True, max_length=128, min_length=1) = Field(..., description="A helpful name for this record")
    description: Optional[constr(strict=True, max_length=1024, min_length=0)] = Field(None, description="More details about this record")
    capacity: Optional[Union[confloat(le=1, ge=0, strict=True), conint(le=1, ge=0, strict=True)]] = Field(None, description="Percentage capacity of record that is filled.")
    last_updated: Optional[datetime] = Field(None, alias="lastUpdated", description="The expected last time the record was updated")
    status: Optional[StrictStr] = Field(None, description="Current status of the access record.")
    account: Optional[AccessRecordAccount] = Field(...)
    users: Optional[conlist(User)] = Field(None, description="The list of users this record applies to")
    admins: Optional[conlist(User)] = Field(None, description="The list of admin that can edit this record even if they do not have global record edit permissions.")
    groups: Optional[conlist(LinkedGroup)] = Field(None, description="The list of groups this record applies to. Users in these groups will be receive access to the resources listed.")
    statements: conlist(Statement, min_items=1) = Field(..., description="A list of statements which match roles to resources.")
    links: Optional[AccountLinks] = Field(...)
    tags: Optional[Dict[str, constr(strict=True, max_length=128)]] = Field(None, description="The tags associated with this resource, this property is an map. { key1: value1, key2: value2 }")
    __properties = ["recordId", "name", "description", "capacity", "lastUpdated", "status", "account", "users", "admins", "groups", "statements", "links", "tags"]

    @validator('record_id')
    def record_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9-_:|~]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9-_:|~]+$/")
        return value

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('ACTIVE', 'DELETED'):
            raise ValueError("must be one of enum values ('ACTIVE', 'DELETED')")
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
    def from_json(cls, json_str: str) -> AccessRecord:
        """Create an instance of AccessRecord from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "capacity",
                            "last_updated",
                            "status",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of account
        if self.account:
            _dict['account'] = self.account.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in users (list)
        _items = []
        if self.users:
            for _item in self.users:
                if _item:
                    _items.append(_item.to_dict())
            _dict['users'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in admins (list)
        _items = []
        if self.admins:
            for _item in self.admins:
                if _item:
                    _items.append(_item.to_dict())
            _dict['admins'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in groups (list)
        _items = []
        if self.groups:
            for _item in self.groups:
                if _item:
                    _items.append(_item.to_dict())
            _dict['groups'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in statements (list)
        _items = []
        if self.statements:
            for _item in self.statements:
                if _item:
                    _items.append(_item.to_dict())
            _dict['statements'] = _items
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['links'] = self.links.to_dict()
        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if users (nullable) is None
        # and __fields_set__ contains the field
        if self.users is None and "users" in self.__fields_set__:
            _dict['users'] = None

        # set to None if admins (nullable) is None
        # and __fields_set__ contains the field
        if self.admins is None and "admins" in self.__fields_set__:
            _dict['admins'] = None

        # set to None if groups (nullable) is None
        # and __fields_set__ contains the field
        if self.groups is None and "groups" in self.__fields_set__:
            _dict['groups'] = None

        # set to None if tags (nullable) is None
        # and __fields_set__ contains the field
        if self.tags is None and "tags" in self.__fields_set__:
            _dict['tags'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AccessRecord:
        """Create an instance of AccessRecord from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AccessRecord.parse_obj(obj)

        _obj = AccessRecord.parse_obj({
            "record_id": obj.get("recordId"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "capacity": obj.get("capacity"),
            "last_updated": obj.get("lastUpdated"),
            "status": obj.get("status"),
            "account": AccessRecordAccount.from_dict(obj.get("account")) if obj.get("account") is not None else None,
            "users": [User.from_dict(_item) for _item in obj.get("users")] if obj.get("users") is not None else None,
            "admins": [User.from_dict(_item) for _item in obj.get("admins")] if obj.get("admins") is not None else None,
            "groups": [LinkedGroup.from_dict(_item) for _item in obj.get("groups")] if obj.get("groups") is not None else None,
            "statements": [Statement.from_dict(_item) for _item in obj.get("statements")] if obj.get("statements") is not None else None,
            "links": AccountLinks.from_dict(obj.get("links")) if obj.get("links") is not None else None,
            "tags": obj.get("tags")
        })
        return _obj


