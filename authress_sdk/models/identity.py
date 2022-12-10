# coding: utf-8

class Identity(object):

    """
    Attributes:
      openapi_spec_types (dict): The key is attribute name and the value is attribute type.
      attribute_serialization_map (dict): The key is attribute name and the value is json key in definition.
    """
    openapi_spec_types = {
        'issuer': 'str',
        'audience': 'str'
    }

    attribute_serialization_map = {
        'issuer': 'issuer',
        'audience': 'audience'
    }

    def __init__(self, issuer=None, audience=None):
        """Identity"""
        self._issuer = None
        self._audience = None
        self.issuer = issuer
        self.audience = audience

    @property
    def issuer(self):
        """Gets the issuer of this Identity.

        The issuer of the JWT token. This can be any OIDC compliant provider.

        :return: The issuer of this Identity.
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this Identity.

        The issuer of the JWT token. This can be any OIDC compliant provider.

        :param issuer: The issuer of this Identity.
        :type: str
        """
        if issuer is None:
            raise ValueError("Invalid value for `issuer`, must not be `None`")

        self._issuer = issuer

    @property
    def audience(self):
        """Gets the audience of this Identity.

        The target of the JWT tokens. This must be a sub target of the account app or the whole app

        :return: The audience of this Identity.
        :rtype: str
        """
        return self._audience

    @audience.setter
    def audience(self, audience):
        """Sets the audience of this Identity.

        The target of the JWT tokens. This must be a sub target of the account app or the whole app

        :param audience: The audience of this Identity.
        :type: str
        """
        if audience is None:
            raise ValueError("Invalid value for `audience`, must not be `None`")

        self._audience = audience
