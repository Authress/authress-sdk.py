# authress-sdk
Authress SDK for Python.

[![NuGet version](https://badge.fury.io/py/authress-sdk.svg)](https://badge.fury.io/py/authress-sdk) [![Build Status](https://travis-ci.com/authress/authress-sdk.py.svg?branch=master)](https://travis-ci.com/authress/authress-sdk.py)


## Usage

```sh
pip install authress-sdk
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import authress_sdk
```

## Getting Started

```python
import time
import authress_sdk


# create an instance of the API class during service initialization
host = "https://DOMAIN.api.authress.io"
authress_client = authress_sdk.ApiClient(host)

# on api route
import authress_sdk
from flask import request

@app.route('/resources/<resourceId>')
def get_resource(resourceId):
  # Get the user token and pass it to authress
  authorization_token = request.headers.get('authorization')
  authress_client.set_token(authorization_token)

  # Check Authress to authorize the user
  api_instance = authress_sdk.UserPermissionsApi(authress_client)

  # Will throw except if the user is not authorized to read the resource
  authress_sdk.authorize_user('USER_ID', f'resources/{resourceId}', 'READ')

  # On success, continue with the route code to load resource and return it
  return 'Resource'

```