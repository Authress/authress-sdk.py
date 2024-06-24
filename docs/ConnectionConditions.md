# ConnectionConditions

Conditions are custom restrictions on connections that prevent the connection from being used when it should not be, or limits its usability for increased security.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**require_business_account** | **bool** | Require the user logging in with this connect to be using a business account. When possible Authress will block user login and request that they select a different account. Enabling this may prevent some users from being able to sign up with this identity connection. | [optional] [default to False]

## Example

```python
from authress.models.connection_conditions import ConnectionConditions

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionConditions from a JSON string
connection_conditions_instance = ConnectionConditions.from_json(json)
# print the JSON string representation of the object
print ConnectionConditions.to_json()

# convert the object into a dict
connection_conditions_dict = connection_conditions_instance.to_dict()
# create an instance of ConnectionConditions from a dict
connection_conditions_from_dict = ConnectionConditions.from_dict(connection_conditions_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


