# rivalika_sdk.CommercialCatalogApi

All URIs are relative to *https://api.rivalika.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_commercial_product**](CommercialCatalogApi.md#archive_commercial_product) | **POST** /api/v1/commercial/products/{productId}/archive | Archive a commercial product
[**create_commercial_partner**](CommercialCatalogApi.md#create_commercial_partner) | **POST** /api/v1/commercial/partners | Create a commercial partner
[**create_commercial_product**](CommercialCatalogApi.md#create_commercial_product) | **POST** /api/v1/commercial/products | Create a commercial product
[**delete_commercial_product**](CommercialCatalogApi.md#delete_commercial_product) | **DELETE** /api/v1/commercial/products/{commercial_product_id} | Delete a commercial product
[**delete_market_link**](CommercialCatalogApi.md#delete_market_link) | **DELETE** /api/v1/commercial/products/{commercial_product_id}/market-link | Remove a market link
[**get_commercial_partner**](CommercialCatalogApi.md#get_commercial_partner) | **GET** /api/v1/commercial/partners/{partner_id} | Get a commercial partner
[**get_commercial_product**](CommercialCatalogApi.md#get_commercial_product) | **GET** /api/v1/commercial/products/{commercial_product_id} | Get a commercial product
[**get_market_link**](CommercialCatalogApi.md#get_market_link) | **GET** /api/v1/commercial/products/{commercial_product_id}/market-link | Get a market link
[**list_commercial_partners**](CommercialCatalogApi.md#list_commercial_partners) | **GET** /api/v1/commercial/partners | List commercial partners
[**list_commercial_products**](CommercialCatalogApi.md#list_commercial_products) | **GET** /api/v1/commercial/products | List commercial products
[**restore_commercial_product**](CommercialCatalogApi.md#restore_commercial_product) | **POST** /api/v1/commercial/products/{productId}/restore | Restore a commercial product
[**set_market_link**](CommercialCatalogApi.md#set_market_link) | **PUT** /api/v1/commercial/products/{commercial_product_id}/market-link | Set a market link
[**update_commercial_partner**](CommercialCatalogApi.md#update_commercial_partner) | **PATCH** /api/v1/commercial/partners/{partner_id} | Update a commercial partner
[**update_commercial_product**](CommercialCatalogApi.md#update_commercial_product) | **PATCH** /api/v1/commercial/products/{commercial_product_id} | Update a commercial product


# **archive_commercial_product**
> CommercialProductLifecycleEnvelope archive_commercial_product(idempotency_key, product_id)

Archive a commercial product

### Example

* Bearer Authentication (RivalikaApiKey):

```python
import rivalika_sdk
from rivalika_sdk.models.commercial_product_lifecycle_envelope import CommercialProductLifecycleEnvelope
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
    api_instance = rivalika_sdk.CommercialCatalogApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | Unique key retained for 24 hours. Reusing a key with another payload returns 409.
    product_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Archive a commercial product
        api_response = await api_instance.archive_commercial_product(idempotency_key, product_id)
        print("The response of CommercialCatalogApi->archive_commercial_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommercialCatalogApi->archive_commercial_product: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique key retained for 24 hours. Reusing a key with another payload returns 409. | 
 **product_id** | **UUID**|  | 

### Return type

[**CommercialProductLifecycleEnvelope**](CommercialProductLifecycleEnvelope.md)

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
**404** | Resource not found |  -  |
**409** | Conflict or idempotency mismatch |  -  |
**429** | Rate or concurrency limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_commercial_partner**
> DataEnvelope create_commercial_partner(idempotency_key, create_commercial_partner_request)

Create a commercial partner

### Example

* Bearer Authentication (RivalikaApiKey):

```python
import rivalika_sdk
from rivalika_sdk.models.create_commercial_partner_request import CreateCommercialPartnerRequest
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
    api_instance = rivalika_sdk.CommercialCatalogApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | Unique key retained for 24 hours. Reusing a key with another payload returns 409.
    create_commercial_partner_request = rivalika_sdk.CreateCommercialPartnerRequest() # CreateCommercialPartnerRequest | 

    try:
        # Create a commercial partner
        api_response = await api_instance.create_commercial_partner(idempotency_key, create_commercial_partner_request)
        print("The response of CommercialCatalogApi->create_commercial_partner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommercialCatalogApi->create_commercial_partner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique key retained for 24 hours. Reusing a key with another payload returns 409. | 
 **create_commercial_partner_request** | [**CreateCommercialPartnerRequest**](CreateCommercialPartnerRequest.md)|  | 

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

# **create_commercial_product**
> DataEnvelope create_commercial_product(idempotency_key, create_commercial_product_request)

Create a commercial product

### Example

* Bearer Authentication (RivalikaApiKey):

```python
import rivalika_sdk
from rivalika_sdk.models.create_commercial_product_request import CreateCommercialProductRequest
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
    api_instance = rivalika_sdk.CommercialCatalogApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | Unique key retained for 24 hours. Reusing a key with another payload returns 409.
    create_commercial_product_request = rivalika_sdk.CreateCommercialProductRequest() # CreateCommercialProductRequest | 

    try:
        # Create a commercial product
        api_response = await api_instance.create_commercial_product(idempotency_key, create_commercial_product_request)
        print("The response of CommercialCatalogApi->create_commercial_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommercialCatalogApi->create_commercial_product: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique key retained for 24 hours. Reusing a key with another payload returns 409. | 
 **create_commercial_product_request** | [**CreateCommercialProductRequest**](CreateCommercialProductRequest.md)|  | 

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

# **delete_commercial_product**
> DataEnvelope delete_commercial_product(idempotency_key, commercial_product_id, delete_commercial_product_request)

Delete a commercial product

### Example

* Bearer Authentication (RivalikaApiKey):

```python
import rivalika_sdk
from rivalika_sdk.models.data_envelope import DataEnvelope
from rivalika_sdk.models.delete_commercial_product_request import DeleteCommercialProductRequest
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
    api_instance = rivalika_sdk.CommercialCatalogApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | Unique key retained for 24 hours. Reusing a key with another payload returns 409.
    commercial_product_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    delete_commercial_product_request = rivalika_sdk.DeleteCommercialProductRequest() # DeleteCommercialProductRequest | 

    try:
        # Delete a commercial product
        api_response = await api_instance.delete_commercial_product(idempotency_key, commercial_product_id, delete_commercial_product_request)
        print("The response of CommercialCatalogApi->delete_commercial_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommercialCatalogApi->delete_commercial_product: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique key retained for 24 hours. Reusing a key with another payload returns 409. | 
 **commercial_product_id** | **UUID**|  | 
 **delete_commercial_product_request** | [**DeleteCommercialProductRequest**](DeleteCommercialProductRequest.md)|  | 

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

# **delete_market_link**
> DataEnvelope delete_market_link(idempotency_key, commercial_product_id)

Remove a market link

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
    api_instance = rivalika_sdk.CommercialCatalogApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | Unique key retained for 24 hours. Reusing a key with another payload returns 409.
    commercial_product_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Remove a market link
        api_response = await api_instance.delete_market_link(idempotency_key, commercial_product_id)
        print("The response of CommercialCatalogApi->delete_market_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommercialCatalogApi->delete_market_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique key retained for 24 hours. Reusing a key with another payload returns 409. | 
 **commercial_product_id** | **UUID**|  | 

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

# **get_commercial_partner**
> DataEnvelope get_commercial_partner(partner_id)

Get a commercial partner

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
    api_instance = rivalika_sdk.CommercialCatalogApi(api_client)
    partner_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get a commercial partner
        api_response = await api_instance.get_commercial_partner(partner_id)
        print("The response of CommercialCatalogApi->get_commercial_partner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommercialCatalogApi->get_commercial_partner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partner_id** | **UUID**|  | 

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

# **get_commercial_product**
> DataEnvelope get_commercial_product(commercial_product_id)

Get a commercial product

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
    api_instance = rivalika_sdk.CommercialCatalogApi(api_client)
    commercial_product_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get a commercial product
        api_response = await api_instance.get_commercial_product(commercial_product_id)
        print("The response of CommercialCatalogApi->get_commercial_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommercialCatalogApi->get_commercial_product: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **commercial_product_id** | **UUID**|  | 

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

# **get_market_link**
> DataEnvelope get_market_link(commercial_product_id)

Get a market link

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
    api_instance = rivalika_sdk.CommercialCatalogApi(api_client)
    commercial_product_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get a market link
        api_response = await api_instance.get_market_link(commercial_product_id)
        print("The response of CommercialCatalogApi->get_market_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommercialCatalogApi->get_market_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **commercial_product_id** | **UUID**|  | 

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

# **list_commercial_partners**
> ListEnvelope list_commercial_partners(page=page, size=size, search=search, role=role, active=active, sort_by=sort_by, sort_direction=sort_direction)

List commercial partners

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
    api_instance = rivalika_sdk.CommercialCatalogApi(api_client)
    page = 56 # int |  (optional)
    size = 56 # int |  (optional)
    search = 'search_example' # str |  (optional)
    role = 'role_example' # str |  (optional)
    active = True # bool |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)

    try:
        # List commercial partners
        api_response = await api_instance.list_commercial_partners(page=page, size=size, search=search, role=role, active=active, sort_by=sort_by, sort_direction=sort_direction)
        print("The response of CommercialCatalogApi->list_commercial_partners:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommercialCatalogApi->list_commercial_partners: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **size** | **int**|  | [optional] 
 **search** | **str**|  | [optional] 
 **role** | **str**|  | [optional] 
 **active** | **bool**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 

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

# **list_commercial_products**
> ListEnvelope list_commercial_products(page=page, size=size, search=search, status=status, match_state=match_state, brands=brands, categories=categories, stock_min=stock_min, stock_max=stock_max, money_field=money_field, money_min=money_min, money_max=money_max, money_currency=money_currency, smart_filters=smart_filters, sort_by=sort_by, sort_direction=sort_direction)

List commercial products

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
    api_instance = rivalika_sdk.CommercialCatalogApi(api_client)
    page = 56 # int |  (optional)
    size = 56 # int |  (optional)
    search = 'search_example' # str |  (optional)
    status = 'status_example' # str |  (optional)
    match_state = 'match_state_example' # str |  (optional)
    brands = ['brands_example'] # List[str] |  (optional)
    categories = ['categories_example'] # List[str] |  (optional)
    stock_min = 56 # int |  (optional)
    stock_max = 56 # int |  (optional)
    money_field = 'money_field_example' # str |  (optional)
    money_min = 3.4 # float |  (optional)
    money_max = 3.4 # float |  (optional)
    money_currency = 'money_currency_example' # str |  (optional)
    smart_filters = ['smart_filters_example'] # List[str] |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)

    try:
        # List commercial products
        api_response = await api_instance.list_commercial_products(page=page, size=size, search=search, status=status, match_state=match_state, brands=brands, categories=categories, stock_min=stock_min, stock_max=stock_max, money_field=money_field, money_min=money_min, money_max=money_max, money_currency=money_currency, smart_filters=smart_filters, sort_by=sort_by, sort_direction=sort_direction)
        print("The response of CommercialCatalogApi->list_commercial_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommercialCatalogApi->list_commercial_products: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **size** | **int**|  | [optional] 
 **search** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **match_state** | **str**|  | [optional] 
 **brands** | [**List[str]**](str.md)|  | [optional] 
 **categories** | [**List[str]**](str.md)|  | [optional] 
 **stock_min** | **int**|  | [optional] 
 **stock_max** | **int**|  | [optional] 
 **money_field** | **str**|  | [optional] 
 **money_min** | **float**|  | [optional] 
 **money_max** | **float**|  | [optional] 
 **money_currency** | **str**|  | [optional] 
 **smart_filters** | [**List[str]**](str.md)|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 

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

# **restore_commercial_product**
> CommercialProductLifecycleEnvelope restore_commercial_product(idempotency_key, product_id)

Restore a commercial product

### Example

* Bearer Authentication (RivalikaApiKey):

```python
import rivalika_sdk
from rivalika_sdk.models.commercial_product_lifecycle_envelope import CommercialProductLifecycleEnvelope
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
    api_instance = rivalika_sdk.CommercialCatalogApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | Unique key retained for 24 hours. Reusing a key with another payload returns 409.
    product_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Restore a commercial product
        api_response = await api_instance.restore_commercial_product(idempotency_key, product_id)
        print("The response of CommercialCatalogApi->restore_commercial_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommercialCatalogApi->restore_commercial_product: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique key retained for 24 hours. Reusing a key with another payload returns 409. | 
 **product_id** | **UUID**|  | 

### Return type

[**CommercialProductLifecycleEnvelope**](CommercialProductLifecycleEnvelope.md)

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
**404** | Resource not found |  -  |
**409** | Conflict or idempotency mismatch |  -  |
**429** | Rate or concurrency limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_market_link**
> DataEnvelope set_market_link(idempotency_key, commercial_product_id, set_market_link_request)

Set a market link

### Example

* Bearer Authentication (RivalikaApiKey):

```python
import rivalika_sdk
from rivalika_sdk.models.data_envelope import DataEnvelope
from rivalika_sdk.models.set_market_link_request import SetMarketLinkRequest
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
    api_instance = rivalika_sdk.CommercialCatalogApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | Unique key retained for 24 hours. Reusing a key with another payload returns 409.
    commercial_product_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    set_market_link_request = rivalika_sdk.SetMarketLinkRequest() # SetMarketLinkRequest | 

    try:
        # Set a market link
        api_response = await api_instance.set_market_link(idempotency_key, commercial_product_id, set_market_link_request)
        print("The response of CommercialCatalogApi->set_market_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommercialCatalogApi->set_market_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique key retained for 24 hours. Reusing a key with another payload returns 409. | 
 **commercial_product_id** | **UUID**|  | 
 **set_market_link_request** | [**SetMarketLinkRequest**](SetMarketLinkRequest.md)|  | 

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

# **update_commercial_partner**
> DataEnvelope update_commercial_partner(idempotency_key, partner_id, update_commercial_partner_request)

Update a commercial partner

### Example

* Bearer Authentication (RivalikaApiKey):

```python
import rivalika_sdk
from rivalika_sdk.models.data_envelope import DataEnvelope
from rivalika_sdk.models.update_commercial_partner_request import UpdateCommercialPartnerRequest
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
    api_instance = rivalika_sdk.CommercialCatalogApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | Unique key retained for 24 hours. Reusing a key with another payload returns 409.
    partner_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    update_commercial_partner_request = rivalika_sdk.UpdateCommercialPartnerRequest() # UpdateCommercialPartnerRequest | 

    try:
        # Update a commercial partner
        api_response = await api_instance.update_commercial_partner(idempotency_key, partner_id, update_commercial_partner_request)
        print("The response of CommercialCatalogApi->update_commercial_partner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommercialCatalogApi->update_commercial_partner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique key retained for 24 hours. Reusing a key with another payload returns 409. | 
 **partner_id** | **UUID**|  | 
 **update_commercial_partner_request** | [**UpdateCommercialPartnerRequest**](UpdateCommercialPartnerRequest.md)|  | 

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

# **update_commercial_product**
> DataEnvelope update_commercial_product(idempotency_key, commercial_product_id, update_commercial_product_request)

Update a commercial product

### Example

* Bearer Authentication (RivalikaApiKey):

```python
import rivalika_sdk
from rivalika_sdk.models.data_envelope import DataEnvelope
from rivalika_sdk.models.update_commercial_product_request import UpdateCommercialProductRequest
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
    api_instance = rivalika_sdk.CommercialCatalogApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | Unique key retained for 24 hours. Reusing a key with another payload returns 409.
    commercial_product_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    update_commercial_product_request = rivalika_sdk.UpdateCommercialProductRequest() # UpdateCommercialProductRequest | 

    try:
        # Update a commercial product
        api_response = await api_instance.update_commercial_product(idempotency_key, commercial_product_id, update_commercial_product_request)
        print("The response of CommercialCatalogApi->update_commercial_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommercialCatalogApi->update_commercial_product: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique key retained for 24 hours. Reusing a key with another payload returns 409. | 
 **commercial_product_id** | **UUID**|  | 
 **update_commercial_product_request** | [**UpdateCommercialProductRequest**](UpdateCommercialProductRequest.md)|  | 

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

