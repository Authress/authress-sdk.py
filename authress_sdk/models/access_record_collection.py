# coding: utf-8


import pprint
import re

import six


class AccessRecordCollection(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'records': 'list[AccessRecord]'
    }

    attribute_map = {
        'records': 'records'
    }

    def __init__(self, records=None):
        """AccessRecordCollection"""
        self._records = None
        self.discriminator = None
        self.records = records

    @property
    def records(self):
        """Gets the records of this AccessRecordCollection.


        :return: The records of this AccessRecordCollection.
        :rtype: list[AccessRecord]
        """
        return self._records

    @records.setter
    def records(self, records):
        """Sets the records of this AccessRecordCollection.


        :param records: The records of this AccessRecordCollection.
        :type: list[AccessRecord]
        """
        if records is None:
            raise ValueError("Invalid value for `records`, must not be `None`")

        self._records = records

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
        if issubclass(AccessRecordCollection, dict):
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
        if not isinstance(other, AccessRecordCollection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
