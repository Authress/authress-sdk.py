# coding: utf-8


import pprint
import re

import six


class ClientAccessKey(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'key_id': 'str',
        'client_id': 'str',
        'generation_date': 'datetime',
        'access_key': 'str'
    }

    attribute_map = {
        'key_id': 'keyId',
        'client_id': 'clientId',
        'generation_date': 'generationDate',
        'access_key': 'accessKey'
    }

    def __init__(self, key_id=None, client_id=None, generation_date=None, access_key=None):
        """ClientAccessKey"""
        self._key_id = None
        self._client_id = None
        self._generation_date = None
        self._access_key = None
        self.discriminator = None
        if key_id is not None:
            self.key_id = key_id
        self.client_id = client_id
        if generation_date is not None:
            self.generation_date = generation_date
        if access_key is not None:
            self.access_key = access_key

    @property
    def key_id(self):
        """Gets the key_id of this ClientAccessKey.

        The unique id of the client.

        :return: The key_id of this ClientAccessKey.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """Sets the key_id of this ClientAccessKey.

        The unique id of the client.

        :param key_id: The key_id of this ClientAccessKey.
        :type: str
        """

        self._key_id = key_id

    @property
    def client_id(self):
        """Gets the client_id of this ClientAccessKey.

        The unique id of the client.

        :return: The client_id of this ClientAccessKey.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this ClientAccessKey.

        The unique id of the client.

        :param client_id: The client_id of this ClientAccessKey.
        :type: str
        """
        if client_id is None:
            raise ValueError("Invalid value for `client_id`, must not be `None`")

        self._client_id = client_id

    @property
    def generation_date(self):
        """Gets the generation_date of this ClientAccessKey.


        :return: The generation_date of this ClientAccessKey.
        :rtype: datetime
        """
        return self._generation_date

    @generation_date.setter
    def generation_date(self, generation_date):
        """Sets the generation_date of this ClientAccessKey.


        :param generation_date: The generation_date of this ClientAccessKey.
        :type: datetime
        """

        self._generation_date = generation_date

    @property
    def access_key(self):
        """Gets the access_key of this ClientAccessKey.

        An encoded access key which contains identifying information for client access token creation. For direct use with the Authress SDKs, not meant to be decoded. Must be saved on created, as it will never be returned from the API ever again. Authress only saved the corresponding public key to verify private access keys.

        :return: The access_key of this ClientAccessKey.
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        """Sets the access_key of this ClientAccessKey.

        An encoded access key which contains identifying information for client access token creation. For direct use with the Authress SDKs, not meant to be decoded. Must be saved on created, as it will never be returned from the API ever again. Authress only saved the corresponding public key to verify private access keys.

        :param access_key: The access_key of this ClientAccessKey.
        :type: str
        """

        self._access_key = access_key

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ClientAccessKey, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ClientAccessKey):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
