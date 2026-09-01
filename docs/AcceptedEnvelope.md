# AcceptedEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AcceptedEnvelopeData**](AcceptedEnvelopeData.md) |  | 

## Example

```python
from rivalika_sdk.models.accepted_envelope import AcceptedEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of AcceptedEnvelope from a JSON string
accepted_envelope_instance = AcceptedEnvelope.from_json(json)
# print the JSON string representation of the object
print(AcceptedEnvelope.to_json())

# convert the object into a dict
accepted_envelope_dict = accepted_envelope_instance.to_dict()
# create an instance of AcceptedEnvelope from a dict
accepted_envelope_from_dict = AcceptedEnvelope.from_dict(accepted_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


