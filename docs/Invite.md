# Invite

The user invite used to invite users to your application or to Authress as an admin.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invite_id** | **str** | The unique identifier for the invite. Use this ID to accept the invite. This parameter is ignored during invite creation. | [readonly] 
**tenant_id** | **str** |  | [optional] 
**statements** | [**List[InviteStatement]**](InviteStatement.md) | A list of statements which match roles to resources. The invited user will all statements apply to them when the invite is accepted. | 
**links** | [**AccountLinks**](AccountLinks.md) |  | [optional] 

## Example

```python
from authress.models.invite import Invite

# TODO update the JSON string below
json = "{}"
# create an instance of Invite from a JSON string
invite_instance = Invite.from_json(json)
# print the JSON string representation of the object
print Invite.to_json()

# convert the object into a dict
invite_dict = invite_instance.to_dict()
# create an instance of Invite from a dict
invite_from_dict = Invite.from_dict(invite_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


