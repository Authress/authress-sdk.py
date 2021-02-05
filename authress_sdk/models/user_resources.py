# coding: utf-8


import pprint
import re

import six


class UserResources(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'user_id': 'str',
        'resources': 'list[AccessRecordResource]'
    }

    attribute_map = {
        'user_id': 'userId',
        'resources': 'resources'
    }

    def __init__(self, user_id=None, resources=None):
        """UserResources"""
        self._user_id = None
        self._resources = None
        self.discriminator = None
        self.user_id = user_id
        if resources is not None:
            self.resources = resources

    @property
    def user_id(self):
        """Gets the user_id of this UserResources.


        :return: The user_id of this UserResources.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this UserResources.


        :param user_id: The user_id of this UserResources.
        :type: str
        """
        self._user_id = user_id

    @property
    def resources(self):
        """Gets the resources of this UserResources.

        A list of the resources the user has some permission to.

        :return: The resources of this UserResources.
        :rtype: list[AccessRecordResource]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this UserResources.

        A list of the resources the user has some permission to.

        :param resources: The resources of this UserResources.
        :type: list[AccessRecordResource]
        """

        self._resources = resources

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
        if issubclass(UserResources, dict):
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
        if not isinstance(other, UserResources):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
