# CreateExportScheduleRequestRecipientsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**display_name** | **str** |  | 

## Example

```python
from rivalika_sdk.models.create_export_schedule_request_recipients_inner import CreateExportScheduleRequestRecipientsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateExportScheduleRequestRecipientsInner from a JSON string
create_export_schedule_request_recipients_inner_instance = CreateExportScheduleRequestRecipientsInner.from_json(json)
# print the JSON string representation of the object
print(CreateExportScheduleRequestRecipientsInner.to_json())

# convert the object into a dict
create_export_schedule_request_recipients_inner_dict = create_export_schedule_request_recipients_inner_instance.to_dict()
# create an instance of CreateExportScheduleRequestRecipientsInner from a dict
create_export_schedule_request_recipients_inner_from_dict = CreateExportScheduleRequestRecipientsInner.from_dict(create_export_schedule_request_recipients_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


