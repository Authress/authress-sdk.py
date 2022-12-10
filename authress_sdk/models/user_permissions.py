# coding: utf-8

class UserPermissions(object):

    """
    Attributes:
      openapi_spec_types (dict): The key is attribute name and the value is attribute type.
      attribute_serialization_map (dict): The key is attribute name and the value is json key in definition.
    """
    openapi_spec_types = {
        'user_id': 'str',
        'permissions': 'list[PermissionObject]'
    }

    attribute_serialization_map = {
        'user_id': 'userId',
        'permissions': 'permissions'
    }

    def __init__(self, user_id=None, permissions=None):
        """UserPermissions"""
        self._user_id = None
        self._permissions = None
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
