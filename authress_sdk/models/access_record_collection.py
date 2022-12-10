# coding: utf-8

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
