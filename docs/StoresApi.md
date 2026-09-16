# rivalika_sdk.StoresApi

All URIs are relative to *https://api.rivalika.md*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_store**](StoresApi.md#get_store) | **GET** /api/v1/stores/{store_id} | Get a monitored store
[**list_stores**](StoresApi.md#list_stores) | **GET** /api/v1/stores | List monitored stores
[**track_store**](StoresApi.md#track_store) | **POST** /api/v1/stores/{store_id}/track | Track a store
[**untrack_store**](StoresApi.md#untrack_store) | **DELETE** /api/v1/stores/{store_id}/track | Stop tracking a store


# **get_store**
> DataEnvelope get_store(store_id)

Get a monitored store

### Example

* Bearer Authentication (RivalikaApiKey):

```python
import rivalika_sdk
from rivalika_sdk.models.data_envelope import DataEnvelope
from rivalika_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rivalika.md
# See configuration.py for a list of all supported configuration parameters.
configuration = rivalika_sdk.Configuration(
    host = "https://api.rivalika.md"
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
    api_instance = rivalika_sdk.StoresApi(api_client)
    store_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get a monitored store
        api_response = await api_instance.get_store(store_id)
        print("The response of StoresApi->get_store:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoresApi->get_store: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **UUID**|  | 

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

# **list_stores**
> ListEnvelope list_stores(page=page, size=size, search=search)

List monitored stores

### Example

* Bearer Authentication (RivalikaApiKey):

```python
import rivalika_sdk
from rivalika_sdk.models.list_envelope import ListEnvelope
from rivalika_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rivalika.md
# See configuration.py for a list of all supported configuration parameters.
configuration = rivalika_sdk.Configuration(
    host = "https://api.rivalika.md"
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
    api_instance = rivalika_sdk.StoresApi(api_client)
    page = 56 # int |  (optional)
    size = 56 # int |  (optional)
    search = 'search_example' # str |  (optional)

    try:
        # List monitored stores
        api_response = await api_instance.list_stores(page=page, size=size, search=search)
        print("The response of StoresApi->list_stores:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoresApi->list_stores: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **size** | **int**|  | [optional] 
 **search** | **str**|  | [optional] 

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

# **track_store**
> DataEnvelope track_store(idempotency_key, store_id)

Track a store

### Example

* Bearer Authentication (RivalikaApiKey):

```python
import rivalika_sdk
from rivalika_sdk.models.data_envelope import DataEnvelope
from rivalika_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rivalika.md
# See configuration.py for a list of all supported configuration parameters.
configuration = rivalika_sdk.Configuration(
    host = "https://api.rivalika.md"
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
    api_instance = rivalika_sdk.StoresApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | Unique key retained for 24 hours. Reusing a key with another payload returns 409.
    store_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Track a store
        api_response = await api_instance.track_store(idempotency_key, store_id)
        print("The response of StoresApi->track_store:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoresApi->track_store: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique key retained for 24 hours. Reusing a key with another payload returns 409. | 
 **store_id** | **UUID**|  | 

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
**201** | Success |  -  |
**400** | Invalid request |  -  |
**401** | Invalid or expired API key |  -  |
**403** | Missing required scope |  -  |
**409** | Conflict or idempotency mismatch |  -  |
**429** | Rate or concurrency limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **untrack_store**
> DataEnvelope untrack_store(idempotency_key, store_id)

Stop tracking a store

### Example

* Bearer Authentication (RivalikaApiKey):

```python
import rivalika_sdk
from rivalika_sdk.models.data_envelope import DataEnvelope
from rivalika_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rivalika.md
# See configuration.py for a list of all supported configuration parameters.
configuration = rivalika_sdk.Configuration(
    host = "https://api.rivalika.md"
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
    api_instance = rivalika_sdk.StoresApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | Unique key retained for 24 hours. Reusing a key with another payload returns 409.
    store_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Stop tracking a store
        api_response = await api_instance.untrack_store(idempotency_key, store_id)
        print("The response of StoresApi->untrack_store:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoresApi->untrack_store: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique key retained for 24 hours. Reusing a key with another payload returns 409. | 
 **store_id** | **UUID**|  | 

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

