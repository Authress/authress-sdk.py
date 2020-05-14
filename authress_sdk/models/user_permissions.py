# coding: utf-8


import pprint
import re

import six


class UserPermissions(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'user_id': 'str',
        'permissions': 'list[PermissionObject]'
    }

    attribute_map = {
        'user_id': 'userId',
        'permissions': 'permissions'
    }

    def __init__(self, user_id=None, permissions=None):
        """UserPermissions"""
        self._user_id = None
        self._permissions = None
        self.discriminator = None
        self.user_id = user_id
        self.permissions = permissions

    @property
    def user_id(self):
        """Gets the user_id of this UserPermissions.


        :return: The user_id of this UserPermissions.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this UserPermissions.


        :param user_id: The user_id of this UserPermissions.
        :type: str
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")

        self._user_id = user_id

    @property
    def permissions(self):
        """Gets the permissions of this UserPermissions.

        A list of the permissions

        :return: The permissions of this UserPermissions.
        :rtype: list[PermissionObject]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this UserPermissions.

        A list of the permissions

        :param permissions: The permissions of this UserPermissions.
        :type: list[PermissionObject]
        """
        if permissions is None:
            raise ValueError("Invalid value for `permissions`, must not be `None`")

        self._permissions = permissions

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
        if issubclass(UserPermissions, dict):
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
        if not isinstance(other, UserPermissions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
