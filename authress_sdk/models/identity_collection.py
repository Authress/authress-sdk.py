# coding: utf-8

class IdentityCollection(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'identities': 'list[Identity]'
    }

    attribute_map = {
        'identities': 'identities'
    }

    def __init__(self, identities=None):
        """IdentityCollection"""
        self._identities = None
        self.identities = identities

    @property
    def identities(self):
        """Gets the identities of this IdentityCollection.


        :return: The identities of this IdentityCollection.
        :rtype: list[Identity]
        """
        return self._identities

    @identities.setter
    def identities(self, identities):
        """Sets the identities of this IdentityCollection.


        :param identities: The identities of this IdentityCollection.
        :type: list[Identity]
        """
        if identities is None:
            raise ValueError("Invalid value for `identities`, must not be `None`")

        self._identities = identities
