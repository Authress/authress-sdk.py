# coding: utf-8


from __future__ import absolute_import

import re

# python 2 and python 3 compatibility library
import six

from authress_sdk.api_client import ApiClient


class ResourcePermissionsApi(object):
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_resources(self, **kwargs):
        """List resource configurations

        Permissions can be set globally at a resource level. Lists any resources with a globally set resource policy
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_resources(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ResourcePermissionCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_resources_with_http_info(**kwargs)
        else:
            (data) = self.get_resources_with_http_info(**kwargs)
            return data

    def get_resources_with_http_info(self, **kwargs):
        """List resource configurations

        Permissions can be set globally at a resource level. Lists any resources with a globally set resource policy
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_resources_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ResourcePermissionCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_resources" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/links+json'])



        return self.api_client.call_api(
            '/v1/resources', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResourcePermissionCollection',

            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_resource_permissions(self, resource_uri, **kwargs):
        """Get a resource permissions object.

        Permissions can be set globally at a resource level. This will apply to all users in an account.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_resource_permissions(resource_uri, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str resource_uri: The uri path of a resource to validate, uri segments are allowed. (required)
        :return: ResourcePermission
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_resource_permissions_with_http_info(resource_uri, **kwargs)
        else:
            (data) = self.get_resource_permissions_with_http_info(resource_uri, **kwargs)
            return data

    def get_resource_permissions_with_http_info(self, resource_uri, **kwargs):
        """Get a resource permissions object.

        Permissions can be set globally at a resource level. This will apply to all users in an account.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_resource_permissions_with_http_info(resource_uri, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str resource_uri: The uri path of a resource to validate, uri segments are allowed. (required)
        :return: ResourcePermission
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['resource_uri']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_resource_permissions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'resource_uri' is set
        if ('resource_uri' not in params or
                params['resource_uri'] is None):
            raise ValueError("Missing the required parameter `resource_uri`.")

        collection_formats = {}

        path_params = {}
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
            '/v1/resources/{resourceUri}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResourcePermission',

            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def set_resource_permissions(self, body, resource_uri, **kwargs):
        """Update a resource permissions object.

        Updates the global permissions on a resource. This applies to all users in an account.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_resource_permissions(body, resource_uri, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ResourcePermission body: The contents of the permission to set on the resource. Overwrites existing data. (required)
        :param str resource_uri: The uri path of a resource to validate, uri segments are allowed. (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.set_resource_permissions_with_http_info(body, resource_uri, **kwargs)
        else:
            (data) = self.set_resource_permissions_with_http_info(body, resource_uri, **kwargs)
            return data

    def set_resource_permissions_with_http_info(self, body, resource_uri, **kwargs):
        """Update a resource permissions object.

        Updates the global permissions on a resource. This applies to all users in an account.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_resource_permissions_with_http_info(body, resource_uri, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ResourcePermission body: The contents of the permission to set on the resource. Overwrites existing data. (required)
        :param str resource_uri: The uri path of a resource to validate, uri segments are allowed. (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'resource_uri']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_resource_permissions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body`.")
        # verify the required parameter 'resource_uri' is set
        if ('resource_uri' not in params or
                params['resource_uri'] is None):
            raise ValueError("Missing the required parameter `resource_uri`.")

        collection_formats = {}

        path_params = {}
        if 'resource_uri' in params:
            path_params['resourceUri'] = params['resource_uri']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/links+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])



        return self.api_client.call_api(
            '/v1/resources/{resourceUri}', 'PUT',
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
