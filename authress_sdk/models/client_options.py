# coding: utf-8


import pprint
import re

import six


class ClientOptions(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'grant_user_permissions_access': 'bool'
    }

    attribute_map = {
        'grant_user_permissions_access': 'grantUserPermissionsAccess'
    }

    def __init__(self, grant_user_permissions_access=None):
        """ClientOptions"""
        self._grant_user_permissions_access = None
        self.discriminator = None
        if grant_user_permissions_access is not None:
            self.grant_user_permissions_access = grant_user_permissions_access

    @property
    def grant_user_permissions_access(self):
        """Gets the grant_user_permissions_access of this ClientOptions.

        Grant the client access to verify authorization on behalf of any user.

        :return: The grant_user_permissions_access of this ClientOptions.
        :rtype: bool
        """
        return self._grant_user_permissions_access

    @grant_user_permissions_access.setter
    def grant_user_permissions_access(self, grant_user_permissions_access):
        """Sets the grant_user_permissions_access of this ClientOptions.

        Grant the client access to verify authorization on behalf of any user.

        :param grant_user_permissions_access: The grant_user_permissions_access of this ClientOptions.
        :type: bool
        """

        self._grant_user_permissions_access = grant_user_permissions_access

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
        if issubclass(ClientOptions, dict):
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
        if not isinstance(other, ClientOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
