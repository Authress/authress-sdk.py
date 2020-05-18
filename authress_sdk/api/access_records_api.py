# coding: utf-8


from __future__ import absolute_import

import re

# python 2 and python 3 compatibility library
import six

from authress_sdk.api_client import ApiClient


class AccessRecordsApi(object):
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_claim(self, body, **kwargs):
        """Claim a resource by an allowed user

        Claim a resource by allowing a user to pick an identifier and receive admin access to that resource if it hasn't already been claimed. This only works for resources specifically marked as <strong>CLAIM</strong>. The result will be a new access record listing that user as the admin for this resource.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_claim(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ClaimRequest body: (required)
        :return: ClaimResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_claim_with_http_info(body, **kwargs)
        else:
            (data) = self.create_claim_with_http_info(body, **kwargs)
            return data

    def create_claim_with_http_info(self, body, **kwargs):
        """Claim a resource by an allowed user

        Claim a resource by allowing a user to pick an identifier and receive admin access to that resource if it hasn't already been claimed. This only works for resources specifically marked as <strong>CLAIM</strong>. The result will be a new access record listing that user as the admin for this resource.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_claim_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ClaimRequest body: (required)
        :return: ClaimResponse
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
                    " to method create_claim" % key
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
            '/v1/claims', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ClaimResponse',
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_records(self, **kwargs):
        """Get all account records.

        <i class=\"far fa-money-bill-alt text-primary\"></i> <span class=\"text-primary\">Billable</span> Returns a paginated records list for the account. Only records the user has access to are returned.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_records(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: AccessRecordCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_records_with_http_info(**kwargs)
        else:
            (data) = self.get_records_with_http_info(**kwargs)
            return data

    def get_records_with_http_info(self, **kwargs):
        """Get all account records.

        <i class=\"far fa-money-bill-alt text-primary\"></i> <span class=\"text-primary\">Billable</span> Returns a paginated records list for the account. Only records the user has access to are returned.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_records_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: AccessRecordCollection
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
                    " to method get_records" % key
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
            '/v1/records', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AccessRecordCollection',
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_record(self, body, **kwargs):
        """Create a new access record

        Specify user roles for specific resources.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_record(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AccessRecord body: (required)
        :return: AccessRecord
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_record_with_http_info(body, **kwargs)
        else:
            (data) = self.create_record_with_http_info(body, **kwargs)
            return data

    def create_record_with_http_info(self, body, **kwargs):
        """Create a new access record

        Specify user roles for specific resources.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_record_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AccessRecord body: (required)
        :return: AccessRecord
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
                    " to method create_record" % key
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
            '/v1/records', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AccessRecord',
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_record(self, record_id, **kwargs):
        """Deletes an access record.

        Remove an access record, removing associated permissions from all users in record. If a user has a permission from another record, that permission will not be removed.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_record(record_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str record_id: The identifier of the access record. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_record_with_http_info(record_id, **kwargs)
        else:
            (data) = self.delete_record_with_http_info(record_id, **kwargs)
            return data

    def delete_record_with_http_info(self, record_id, **kwargs):
        """Deletes an access record.

        Remove an access record, removing associated permissions from all users in record. If a user has a permission from another record, that permission will not be removed.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_record_with_http_info(record_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str record_id: The identifier of the access record. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['record_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_record" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'record_id' is set
        if ('record_id' not in params or
                params['record_id'] is None):
            raise ValueError("Missing the required parameter `record_id`.")

        collection_formats = {}

        path_params = {}
        if 'record_id' in params:
            path_params['recordId'] = params['record_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None


        return self.api_client.call_api(
            '/v1/records/{recordId}', 'DELETE',
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

    def get_record(self, record_id, **kwargs):
        """Get an access record for the account.

        Access records contain information assigning permissions to users for resources.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_record(record_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str record_id: The identifier of the access record. (required)
        :return: AccessRecord
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_record_with_http_info(record_id, **kwargs)
        else:
            (data) = self.get_record_with_http_info(record_id, **kwargs)
            return data

    def get_record_with_http_info(self, record_id, **kwargs):
        """Get an access record for the account.

        Access records contain information assigning permissions to users for resources.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_record_with_http_info(record_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str record_id: The identifier of the access record. (required)
        :return: AccessRecord
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['record_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_record" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'record_id' is set
        if ('record_id' not in params or
                params['record_id'] is None):
            raise ValueError("Missing the required parameter `record_id`.")

        collection_formats = {}

        path_params = {}
        if 'record_id' in params:
            path_params['recordId'] = params['record_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/links+json'])



        return self.api_client.call_api(
            '/v1/records/{recordId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AccessRecord',
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_record(self, body, record_id, **kwargs):
        """Update an access record.

        Updates an access record adding or removing user permissions to resources.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_record(body, record_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AccessRecord body: (required)
        :param str record_id: The identifier of the access record. (required)
        :return: AccessRecord
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_record_with_http_info(body, record_id, **kwargs)
        else:
            (data) = self.update_record_with_http_info(body, record_id, **kwargs)
            return data

    def update_record_with_http_info(self, body, record_id, **kwargs):
        """Update an access record.

        Updates an access record adding or removing user permissions to resources.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_record_with_http_info(body, record_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AccessRecord body: (required)
        :param str record_id: The identifier of the access record. (required)
        :return: AccessRecord
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'record_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_record" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body`.")
        # verify the required parameter 'record_id' is set
        if ('record_id' not in params or
                params['record_id'] is None):
            raise ValueError("Missing the required parameter `record_id`.")

        collection_formats = {}

        path_params = {}
        if 'record_id' in params:
            path_params['recordId'] = params['record_id']

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
            '/v1/records/{recordId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AccessRecord',
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
