# coding: utf-8


import pprint
import re

import six


class ResourcePermissionPermissions(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'action': 'str',
        'allow': 'str'
    }

    attribute_map = {
        'action': 'action',
        'allow': 'allow'
    }

    def __init__(self, action=None, allow=None):
        """ResourcePermissionPermissions"""
        self._action = None
        self._allow = None
        self.discriminator = None
        self.action = action
        self.allow = allow

    @property
    def action(self):
        """Gets the action of this ResourcePermissionPermissions.


        :return: The action of this ResourcePermissionPermissions.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ResourcePermissionPermissions.


        :param action: The action of this ResourcePermissionPermissions.
        :type: str
        """
        if action is None:
            raise ValueError("Invalid value for `action`, must not be `None`")
        allowed_values = ["CLAIM", "PUBLIC"]
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def allow(self):
        """Gets the allow of this ResourcePermissionPermissions.


        :return: The allow of this ResourcePermissionPermissions.
        :rtype: str
        """
        return self._allow

    @allow.setter
    def allow(self, allow):
        """Sets the allow of this ResourcePermissionPermissions.


        :param allow: The allow of this ResourcePermissionPermissions.
        :type: str
        """
        if allow is None:
            raise ValueError("Invalid value for `allow`, must not be `None`")

        self._allow = allow

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
        if issubclass(ResourcePermissionPermissions, dict):
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
        if not isinstance(other, ResourcePermissionPermissions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
