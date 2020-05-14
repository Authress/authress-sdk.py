# coding: utf-8


import pprint
import re

import six


class AccessRecordResources(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'resource_uri': 'str'
    }

    attribute_map = {
        'resource_uri': 'resourceUri'
    }

    def __init__(self, resource_uri=None):
        """AccessRecordResources"""
        self._resource_uri = None
        self.discriminator = None
        self.resource_uri = resource_uri

    @property
    def resource_uri(self):
        """Gets the resource_uri of this AccessRecordResources.

        A resource path which can be top level, fully qualified, or end with a *. Parent resources imply permissions to sub resources.

        :return: The resource_uri of this AccessRecordResources.
        :rtype: str
        """
        return self._resource_uri

    @resource_uri.setter
    def resource_uri(self, resource_uri):
        """Sets the resource_uri of this AccessRecordResources.

        A resource path which can be top level, fully qualified, or end with a *. Parent resources imply permissions to sub resources.

        :param resource_uri: The resource_uri of this AccessRecordResources.
        :type: str
        """
        if resource_uri is None:
            raise ValueError("Invalid value for `resource_uri`, must not be `None`")

        self._resource_uri = resource_uri

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
        if issubclass(AccessRecordResources, dict):
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
        if not isinstance(other, AccessRecordResources):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
