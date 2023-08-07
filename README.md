
<p align="center">
    <img src="https://github.com/Authress/authress-local/assets/5056218/156e3881-b359-4810-bc96-7abeaf9ddbdb" height="300px" alt="Authress Media Banner">
</p>

# Authress SDK for Python

This is the Authress SDK for Python. Authress provides an authorization API for user identity, access control, and api key management as a drop in SaaS.

The Nuget package connects to the [Authress API](https://authress.io/app/#/api). You can use Authress to build authentication and authorization directly into your applications and services. Additionally, Authress can be used locally to develop faster without needing an [Authress Account](https://authress.io).

<p align="center">
    <a href="https://badge.fury.io/py/authress" alt="Authress pypi package">
        <img src="https://badge.fury.io/py/authress.svg">
    </a>
    <a href="https://github.com/Authress/authress-sdk.py/actions/workflows/build.yml" alt="Build status">
      <img src="https://github.com/Authress/authress-sdk.py/actions/workflows/build.yml/badge.svg">
    </a>
    <a href="./LICENSE" alt="Apache-2.0">
      <img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg">
    </a>
    <a href="https://authress.io/community" alt="authress community">
      <img src="https://img.shields.io/badge/Community-Authress-fbaf0b.svg">
    </a>
</p>

## Usage

```sh
pip install authress
```
(you may need to run `pip` with root permission: `sudo pip install authress`)

Then import the package:
```python
import authress
```

## Getting Started


### Reference Guide

See the SDK reference guide for a examples of commonly executed blocks with descriptions.

[SDK Documentation](./docs/README.md)


## Quick Examples:

### Authorize using a user token
```python
from authress import AuthressClient

# create an instance of the API class during service initialization
# Authress custom domain or if there isn't one yet, use the authress account specific url
authress_api_url = "https://login.your.domain.com" # or "https://ACCOUNT_ID.api.authress.io"

# The Service Client Access Key for your service client.
service_client_access_key = "sc_key_001"
authress_client = AuthressClient(authress_api_url=authress_api_url , service_client_access_key=service_client_access_key)

# on api route
from flask import request
from authress import ApiException

@app.route('/resources/<resourceId>')
def get_resource(resourceId):
  # Get the user token and pass it to authress
  authorization_token = request.headers.get('authorization')
  authress_client.set_token(authorization_token)

  # Check Authress to authorize the user
  try
    authress_client.users.authorize_user(None, f'resources/{resourceId}', 'READ')
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
from authress import AuthressClient

# create an instance of the API class during service initialization
# Authress custom domain or if there isn't one yet, use the authress account specific url
authress_api_url = "https://login.your.domain.com" # or "https://ACCOUNT_ID.api.authress.io"

# Create a service client in the Authress management portal and past the access token here
service_client_access_key = 'eyJrZXlJ....'
authress_client = AuthressClient(authress_api_url=authress_api_url , service_client_access_key=service_client_access_key)

# on api route
from flask import request
from authress import ApiException

@app.route('/resources/<resourceId>')
def get_resource(resourceId):
  # Get the user
  user_id = get_user_id(request)

  # Check Authress to authorize the user
  try
    authress_client.users.authorize_user(user_id, f'resources/{resourceId}', 'READ')
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
from authress import AuthressClient

access_key = "eyARB5k-..." # For your API clients, these can be created via the API at https://authress.io/app/#/api
authress_api_url = None # Optionally you can call the Authress API if there are authress resources to be fetched
authress_client = AuthressClient(authress_api_url=authress_api_url, service_client_access_key=service_client_access_key)
# Generates a JWT to be used as a Bearer token for your API
jwt_token = authress_client.get_client_token()
```

In the case of a CLI or an SDK, the recommendation is to receive the access key from the user, perform these steps and then use the resulting `jwt_token` with your API. You can handle the JWTs as you would validate any JWT, in most cases it might be easier to make a request to Authress on the service side for token validation. An example is above:
```python
authress_client.set_token(jwt_token)
authress_client.users.authorize_user(...)
```

### Generation of service client
Since part of this process involves creating the service client and access token as part of your api. First create a service client which has `Authress:Owner` to resource `Authress:ServiceClients/*`. Then execute the following on user request to create a new api key.

```python
from authress import AuthressClient
from authress.models import *

# Your service's service client access token
service_client_access_key = 'eyJrZXlJ....'
# Authress custom domain or if there isn't one yet, use the authress account specific url
authress_api_url = "https://login.your.domain.com" # or "https://ACCOUNT_ID.api.authress.io"
authress_client = AuthressClient(authress_api_url=authress_api_url, service_client_access_key=service_client_access_key)

# User to create access token for
user_id = 'USER_A1'

# Create the service client
new_client = authress_client.clients.create_client(Client(name=f'ServiceClient for User {user_id}'))

# Give the service client access to the users data
authress_client.records.create_record(AccessRecord(
  name=f'API Key {new_client.client_id}',
  users=[AccessRecordUser(f'Authress:ServiceClients/{new_client.client_id}')],
  # Add the list of permissions this api key should have, for example here we've added all access to all the users resources as defined in Authress
  statements=[AccessRecordStatement(['Authress:Owner'], [AccessRecordResource(f'/users/{user_id}')])]))
# Request a new access key for that client
data = service_client_api.request_access_key(new_client.client_id)
# Return the access key to the user for usage
return data.access_key
```

### Token Verifier
To verify incoming tokens from Authress call the `verify_token` method on the `AuthressClient`

```python
from authress import AuthressClient

# User's access token from request
authorization_token = request.headers.get("authorization")

# Authress custom domain or if there isn't one yet, use the authress account specific url
host = "https://login.your.domain.com" # or "https://ACCOUNT_ID.api.authress.io"

# Instantiate the client
authress_client = AuthressClient(host)

# Verify the token, on successful verification the response is the decoded user identity JWT. On failure this raises an exception
user_identity = authress_client.verify_token(authorization_token)

```

## Contribution Guide

[Developing for the Python SDK](./contributing.md)