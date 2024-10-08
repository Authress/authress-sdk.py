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
    from pydantic.v1 import BaseModel, Field, conlist
except ImportError:
    from pydantic import BaseModel, Field, conlist
from authress.models.access_record import AccessRecord
from authress.models.collection_links import CollectionLinks
from authress.models.pagination import Pagination

class AccessRecordCollection(BaseModel):
    """
    A collection of access records  # noqa: E501
    """
    records: conlist(AccessRecord) = Field(default=..., description="A list of access records")
    pagination: Optional[Pagination] = None
    links: CollectionLinks = Field(...)
    __properties = ["records", "pagination", "links"]

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
    def from_json(cls, json_str: str) -> AccessRecordCollection:
        """Create an instance of AccessRecordCollection from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in records (list)
        _items = []
        if self.records:
            for _item in self.records:
                if _item:
                    _items.append(_item.to_dict())
            _dict['records'] = _items
        # override the default output from pydantic by calling `to_dict()` of pagination
        if self.pagination:
            _dict['pagination'] = self.pagination.to_dict()
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['links'] = self.links.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AccessRecordCollection:
        """Create an instance of AccessRecordCollection from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AccessRecordCollection.parse_obj(obj)

        _obj = AccessRecordCollection.parse_obj({
            "records": [AccessRecord.from_dict(_item) for _item in obj.get("records")] if obj.get("records") is not None else None,
            "pagination": Pagination.from_dict(obj.get("pagination")) if obj.get("pagination") is not None else None,
            "links": CollectionLinks.from_dict(obj.get("links")) if obj.get("links") is not None else None
        })
        return _obj


