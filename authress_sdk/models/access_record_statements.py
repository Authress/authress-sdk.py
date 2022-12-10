# coding: utf-8

class AccessRecordStatements(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'roles': 'list[str]',
        'resources': 'list[AccessRecordResources]'
    }

    attribute_map = {
        'roles': 'roles',
        'resources': 'resources'
    }

    def __init__(self, roles=None, resources=None):
        """AccessRecordStatements"""
        self._roles = None
        self._resources = None
        self.roles = roles
        self.resources = resources

    @property
    def roles(self):
        """Gets the roles of this AccessRecordStatements.


        :return: The roles of this AccessRecordStatements.
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this AccessRecordStatements.


        :param roles: The roles of this AccessRecordStatements.
        :type: list[str]
        """
        if roles is None:
            raise ValueError("Invalid value for `roles`, must not be `None`")

        self._roles = roles

    @property
    def resources(self):
        """Gets the resources of this AccessRecordStatements.


        :return: The resources of this AccessRecordStatements.
        :rtype: list[AccessRecordResources]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this AccessRecordStatements.


        :param resources: The resources of this AccessRecordStatements.
        :type: list[AccessRecordResources]
        """
        if resources is None:
            raise ValueError("Invalid value for `resources`, must not be `None`")

        self._resources = resources
