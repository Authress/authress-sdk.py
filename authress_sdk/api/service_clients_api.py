# coding: utf-8


from __future__ import absolute_import

import re

# python 2 and python 3 compatibility library
import six

from authress_sdk.api_client import ApiClient


class ServiceClientsApi(object):
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_access_key(self, client_id, key_id, **kwargs):
        """Remove an access key for a client

        Deletes an access key for a client prevent it from being used to authenticate with Authress.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_access_key(client_id, key_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str client_id: The unique identifier of the client. (required)
        :param str key_id: The id of the access key to remove from the client. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_access_key_with_http_info(client_id, key_id, **kwargs)
        else:
            (data) = self.delete_access_key_with_http_info(client_id, key_id, **kwargs)
            return data

    def delete_access_key_with_http_info(self, client_id, key_id, **kwargs):
        """Remove an access key for a client

        Deletes an access key for a client prevent it from being used to authenticate with Authress.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_access_key_with_http_info(client_id, key_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str client_id: The unique identifier of the client. (required)
        :param str key_id: The id of the access key to remove from the client. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['client_id', 'key_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_access_key" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'client_id' is set
        if ('client_id' not in params or
                params['client_id'] is None):
            raise ValueError("Missing the required parameter `client_id`.")
        # verify the required parameter 'key_id' is set
        if ('key_id' not in params or
                params['key_id'] is None):
            raise ValueError("Missing the required parameter `key_id`.")

        collection_formats = {}

        path_params = {}
        if 'client_id' in params:
            path_params['clientId'] = params['client_id']
        if 'key_id' in params:
            path_params['keyId'] = params['key_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None


        return self.api_client.call_api(
            '/v1/clients/{clientId}/access-keys/{keyId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,

            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def request_access_key(self, client_id, **kwargs):
        """Request a new access key

        Create a new access key for the client so that a service can authenticate with Authress as that client. Using the client will allow delegation of permission checking of users.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.request_access_key(client_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str client_id: The unique identifier of the client. (required)
        :return: ClientAccessKey
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.request_access_key_with_http_info(client_id, **kwargs)
        else:
            (data) = self.request_access_key_with_http_info(client_id, **kwargs)
            return data

    def request_access_key_with_http_info(self, client_id, **kwargs):
        """Request a new access key

        Create a new access key for the client so that a service can authenticate with Authress as that client. Using the client will allow delegation of permission checking of users.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.request_access_key_with_http_info(client_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str client_id: The unique identifier of the client. (required)
        :return: ClientAccessKey
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['client_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method request_access_key" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'client_id' is set
        if ('client_id' not in params or
                params['client_id'] is None):
            raise ValueError("Missing the required parameter `client_id`.")

        collection_formats = {}

        path_params = {}
        if 'client_id' in params:
            path_params['clientId'] = params['client_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/links+json'])



        return self.api_client.call_api(
            '/v1/clients/{clientId}/access-keys', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ClientAccessKey',

            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_client(self, client_id, **kwargs):
        """Delete a client

        This deletes the service client.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_client(client_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str client_id: The unique identifier for the client. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_client_with_http_info(client_id, **kwargs)
        else:
            (data) = self.delete_client_with_http_info(client_id, **kwargs)
            return data

    def delete_client_with_http_info(self, client_id, **kwargs):
        """Delete a client

        This deletes the service client.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_client_with_http_info(client_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str client_id: The unique identifier for the client. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['client_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_clients_client_id_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'client_id' is set
        if ('client_id' not in params or
                params['client_id'] is None):
            raise ValueError("Missing the required parameter `client_id`.")

        collection_formats = {}

        path_params = {}
        if 'client_id' in params:
            path_params['clientId'] = params['client_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None


        return self.api_client.call_api(
            '/v1/clients/{clientId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,

            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_client(self, client_id, **kwargs):
        """Get a client.

        Returns all information related to client except for the private access keys.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_client(client_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str client_id: The unique identifier for the client. (required)
        :return: Client
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_client_with_http_info(client_id, **kwargs)
        else:
            (data) = self.get_client_with_http_info(client_id, **kwargs)
            return data

    def get_client_with_http_info(self, client_id, **kwargs):
        """Get a client.

        Returns all information related to client except for the private access keys.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_client_with_http_info(client_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str client_id: The unique identifier for the client. (required)
        :return: Client
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['client_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_client" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'client_id' is set
        if ('client_id' not in params or
                params['client_id'] is None):
            raise ValueError("Missing the required parameter `client_id`.")

        collection_formats = {}

        path_params = {}
        if 'client_id' in params:
            path_params['clientId'] = params['client_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/links+json'])



        return self.api_client.call_api(
            '/v1/clients/{clientId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Client',

            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_client(self, body, client_id, **kwargs):
        """Update a client

        Updates a client information.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_client(body, client_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Client body: (required)
        :param str client_id: The unique identifier for the client. (required)
        :return: Client
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_client_http_info(body, client_id, **kwargs)
        else:
            (data) = self.update_client_http_info(body, client_id, **kwargs)
            return data

    def update_client_http_info(self, body, client_id, **kwargs):
        """Update a client

        Updates a client information.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_client_http_info(body, client_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Client body: (required)
        :param str client_id: The unique identifier for the client. (required)
        :return: Client
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'client_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_clients_client_id_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body`.")
        # verify the required parameter 'client_id' is set
        if ('client_id' not in params or
                params['client_id'] is None):
            raise ValueError("Missing the required parameter `client_id`.")

        collection_formats = {}

        path_params = {}
        if 'client_id' in params:
            path_params['clientId'] = params['client_id']

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
            '/v1/clients/{clientId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Client',

            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_clients(self, **kwargs):
        """Get clients collection

        Returns all clients that the user has access to in the account.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_clients(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ClientCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_clients_with_http_info(**kwargs)
        else:
            (data) = self.get_clients_with_http_info(**kwargs)
            return data

    def get_clients_with_http_info(self, **kwargs):
        """Get clients collection

        Returns all clients that the user has access to in the account.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_clients_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ClientCollection
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
                    " to method get_clients" % key
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
            '/v1/clients', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ClientCollection',

            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_client(self, body, **kwargs):
        """Create a new client.

        Creates a service client to interact with Authress or any other service on behalf of users. Each client has secret private keys used to authenticate with Authress. To use service clients created through other mechanisms, skip creating a client and create access records with the client identifier.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_client(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Client body: (required)
        :return: Client
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_client_with_http_info(body, **kwargs)
        else:
            (data) = self.create_client_with_http_info(body, **kwargs)
            return data

    def create_client_with_http_info(self, body, **kwargs):
        """Create a new client.

        Creates a service client to interact with Authress or any other service on behalf of users. Each client has secret private keys used to authenticate with Authress. To use service clients created through other mechanisms, skip creating a client and create access records with the client identifier.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_client_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Client body: (required)
        :return: Client
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_client" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body`.")

        collection_formats = {}

        path_params = {}

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
            '/v1/clients', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Client',

            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
