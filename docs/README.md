[Back to Repository](../README.md)

## Documentation for API Endpoints

All URIs are relative to your [Authress Host URL](https://authress.io/app/#/api).

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
`authress.access_records` | [**create_claim**](./AccessRecordsApi.md#create_claim) | **POST** /v1/claims | Create resource Claim
`authress.access_records` | [**create_invite**](./AccessRecordsApi.md#create_invite) | **POST** /v1/invites | Create user invite
`authress.access_records` | [**create_record**](./AccessRecordsApi.md#create_record) | **POST** /v1/records | Create access record
`authress.access_records` | [**create_request**](./AccessRecordsApi.md#create_request) | **POST** /v1/requests | Create access request
`authress.access_records` | [**delete_invite**](./AccessRecordsApi.md#delete_invite) | **DELETE** /v1/invites/{inviteId} | Delete invite
`authress.access_records` | [**delete_record**](./AccessRecordsApi.md#delete_record) | **DELETE** /v1/records/{recordId} | Deletes access record
`authress.access_records` | [**delete_request**](./AccessRecordsApi.md#delete_request) | **DELETE** /v1/requests/{requestId} | Deletes access request
`authress.access_records` | [**get_record**](./AccessRecordsApi.md#get_record) | **GET** /v1/records/{recordId} | Retrieve access record
`authress.access_records` | [**get_records**](./AccessRecordsApi.md#get_records) | **GET** /v1/records | List access records
`authress.access_records` | [**get_request**](./AccessRecordsApi.md#get_request) | **GET** /v1/requests/{requestId} | Retrieve access request
`authress.access_records` | [**get_requests**](./AccessRecordsApi.md#get_requests) | **GET** /v1/requests | List access requests
`authress.access_records` | [**respond_to_access_request**](./AccessRecordsApi.md#respond_to_access_request) | **PATCH** /v1/requests/{requestId} | Approve or deny access request
`authress.access_records` | [**respond_to_invite**](./AccessRecordsApi.md#respond_to_invite) | **PATCH** /v1/invites/{inviteId} | Accept invite
`authress.access_records` | [**update_record**](./AccessRecordsApi.md#update_record) | **PUT** /v1/records/{recordId} | Update access record
`authress.accounts` | [**delegate_authentication**](./AccountsApi.md#delegate_authentication) | **POST** /v1/identities | Link external provider
`authress.accounts` | [**get_account**](./AccountsApi.md#get_account) | **GET** /v1/accounts/{accountId} | Retrieve account information
`authress.accounts` | [**get_account_identities**](./AccountsApi.md#get_account_identities) | **GET** /v1/identities | List linked external providers
`authress.accounts` | [**get_accounts**](./AccountsApi.md#get_accounts) | **GET** /v1/accounts | List user Authress accounts
`authress.applications` | [**delegate_user_login**](./ApplicationsApi.md#delegate_user_login) | **POST** /v1/applications/{applicationId}/users/{userId}/delegation | Log user into third-party application
`authress.connections` | [**create_connection**](./ConnectionsApi.md#create_connection) | **POST** /v1/connections | Create SSO connection
`authress.connections` | [**delete_connection**](./ConnectionsApi.md#delete_connection) | **DELETE** /v1/connections/{connectionId} | Delete SSO connection
`authress.connections` | [**get_connection**](./ConnectionsApi.md#get_connection) | **GET** /v1/connections/{connectionId} | Retrieve SSO connection
`authress.connections` | [**get_connection_credentials**](./ConnectionsApi.md#get_connection_credentials) | **GET** /v1/connections/{connectionId}/users/{userId}/credentials | Retrieve user connection credentials
`authress.connections` | [**get_connections**](./ConnectionsApi.md#get_connections) | **GET** /v1/connections | List SSO connections
`authress.connections` | [**update_connection**](./ConnectionsApi.md#update_connection) | **PUT** /v1/connections/{connectionId} | Update SSO connection
`authress.extensions` | [**create_extension**](./ExtensionsApi.md#create_extension) | **POST** /v1/extensions | Create extension
`authress.extensions` | [**delete_extension**](./ExtensionsApi.md#delete_extension) | **DELETE** /v1/extensions/{extensionId} | Delete extension
`authress.extensions` | [**get_extension**](./ExtensionsApi.md#get_extension) | **GET** /v1/extensions/{extensionId} | Retrieve extension
`authress.extensions` | [**get_extensions**](./ExtensionsApi.md#get_extensions) | **GET** /v1/extensions | List extensions
`authress.extensions` | [**login**](./ExtensionsApi.md#login) | **GET** / | OAuth Authorize
`authress.extensions` | [**request_token**](./ExtensionsApi.md#request_token) | **POST** /api/authentication/oauth/tokens | OAuth Token
`authress.extensions` | [**update_extension**](./ExtensionsApi.md#update_extension) | **PUT** /v1/extensions/{extensionId} | Update extension
`authress.groups` | [**create_group**](./GroupsApi.md#create_group) | **POST** /v1/groups | Create group
`authress.groups` | [**delete_group**](./GroupsApi.md#delete_group) | **DELETE** /v1/groups/{groupId} | Deletes group
`authress.groups` | [**get_group**](./GroupsApi.md#get_group) | **GET** /v1/groups/{groupId} | Retrieve group
`authress.groups` | [**get_groups**](./GroupsApi.md#get_groups) | **GET** /v1/groups | List groups
`authress.groups` | [**update_group**](./GroupsApi.md#update_group) | **PUT** /v1/groups/{groupId} | Update a group
`authress.invites` | [**create_invite**](./InvitesApi.md#create_invite) | **POST** /v1/invites | Create user invite
`authress.invites` | [**delete_invite**](./InvitesApi.md#delete_invite) | **DELETE** /v1/invites/{inviteId} | Delete invite
`authress.invites` | [**get_invite**](./InvitesApi.md#get_invite) | **GET** /v1/invites/{inviteId} | Retrieve invite
`authress.invites` | [**respond_to_invite**](./InvitesApi.md#respond_to_invite) | **PATCH** /v1/invites/{inviteId} | Accept invite
`authress.resourcePermissions` | [**get_permissioned_resource**](./ResourcePermissionsApi.md#get_permissioned_resource) | **GET** /v1/resources/{resourceUri} | Retrieve resource configuration
`authress.resourcePermissions` | [**get_permissioned_resources**](./ResourcePermissionsApi.md#get_permissioned_resources) | **GET** /v1/resources | List all resource configurations
`authress.resourcePermissions` | [**get_resource_users**](./ResourcePermissionsApi.md#get_resource_users) | **GET** /v1/resources/{resourceUri}/users | List users with resource access
`authress.resourcePermissions` | [**update_permissioned_resource**](./ResourcePermissionsApi.md#update_permissioned_resource) | **PUT** /v1/resources/{resourceUri} | Update resource configuration
`authress.roles` | [**create_role**](./RolesApi.md#create_role) | **POST** /v1/roles | Create role
`authress.roles` | [**delete_role**](./RolesApi.md#delete_role) | **DELETE** /v1/roles/{roleId} | Deletes role
`authress.roles` | [**get_role**](./RolesApi.md#get_role) | **GET** /v1/roles/{roleId} | Retrieve role
`authress.roles` | [**get_roles**](./RolesApi.md#get_roles) | **GET** /v1/roles | List roles
`authress.roles` | [**update_role**](./RolesApi.md#update_role) | **PUT** /v1/roles/{roleId} | Update role
`authress.serviceClients` | [**create_client**](./ServiceClientsApi.md#create_client) | **POST** /v1/clients | Create service client
`authress.serviceClients` | [**delete_access_key**](./ServiceClientsApi.md#delete_access_key) | **DELETE** /v1/clients/{clientId}/access-keys/{keyId} | Delete service client access key
`authress.serviceClients` | [**delete_client**](./ServiceClientsApi.md#delete_client) | **DELETE** /v1/clients/{clientId} | Delete service client
`authress.serviceClients` | [**get_client**](./ServiceClientsApi.md#get_client) | **GET** /v1/clients/{clientId} | Retrieve service client
`authress.serviceClients` | [**get_clients**](./ServiceClientsApi.md#get_clients) | **GET** /v1/clients | List service clients
`authress.serviceClients` | [**request_access_key**](./ServiceClientsApi.md#request_access_key) | **POST** /v1/clients/{clientId}/access-keys | Generate service client access key
`authress.serviceClients` | [**update_client**](./ServiceClientsApi.md#update_client) | **PUT** /v1/clients/{clientId} | Update service client
`authress.tenants` | [**create_tenant**](./TenantsApi.md#create_tenant) | **POST** /v1/tenants | Create tenant
`authress.tenants` | [**delete_tenant**](./TenantsApi.md#delete_tenant) | **DELETE** /v1/tenants/{tenantId} | Delete tenant
`authress.tenants` | [**get_tenant**](./TenantsApi.md#get_tenant) | **GET** /v1/tenants/{tenantId} | Retrieve tenant
`authress.tenants` | [**get_tenants**](./TenantsApi.md#get_tenants) | **GET** /v1/tenants | List tenants
`authress.tenants` | [**update_tenant**](./TenantsApi.md#update_tenant) | **PUT** /v1/tenants/{tenantId} | Update tenant
`authress.userPermissions` | [**authorize_user**](./UserPermissionsApi.md#authorize_user) | **GET** /v1/users/{userId}/resources/{resourceUri}/permissions/{permission} | Verify user authorization
`authress.userPermissions` | [**get_user_permissions_for_resource**](./UserPermissionsApi.md#get_user_permissions_for_resource) | **GET** /v1/users/{userId}/resources/{resourceUri}/permissions | Get user permissions for resource
`authress.userPermissions` | [**get_user_resources**](./UserPermissionsApi.md#get_user_resources) | **GET** /v1/users/{userId}/resources | List user resources
`authress.userPermissions` | [**get_user_roles_for_resource**](./UserPermissionsApi.md#get_user_roles_for_resource) | **GET** /v1/users/{userId}/resources/{resourceUri}/roles | Get user roles for resource
`authress.users` | [**delete_user**](./UsersApi.md#delete_user) | **DELETE** /v1/users/{userId} | Delete a user
`authress.users` | [**get_user**](./UsersApi.md#get_user) | **GET** /v1/users/{userId} | Retrieve a user
`authress.users` | [**get_users**](./UsersApi.md#get_users) | **GET** /v1/users | List users

## Documentation For Models

 - [AccessRecord](./AccessRecord.md)
 - [AccessRecordCollection](./AccessRecordCollection.md)
 - [AccessRequest](./AccessRequest.md)
 - [AccessRequestCollection](./AccessRequestCollection.md)
 - [AccessRequestResponse](./AccessRequestResponse.md)
 - [AccessTemplate](./AccessTemplate.md)
 - [Account](./Account.md)
 - [AccountCollection](./AccountCollection.md)
 - [ApplicationDelegation](./ApplicationDelegation.md)
 - [ClaimRequest](./ClaimRequest.md)
 - [Client](./Client.md)
 - [ClientAccessKey](./ClientAccessKey.md)
 - [ClientCollection](./ClientCollection.md)
 - [ClientOptions](./ClientOptions.md)
 - [CollectionLinks](./CollectionLinks.md)
 - [Connection](./Connection.md)
 - [ConnectionCollection](./ConnectionCollection.md)
 - [ConnectionData](./ConnectionData.md)
 - [ConnectionDefaultConnectionProperties](./ConnectionDefaultConnectionProperties.md)
 - [Extension](./Extension.md)
 - [ExtensionApplication](./ExtensionApplication.md)
 - [ExtensionClient](./ExtensionClient.md)
 - [ExtensionCollection](./ExtensionCollection.md)
 - [Group](./Group.md)
 - [GroupCollection](./GroupCollection.md)
 - [Identity](./Identity.md)
 - [IdentityCollection](./IdentityCollection.md)
 - [IdentityRequest](./IdentityRequest.md)
 - [Invite](./Invite.md)
 - [Link](./Link.md)
 - [LinkedGroup](./LinkedGroup.md)
 - [Links](./Links.md)
 - [MetadataObject](./MetadataObject.md)
 - [MetadataObjectAccount](./MetadataObjectAccount.md)
 - [OAuthAuthorizeResponse](./OAuthAuthorizeResponse.md)
 - [OAuthTokenRequest](./OAuthTokenRequest.md)
 - [OAuthTokenResponse](./OAuthTokenResponse.md)
 - [Pagination](./Pagination.md)
 - [PaginationCursor](./PaginationCursor.md)
 - [PermissionCollection](./PermissionCollection.md)
 - [PermissionObject](./PermissionObject.md)
 - [PermissionedResource](./PermissionedResource.md)
 - [PermissionedResourceCollection](./PermissionedResourceCollection.md)
 - [Resource](./Resource.md)
 - [ResourcePermission](./ResourcePermission.md)
 - [ResourceUsersCollection](./ResourceUsersCollection.md)
 - [Role](./Role.md)
 - [RoleCollection](./RoleCollection.md)
 - [Statement](./Statement.md)
 - [Tenant](./Tenant.md)
 - [TenantCollection](./TenantCollection.md)
 - [TenantConnection](./TenantConnection.md)
 - [TenantData](./TenantData.md)
 - [TokenRequest](./TokenRequest.md)
 - [User](./User.md)
 - [UserConnectionCredentials](./UserConnectionCredentials.md)
 - [UserIdentity](./UserIdentity.md)
 - [UserIdentityCollection](./UserIdentityCollection.md)
 - [UserResourcesCollection](./UserResourcesCollection.md)
 - [UserRole](./UserRole.md)
 - [UserRoleCollection](./UserRoleCollection.md)
 - [UserToken](./UserToken.md)
