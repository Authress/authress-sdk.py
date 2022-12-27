# coding: utf-8

class AccessRecordUser(object):

    """
    Attributes:
      openapi_spec_types (dict): The key is attribute name and the value is attribute type.
      attribute_serialization_map (dict): The key is attribute name and the value is json key in definition.
    """
    openapi_spec_types = {
        'user_id': 'str'
    }

    attribute_serialization_map = {
        'user_id': 'userId'
    }

    def __init__(self, user_id=None):
        """AccessRecordUser"""
        self._user_id = None
        self.user_id = user_id

    @property
    def user_id(self):
        """Gets the user_id of this AccessRecordUser.


        :return: The user_id of this AccessRecordUser.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this AccessRecordUser.


        :param user_id: The user_id of this AccessRecordUser.
        :type: str
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")

        self._user_id = user_id
