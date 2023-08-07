# ApplicationDelegation

The delegation response.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_url** | **str** | Redirect the user to this url to automatically log them into a third-party application. |

## Example

```python
from authress.models.application_delegation import ApplicationDelegation

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationDelegation from a JSON string
application_delegation_instance = ApplicationDelegation.from_json(json)
# print the JSON string representation of the object
print ApplicationDelegation.to_json()

# convert the object into a dict
application_delegation_dict = application_delegation_instance.to_dict()
# create an instance of ApplicationDelegation from a dict
application_delegation_form_dict = application_delegation.from_dict(application_delegation_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


