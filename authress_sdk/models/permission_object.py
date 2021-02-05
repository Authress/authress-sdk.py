# coding: utf-8


import pprint
import re

import six


class PermissionObject(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'action': 'str',
        'allow': 'bool',
        'grant': 'bool',
        'delegate': 'bool'
    }

    attribute_map = {
        'action': 'action',
        'allow': 'allow',
        'grant': 'grant',
        'delegate': 'delegate'
    }

    def __init__(self, action=None, allow=None, grant=None, delegate=None):
        """PermissionObject"""
        self._action = None
        self._allow = None
        self._grant = None
        self._delegate = None
        self.discriminator = None
        self.action = action
        self.allow = allow
        self.grant = grant
        self.delegate = delegate

    @property
    def action(self):
        """Gets the action of this PermissionObject.

        The action the permission grants, can be scoped using `:` and parent actions imply child permissions, action:* or action implies action:sub-action.

        :return: The action of this PermissionObject.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this PermissionObject.

        The action the permission grants, can be scoped using `:` and parent actions imply child permissions, action:* or action implies action:sub-action.

        :param action: The action of this PermissionObject.
        :type: str
        """
        self._action = action

    @property
    def allow(self):
        """Gets the allow of this PermissionObject.

        Does this permission grant the user the ability to execute the action?

        :return: The allow of this PermissionObject.
        :rtype: bool
        """
        return self._allow

    @allow.setter
    def allow(self, allow):
        """Sets the allow of this PermissionObject.

        Does this permission grant the user the ability to execute the action?

        :param allow: The allow of this PermissionObject.
        :type: bool
        """
        self._allow = allow

    @property
    def grant(self):
        """Gets the grant of this PermissionObject.

        Allows the user to give the permission to others without being able to execute the action.

        :return: The grant of this PermissionObject.
        :rtype: bool
        """
        return self._grant

    @grant.setter
    def grant(self, grant):
        """Sets the grant of this PermissionObject.

        Allows the user to give the permission to others without being able to execute the action.

        :param grant: The grant of this PermissionObject.
        :type: bool
        """
        self._grant = grant

    @property
    def delegate(self):
        """Gets the delegate of this PermissionObject.

        Allows delegating or granting the permission to others without being able to execute tha action.

        :return: The delegate of this PermissionObject.
        :rtype: bool
        """
        return self._delegate

    @delegate.setter
    def delegate(self, delegate):
        """Sets the delegate of this PermissionObject.

        Allows delegating or granting the permission to others without being able to execute tha action.

        :param delegate: The delegate of this PermissionObject.
        :type: bool
        """
        self._delegate = delegate

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
        if issubclass(PermissionObject, dict):
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
        if not isinstance(other, PermissionObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
