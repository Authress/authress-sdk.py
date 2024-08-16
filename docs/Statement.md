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

statement = Statement(
    roles=["ro_viewer"],
    resources=[
        Resource(resourceUri="/accounts/acc_001/documents/*")
    ]
)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


