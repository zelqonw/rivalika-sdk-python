# CreateCommercialImportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**file_name** | **str** |  | 
**storage_key** | **str** |  | 
**content_sha256** | **str** |  | 
**size_bytes** | **int** |  | 
**sheet_name** | **str** |  | [optional] 
**mapping** | **Dict[str, object]** |  | [optional] 
**auto_match_enabled** | **bool** |  | [optional] 
**dry_run** | **bool** |  | [optional] 

## Example

```python
from rivalika_sdk.models.create_commercial_import_request import CreateCommercialImportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCommercialImportRequest from a JSON string
create_commercial_import_request_instance = CreateCommercialImportRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCommercialImportRequest.to_json())

# convert the object into a dict
create_commercial_import_request_dict = create_commercial_import_request_instance.to_dict()
# create an instance of CreateCommercialImportRequest from a dict
create_commercial_import_request_from_dict = CreateCommercialImportRequest.from_dict(create_commercial_import_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


