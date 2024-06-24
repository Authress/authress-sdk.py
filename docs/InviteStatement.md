# InviteStatement


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**roles** | **List[str]** |  | 
**resources** | [**List[Resource]**](Resource.md) |  | 
**users** | **List[str]** |  | [optional] 
**groups** | **List[str]** |  | [optional] 

## Example

```python
from authress.models.invite_statement import InviteStatement

# TODO update the JSON string below
json = "{}"
# create an instance of InviteStatement from a JSON string
invite_statement_instance = InviteStatement.from_json(json)
# print the JSON string representation of the object
print InviteStatement.to_json()

# convert the object into a dict
invite_statement_dict = invite_statement_instance.to_dict()
# create an instance of InviteStatement from a dict
invite_statement_from_dict = InviteStatement.from_dict(invite_statement_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


