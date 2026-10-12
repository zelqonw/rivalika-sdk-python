# PreviewReportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**configuration** | **Dict[str, object]** |  | [optional] 

## Example

```python
from rivalika_sdk.models.preview_report_request import PreviewReportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewReportRequest from a JSON string
preview_report_request_instance = PreviewReportRequest.from_json(json)
# print the JSON string representation of the object
print(PreviewReportRequest.to_json())

# convert the object into a dict
preview_report_request_dict = preview_report_request_instance.to_dict()
# create an instance of PreviewReportRequest from a dict
preview_report_request_from_dict = PreviewReportRequest.from_dict(preview_report_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


