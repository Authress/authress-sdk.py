# coding: utf-8

class ResourcePermission(object):

    """
    Attributes:
      openapi_spec_types (dict): The key is attribute name and the value is attribute type.
      attribute_serialization_map (dict): The key is attribute name and the value is json key in definition.
    """
    openapi_spec_types = {
        'permissions': 'list[ResourcePermissionObject]'
    }

    attribute_serialization_map = {
        'permissions': 'permissions'
    }

    def __init__(self, permissions=None):
        """ResourcePermission"""
        self._permissions = None
        self.permissions = permissions

    @property
    def permissions(self):
        """Gets the permissions of this ResourcePermission.


        :return: The permissions of this ResourcePermission.
        :rtype: list[ResourcePermissionObject]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this ResourcePermission.


        :param permissions: The permissions of this ResourcePermission.
        :type: list[ResourcePermissionObject]
        """
        if permissions is None:
            raise ValueError("Invalid value for `permissions`, must not be `None`")

        self._permissions = permissions
