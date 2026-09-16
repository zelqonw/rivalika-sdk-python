# CreateExportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | **str** | Lossless machine profile: ZIP with integration.csv (record_json column) and metadata.json. Exact decimal strings, stable IDs, UTC timestamps and publication provenance. | [optional] 
**dataset** | **str** |  | 
**format** | **str** |  | 
**locale** | **str** |  | 
**timezone** | **str** |  | 
**columns** | **List[str]** |  | 
**filters** | **Dict[str, object]** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from rivalika_sdk.models.create_export_request import CreateExportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateExportRequest from a JSON string
create_export_request_instance = CreateExportRequest.from_json(json)
# print the JSON string representation of the object
print(CreateExportRequest.to_json())

# convert the object into a dict
create_export_request_dict = create_export_request_instance.to_dict()
# create an instance of CreateExportRequest from a dict
create_export_request_from_dict = CreateExportRequest.from_dict(create_export_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


