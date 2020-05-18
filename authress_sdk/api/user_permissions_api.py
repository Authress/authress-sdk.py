# coding: utf-8


from __future__ import absolute_import

import re

# python 2 and python 3 compatibility library
import six

from authress_sdk.api_client import ApiClient


class UserPermissionsApi(object):
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_user_resources(self, user_id, **kwargs):
        """Get the resources a user has to permission to.

        <i class=\"far fa-money-bill-alt text-primary\"></i> <span class=\"text-primary\">Billable</span> Get most conservative resource permission a user has access to. Since resource uris are cascading, a user with * access will always return a list with a single result. In the case that the user only has access to a list of resources in a collection, the list will be paginated.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_resources(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: The user to check permissions on, if not specified will use the token sub as the expected user to authorize
        :param str resource_uri: The top level uri path of a resource to query for. Will only match explicit or collection resource children. Will not partial match resource names.
        :return: UserResources
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if user_id is None:
          user_id = self.api_client.get_user_from_token()

        if kwargs.get('async_req'):
            return self.get_user_resources_with_http_info(user_id, **kwargs)
        else:
            (data) = self.get_user_resources_with_http_info(user_id, **kwargs)
            return data

    def get_user_resources_with_http_info(self, user_id, **kwargs):
        """Get the resources a user has to permission to.

        <i class=\"far fa-money-bill-alt text-primary\"></i> <span class=\"text-primary\">Billable</span> Get most conservative resource permission a user has access to. Since resource uris are cascading, a user with * access will always return a list with a single result. In the case that the user only has access to a list of resources in a collection, the list will be paginated.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_resources_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: The user to check permissions on (required)
        :param str resource_uri: The top level uri path of a resource to query for. Will only match explicit or collection resource children. Will not partial match resource names.
        :return: UserResources
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'resource_uri']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_resources" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id`.")

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']

        query_params = []
        if 'resource_uri' in params:
            query_params.append(('resourceUri', params['resource_uri']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/links+json'])



        return self.api_client.call_api(
            '/v1/users/{userId}/resources', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserResources',

            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_authorization_for_resource (self, user_id, resource_uri, **kwargs):
        """Get the permissions a user has to a resource.

        <i class=\"far fa-money-bill-alt text-primary\"></i> <span class=\"text-primary\">Billable</span> Get a summary of the permissions a user has to a particular resource.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_authorization_for_resource(user_id, resource_uri, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: The user to check permissions on, if not specified will use the token sub as the expected user to authorize
        :param str resource_uri: The uri path of a resource to validate, uri segments are allowed. (required)
        :return: UserPermissions
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if user_id is None:
          user_id = self.api_client.get_user_from_token()

        if kwargs.get('async_req'):
            return self.get_user_authorization_for_resource_with_http_info(user_id, resource_uri, **kwargs)
        else:
            (data) = self.get_user_authorization_for_resource_with_http_info(user_id, resource_uri, **kwargs)
            return data

    def get_user_authorization_for_resource_with_http_info(self, user_id, resource_uri, **kwargs):
        """Get the permissions a user has to a resource.

        <i class=\"far fa-money-bill-alt text-primary\"></i> <span class=\"text-primary\">Billable</span> Get a summary of the permissions a user has to a particular resource.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_authorization_for_resource_with_http_info(user_id, resource_uri, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: The user to check permissions on (required)
        :param str resource_uri: The uri path of a resource to validate, uri segments are allowed. (required)
        :return: UserPermissions
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'resource_uri']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_authorization_for_resource" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id`.")
        # verify the required parameter 'resource_uri' is set
        if ('resource_uri' not in params or
                params['resource_uri'] is None):
            raise ValueError("Missing the required parameter `resource_uri`.")

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']
        if 'resource_uri' in params:
            path_params['resourceUri'] = params['resource_uri']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/links+json'])



        return self.api_client.call_api(
            '/v1/users/{userId}/resources/{resourceUri}/permissions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserPermissions',

            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def authorize_user(self, user_id, resource_uri, permission, **kwargs):
        """Check to see if a user has permissions to a resource.

        <i class=\"far fa-money-bill-alt text-primary\"></i> <span class=\"text-primary\">Billable</span> Does the user have the specified permissions to the resource?
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.authorize_user(user_id, resource_uri, permission, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: The user to check permissions on, if not specified will use the token sub as the expected user to authorize
        :param str resource_uri: The uri path of a resource to validate, uri segments are allowed, the resource must be a full path, and permissions are not inherited by sub resources. (required)
        :param str permission: Permission to check, '*' and scoped permissions can also be checked here. (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True


        if user_id is None:
          user_id = self.api_client.get_user_from_token()

        if kwargs.get('async_req'):
            return self.authorize_user_with_http_info(user_id, resource_uri, permission, **kwargs)
        else:
            (data) = self.authorize_user_with_http_info(user_id, resource_uri, permission, **kwargs)
            return data

    def authorize_user_with_http_info(self, user_id, resource_uri, permission, **kwargs):
        """Check to see if a user has permissions to a resource.

        <i class=\"far fa-money-bill-alt text-primary\"></i> <span class=\"text-primary\">Billable</span> Does the user have the specified permissions to the resource?
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.authorize_user_with_http_info(user_id, resource_uri, permission, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: The user to check permissions on (required)
        :param str resource_uri: The uri path of a resource to validate, uri segments are allowed, the resource must be a full path, and permissions are not inherited by sub resources. (required)
        :param str permission: Permission to check, '*' and scoped permissions can also be checked here. (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'resource_uri', 'permission']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method authorize_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id`.")
        # verify the required parameter 'resource_uri' is set
        if ('resource_uri' not in params or
                params['resource_uri'] is None):
            raise ValueError("Missing the required parameter `resource_uri`.")
        # verify the required parameter 'permission' is set
        if ('permission' not in params or
                params['permission'] is None):
            raise ValueError("Missing the required parameter `permission`.")

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']
        if 'resource_uri' in params:
            path_params['resourceUri'] = params['resource_uri']
        if 'permission' in params:
            path_params['permission'] = params['permission']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/links+json'])

        return self.api_client.call_api(
            '/v1/users/{userId}/resources/{resourceUri}/permissions/{permission}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',

            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
