# coding: utf-8

class AccountCollection(object):

    """
    Attributes:
      openapi_spec_types (dict): The key is attribute name and the value is attribute type.
      attribute_serialization_map (dict): The key is attribute name and the value is json key in definition.
    """
    openapi_spec_types = {
        'accounts': 'list[Account]'
    }

    attribute_serialization_map = {
        'accounts': 'accounts'
    }

    def __init__(self, accounts=None):
        """AccountCollection"""
        self._accounts = None
        self.accounts = accounts

    @property
    def accounts(self):
        """Gets the accounts of this AccountCollection.


        :return: The accounts of this AccountCollection.
        :rtype: list[Account]
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """Sets the accounts of this AccountCollection.


        :param accounts: The accounts of this AccountCollection.
        :type: list[Account]
        """
        self._accounts = accounts
