# CommercialImportPreparedUploadEnvelopeData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storage_key** | **str** |  | 
**upload_url** | **str** |  | 
**upload_headers** | [**CommercialImportPreparedUploadEnvelopeDataUploadHeaders**](CommercialImportPreparedUploadEnvelopeDataUploadHeaders.md) |  | 
**expires_in_seconds** | **int** |  | 

## Example

```python
from rivalika_sdk.models.commercial_import_prepared_upload_envelope_data import CommercialImportPreparedUploadEnvelopeData

# TODO update the JSON string below
json = "{}"
# create an instance of CommercialImportPreparedUploadEnvelopeData from a JSON string
commercial_import_prepared_upload_envelope_data_instance = CommercialImportPreparedUploadEnvelopeData.from_json(json)
# print the JSON string representation of the object
print(CommercialImportPreparedUploadEnvelopeData.to_json())

# convert the object into a dict
commercial_import_prepared_upload_envelope_data_dict = commercial_import_prepared_upload_envelope_data_instance.to_dict()
# create an instance of CommercialImportPreparedUploadEnvelopeData from a dict
commercial_import_prepared_upload_envelope_data_from_dict = CommercialImportPreparedUploadEnvelopeData.from_dict(commercial_import_prepared_upload_envelope_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


