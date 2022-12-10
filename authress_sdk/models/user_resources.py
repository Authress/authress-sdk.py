# coding: utf-8

class UserResources(object):

    """
    Attributes:
      openapi_spec_types (dict): The key is attribute name and the value is attribute type.
      attribute_serialization_map (dict): The key is attribute name and the value is json key in definition.
    """
    openapi_spec_types = {
        'user_id': 'str',
        'resources': 'list[AccessRecordResource]'
    }

    attribute_serialization_map = {
        'user_id': 'userId',
        'resources': 'resources'
    }

    def __init__(self, user_id=None, resources=None):
        """UserResources"""
        self._user_id = None
        self._resources = None
        self.user_id = user_id
        if resources is not None:
            self.resources = resources

    @property
    def user_id(self):
        """Gets the user_id of this UserResources.


        :return: The user_id of this UserResources.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this UserResources.


        :param user_id: The user_id of this UserResources.
        :type: str
        """
        self._user_id = user_id

    @property
    def resources(self):
        """Gets the resources of this UserResources.

        A list of the resources the user has some permission to.

        :return: The resources of this UserResources.
        :rtype: list[AccessRecordResource]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this UserResources.

        A list of the resources the user has some permission to.

        :param resources: The resources of this UserResources.
        :type: list[AccessRecordResource]
        """

        self._resources = resources
