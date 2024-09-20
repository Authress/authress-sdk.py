# Change log
This is the changelog for [Authress SDK](readme.md).

## 3.1 ##
* [Breaking] Throw validation error on setting a property that doesn't exist in any of the Authress DTO Models.

## 3.0 ##
* [Breaking] Added type checking everywhere - This means most models have breaking changes.
* [Breaking] Converted properties to be consistent across all generators
* [Breaking] User ID is now explicitly required in the user permissions api methods to ensure that the correct user ID is being passed.
* [Breaking] Moved `authress_client.users` api to `authress_client.user_permissions`.
* [Breaking] Moved `authress_client.records` api to `authress_client.access_records`.
* [Breaking] Moved `authress_client.clients` api to `authress_client.service_clients`.
* [Breaking] Renamed `AccessRecordStatement` model to `Statement` in `models.statement.py`.
* [Breaking] Renamed `AccessRecordResource` model to `Resource` in `models.resource.py`.
* [Breaking] Renamed parameter `if_unmodified_since` in the Access Record API to be `expected_last_modified_time`.
* Add missing `If-Unmodified-Since` support to the `update_group` in the `Groups` API.
* Improve caching in `verify_token`
* Support additionally pydantic v2 dependencies. Support for v1 will be removed in a future version.
* Prevent unnecessary extra trailing slashes in domain name.
* Add support for the `generateUserLoginUrl` from the ServiceClientTokenProvider.
* [Breaking] Removed client_id from ClientAccessKey.py model, because it does not contain a clientId when fetching client data.
* Add support for `tokenConfiguration` at the tenant level.

## 2.0 ##
* Add support for users and groups at the statement level of access records.
* Fix naming of some incorrectly named plural classes in the Access Record Models.
* Rename `HttpClient` to `AuthressClient` and split out non-essential functionality to a separate HttpClient.
* Add `limit`, `filter`, `cursor` to `get_records` endpoint.

## 1.1 ##
* Add the `TokenVerifier`

## 1.0 ##
* Add EdDSA support
* Add `Groups` to `AccessRecords`
* Explicitly set the algorithms in decoding the user token to identify the user sub
