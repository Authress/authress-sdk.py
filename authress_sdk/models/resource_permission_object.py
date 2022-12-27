# coding: utf-8

class ResourcePermissionObject(object):

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
        """ResourcePermissionObject"""
        self._action = None
        self._allow = None
        self.action = action
        self.allow = allow

    @property
    def action(self):
        """Gets the action of this ResourcePermissionObject.


        :return: The action of this ResourcePermissionObject.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ResourcePermissionObject.


        :param action: The action of this ResourcePermissionObject.
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
        """Gets the allow of this ResourcePermissionObject.


        :return: The allow of this ResourcePermissionObject.
        :rtype: str
        """
        return self._allow

    @allow.setter
    def allow(self, allow):
        """Sets the allow of this ResourcePermissionObject.


        :param allow: The allow of this ResourcePermissionObject.
        :type: str
        """
        if allow is None:
            raise ValueError("Invalid value for `allow`, must not be `None`")

        self._allow = allow
