# EstimateExportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **str** |  | 
**format** | **str** |  | 
**locale** | **str** |  | 
**timezone** | **str** |  | 
**columns** | **List[str]** |  | 
**filters** | **Dict[str, object]** |  | [optional] 

## Example

```python
from rivalika_sdk.models.estimate_export_request import EstimateExportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EstimateExportRequest from a JSON string
estimate_export_request_instance = EstimateExportRequest.from_json(json)
# print the JSON string representation of the object
print(EstimateExportRequest.to_json())

# convert the object into a dict
estimate_export_request_dict = estimate_export_request_instance.to_dict()
# create an instance of EstimateExportRequest from a dict
estimate_export_request_from_dict = EstimateExportRequest.from_dict(estimate_export_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


