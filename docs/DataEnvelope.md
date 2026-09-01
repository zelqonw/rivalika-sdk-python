# DataEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **Dict[str, object]** |  | 

## Example

```python
from rivalika_sdk.models.data_envelope import DataEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of DataEnvelope from a JSON string
data_envelope_instance = DataEnvelope.from_json(json)
# print the JSON string representation of the object
print(DataEnvelope.to_json())

# convert the object into a dict
data_envelope_dict = data_envelope_instance.to_dict()
# create an instance of DataEnvelope from a dict
data_envelope_from_dict = DataEnvelope.from_dict(data_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


