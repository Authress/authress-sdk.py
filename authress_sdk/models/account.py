# coding: utf-8


import pprint
import re

import six


class Account(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'account_id': 'str',
        'created_time': 'datetime',
        'domain': 'str',
        'company': 'object',
        'links': 'object'
    }

    attribute_map = {
        'account_id': 'accountId',
        'created_time': 'createdTime',
        'domain': 'domain',
        'company': 'company',
        'links': 'links'
    }

    def __init__(self, account_id=None, created_time=None, domain=None, company=None, links=None):
        """Account"""
        self._account_id = None
        self._created_time = None
        self._domain = None
        self._company = None
        self._links = None
        self.discriminator = None
        self.account_id = account_id
        self.created_time = created_time
        self.domain = domain
        self.company = company
        self.links = links

    @property
    def account_id(self):
        """Gets the account_id of this Account.


        :return: The account_id of this Account.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this Account.


        :param account_id: The account_id of this Account.
        :type: str
        """
        self._account_id = account_id

    @property
    def created_time(self):
        """Gets the created_time of this Account.


        :return: The created_time of this Account.
        :rtype: datetime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this Account.


        :param created_time: The created_time of this Account.
        :type: datetime
        """
        self._created_time = created_time

    @property
    def domain(self):
        """Gets the domain of this Account.

        The top authress sub domain specific for this account to be used with this API.

        :return: The domain of this Account.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this Account.

        The top authress sub domain specific for this account to be used with this API.

        :param domain: The domain of this Account.
        :type: str
        """
        self._domain = domain

    @property
    def company(self):
        """Gets the company of this Account.


        :return: The company of this Account.
        :rtype: object
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this Account.


        :param company: The company of this Account.
        :type: object
        """
        self._company = company

    @property
    def links(self):
        """Gets the links of this Account.


        :return: The links of this Account.
        :rtype: object
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Account.


        :param links: The links of this Account.
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
        if issubclass(Account, dict):
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
        if not isinstance(other, Account):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
