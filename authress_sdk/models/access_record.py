# coding: utf-8


import pprint
import re

import six


class AccessRecord(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'record_id': 'str',
        'name': 'str',
        'account': 'AccessRecordAccount',
        'users': 'list[AccessRecordUsers]',
        'admins': 'list[AccessRecordUsers]',
        'statements': 'list[AccessRecordStatements]',
        'links': 'object'
    }

    attribute_map = {
        'record_id': 'recordId',
        'name': 'name',
        'account': 'account',
        'users': 'users',
        'admins': 'admins',
        'statements': 'statements',
        'links': 'links'
    }

    def __init__(self, record_id=None, name=None, account=None, users=None, admins=None, statements=None, links=None):
        """AccessRecord"""
        self._record_id = None
        self._name = None
        self._account = None
        self._users = None
        self._admins = None
        self._statements = None
        self._links = None
        self.discriminator = None
        self.record_id = record_id
        self.name = name
        self.account = account
        self.users = users
        self.admins = admins
        self.statements = statements
        self.links = links

    @property
    def record_id(self):
        """Gets the record_id of this AccessRecord.

        Unique identifier for the record, can be specified on record creation.

        :return: The record_id of this AccessRecord.
        :rtype: str
        """
        return self._record_id

    @record_id.setter
    def record_id(self, record_id):
        """Sets the record_id of this AccessRecord.

        Unique identifier for the record, can be specified on record creation.

        :param record_id: The record_id of this AccessRecord.
        :type: str
        """
        self._record_id = record_id

    @property
    def name(self):
        """Gets the name of this AccessRecord.

        A helpful name for this record

        :return: The name of this AccessRecord.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AccessRecord.

        A helpful name for this record

        :param name: The name of this AccessRecord.
        :type: str
        """
        self._name = name

    @property
    def account(self):
        """Gets the account of this AccessRecord.


        :return: The account of this AccessRecord.
        :rtype: AccessRecordAccount
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this AccessRecord.


        :param account: The account of this AccessRecord.
        :type: AccessRecordAccount
        """
        self._account = account

    @property
    def users(self):
        """Gets the users of this AccessRecord.

        The list of users this record applies to

        :return: The users of this AccessRecord.
        :rtype: list[AccessRecordUsers]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this AccessRecord.

        The list of users this record applies to

        :param users: The users of this AccessRecord.
        :type: list[AccessRecordUsers]
        """
        self._users = users

    @property
    def admins(self):
        """Gets the admins of this AccessRecord.

        The list of admin that can edit this record even if they do not have global record edit permissions.

        :return: The admins of this AccessRecord.
        :rtype: list[AccessRecordUsers]
        """
        return self._admins

    @admins.setter
    def admins(self, admins):
        """Sets the admins of this AccessRecord.

        The list of admin that can edit this record even if they do not have global record edit permissions.

        :param admins: The admins of this AccessRecord.
        :type: list[AccessRecordUsers]
        """
        self._admins = admins

    @property
    def statements(self):
        """Gets the statements of this AccessRecord.

        A list of statements which match roles to resources. Users in this record have all statements apply to them

        :return: The statements of this AccessRecord.
        :rtype: list[AccessRecordStatements]
        """
        return self._statements

    @statements.setter
    def statements(self, statements):
        """Sets the statements of this AccessRecord.

        A list of statements which match roles to resources. Users in this record have all statements apply to them

        :param statements: The statements of this AccessRecord.
        :type: list[AccessRecordStatements]
        """
        if statements is None:
            raise ValueError("Invalid value for `statements`, must not be `None`")

        self._statements = statements

    @property
    def links(self):
        """Gets the links of this AccessRecord.


        :return: The links of this AccessRecord.
        :rtype: object
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this AccessRecord.


        :param links: The links of this AccessRecord.
        :type: object
        """
        self._links = links

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
        if issubclass(AccessRecord, dict):
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
        if not isinstance(other, AccessRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
