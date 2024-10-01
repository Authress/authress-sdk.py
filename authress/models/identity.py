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
    from pydantic.v1 import BaseModel, Field, StrictStr, constr
except ImportError:
    from pydantic import BaseModel, Field, StrictStr, constr

class Identity(BaseModel):
    """
    The identifying information which uniquely links a JWT OIDC token to an identity provider  # noqa: E501
    """
    issuer: StrictStr = Field(default=..., description="The issuer of the JWT token. This can be any OIDC compliant provider.")
    audience: StrictStr = Field(default=..., description="The audience of the JWT token. This can be either an audience for your entire app, or one particular audience for it. If there is more than one audience, multiple identities can be created.")
    user_id_expression: Optional[constr(strict=True, max_length=128, min_length=0)] = Field(default='{sub}', alias="userIdExpression", description="By default, the **sub** claim of the JWT is used to identify the user from this provider. To use an alternate claim or a compound userId resolution, specify an expression. The resolved userId must be the same one that is later used in Authress access records.")
    __properties = ["issuer", "audience", "userIdExpression"]

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
    def from_json(cls, json_str: str) -> Identity:
        """Create an instance of Identity from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if user_id_expression (nullable) is None
        # and __fields_set__ contains the field
        if self.user_id_expression is None and "user_id_expression" in self.__fields_set__:
            _dict['userIdExpression'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Identity:
        """Create an instance of Identity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Identity.parse_obj(obj)

        _obj = Identity.parse_obj({
            "issuer": obj.get("issuer"),
            "audience": obj.get("audience"),
            "user_id_expression": obj.get("userIdExpression") if obj.get("userIdExpression") is not None else '{sub}'
        })
        return _obj


