# coding: utf-8

class AccessRecord(object):

    """
    Attributes:
      openapi_spec_types (dict): The key is attribute name and the value is attribute type.
      attribute_serialization_map (dict): The key is attribute name and the value is json key in definition.
    """
    openapi_spec_types = {
        'record_id': 'str',
        'name': 'str',
        'account': 'AccessRecordAccount',
        'users': 'list[AccessRecordUser]',
        'groups': 'list[AccessRecordGroup]',
        'admins': 'list[AccessRecordUser]',
        'statements': 'list[AccessRecordStatement]',
        'links': 'object'
    }

    attribute_serialization_map = {
        'record_id': 'recordId',
        'name': 'name',
        'account': 'account',
        'users': 'users',
        'groups': 'groups',
        'admins': 'admins',
        'statements': 'statements',
        'links': 'links'
    }

    def __init__(self, record_id=None, name=None, account=None, users=None, admins=None, statements=None, links=None, groups=None):
        """AccessRecord"""
        self._record_id = None
        self._name = None
        self._account = None
        self._users = None
        self._groups = None
        self._admins = None
        self._statements = None
        self._links = None
        self.record_id = record_id
        self.name = name
        self.account = account
        self.users = users
        self.groups = groups
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
        :rtype: list[AccessRecordUser]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this AccessRecord.

        The list of users this record applies to

        :param users: The users of this AccessRecord.
        :type: list[AccessRecordUser]
        """
        self._users = users

    @property
    def groups(self):
        """Gets the groups of this AccessRecord.

        The list of groups this record applies to. Users in these groups will be receive access to the resources listed.

        :return: The groups of this AccessRecord.
        :rtype: list[AccessRecordGroup]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this AccessRecord.

        The list of groups this record applies to. Users in these groups will be receive access to the resources listed.

        :param groups: The groups of this AccessRecord.
        :type: list[AccessRecordGroup]
        """
        self._groups = groups

    @property
    def admins(self):
        """Gets the admins of this AccessRecord.

        The list of admin that can edit this record even if they do not have global record edit permissions.

        :return: The admins of this AccessRecord.
        :rtype: list[AccessRecordUser]
        """
        return self._admins

    @admins.setter
    def admins(self, admins):
        """Sets the admins of this AccessRecord.

        The list of admin that can edit this record even if they do not have global record edit permissions.

        :param admins: The admins of this AccessRecord.
        :type: list[AccessRecordUser]
        """
        self._admins = admins

    @property
    def statements(self):
        """Gets the statements of this AccessRecord.

        A list of statements which match roles to resources. Users in this record have all statements apply to them

        :return: The statements of this AccessRecord.
        :rtype: list[AccessRecordStatement]
        """
        return self._statements

    @statements.setter
    def statements(self, statements):
        """Sets the statements of this AccessRecord.

        A list of statements which match roles to resources. Users in this record have all statements apply to them

        :param statements: The statements of this AccessRecord.
        :type: list[AccessRecordStatement]
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
