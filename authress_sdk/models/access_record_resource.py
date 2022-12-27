# coding: utf-8

class AccessRecordResource(object):

    """
    Attributes:
      openapi_spec_types (dict): The key is attribute name and the value is attribute type.
      attribute_serialization_map (dict): The key is attribute name and the value is json key in definition.
    """
    openapi_spec_types = {
        'resource_uri': 'str'
    }

    attribute_serialization_map = {
        'resource_uri': 'resourceUri'
    }

    def __init__(self, resource_uri=None):
        """AccessRecordResource"""
        self._resource_uri = None
        self.resource_uri = resource_uri

    @property
    def resource_uri(self):
        """Gets the resource_uri of this AccessRecordResource.

        A resource path which can be top level, fully qualified, or end with a *. Parent resources imply permissions to sub resources.

        :return: The resource_uri of this AccessRecordResource.
        :rtype: str
        """
        return self._resource_uri

    @resource_uri.setter
    def resource_uri(self, resource_uri):
        """Sets the resource_uri of this AccessRecordResource.

        A resource path which can be top level, fully qualified, or end with a *. Parent resources imply permissions to sub resources.

        :param resource_uri: The resource_uri of this AccessRecordResource.
        :type: str
        """
        if resource_uri is None:
            raise ValueError("Invalid value for `resource_uri`, must not be `None`")

        self._resource_uri = resource_uri
