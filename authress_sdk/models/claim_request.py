# coding: utf-8


import pprint
import re

import six


class ClaimRequest(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'collection_resource': 'str',
        'resource_id': 'str'
    }

    attribute_map = {
        'collection_resource': 'collectionResource',
        'resource_id': 'resourceId'
    }

    def __init__(self, collection_resource=None, resource_id=None):
        """ClaimRequest"""
        self._collection_resource = None
        self._resource_id = None
        self.discriminator = None
        self.collection_resource = collection_resource
        self.resource_id = resource_id

    @property
    def collection_resource(self):
        """Gets the collection_resource of this ClaimRequest.

        The parent resource to add a child resource to. The resource must have a resource configuration that add the permission CLAIM for this to work.

        :return: The collection_resource of this ClaimRequest.
        :rtype: str
        """
        return self._collection_resource

    @collection_resource.setter
    def collection_resource(self, collection_resource):
        """Sets the collection_resource of this ClaimRequest.

        The parent resource to add a child resource to. The resource must have a resource configuration that add the permission CLAIM for this to work.

        :param collection_resource: The collection_resource of this ClaimRequest.
        :type: str
        """
        if collection_resource is None:
            raise ValueError("Invalid value for `collection_resource`, must not be `None`")

        self._collection_resource = collection_resource

    @property
    def resource_id(self):
        """Gets the resource_id of this ClaimRequest.

        The child resource the user is requesting Admin ownership over.

        :return: The resource_id of this ClaimRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ClaimRequest.

        The child resource the user is requesting Admin ownership over.

        :param resource_id: The resource_id of this ClaimRequest.
        :type: str
        """
        if resource_id is None:
            raise ValueError("Invalid value for `resource_id`, must not be `None`")

        self._resource_id = resource_id

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
        if issubclass(ClaimRequest, dict):
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
        if not isinstance(other, ClaimRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
