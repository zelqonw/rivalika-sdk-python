# SetAlertRuleRecipientsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipients** | [**List[SetAlertRuleRecipientsRequestRecipientsInner]**](SetAlertRuleRecipientsRequestRecipientsInner.md) |  | 

## Example

```python
from rivalika_sdk.models.set_alert_rule_recipients_request import SetAlertRuleRecipientsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetAlertRuleRecipientsRequest from a JSON string
set_alert_rule_recipients_request_instance = SetAlertRuleRecipientsRequest.from_json(json)
# print the JSON string representation of the object
print(SetAlertRuleRecipientsRequest.to_json())

# convert the object into a dict
set_alert_rule_recipients_request_dict = set_alert_rule_recipients_request_instance.to_dict()
# create an instance of SetAlertRuleRecipientsRequest from a dict
set_alert_rule_recipients_request_from_dict = SetAlertRuleRecipientsRequest.from_dict(set_alert_rule_recipients_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


