# coding: utf-8

class ResourcePermissionPermissions(object):

    """
    Attributes:
      openapi_spec_types (dict): The key is attribute name and the value is attribute type.
      attribute_serialization_map (dict): The key is attribute name and the value is json key in definition.
    """
    openapi_spec_types = {
        'action': 'str',
        'allow': 'str'
    }

    attribute_serialization_map = {
        'action': 'action',
        'allow': 'allow'
    }

    def __init__(self, action=None, allow=None):
        """ResourcePermissionPermissions"""
        self._action = None
        self._allow = None
        self.action = action
        self.allow = allow

    @property
    def action(self):
        """Gets the action of this ResourcePermissionPermissions.


        :return: The action of this ResourcePermissionPermissions.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ResourcePermissionPermissions.


        :param action: The action of this ResourcePermissionPermissions.
        :type: str
        """
        if action is None:
            raise ValueError("Invalid value for `action`, must not be `None`")
        allowed_values = ["CLAIM", "PUBLIC"]
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def allow(self):
        """Gets the allow of this ResourcePermissionPermissions.


        :return: The allow of this ResourcePermissionPermissions.
        :rtype: str
        """
        return self._allow

    @allow.setter
    def allow(self, allow):
        """Sets the allow of this ResourcePermissionPermissions.


        :param allow: The allow of this ResourcePermissionPermissions.
        :type: str
        """
        if allow is None:
            raise ValueError("Invalid value for `allow`, must not be `None`")

        self._allow = allow
