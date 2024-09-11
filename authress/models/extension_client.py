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
    from pydantic.v1 import BaseModel, Field, StrictStr, conlist
except ImportError:
    from pydantic import BaseModel, Field, StrictStr, conlist
from authress.models.client_rate_limit import ClientRateLimit
from authress.models.links import Links

class ExtensionClient(BaseModel):
    """
    The extension's client configuration.  # noqa: E501
    """
    client_id: Optional[StrictStr] = Field(default=None, alias="clientId", description="The unique ID of the client.")
    rate_limits: Optional[conlist(ClientRateLimit, max_items=1, min_items=0)] = Field(default=None, alias="rateLimits", description="A list of the service client rate limits. Rate Limits can be used to prevent service clients from creating too many requests to your API. They can also limit the number of requests to Authress management APIs, or contain a maximum quota for a client before it is not longer allowed to make additional requests.")
    links: Optional[Links] = None
    __properties = ["clientId", "rateLimits", "links"]

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
    def from_json(cls, json_str: str) -> ExtensionClient:
        """Create an instance of ExtensionClient from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "client_id",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in rate_limits (list)
        _items = []
        if self.rate_limits:
            for _item in self.rate_limits:
                if _item:
                    _items.append(_item.to_dict())
            _dict['rateLimits'] = _items
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['links'] = self.links.to_dict()
        # set to None if rate_limits (nullable) is None
        # and __fields_set__ contains the field
        if self.rate_limits is None and "rate_limits" in self.__fields_set__:
            _dict['rateLimits'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ExtensionClient:
        """Create an instance of ExtensionClient from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ExtensionClient.parse_obj(obj)

        _obj = ExtensionClient.parse_obj({
            "client_id": obj.get("clientId"),
            "rate_limits": [ClientRateLimit.from_dict(_item) for _item in obj.get("rateLimits")] if obj.get("rateLimits") is not None else None,
            "links": Links.from_dict(obj.get("links")) if obj.get("links") is not None else None
        })
        return _obj


