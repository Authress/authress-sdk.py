# coding: utf-8

class AccessRecordAccount(object):

    """
    Attributes:
      openapi_spec_types (dict): The key is attribute name and the value is attribute type.
      attribute_serialization_map (dict): The key is attribute name and the value is json key in definition.
    """
    openapi_spec_types = {
        'account_id': 'str'
    }

    attribute_serialization_map = {
        'account_id': 'accountId'
    }

    def __init__(self, account_id=None):
        """AccessRecordAccount"""
        self._account_id = None
        self.account_id = account_id

    @property
    def account_id(self) -> str:
        """Gets the account_id of this AccessRecordAccount.


        :return: The account_id of this AccessRecordAccount.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id: str):
        """Sets the account_id of this AccessRecordAccount.


        :param account_id: The account_id of this AccessRecordAccount.
        :type: str
        """
        self._account_id = account_id
