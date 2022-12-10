# coding: utf-8

class ClientCollection(object):

    """
    Attributes:
      openapi_spec_types (dict): The key is attribute name and the value is attribute type.
      attribute_serialization_map (dict): The key is attribute name and the value is json key in definition.
    """
    openapi_spec_types = {
        'clients': 'list[Client]'
    }

    attribute_serialization_map = {
        'clients': 'clients'
    }

    def __init__(self, clients=None):
        """ClientCollection"""
        self._clients = None
        self.clients = clients

    @property
    def clients(self):
        """Gets the clients of this ClientCollection.

        A list of clients

        :return: The clients of this ClientCollection.
        :rtype: list[Client]
        """
        return self._clients

    @clients.setter
    def clients(self, clients):
        """Sets the clients of this ClientCollection.

        A list of clients

        :param clients: The clients of this ClientCollection.
        :type: list[Client]
        """
        if clients is None:
            raise ValueError("Invalid value for `clients`, must not be `None`")

        self._clients = clients
