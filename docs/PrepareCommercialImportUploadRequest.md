# PrepareCommercialImportUploadRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** |  | 
**content_sha256** | **str** |  | 
**size_bytes** | **int** |  | 

## Example

```python
from rivalika_sdk.models.prepare_commercial_import_upload_request import PrepareCommercialImportUploadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PrepareCommercialImportUploadRequest from a JSON string
prepare_commercial_import_upload_request_instance = PrepareCommercialImportUploadRequest.from_json(json)
# print the JSON string representation of the object
print(PrepareCommercialImportUploadRequest.to_json())

# convert the object into a dict
prepare_commercial_import_upload_request_dict = prepare_commercial_import_upload_request_instance.to_dict()
# create an instance of PrepareCommercialImportUploadRequest from a dict
prepare_commercial_import_upload_request_from_dict = PrepareCommercialImportUploadRequest.from_dict(prepare_commercial_import_upload_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


