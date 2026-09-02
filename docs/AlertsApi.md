# rivalika_sdk.AlertsApi

All URIs are relative to *https://api.rivalika.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_alert_rule**](AlertsApi.md#create_alert_rule) | **POST** /api/v1/alert-rules | Create an alert rule
[**delete_alert_rule**](AlertsApi.md#delete_alert_rule) | **DELETE** /api/v1/alert-rules/{alert_rule_id} | Delete an alert rule
[**get_alert_rule**](AlertsApi.md#get_alert_rule) | **GET** /api/v1/alert-rules/{alert_rule_id} | Get an alert rule
[**get_alert_settings**](AlertsApi.md#get_alert_settings) | **GET** /api/v1/alert-settings | Get alert settings
[**list_alert_events**](AlertsApi.md#list_alert_events) | **GET** /api/v1/alert-events | List alert events
[**list_alert_rules**](AlertsApi.md#list_alert_rules) | **GET** /api/v1/alert-rules | List alert rules
[**update_alert_rule**](AlertsApi.md#update_alert_rule) | **PATCH** /api/v1/alert-rules/{alert_rule_id} | Update an alert rule
[**update_alert_settings**](AlertsApi.md#update_alert_settings) | **PUT** /api/v1/alert-settings | Update alert settings


# **create_alert_rule**
> DataEnvelope create_alert_rule(idempotency_key, create_alert_rule_request)

Create an alert rule

### Example

* Bearer Authentication (RivalikaApiKey):

```python
import rivalika_sdk
from rivalika_sdk.models.create_alert_rule_request import CreateAlertRuleRequest
from rivalika_sdk.models.data_envelope import DataEnvelope
from rivalika_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rivalika.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rivalika_sdk.Configuration(
    host = "https://api.rivalika.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: RivalikaApiKey
configuration = rivalika_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with rivalika_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rivalika_sdk.AlertsApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | Unique key retained for 24 hours. Reusing a key with another payload returns 409.
    create_alert_rule_request = rivalika_sdk.CreateAlertRuleRequest() # CreateAlertRuleRequest | 

    try:
        # Create an alert rule
        api_response = await api_instance.create_alert_rule(idempotency_key, create_alert_rule_request)
        print("The response of AlertsApi->create_alert_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->create_alert_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique key retained for 24 hours. Reusing a key with another payload returns 409. | 
 **create_alert_rule_request** | [**CreateAlertRuleRequest**](CreateAlertRuleRequest.md)|  | 

### Return type

[**DataEnvelope**](DataEnvelope.md)

### Authorization

[RivalikaApiKey](../README.md#RivalikaApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**400** | Invalid request |  -  |
**401** | Invalid or expired API key |  -  |
**403** | Missing required scope |  -  |
**409** | Conflict or idempotency mismatch |  -  |
**429** | Rate or concurrency limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_alert_rule**
> DataEnvelope delete_alert_rule(idempotency_key, alert_rule_id)

Delete an alert rule

### Example

* Bearer Authentication (RivalikaApiKey):

```python
import rivalika_sdk
from rivalika_sdk.models.data_envelope import DataEnvelope
from rivalika_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rivalika.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rivalika_sdk.Configuration(
    host = "https://api.rivalika.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: RivalikaApiKey
configuration = rivalika_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with rivalika_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rivalika_sdk.AlertsApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | Unique key retained for 24 hours. Reusing a key with another payload returns 409.
    alert_rule_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete an alert rule
        api_response = await api_instance.delete_alert_rule(idempotency_key, alert_rule_id)
        print("The response of AlertsApi->delete_alert_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->delete_alert_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique key retained for 24 hours. Reusing a key with another payload returns 409. | 
 **alert_rule_id** | **UUID**|  | 

### Return type

[**DataEnvelope**](DataEnvelope.md)

### Authorization

[RivalikaApiKey](../README.md#RivalikaApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request |  -  |
**401** | Invalid or expired API key |  -  |
**403** | Missing required scope |  -  |
**409** | Conflict or idempotency mismatch |  -  |
**429** | Rate or concurrency limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_rule**
> DataEnvelope get_alert_rule(alert_rule_id)

Get an alert rule

### Example

* Bearer Authentication (RivalikaApiKey):

```python
import rivalika_sdk
from rivalika_sdk.models.data_envelope import DataEnvelope
from rivalika_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rivalika.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rivalika_sdk.Configuration(
    host = "https://api.rivalika.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: RivalikaApiKey
configuration = rivalika_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with rivalika_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rivalika_sdk.AlertsApi(api_client)
    alert_rule_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get an alert rule
        api_response = await api_instance.get_alert_rule(alert_rule_id)
        print("The response of AlertsApi->get_alert_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->get_alert_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_rule_id** | **UUID**|  | 

### Return type

[**DataEnvelope**](DataEnvelope.md)

### Authorization

[RivalikaApiKey](../README.md#RivalikaApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request |  -  |
**401** | Invalid or expired API key |  -  |
**403** | Missing required scope |  -  |
**409** | Conflict or idempotency mismatch |  -  |
**429** | Rate or concurrency limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_settings**
> DataEnvelope get_alert_settings()

Get alert settings

### Example

* Bearer Authentication (RivalikaApiKey):

```python
import rivalika_sdk
from rivalika_sdk.models.data_envelope import DataEnvelope
from rivalika_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rivalika.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rivalika_sdk.Configuration(
    host = "https://api.rivalika.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: RivalikaApiKey
configuration = rivalika_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with rivalika_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rivalika_sdk.AlertsApi(api_client)

    try:
        # Get alert settings
        api_response = await api_instance.get_alert_settings()
        print("The response of AlertsApi->get_alert_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->get_alert_settings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DataEnvelope**](DataEnvelope.md)

### Authorization

[RivalikaApiKey](../README.md#RivalikaApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request |  -  |
**401** | Invalid or expired API key |  -  |
**403** | Missing required scope |  -  |
**409** | Conflict or idempotency mismatch |  -  |
**429** | Rate or concurrency limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_alert_events**
> ListEnvelope list_alert_events(page=page, size=size, search=search, acknowledged=acknowledged, history_days=history_days, event_type=event_type)

List alert events

### Example

* Bearer Authentication (RivalikaApiKey):

```python
import rivalika_sdk
from rivalika_sdk.models.list_envelope import ListEnvelope
from rivalika_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rivalika.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rivalika_sdk.Configuration(
    host = "https://api.rivalika.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: RivalikaApiKey
configuration = rivalika_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with rivalika_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rivalika_sdk.AlertsApi(api_client)
    page = 56 # int |  (optional)
    size = 56 # int |  (optional)
    search = 'search_example' # str |  (optional)
    acknowledged = True # bool |  (optional)
    history_days = 56 # int |  (optional)
    event_type = 'event_type_example' # str |  (optional)

    try:
        # List alert events
        api_response = await api_instance.list_alert_events(page=page, size=size, search=search, acknowledged=acknowledged, history_days=history_days, event_type=event_type)
        print("The response of AlertsApi->list_alert_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->list_alert_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **size** | **int**|  | [optional] 
 **search** | **str**|  | [optional] 
 **acknowledged** | **bool**|  | [optional] 
 **history_days** | **int**|  | [optional] 
 **event_type** | **str**|  | [optional] 

### Return type

[**ListEnvelope**](ListEnvelope.md)

### Authorization

[RivalikaApiKey](../README.md#RivalikaApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request |  -  |
**401** | Invalid or expired API key |  -  |
**403** | Missing required scope |  -  |
**409** | Conflict or idempotency mismatch |  -  |
**429** | Rate or concurrency limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_alert_rules**
> ListEnvelope list_alert_rules(page=page, size=size, search=search, is_active=is_active, condition=condition)

List alert rules

### Example

* Bearer Authentication (RivalikaApiKey):

```python
import rivalika_sdk
from rivalika_sdk.models.list_envelope import ListEnvelope
from rivalika_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rivalika.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rivalika_sdk.Configuration(
    host = "https://api.rivalika.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: RivalikaApiKey
configuration = rivalika_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with rivalika_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rivalika_sdk.AlertsApi(api_client)
    page = 56 # int |  (optional)
    size = 56 # int |  (optional)
    search = 'search_example' # str |  (optional)
    is_active = True # bool |  (optional)
    condition = 'condition_example' # str |  (optional)

    try:
        # List alert rules
        api_response = await api_instance.list_alert_rules(page=page, size=size, search=search, is_active=is_active, condition=condition)
        print("The response of AlertsApi->list_alert_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->list_alert_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **size** | **int**|  | [optional] 
 **search** | **str**|  | [optional] 
 **is_active** | **bool**|  | [optional] 
 **condition** | **str**|  | [optional] 

### Return type

[**ListEnvelope**](ListEnvelope.md)

### Authorization

[RivalikaApiKey](../README.md#RivalikaApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request |  -  |
**401** | Invalid or expired API key |  -  |
**403** | Missing required scope |  -  |
**409** | Conflict or idempotency mismatch |  -  |
**429** | Rate or concurrency limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_alert_rule**
> DataEnvelope update_alert_rule(idempotency_key, alert_rule_id, update_alert_rule_request)

Update an alert rule

### Example

* Bearer Authentication (RivalikaApiKey):

```python
import rivalika_sdk
from rivalika_sdk.models.data_envelope import DataEnvelope
from rivalika_sdk.models.update_alert_rule_request import UpdateAlertRuleRequest
from rivalika_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rivalika.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rivalika_sdk.Configuration(
    host = "https://api.rivalika.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: RivalikaApiKey
configuration = rivalika_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with rivalika_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rivalika_sdk.AlertsApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | Unique key retained for 24 hours. Reusing a key with another payload returns 409.
    alert_rule_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    update_alert_rule_request = rivalika_sdk.UpdateAlertRuleRequest() # UpdateAlertRuleRequest | 

    try:
        # Update an alert rule
        api_response = await api_instance.update_alert_rule(idempotency_key, alert_rule_id, update_alert_rule_request)
        print("The response of AlertsApi->update_alert_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->update_alert_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique key retained for 24 hours. Reusing a key with another payload returns 409. | 
 **alert_rule_id** | **UUID**|  | 
 **update_alert_rule_request** | [**UpdateAlertRuleRequest**](UpdateAlertRuleRequest.md)|  | 

### Return type

[**DataEnvelope**](DataEnvelope.md)

### Authorization

[RivalikaApiKey](../README.md#RivalikaApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request |  -  |
**401** | Invalid or expired API key |  -  |
**403** | Missing required scope |  -  |
**409** | Conflict or idempotency mismatch |  -  |
**429** | Rate or concurrency limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_alert_settings**
> DataEnvelope update_alert_settings(idempotency_key, update_alert_settings_request)

Update alert settings

### Example

* Bearer Authentication (RivalikaApiKey):

```python
import rivalika_sdk
from rivalika_sdk.models.data_envelope import DataEnvelope
from rivalika_sdk.models.update_alert_settings_request import UpdateAlertSettingsRequest
from rivalika_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rivalika.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rivalika_sdk.Configuration(
    host = "https://api.rivalika.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: RivalikaApiKey
configuration = rivalika_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with rivalika_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rivalika_sdk.AlertsApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | Unique key retained for 24 hours. Reusing a key with another payload returns 409.
    update_alert_settings_request = rivalika_sdk.UpdateAlertSettingsRequest() # UpdateAlertSettingsRequest | 

    try:
        # Update alert settings
        api_response = await api_instance.update_alert_settings(idempotency_key, update_alert_settings_request)
        print("The response of AlertsApi->update_alert_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->update_alert_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique key retained for 24 hours. Reusing a key with another payload returns 409. | 
 **update_alert_settings_request** | [**UpdateAlertSettingsRequest**](UpdateAlertSettingsRequest.md)|  | 

### Return type

[**DataEnvelope**](DataEnvelope.md)

### Authorization

[RivalikaApiKey](../README.md#RivalikaApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request |  -  |
**401** | Invalid or expired API key |  -  |
**403** | Missing required scope |  -  |
**409** | Conflict or idempotency mismatch |  -  |
**429** | Rate or concurrency limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

