# coding: utf-8

class ClaimRequest(object):

    """
    Attributes:
      openapi_spec_types (dict): The key is attribute name and the value is attribute type.
      attribute_serialization_map (dict): The key is attribute name and the value is json key in definition.
    """
    openapi_spec_types = {
        'collection_resource': 'str',
        'resource_id': 'str'
    }

    attribute_serialization_map = {
        'collection_resource': 'collectionResource',
        'resource_id': 'resourceId'
    }

    def __init__(self, collection_resource=None, resource_id=None):
        """ClaimRequest"""
        self._collection_resource = None
        self._resource_id = None
        self.collection_resource = collection_resource
        self.resource_id = resource_id

    @property
    def collection_resource(self):
        """Gets the collection_resource of this ClaimRequest.

        The parent resource to add a child resource to. The resource must have a resource configuration that add the permission CLAIM for this to work.

        :return: The collection_resource of this ClaimRequest.
        :rtype: str
        """
        return self._collection_resource

    @collection_resource.setter
    def collection_resource(self, collection_resource):
        """Sets the collection_resource of this ClaimRequest.

        The parent resource to add a child resource to. The resource must have a resource configuration that add the permission CLAIM for this to work.

        :param collection_resource: The collection_resource of this ClaimRequest.
        :type: str
        """
        if collection_resource is None:
            raise ValueError("Invalid value for `collection_resource`, must not be `None`")

        self._collection_resource = collection_resource

    @property
    def resource_id(self):
        """Gets the resource_id of this ClaimRequest.

        The child resource the user is requesting Admin ownership over.

        :return: The resource_id of this ClaimRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ClaimRequest.

        The child resource the user is requesting Admin ownership over.

        :param resource_id: The resource_id of this ClaimRequest.
        :type: str
        """
        if resource_id is None:
            raise ValueError("Invalid value for `resource_id`, must not be `None`")

        self._resource_id = resource_id
