# coding: utf-8


import pprint
import re

import six


class ResourcePermissionCollection(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'resources': 'list[ResourcePermission]'
    }

    attribute_map = {
        'resources': 'resources'
    }

    def __init__(self, resources=None):
        """ResourcePermissionCollection"""
        self._resources = None
        self.discriminator = None
        self.resources = resources

    @property
    def resources(self):
        """Gets the resources of this ResourcePermissionCollection.


        :return: The resources of this ResourcePermissionCollection.
        :rtype: list[ResourcePermission]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this ResourcePermissionCollection.


        :param resources: The resources of this ResourcePermissionCollection.
        :type: ResourcePermission
        """
        if resources is None:
            raise ValueError("Invalid value for `resources`, must not be `None`")

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
        if issubclass(ResourcePermissionCollection, dict):
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
        if not isinstance(other, ResourcePermissionCollection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
