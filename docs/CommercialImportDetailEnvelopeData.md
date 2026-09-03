# CommercialImportDetailEnvelopeData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**kind** | **str** |  | 
**status** | **str** |  | 
**file_name** | **str** |  | 
**dry_run** | **bool** |  | 
**sheet_name** | **str** |  | 
**total_rows** | **int** |  | 
**imported_rows** | **int** |  | 
**rejected_rows** | **int** |  | 
**last_processed_row** | **int** |  | 
**has_error_report** | **bool** |  | 
**failure_summary** | **str** |  | 
**row_errors** | [**List[CommercialImportDetailEnvelopeDataRowErrorsInner]**](CommercialImportDetailEnvelopeDataRowErrorsInner.md) |  | 
**row_errors_truncated** | **bool** |  | 
**started_at** | **datetime** |  | 
**completed_at** | **datetime** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from rivalika_sdk.models.commercial_import_detail_envelope_data import CommercialImportDetailEnvelopeData

# TODO update the JSON string below
json = "{}"
# create an instance of CommercialImportDetailEnvelopeData from a JSON string
commercial_import_detail_envelope_data_instance = CommercialImportDetailEnvelopeData.from_json(json)
# print the JSON string representation of the object
print(CommercialImportDetailEnvelopeData.to_json())

# convert the object into a dict
commercial_import_detail_envelope_data_dict = commercial_import_detail_envelope_data_instance.to_dict()
# create an instance of CommercialImportDetailEnvelopeData from a dict
commercial_import_detail_envelope_data_from_dict = CommercialImportDetailEnvelopeData.from_dict(commercial_import_detail_envelope_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


