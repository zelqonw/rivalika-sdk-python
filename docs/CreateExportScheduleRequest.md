# CreateExportScheduleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**request** | [**CreateExportScheduleRequestRequest**](CreateExportScheduleRequestRequest.md) |  | 
**date_window** | [**CreateExportScheduleRequestDateWindow**](CreateExportScheduleRequestDateWindow.md) |  | [optional] 
**schedule** | **Dict[str, object]** |  | 
**timezone** | **str** |  | 
**recipients** | [**List[CreateExportScheduleRequestRecipientsInner]**](CreateExportScheduleRequestRecipientsInner.md) |  | [optional] 
**attach_file** | **bool** |  | [optional] 
**template_id** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 

## Example

```python
from rivalika_sdk.models.create_export_schedule_request import CreateExportScheduleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateExportScheduleRequest from a JSON string
create_export_schedule_request_instance = CreateExportScheduleRequest.from_json(json)
# print the JSON string representation of the object
print(CreateExportScheduleRequest.to_json())

# convert the object into a dict
create_export_schedule_request_dict = create_export_schedule_request_instance.to_dict()
# create an instance of CreateExportScheduleRequest from a dict
create_export_schedule_request_from_dict = CreateExportScheduleRequest.from_dict(create_export_schedule_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


