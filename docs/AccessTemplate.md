# AccessTemplate

A logical grouping of access related elements

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[User]**](User.md) | The list of users access applies to. Access templates are finite in size, for patterns where the list of users might grow indefinitely, the recommended solution is to specify each user in their own access record. | 
**statements** | [**List[Statement]**](Statement.md) | A list of statements which match roles to resources. | 

## Example

```python
from authress.models.access_template import AccessTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of AccessTemplate from a JSON string
access_template_instance = AccessTemplate.from_json(json)
# print the JSON string representation of the object
print AccessTemplate.to_json()

# convert the object into a dict
access_template_dict = access_template_instance.to_dict()
# create an instance of AccessTemplate from a dict
access_template_from_dict = AccessTemplate.from_dict(access_template_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


