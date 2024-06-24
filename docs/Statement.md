# Statement


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**roles** | **List[str]** |  | 
**resources** | [**List[Resource]**](Resource.md) |  | 
**users** | [**List[User]**](User.md) | The list of users this statement applies to. Users and groups can be set at either the statement level or the record level, but not both. | [optional] 
**groups** | [**List[LinkedGroup]**](LinkedGroup.md) | The list of groups this statement applies to. Users in these groups will be receive access to the resources listed. Users and groups can be set at either the statement level or the record level, but not both. | [optional] 

## Example

```python
from authress.models.statement import Statement

# TODO update the JSON string below
json = "{}"
# create an instance of Statement from a JSON string
statement_instance = Statement.from_json(json)
# print the JSON string representation of the object
print Statement.to_json()

# convert the object into a dict
statement_dict = statement_instance.to_dict()
# create an instance of Statement from a dict
statement_from_dict = Statement.from_dict(statement_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


