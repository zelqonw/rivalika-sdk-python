# CreateExportScheduleRequestDateWindow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** |  | 
**days** | **float** |  | [optional] 

## Example

```python
from rivalika_sdk.models.create_export_schedule_request_date_window import CreateExportScheduleRequestDateWindow

# TODO update the JSON string below
json = "{}"
# create an instance of CreateExportScheduleRequestDateWindow from a JSON string
create_export_schedule_request_date_window_instance = CreateExportScheduleRequestDateWindow.from_json(json)
# print the JSON string representation of the object
print(CreateExportScheduleRequestDateWindow.to_json())

# convert the object into a dict
create_export_schedule_request_date_window_dict = create_export_schedule_request_date_window_instance.to_dict()
# create an instance of CreateExportScheduleRequestDateWindow from a dict
create_export_schedule_request_date_window_from_dict = CreateExportScheduleRequestDateWindow.from_dict(create_export_schedule_request_date_window_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


