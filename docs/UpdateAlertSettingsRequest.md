# UpdateAlertSettingsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_notify_email** | **bool** |  | [optional] 
**quiet_hours_start_utc** | **str** |  | [optional] 
**quiet_hours_end_utc** | **str** |  | [optional] 

## Example

```python
from rivalika_sdk.models.update_alert_settings_request import UpdateAlertSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAlertSettingsRequest from a JSON string
update_alert_settings_request_instance = UpdateAlertSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAlertSettingsRequest.to_json())

# convert the object into a dict
update_alert_settings_request_dict = update_alert_settings_request_instance.to_dict()
# create an instance of UpdateAlertSettingsRequest from a dict
update_alert_settings_request_from_dict = UpdateAlertSettingsRequest.from_dict(update_alert_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


