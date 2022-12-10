# coding: utf-8

class IdentityRequest(object):

    """
    Attributes:
      openapi_spec_types (dict): The key is attribute name and the value is attribute type.
      attribute_serialization_map (dict): The key is attribute name and the value is json key in definition.
    """
    openapi_spec_types = {
        'jwt': 'str',
        'preferred_audience': 'str'
    }

    attribute_serialization_map = {
        'jwt': 'jwt',
        'preferred_audience': 'preferredAudience'
    }

    def __init__(self, jwt=None, preferred_audience=None):
        """IdentityRequest"""
        self._jwt = None
        self._preferred_audience = None
        self.jwt = jwt
        if preferred_audience is not None:
            self.preferred_audience = preferred_audience

    @property
    def jwt(self):
        """Gets the jwt of this IdentityRequest.

        A valid JWT OIDC compliant token which will still pass authentication requests to the identity provider. Must contain a unique audience and issuer.

        :return: The jwt of this IdentityRequest.
        :rtype: str
        """
        return self._jwt

    @jwt.setter
    def jwt(self, jwt):
        """Sets the jwt of this IdentityRequest.

        A valid JWT OIDC compliant token which will still pass authentication requests to the identity provider. Must contain a unique audience and issuer.

        :param jwt: The jwt of this IdentityRequest.
        :type: str
        """
        if jwt is None:
            raise ValueError("Invalid value for `jwt`, must not be `None`")

        self._jwt = jwt

    @property
    def preferred_audience(self):
        """Gets the preferred_audience of this IdentityRequest.

        If the `jwt` token contains more than one valid audience, then the single audience that should associated with Authress. If more than one audience is preferred, repeat this call with each one.

        :return: The preferred_audience of this IdentityRequest.
        :rtype: str
        """
        return self._preferred_audience

    @preferred_audience.setter
    def preferred_audience(self, preferred_audience):
        """Sets the preferred_audience of this IdentityRequest.

        If the `jwt` token contains more than one valid audience, then the single audience that should associated with Authress. If more than one audience is preferred, repeat this call with each one.

        :param preferred_audience: The preferred_audience of this IdentityRequest.
        :type: str
        """

        self._preferred_audience = preferred_audience
