# coding: utf-8
import pprint
import re

import six


class ResourcePermission(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'permissions': 'list[ResourcePermissionPermissions]'
    }

    attribute_map = {
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
        :rtype: list[ResourcePermissionPermissions]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this ResourcePermission.


        :param permissions: The permissions of this ResourcePermission.
        :type: list[ResourcePermissionPermissions]
        """
        if permissions is None:
            raise ValueError("Invalid value for `permissions`, must not be `None`")

        self._permissions = permissions
