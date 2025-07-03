# aind_sharepoint_service_async_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_las2020**](DefaultApi.md#get_las2020) | **GET** /las_2020/{subject_id} | Get Las 2020
[**get_nsb2019**](DefaultApi.md#get_nsb2019) | **GET** /nsb_2019/{subject_id} | Get Nsb 2019
[**get_nsb2023**](DefaultApi.md#get_nsb2023) | **GET** /nsb_2023/{subject_id} | Get Nsb 2023
[**get_nsb_present**](DefaultApi.md#get_nsb_present) | **GET** /nsb_present/{subject_id} | Get Nsb Present


# **get_las2020**
> List[Las2020List] get_las2020(subject_id)

Get Las 2020

# LAS 2020 Endpoint
Retrieve information from the LAS 2020 list for a given subject ID.

### Example


```python
import aind_sharepoint_service_async_client
from aind_sharepoint_service_async_client.models.las2020_list import Las2020List
from aind_sharepoint_service_async_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = aind_sharepoint_service_async_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with aind_sharepoint_service_async_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aind_sharepoint_service_async_client.DefaultApi(api_client)
    subject_id = '805811' # str | 

    try:
        # Get Las 2020
        api_response = await api_instance.get_las2020(subject_id)
        print("The response of DefaultApi->get_las2020:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_las2020: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject_id** | **str**|  | 

### Return type

[**List[Las2020List]**](Las2020List.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nsb2019**
> List[NSB2019List] get_nsb2019(subject_id)

Get Nsb 2019

# NSB 2019 Endpoint
Retrieve information from the NSB 2019 list for a given subject ID.

### Example


```python
import aind_sharepoint_service_async_client
from aind_sharepoint_service_async_client.models.nsb2019_list import NSB2019List
from aind_sharepoint_service_async_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = aind_sharepoint_service_async_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with aind_sharepoint_service_async_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aind_sharepoint_service_async_client.DefaultApi(api_client)
    subject_id = '656374' # str | 

    try:
        # Get Nsb 2019
        api_response = await api_instance.get_nsb2019(subject_id)
        print("The response of DefaultApi->get_nsb2019:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_nsb2019: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject_id** | **str**|  | 

### Return type

[**List[NSB2019List]**](NSB2019List.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nsb2023**
> List[NSB2023List] get_nsb2023(subject_id)

Get Nsb 2023

# NSB 2023 Endpoint
Retrieve information from the NSB 2023-Archive list for a given subject ID.

### Example


```python
import aind_sharepoint_service_async_client
from aind_sharepoint_service_async_client.models.nsb2023_list import NSB2023List
from aind_sharepoint_service_async_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = aind_sharepoint_service_async_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with aind_sharepoint_service_async_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aind_sharepoint_service_async_client.DefaultApi(api_client)
    subject_id = '657849' # str | 

    try:
        # Get Nsb 2023
        api_response = await api_instance.get_nsb2023(subject_id)
        print("The response of DefaultApi->get_nsb2023:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_nsb2023: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject_id** | **str**|  | 

### Return type

[**List[NSB2023List]**](NSB2023List.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nsb_present**
> List[NSB2023List] get_nsb_present(subject_id)

Get Nsb Present

# NSB Present Endpoint
Retrieve information from the NSB 2023-Present list for a given subject ID.

### Example


```python
import aind_sharepoint_service_async_client
from aind_sharepoint_service_async_client.models.nsb2023_list import NSB2023List
from aind_sharepoint_service_async_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = aind_sharepoint_service_async_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with aind_sharepoint_service_async_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aind_sharepoint_service_async_client.DefaultApi(api_client)
    subject_id = '790025' # str | 

    try:
        # Get Nsb Present
        api_response = await api_instance.get_nsb_present(subject_id)
        print("The response of DefaultApi->get_nsb_present:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_nsb_present: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject_id** | **str**|  | 

### Return type

[**List[NSB2023List]**](NSB2023List.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

