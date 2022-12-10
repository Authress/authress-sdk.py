# coding: utf-8

class ResourcePermissionCollection(object):

    """
    Attributes:
      openapi_spec_types (dict): The key is attribute name and the value is attribute type.
      attribute_serialization_map (dict): The key is attribute name and the value is json key in definition.
    """
    openapi_spec_types = {
        'resources': 'list[ResourcePermission]'
    }

    attribute_serialization_map = {
        'resources': 'resources'
    }

    def __init__(self, resources=None):
        """ResourcePermissionCollection"""
        self._resources = None
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
