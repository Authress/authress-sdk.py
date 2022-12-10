# coding: utf-8

class AccessRecordGroup(object):

    """
    Attributes:
      openapi_spec_types (dict): The key is attribute name and the value is attribute type.
      attribute_serialization_map (dict): The key is attribute name and the value is json key in definition.
    """
    openapi_spec_types = {
        'group_id': 'str'
    }

    attribute_serialization_map = {
        'group_id': 'groupId'
    }

    def __init__(self, group_id=None):
        """AccessRecordGroup"""
        self._group_id = None
        self.group_id = group_id

    @property
    def group_id(self):
        """Gets the group_id of this AccessRecordGroup.


        :return: The group_id of this AccessRecordGroup.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this AccessRecordGroup.


        :param group_id: The group_id of this AccessRecordGroup.
        :type: str
        """
        if group_id is None:
            raise ValueError("Invalid value for `group_id`, must not be `None`")

        self._group_id = group_id
