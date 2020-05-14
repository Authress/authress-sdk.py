# coding: utf-8


import pprint
import re

import six


class Identity(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'issuer': 'str',
        'audience': 'str'
    }

    attribute_map = {
        'issuer': 'issuer',
        'audience': 'audience'
    }

    def __init__(self, issuer=None, audience=None):
        """Identity"""
        self._issuer = None
        self._audience = None
        self.discriminator = None
        self.issuer = issuer
        self.audience = audience

    @property
    def issuer(self):
        """Gets the issuer of this Identity.

        The issuer of the JWT token. This can be any OIDC compliant provider.

        :return: The issuer of this Identity.
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this Identity.

        The issuer of the JWT token. This can be any OIDC compliant provider.

        :param issuer: The issuer of this Identity.
        :type: str
        """
        if issuer is None:
            raise ValueError("Invalid value for `issuer`, must not be `None`")

        self._issuer = issuer

    @property
    def audience(self):
        """Gets the audience of this Identity.

        The target of the JWT tokens. This must be a sub target of the account app or the whole app

        :return: The audience of this Identity.
        :rtype: str
        """
        return self._audience

    @audience.setter
    def audience(self, audience):
        """Sets the audience of this Identity.

        The target of the JWT tokens. This must be a sub target of the account app or the whole app

        :param audience: The audience of this Identity.
        :type: str
        """
        if audience is None:
            raise ValueError("Invalid value for `audience`, must not be `None`")

        self._audience = audience

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Identity, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Identity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
