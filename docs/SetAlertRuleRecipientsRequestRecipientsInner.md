# SetAlertRuleRecipientsRequestRecipientsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**notify_email** | **bool** |  | 

## Example

```python
from rivalika_sdk.models.set_alert_rule_recipients_request_recipients_inner import SetAlertRuleRecipientsRequestRecipientsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SetAlertRuleRecipientsRequestRecipientsInner from a JSON string
set_alert_rule_recipients_request_recipients_inner_instance = SetAlertRuleRecipientsRequestRecipientsInner.from_json(json)
# print the JSON string representation of the object
print(SetAlertRuleRecipientsRequestRecipientsInner.to_json())

# convert the object into a dict
set_alert_rule_recipients_request_recipients_inner_dict = set_alert_rule_recipients_request_recipients_inner_instance.to_dict()
# create an instance of SetAlertRuleRecipientsRequestRecipientsInner from a dict
set_alert_rule_recipients_request_recipients_inner_from_dict = SetAlertRuleRecipientsRequestRecipientsInner.from_dict(set_alert_rule_recipients_request_recipients_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


