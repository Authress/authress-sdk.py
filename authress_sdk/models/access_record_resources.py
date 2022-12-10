# coding: utf-8

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
