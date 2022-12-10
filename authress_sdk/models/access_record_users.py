# coding: utf-8

class AccessRecordUsers(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'user_id': 'str'
    }

    attribute_map = {
        'user_id': 'userId'
    }

    def __init__(self, user_id=None):
        """AccessRecordUsers"""
        self._user_id = None
        self.user_id = user_id

    @property
    def user_id(self):
        """Gets the user_id of this AccessRecordUsers.


        :return: The user_id of this AccessRecordUsers.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this AccessRecordUsers.


        :param user_id: The user_id of this AccessRecordUsers.
        :type: str
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")

        self._user_id = user_id
