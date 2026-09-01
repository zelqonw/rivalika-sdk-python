# AcceptedEnvelopeData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**status** | **str** |  | 

## Example

```python
from rivalika_sdk.models.accepted_envelope_data import AcceptedEnvelopeData

# TODO update the JSON string below
json = "{}"
# create an instance of AcceptedEnvelopeData from a JSON string
accepted_envelope_data_instance = AcceptedEnvelopeData.from_json(json)
# print the JSON string representation of the object
print(AcceptedEnvelopeData.to_json())

# convert the object into a dict
accepted_envelope_data_dict = accepted_envelope_data_instance.to_dict()
# create an instance of AcceptedEnvelopeData from a dict
accepted_envelope_data_from_dict = AcceptedEnvelopeData.from_dict(accepted_envelope_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


