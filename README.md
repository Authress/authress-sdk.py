# authress-sdk
Authress SDK for Python.

[![NuGet version](https://badge.fury.io/py/authress-sdk.svg)](https://badge.fury.io/py/authress-sdk) [![Build Status](https://travis-ci.com/Authress/authress-sdk.py.svg?branch=release%2F1.0)](https://travis-ci.com/authress/authress-sdk.py)

This is the Authress SDK used to integrate with the authorization as a service provider Authress at https://authress.io.

## Usage

```sh
pip install authress-sdk
```
(you may need to run `pip` with root permission: `sudo pip install authress-sdk`)

Then import the package:
```python
import authress_sdk
```

## Getting Started

### Authorize using a user token
```python
from authress_sdk import ApiClient

# create an instance of the API class during service initialization
# Replace DOMAIN with the Authress domain for your account
host = "https://DOMAIN.api.authress.io"
authress_client = ApiClient(host)

# on api route
from flask import request
from authress_sdk import UserPermissionsApi, ApiException

@app.route('/resources/<resourceId>')
def get_resource(resourceId):
  # Get the user token and pass it to authress
  authorization_token = request.headers.get('authorization')
  authress_client.set_token(authorization_token)

  # Check Authress to authorize the user
  try
    api_instance = UserPermissionsApi(authress_client)
    api_instance.authorize_user(None, f'resources/{resourceId}', 'READ')
  except ApiException as api_exception:
    # Will throw except if the user is not authorized to read the resource
    if api_exception.status is 403:
      return 403

    raise api_exception

  # On success, continue with the route code to load resource and return it
  return 'Resource', 200
```

### Authorize with a service client
```python
from authress_sdk import ApiClient

# create an instance of the API class during service initialization
# Replace DOMAIN with the Authress domain for your account
host = "https://DOMAIN.api.authress.io"

# Create a service client in the Authress management portal and past the access token here
access_token = 'eyJrZXlJ....'
authress_client = ApiClient(host, access_token)

# on api route
from flask import request
from authress_sdk import UserPermissionsApi, ApiException

@app.route('/resources/<resourceId>')
def get_resource(resourceId):
  # Get the user
  user_id = get_user_id(request)

  # Check Authress to authorize the user
  try
    api_instance = UserPermissionsApi(authress_client)
    api_instance.authorize_user(user_id, f'resources/{resourceId}', 'READ')
  except ApiException as api_exception:
    # Will throw except if the user is not authorized to read the resource
    if api_exception.status is 403:
      return 403

    raise api_exception

  # On success, continue with the route code to load resource and return it
  return 'Resource', 200
```

## Using the Authress service client as an API key
You can use the Authress service client access token as an api key for your application. This is as simple as pulling in the SDK and referencing the token provider.

### Application SDK example
```python
from authress_sdk import ApiClient as AuthressClient

access_key = "eyARB5k-..." # For your API clients, these can be created via the API at https://authress.io/app/#/api
authress_host = None # Optionally you can call the Authress API if there are authress resources to be fetched
authress_client = AuthressClient(authress_host, access_key)
# Generates a JWT to be used as a Bearer token for your API
jwt_token = authress_client.get_client_token()
```

In the case of a CLI or an SDK, the recommendation is to receive the access key from the user, perform these steps and then use the resulting `jwt_token` with your API. You can handle the JWTs as you would validate any JWT, in most cases it might be easier to make a request to Authress on the service side for token validation. An example is above:
```python
authress_client.set_token(jwt_token)
api_instance = UserPermissionsApi(authress_client)
api_instance.authorize_user(...)
```

### Generation of service client
Since part of this process involves creating the service client and access token as part of your api. First create a service client which has `Authress:Owner` to resource `Authress:ServiceClients/*`. Then execute the following on user request to create a new api key.

```python
from authress_sdk import ServiceClientsApi, AccessRecordsApi, ApiClient
from authress_sdk.models import *

# Your service's service client access token
access_token = 'eyJrZXlJ....'
host = "https://DOMAIN.api.authress.io"
authress_client = ApiClient(host, access_token)

# User to create access token for
user_id = 'USER_A1'

# Create the service client
service_client_api = ServiceClientsApi(authress_client)
new_client = service_client_api.create_client(Client(name=f'ServiceClient for User {user_id}'))

# Give the service client access to the users data
record_api = AccessRecordsApi(authress_client)
record_api.create_record(AccessRecord(
  name=f'API Key {new_client.client_id}',
  users=[AccessRecordUsers(f'Authress:ServiceClients/{new_client.client_id}')],
  # Add the list of permissions this api key should have, for example here we've added all access to all the users resources as defined in Authress
  statements=[AccessRecordStatements(['Authress:Owner'], [AccessRecordResources(f'/users/{user_id}')])]))
# Request a new access key for that client
data = service_client_api.request_access_key(new_client.client_id)
# Return the access key to the user for usage
return data.access_key
```