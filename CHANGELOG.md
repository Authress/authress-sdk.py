# Change log
This is the changelog for [Authress SDK](readme.md).

## 3.0 ##
* Added type checking everywhere
* Converted properties to be consistent across all generators
* [Breaking] Moved `authress_client.users` api to `authress_client.user_permissions`.
* [Breaking] Moved `authress_client.records` api to `authress_client.access_records`.
* [Breaking] Moved `authress_client.clients` api to `authress_client.service_clients`.
* [Breaking] Renamed `AccessRecordStatement` model to `Statement` in `models.statement.py`.
* [Breaking] Renamed `AccessRecordResource` model to `Resource` in `models.resource.py`.

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
