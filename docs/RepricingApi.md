# rivalika_sdk.RepricingApi

All URIs are relative to *https://api.rivalika.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_repricer_recommendation**](RepricingApi.md#apply_repricer_recommendation) | **POST** /api/v1/repricer/recommendations/{recommendation_id}/apply | Apply a repricer recommendation
[**create_repricer_exclusion**](RepricingApi.md#create_repricer_exclusion) | **POST** /api/v1/repricer/exclusions | Create a repricer exclusion
[**create_repricer_policy**](RepricingApi.md#create_repricer_policy) | **POST** /api/v1/repricer/policies | Create a repricer policy
[**create_repricer_run**](RepricingApi.md#create_repricer_run) | **POST** /api/v1/repricer/runs | Create a repricer run
[**delete_repricer_exclusion**](RepricingApi.md#delete_repricer_exclusion) | **DELETE** /api/v1/repricer/exclusions/{exclusion_id} | Delete a repricer exclusion
[**delete_repricer_policy**](RepricingApi.md#delete_repricer_policy) | **DELETE** /api/v1/repricer/policies/{policy_id} | Delete a repricer policy
[**get_repricer_analytics**](RepricingApi.md#get_repricer_analytics) | **GET** /api/v1/repricer/analytics | Get repricer analytics
[**get_repricer_settings**](RepricingApi.md#get_repricer_settings) | **GET** /api/v1/repricer/settings | Get repricer settings
[**list_repricer_applications**](RepricingApi.md#list_repricer_applications) | **GET** /api/v1/repricer/applications | List repricer applications
[**list_repricer_exclusions**](RepricingApi.md#list_repricer_exclusions) | **GET** /api/v1/repricer/exclusions | List repricer exclusions
[**list_repricer_policies**](RepricingApi.md#list_repricer_policies) | **GET** /api/v1/repricer/policies | List repricer policies
[**list_repricer_recommendations**](RepricingApi.md#list_repricer_recommendations) | **GET** /api/v1/repricer/recommendations | List repricer recommendations
[**list_repricer_runs**](RepricingApi.md#list_repricer_runs) | **GET** /api/v1/repricer/runs | List repricer runs
[**rollback_repricer_application**](RepricingApi.md#rollback_repricer_application) | **POST** /api/v1/repricer/applications/{application_id}/rollback | Rollback a repricer application
[**update_repricer_policy**](RepricingApi.md#update_repricer_policy) | **PATCH** /api/v1/repricer/policies/{policy_id} | Update a repricer policy
[**update_repricer_settings**](RepricingApi.md#update_repricer_settings) | **PUT** /api/v1/repricer/settings | Update repricer settings


# **apply_repricer_recommendation**
> DataEnvelope apply_repricer_recommendation(idempotency_key, recommendation_id, apply_repricer_recommendation_request)

Apply a repricer recommendation

### Example

* Bearer (Rivalika API key) Authentication (RivalikaApiKey):

```python
import rivalika_sdk
from rivalika_sdk.models.apply_repricer_recommendation_request import ApplyRepricerRecommendationRequest
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

# Configure Bearer authorization (Rivalika API key): RivalikaApiKey
configuration = rivalika_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with rivalika_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rivalika_sdk.RepricingApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | Unique key retained for 24 hours. Reusing a key with another payload returns 409.
    recommendation_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    apply_repricer_recommendation_request = rivalika_sdk.ApplyRepricerRecommendationRequest() # ApplyRepricerRecommendationRequest | 

    try:
        # Apply a repricer recommendation
        api_response = await api_instance.apply_repricer_recommendation(idempotency_key, recommendation_id, apply_repricer_recommendation_request)
        print("The response of RepricingApi->apply_repricer_recommendation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepricingApi->apply_repricer_recommendation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique key retained for 24 hours. Reusing a key with another payload returns 409. | 
 **recommendation_id** | **UUID**|  | 
 **apply_repricer_recommendation_request** | [**ApplyRepricerRecommendationRequest**](ApplyRepricerRecommendationRequest.md)|  | 

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

# **create_repricer_exclusion**
> DataEnvelope create_repricer_exclusion(idempotency_key, create_repricer_exclusion_request)

Create a repricer exclusion

### Example

* Bearer (Rivalika API key) Authentication (RivalikaApiKey):

```python
import rivalika_sdk
from rivalika_sdk.models.create_repricer_exclusion_request import CreateRepricerExclusionRequest
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

# Configure Bearer authorization (Rivalika API key): RivalikaApiKey
configuration = rivalika_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with rivalika_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rivalika_sdk.RepricingApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | Unique key retained for 24 hours. Reusing a key with another payload returns 409.
    create_repricer_exclusion_request = rivalika_sdk.CreateRepricerExclusionRequest() # CreateRepricerExclusionRequest | 

    try:
        # Create a repricer exclusion
        api_response = await api_instance.create_repricer_exclusion(idempotency_key, create_repricer_exclusion_request)
        print("The response of RepricingApi->create_repricer_exclusion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepricingApi->create_repricer_exclusion: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique key retained for 24 hours. Reusing a key with another payload returns 409. | 
 **create_repricer_exclusion_request** | [**CreateRepricerExclusionRequest**](CreateRepricerExclusionRequest.md)|  | 

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

# **create_repricer_policy**
> DataEnvelope create_repricer_policy(idempotency_key, create_repricer_policy_request)

Create a repricer policy

### Example

* Bearer (Rivalika API key) Authentication (RivalikaApiKey):

```python
import rivalika_sdk
from rivalika_sdk.models.create_repricer_policy_request import CreateRepricerPolicyRequest
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

# Configure Bearer authorization (Rivalika API key): RivalikaApiKey
configuration = rivalika_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with rivalika_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rivalika_sdk.RepricingApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | Unique key retained for 24 hours. Reusing a key with another payload returns 409.
    create_repricer_policy_request = rivalika_sdk.CreateRepricerPolicyRequest() # CreateRepricerPolicyRequest | 

    try:
        # Create a repricer policy
        api_response = await api_instance.create_repricer_policy(idempotency_key, create_repricer_policy_request)
        print("The response of RepricingApi->create_repricer_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepricingApi->create_repricer_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique key retained for 24 hours. Reusing a key with another payload returns 409. | 
 **create_repricer_policy_request** | [**CreateRepricerPolicyRequest**](CreateRepricerPolicyRequest.md)|  | 

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

# **create_repricer_run**
> AcceptedEnvelope create_repricer_run(idempotency_key)

Create a repricer run

### Example

* Bearer (Rivalika API key) Authentication (RivalikaApiKey):

```python
import rivalika_sdk
from rivalika_sdk.models.accepted_envelope import AcceptedEnvelope
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

# Configure Bearer authorization (Rivalika API key): RivalikaApiKey
configuration = rivalika_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with rivalika_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rivalika_sdk.RepricingApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | Unique key retained for 24 hours. Reusing a key with another payload returns 409.

    try:
        # Create a repricer run
        api_response = await api_instance.create_repricer_run(idempotency_key)
        print("The response of RepricingApi->create_repricer_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepricingApi->create_repricer_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique key retained for 24 hours. Reusing a key with another payload returns 409. | 

### Return type

[**AcceptedEnvelope**](AcceptedEnvelope.md)

### Authorization

[RivalikaApiKey](../README.md#RivalikaApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Invalid request |  -  |
**401** | Invalid or expired API key |  -  |
**403** | Missing required scope |  -  |
**409** | Conflict or idempotency mismatch |  -  |
**429** | Rate or concurrency limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_repricer_exclusion**
> DataEnvelope delete_repricer_exclusion(idempotency_key, exclusion_id)

Delete a repricer exclusion

### Example

* Bearer (Rivalika API key) Authentication (RivalikaApiKey):

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

# Configure Bearer authorization (Rivalika API key): RivalikaApiKey
configuration = rivalika_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with rivalika_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rivalika_sdk.RepricingApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | Unique key retained for 24 hours. Reusing a key with another payload returns 409.
    exclusion_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete a repricer exclusion
        api_response = await api_instance.delete_repricer_exclusion(idempotency_key, exclusion_id)
        print("The response of RepricingApi->delete_repricer_exclusion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepricingApi->delete_repricer_exclusion: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique key retained for 24 hours. Reusing a key with another payload returns 409. | 
 **exclusion_id** | **UUID**|  | 

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

# **delete_repricer_policy**
> DataEnvelope delete_repricer_policy(idempotency_key, policy_id)

Delete a repricer policy

### Example

* Bearer (Rivalika API key) Authentication (RivalikaApiKey):

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

# Configure Bearer authorization (Rivalika API key): RivalikaApiKey
configuration = rivalika_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with rivalika_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rivalika_sdk.RepricingApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | Unique key retained for 24 hours. Reusing a key with another payload returns 409.
    policy_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete a repricer policy
        api_response = await api_instance.delete_repricer_policy(idempotency_key, policy_id)
        print("The response of RepricingApi->delete_repricer_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepricingApi->delete_repricer_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique key retained for 24 hours. Reusing a key with another payload returns 409. | 
 **policy_id** | **UUID**|  | 

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

# **get_repricer_analytics**
> DataEnvelope get_repricer_analytics(currency, period, policy_id=policy_id, price_book_id=price_book_id)

Get repricer analytics

### Example

* Bearer (Rivalika API key) Authentication (RivalikaApiKey):

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

# Configure Bearer authorization (Rivalika API key): RivalikaApiKey
configuration = rivalika_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with rivalika_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rivalika_sdk.RepricingApi(api_client)
    currency = 'currency_example' # str | 
    period = 'period_example' # str | 
    policy_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |  (optional)
    price_book_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |  (optional)

    try:
        # Get repricer analytics
        api_response = await api_instance.get_repricer_analytics(currency, period, policy_id=policy_id, price_book_id=price_book_id)
        print("The response of RepricingApi->get_repricer_analytics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepricingApi->get_repricer_analytics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**|  | 
 **period** | **str**|  | 
 **policy_id** | **UUID**|  | [optional] 
 **price_book_id** | **UUID**|  | [optional] 

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

# **get_repricer_settings**
> DataEnvelope get_repricer_settings()

Get repricer settings

### Example

* Bearer (Rivalika API key) Authentication (RivalikaApiKey):

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

# Configure Bearer authorization (Rivalika API key): RivalikaApiKey
configuration = rivalika_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with rivalika_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rivalika_sdk.RepricingApi(api_client)

    try:
        # Get repricer settings
        api_response = await api_instance.get_repricer_settings()
        print("The response of RepricingApi->get_repricer_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepricingApi->get_repricer_settings: %s\n" % e)
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

# **list_repricer_applications**
> ListEnvelope list_repricer_applications()

List repricer applications

### Example

* Bearer (Rivalika API key) Authentication (RivalikaApiKey):

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

# Configure Bearer authorization (Rivalika API key): RivalikaApiKey
configuration = rivalika_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with rivalika_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rivalika_sdk.RepricingApi(api_client)

    try:
        # List repricer applications
        api_response = await api_instance.list_repricer_applications()
        print("The response of RepricingApi->list_repricer_applications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepricingApi->list_repricer_applications: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

# **list_repricer_exclusions**
> ListEnvelope list_repricer_exclusions(page=page, size=size, q=q, enabled=enabled, scope_type=scope_type, scope_target_ids=scope_target_ids, expiry_state=expiry_state, created_from=created_from, created_to=created_to, sort=sort, direction=direction)

List repricer exclusions

### Example

* Bearer (Rivalika API key) Authentication (RivalikaApiKey):

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

# Configure Bearer authorization (Rivalika API key): RivalikaApiKey
configuration = rivalika_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with rivalika_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rivalika_sdk.RepricingApi(api_client)
    page = 56 # int |  (optional)
    size = 56 # int |  (optional)
    q = 'q_example' # str |  (optional)
    enabled = True # bool |  (optional)
    scope_type = 'scope_type_example' # str |  (optional)
    scope_target_ids = None # List[UUID] |  (optional)
    expiry_state = 'expiry_state_example' # str |  (optional)
    created_from = '2013-10-20' # date |  (optional)
    created_to = '2013-10-20' # date |  (optional)
    sort = 'sort_example' # str |  (optional)
    direction = 'direction_example' # str |  (optional)

    try:
        # List repricer exclusions
        api_response = await api_instance.list_repricer_exclusions(page=page, size=size, q=q, enabled=enabled, scope_type=scope_type, scope_target_ids=scope_target_ids, expiry_state=expiry_state, created_from=created_from, created_to=created_to, sort=sort, direction=direction)
        print("The response of RepricingApi->list_repricer_exclusions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepricingApi->list_repricer_exclusions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **size** | **int**|  | [optional] 
 **q** | **str**|  | [optional] 
 **enabled** | **bool**|  | [optional] 
 **scope_type** | **str**|  | [optional] 
 **scope_target_ids** | [**List[UUID]**](UUID.md)|  | [optional] 
 **expiry_state** | **str**|  | [optional] 
 **created_from** | **date**|  | [optional] 
 **created_to** | **date**|  | [optional] 
 **sort** | **str**|  | [optional] 
 **direction** | **str**|  | [optional] 

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

# **list_repricer_policies**
> ListEnvelope list_repricer_policies(page=page, size=size, q=q, enabled=enabled, strategies=strategies, scope_type=scope_type, scope_target_ids=scope_target_ids, priority_min=priority_min, priority_max=priority_max, guardrail_state=guardrail_state, sort=sort, direction=direction)

List repricer policies

### Example

* Bearer (Rivalika API key) Authentication (RivalikaApiKey):

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

# Configure Bearer authorization (Rivalika API key): RivalikaApiKey
configuration = rivalika_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with rivalika_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rivalika_sdk.RepricingApi(api_client)
    page = 56 # int |  (optional)
    size = 56 # int |  (optional)
    q = 'q_example' # str |  (optional)
    enabled = True # bool |  (optional)
    strategies = ['strategies_example'] # List[str] |  (optional)
    scope_type = 'scope_type_example' # str |  (optional)
    scope_target_ids = None # List[UUID] |  (optional)
    priority_min = 56 # int |  (optional)
    priority_max = 56 # int |  (optional)
    guardrail_state = 'guardrail_state_example' # str |  (optional)
    sort = 'sort_example' # str |  (optional)
    direction = 'direction_example' # str |  (optional)

    try:
        # List repricer policies
        api_response = await api_instance.list_repricer_policies(page=page, size=size, q=q, enabled=enabled, strategies=strategies, scope_type=scope_type, scope_target_ids=scope_target_ids, priority_min=priority_min, priority_max=priority_max, guardrail_state=guardrail_state, sort=sort, direction=direction)
        print("The response of RepricingApi->list_repricer_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepricingApi->list_repricer_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **size** | **int**|  | [optional] 
 **q** | **str**|  | [optional] 
 **enabled** | **bool**|  | [optional] 
 **strategies** | [**List[str]**](str.md)|  | [optional] 
 **scope_type** | **str**|  | [optional] 
 **scope_target_ids** | [**List[UUID]**](UUID.md)|  | [optional] 
 **priority_min** | **int**|  | [optional] 
 **priority_max** | **int**|  | [optional] 
 **guardrail_state** | **str**|  | [optional] 
 **sort** | **str**|  | [optional] 
 **direction** | **str**|  | [optional] 

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

# **list_repricer_recommendations**
> ListEnvelope list_repricer_recommendations(page=page, size=size, q=q, status=status, product_ids=product_ids, policy_ids=policy_ids, price_book_ids=price_book_ids, currencies=currencies, movement=movement, move_percent_min=move_percent_min, move_percent_max=move_percent_max, amount_field=amount_field, amount_min=amount_min, amount_max=amount_max, evidence_min=evidence_min, evidence_max=evidence_max, created_from=created_from, created_to=created_to, smart_filters=smart_filters, sort=sort, direction=direction)

List repricer recommendations

### Example

* Bearer (Rivalika API key) Authentication (RivalikaApiKey):

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

# Configure Bearer authorization (Rivalika API key): RivalikaApiKey
configuration = rivalika_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with rivalika_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rivalika_sdk.RepricingApi(api_client)
    page = 56 # int |  (optional)
    size = 56 # int |  (optional)
    q = 'q_example' # str |  (optional)
    status = 'status_example' # str |  (optional)
    product_ids = None # List[UUID] |  (optional)
    policy_ids = None # List[UUID] |  (optional)
    price_book_ids = None # List[UUID] |  (optional)
    currencies = ['currencies_example'] # List[str] |  (optional)
    movement = 'movement_example' # str |  (optional)
    move_percent_min = 3.4 # float |  (optional)
    move_percent_max = 3.4 # float |  (optional)
    amount_field = 'amount_field_example' # str |  (optional)
    amount_min = 3.4 # float |  (optional)
    amount_max = 3.4 # float |  (optional)
    evidence_min = 56 # int |  (optional)
    evidence_max = 56 # int |  (optional)
    created_from = '2013-10-20' # date |  (optional)
    created_to = '2013-10-20' # date |  (optional)
    smart_filters = ['smart_filters_example'] # List[str] |  (optional)
    sort = 'sort_example' # str |  (optional)
    direction = 'direction_example' # str |  (optional)

    try:
        # List repricer recommendations
        api_response = await api_instance.list_repricer_recommendations(page=page, size=size, q=q, status=status, product_ids=product_ids, policy_ids=policy_ids, price_book_ids=price_book_ids, currencies=currencies, movement=movement, move_percent_min=move_percent_min, move_percent_max=move_percent_max, amount_field=amount_field, amount_min=amount_min, amount_max=amount_max, evidence_min=evidence_min, evidence_max=evidence_max, created_from=created_from, created_to=created_to, smart_filters=smart_filters, sort=sort, direction=direction)
        print("The response of RepricingApi->list_repricer_recommendations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepricingApi->list_repricer_recommendations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **size** | **int**|  | [optional] 
 **q** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **product_ids** | [**List[UUID]**](UUID.md)|  | [optional] 
 **policy_ids** | [**List[UUID]**](UUID.md)|  | [optional] 
 **price_book_ids** | [**List[UUID]**](UUID.md)|  | [optional] 
 **currencies** | [**List[str]**](str.md)|  | [optional] 
 **movement** | **str**|  | [optional] 
 **move_percent_min** | **float**|  | [optional] 
 **move_percent_max** | **float**|  | [optional] 
 **amount_field** | **str**|  | [optional] 
 **amount_min** | **float**|  | [optional] 
 **amount_max** | **float**|  | [optional] 
 **evidence_min** | **int**|  | [optional] 
 **evidence_max** | **int**|  | [optional] 
 **created_from** | **date**|  | [optional] 
 **created_to** | **date**|  | [optional] 
 **smart_filters** | [**List[str]**](str.md)|  | [optional] 
 **sort** | **str**|  | [optional] 
 **direction** | **str**|  | [optional] 

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

# **list_repricer_runs**
> ListEnvelope list_repricer_runs(page=page, size=size, q=q, status=status, trigger=trigger, requested_from=requested_from, requested_to=requested_to, outcome=outcome, sort=sort, direction=direction)

List repricer runs

### Example

* Bearer (Rivalika API key) Authentication (RivalikaApiKey):

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

# Configure Bearer authorization (Rivalika API key): RivalikaApiKey
configuration = rivalika_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with rivalika_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rivalika_sdk.RepricingApi(api_client)
    page = 56 # int |  (optional)
    size = 56 # int |  (optional)
    q = 'q_example' # str |  (optional)
    status = 'status_example' # str |  (optional)
    trigger = 'trigger_example' # str |  (optional)
    requested_from = '2013-10-20' # date |  (optional)
    requested_to = '2013-10-20' # date |  (optional)
    outcome = 'outcome_example' # str |  (optional)
    sort = 'sort_example' # str |  (optional)
    direction = 'direction_example' # str |  (optional)

    try:
        # List repricer runs
        api_response = await api_instance.list_repricer_runs(page=page, size=size, q=q, status=status, trigger=trigger, requested_from=requested_from, requested_to=requested_to, outcome=outcome, sort=sort, direction=direction)
        print("The response of RepricingApi->list_repricer_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepricingApi->list_repricer_runs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **size** | **int**|  | [optional] 
 **q** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **trigger** | **str**|  | [optional] 
 **requested_from** | **date**|  | [optional] 
 **requested_to** | **date**|  | [optional] 
 **outcome** | **str**|  | [optional] 
 **sort** | **str**|  | [optional] 
 **direction** | **str**|  | [optional] 

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

# **rollback_repricer_application**
> DataEnvelope rollback_repricer_application(idempotency_key, application_id)

Rollback a repricer application

### Example

* Bearer (Rivalika API key) Authentication (RivalikaApiKey):

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

# Configure Bearer authorization (Rivalika API key): RivalikaApiKey
configuration = rivalika_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with rivalika_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rivalika_sdk.RepricingApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | Unique key retained for 24 hours. Reusing a key with another payload returns 409.
    application_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Rollback a repricer application
        api_response = await api_instance.rollback_repricer_application(idempotency_key, application_id)
        print("The response of RepricingApi->rollback_repricer_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepricingApi->rollback_repricer_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique key retained for 24 hours. Reusing a key with another payload returns 409. | 
 **application_id** | **UUID**|  | 

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

# **update_repricer_policy**
> DataEnvelope update_repricer_policy(idempotency_key, policy_id, create_repricer_policy_request)

Update a repricer policy

### Example

* Bearer (Rivalika API key) Authentication (RivalikaApiKey):

```python
import rivalika_sdk
from rivalika_sdk.models.create_repricer_policy_request import CreateRepricerPolicyRequest
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

# Configure Bearer authorization (Rivalika API key): RivalikaApiKey
configuration = rivalika_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with rivalika_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rivalika_sdk.RepricingApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | Unique key retained for 24 hours. Reusing a key with another payload returns 409.
    policy_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    create_repricer_policy_request = rivalika_sdk.CreateRepricerPolicyRequest() # CreateRepricerPolicyRequest | 

    try:
        # Update a repricer policy
        api_response = await api_instance.update_repricer_policy(idempotency_key, policy_id, create_repricer_policy_request)
        print("The response of RepricingApi->update_repricer_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepricingApi->update_repricer_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique key retained for 24 hours. Reusing a key with another payload returns 409. | 
 **policy_id** | **UUID**|  | 
 **create_repricer_policy_request** | [**CreateRepricerPolicyRequest**](CreateRepricerPolicyRequest.md)|  | 

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

# **update_repricer_settings**
> DataEnvelope update_repricer_settings(idempotency_key, update_repricer_settings_request)

Update repricer settings

### Example

* Bearer (Rivalika API key) Authentication (RivalikaApiKey):

```python
import rivalika_sdk
from rivalika_sdk.models.data_envelope import DataEnvelope
from rivalika_sdk.models.update_repricer_settings_request import UpdateRepricerSettingsRequest
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

# Configure Bearer authorization (Rivalika API key): RivalikaApiKey
configuration = rivalika_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with rivalika_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rivalika_sdk.RepricingApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | Unique key retained for 24 hours. Reusing a key with another payload returns 409.
    update_repricer_settings_request = rivalika_sdk.UpdateRepricerSettingsRequest() # UpdateRepricerSettingsRequest | 

    try:
        # Update repricer settings
        api_response = await api_instance.update_repricer_settings(idempotency_key, update_repricer_settings_request)
        print("The response of RepricingApi->update_repricer_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepricingApi->update_repricer_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique key retained for 24 hours. Reusing a key with another payload returns 409. | 
 **update_repricer_settings_request** | [**UpdateRepricerSettingsRequest**](UpdateRepricerSettingsRequest.md)|  | 

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

