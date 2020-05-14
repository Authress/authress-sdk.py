# coding: utf-8


import pprint
import re

import six


class IdentityRequest(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'jwt': 'str',
        'preferred_audience': 'str'
    }

    attribute_map = {
        'jwt': 'jwt',
        'preferred_audience': 'preferredAudience'
    }

    def __init__(self, jwt=None, preferred_audience=None):
        """IdentityRequest"""
        self._jwt = None
        self._preferred_audience = None
        self.discriminator = None
        self.jwt = jwt
        if preferred_audience is not None:
            self.preferred_audience = preferred_audience

    @property
    def jwt(self):
        """Gets the jwt of this IdentityRequest.

        A valid JWT OIDC compliant token which will still pass authentication requests to the identity provider. Must contain a unique audience and issuer.

        :return: The jwt of this IdentityRequest.
        :rtype: str
        """
        return self._jwt

    @jwt.setter
    def jwt(self, jwt):
        """Sets the jwt of this IdentityRequest.

        A valid JWT OIDC compliant token which will still pass authentication requests to the identity provider. Must contain a unique audience and issuer.

        :param jwt: The jwt of this IdentityRequest.
        :type: str
        """
        if jwt is None:
            raise ValueError("Invalid value for `jwt`, must not be `None`")

        self._jwt = jwt

    @property
    def preferred_audience(self):
        """Gets the preferred_audience of this IdentityRequest.

        If the `jwt` token contains more than one valid audience, then the single audience that should associated with Authress. If more than one audience is preferred, repeat this call with each one.

        :return: The preferred_audience of this IdentityRequest.
        :rtype: str
        """
        return self._preferred_audience

    @preferred_audience.setter
    def preferred_audience(self, preferred_audience):
        """Sets the preferred_audience of this IdentityRequest.

        If the `jwt` token contains more than one valid audience, then the single audience that should associated with Authress. If more than one audience is preferred, repeat this call with each one.

        :param preferred_audience: The preferred_audience of this IdentityRequest.
        :type: str
        """

        self._preferred_audience = preferred_audience

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
        if issubclass(IdentityRequest, dict):
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
        if not isinstance(other, IdentityRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
