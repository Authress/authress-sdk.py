# Change log
This is the changelog for [Authress SDK](readme.md).

## 2.0 ##
* Add support for users and groups at the statement level of access records.
* Fix naming of some incorrectly named plural classes in the Access Record Models.
* Rename `ApiClient` to `AuthressClient` and split out non-essential functionality to a separate HttpClient.
* Add `limit`, `filter`, `cursor` to `get_records` endpoint.

## 1.1 ##
* Add the `TokenVerifier`

## 1.0 ##
* Add EdDSA support
* Add `Groups` to `AccessRecords`
* Explicitly set the algorithms in decoding the user token to identify the user sub