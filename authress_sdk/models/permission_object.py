# coding: utf-8

class PermissionObject(object):

    """
    Attributes:
      openapi_spec_types (dict): The key is attribute name and the value is attribute type.
      attribute_serialization_map (dict): The key is attribute name and the value is json key in definition.
    """
    openapi_spec_types = {
        'action': 'str',
        'allow': 'bool',
        'grant': 'bool',
        'delegate': 'bool'
    }

    attribute_serialization_map = {
        'action': 'action',
        'allow': 'allow',
        'grant': 'grant',
        'delegate': 'delegate'
    }

    def __init__(self, action=None, allow=None, grant=None, delegate=None):
        """PermissionObject"""
        self._action = None
        self._allow = None
        self._grant = None
        self._delegate = None
        self.action = action
        self.allow = allow
        self.grant = grant
        self.delegate = delegate

    @property
    def action(self):
        """Gets the action of this PermissionObject.

        The action the permission grants, can be scoped using `:` and parent actions imply child permissions, action:* or action implies action:sub-action.

        :return: The action of this PermissionObject.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this PermissionObject.

        The action the permission grants, can be scoped using `:` and parent actions imply child permissions, action:* or action implies action:sub-action.

        :param action: The action of this PermissionObject.
        :type: str
        """
        self._action = action

    @property
    def allow(self):
        """Gets the allow of this PermissionObject.

        Does this permission grant the user the ability to execute the action?

        :return: The allow of this PermissionObject.
        :rtype: bool
        """
        return self._allow

    @allow.setter
    def allow(self, allow):
        """Sets the allow of this PermissionObject.

        Does this permission grant the user the ability to execute the action?

        :param allow: The allow of this PermissionObject.
        :type: bool
        """
        self._allow = allow

    @property
    def grant(self):
        """Gets the grant of this PermissionObject.

        Allows the user to give the permission to others without being able to execute the action.

        :return: The grant of this PermissionObject.
        :rtype: bool
        """
        return self._grant

    @grant.setter
    def grant(self, grant):
        """Sets the grant of this PermissionObject.

        Allows the user to give the permission to others without being able to execute the action.

        :param grant: The grant of this PermissionObject.
        :type: bool
        """
        self._grant = grant

    @property
    def delegate(self):
        """Gets the delegate of this PermissionObject.

        Allows delegating or granting the permission to others without being able to execute tha action.

        :return: The delegate of this PermissionObject.
        :rtype: bool
        """
        return self._delegate

    @delegate.setter
    def delegate(self, delegate):
        """Sets the delegate of this PermissionObject.

        Allows delegating or granting the permission to others without being able to execute tha action.

        :param delegate: The delegate of this PermissionObject.
        :type: bool
        """
        self._delegate = delegate
