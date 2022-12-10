# coding: utf-8

class Client(object):

    """
    Attributes:
      openapi_spec_types (dict): The key is attribute name and the value is attribute type.
      attribute_serialization_map (dict): The key is attribute name and the value is json key in definition.
    """
    openapi_spec_types = {
        'client_id': 'str',
        'created_time': 'datetime',
        'name': 'str',
        'options': 'ClientOptions'
    }

    attribute_serialization_map = {
        'client_id': 'clientId',
        'created_time': 'createdTime',
        'name': 'name',
        'options': 'options'
    }

    def __init__(self, client_id=None, created_time=None, name=None, options=None):
        """Client"""
        self._client_id = None
        self._created_time = None
        self._name = None
        self._options = None
        self.client_id = client_id
        self.created_time = created_time
        self.name = name
        if options is not None:
            self.options = options

    @property
    def client_id(self):
        """Gets the client_id of this Client.

        The unique id of the client.

        :return: The client_id of this Client.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this Client.

        The unique id of the client.

        :param client_id: The client_id of this Client.
        :type: str
        """
        self._client_id = client_id

    @property
    def created_time(self):
        """Gets the created_time of this Client.


        :return: The created_time of this Client.
        :rtype: datetime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this Client.


        :param created_time: The created_time of this Client.
        :type: datetime
        """
        self._created_time = created_time

    @property
    def name(self):
        """Gets the name of this Client.

        The name of the client

        :return: The name of this Client.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Client.

        The name of the client

        :param name: The name of this Client.
        :type: str
        """
        self._name = name

    @property
    def options(self):
        """Gets the options of this Client.


        :return: The options of this Client.
        :rtype: ClientOptions
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this Client.


        :param options: The options of this Client.
        :type: ClientOptions
        """

        self._options = options
