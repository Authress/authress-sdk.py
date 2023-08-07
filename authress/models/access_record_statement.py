# coding: utf-8

class AccessRecordStatement(object):

    """
    Attributes:
      openapi_spec_types (dict): The key is attribute name and the value is attribute type.
      attribute_serialization_map (dict): The key is attribute name and the value is json key in definition.
    """
    openapi_spec_types = {
        'roles': 'list[str]',
        'resources': 'list[AccessRecordResource]',
        'users': 'list[AccessRecordUser]',
        'groups': 'list[AccessRecordGroup]'
    }

    attribute_serialization_map = {
        'roles': 'roles',
        'resources': 'resources',
        'users': 'users',
        'groups': 'groups',
    }

    def __init__(self, roles=None, resources=None, users=None, groups=None):
        """AccessRecordStatement"""
        self._roles = None
        self._resources = None
        self._users = None
        self._groups = None
        self.roles = roles
        self.resources = resources
        self.users = users
        self.groups = groups

    @property
    def roles(self):
        """Gets the roles of this AccessRecordStatement.


        :return: The roles of this AccessRecordStatement.
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this AccessRecordStatement.


        :param roles: The roles of this AccessRecordStatement.
        :type: list[str]
        """
        if roles is None:
            raise ValueError("Invalid value for `roles`, must not be `None`")

        self._roles = roles

    @property
    def resources(self):
        """Gets the resources of this AccessRecordStatement.


        :return: The resources of this AccessRecordStatement.
        :rtype: list[AccessRecordResource]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this AccessRecordStatement.


        :param resources: The resources of this AccessRecordStatement.
        :type: list[AccessRecordResource]
        """
        if resources is None:
            raise ValueError("Invalid value for `resources`, must not be `None`")

        self._resources = resources

    @property
    def users(self):
        """Gets the users of this AccessRecordStatement.

        The list of users this record applies to

        :return: The users of this AccessRecordStatement.
        :rtype: list[AccessRecordUser]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this AccessRecordStatement.

        The list of users this record applies to

        :param users: The users of this AccessRecordStatement.
        :type: list[AccessRecordUser]
        """
        self._users = users

    @property
    def groups(self):
        """Gets the groups of this AccessRecordStatement.

        The list of groups this record applies to. Users in these groups will be receive access to the resources listed.

        :return: The groups of this AccessRecordStatement.
        :rtype: list[AccessRecordGroup]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this AccessRecordStatement.

        The list of groups this record applies to. Users in these groups will be receive access to the resources listed.

        :param groups: The groups of this AccessRecordStatement.
        :type: list[AccessRecordGroup]
        """
        self._groups = groups