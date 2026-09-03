# CommercialProductLifecycleEnvelopeData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **UUID** |  | 
**status** | **str** |  | 

## Example

```python
from rivalika_sdk.models.commercial_product_lifecycle_envelope_data import CommercialProductLifecycleEnvelopeData

# TODO update the JSON string below
json = "{}"
# create an instance of CommercialProductLifecycleEnvelopeData from a JSON string
commercial_product_lifecycle_envelope_data_instance = CommercialProductLifecycleEnvelopeData.from_json(json)
# print the JSON string representation of the object
print(CommercialProductLifecycleEnvelopeData.to_json())

# convert the object into a dict
commercial_product_lifecycle_envelope_data_dict = commercial_product_lifecycle_envelope_data_instance.to_dict()
# create an instance of CommercialProductLifecycleEnvelopeData from a dict
commercial_product_lifecycle_envelope_data_from_dict = CommercialProductLifecycleEnvelopeData.from_dict(commercial_product_lifecycle_envelope_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


