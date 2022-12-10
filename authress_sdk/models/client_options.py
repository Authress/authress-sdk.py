# coding: utf-8

class ClientOptions(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'grant_user_permissions_access': 'bool'
    }

    attribute_map = {
        'grant_user_permissions_access': 'grantUserPermissionsAccess'
    }

    def __init__(self, grant_user_permissions_access=None):
        """ClientOptions"""
        self._grant_user_permissions_access = None
        if grant_user_permissions_access is not None:
            self.grant_user_permissions_access = grant_user_permissions_access

    @property
    def grant_user_permissions_access(self):
        """Gets the grant_user_permissions_access of this ClientOptions.

        Grant the client access to verify authorization on behalf of any user.

        :return: The grant_user_permissions_access of this ClientOptions.
        :rtype: bool
        """
        return self._grant_user_permissions_access

    @grant_user_permissions_access.setter
    def grant_user_permissions_access(self, grant_user_permissions_access):
        """Sets the grant_user_permissions_access of this ClientOptions.

        Grant the client access to verify authorization on behalf of any user.

        :param grant_user_permissions_access: The grant_user_permissions_access of this ClientOptions.
        :type: bool
        """

        self._grant_user_permissions_access = grant_user_permissions_access
