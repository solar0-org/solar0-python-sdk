# solar0_python_sdk.SolarApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**solar_day_post**](SolarApi.md#solar_day_post) | **POST** /solar/day | Add day data to influxdb
[**solar_min_post**](SolarApi.md#solar_min_post) | **POST** /solar/min | Add minute data to influxdb


# **solar_day_post**
> List[DataSolarDayDatapoint] solar_day_post(tenant, request)

Add day data to influxdb

### Example


```python
import time
import os
import solar0_python_sdk
from solar0_python_sdk.models.data_solar_day_datapoint import DataSolarDayDatapoint
from solar0_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = solar0_python_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with solar0_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = solar0_python_sdk.SolarApi(api_client)
    tenant = 'tenant_example' # str | Tenant
    request = [solar0_python_sdk.DataSolarDayDatapoint()] # List[DataSolarDayDatapoint] | Request

    try:
        # Add day data to influxdb
        api_response = api_instance.solar_day_post(tenant, request)
        print("The response of SolarApi->solar_day_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SolarApi->solar_day_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant** | **str**| Tenant | 
 **request** | [**List[DataSolarDayDatapoint]**](DataSolarDayDatapoint.md)| Request | 

### Return type

[**List[DataSolarDayDatapoint]**](DataSolarDayDatapoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **solar_min_post**
> List[DataSolarMinDatapoint] solar_min_post(tenant, request)

Add minute data to influxdb

### Example


```python
import time
import os
import solar0_python_sdk
from solar0_python_sdk.models.data_solar_min_datapoint import DataSolarMinDatapoint
from solar0_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = solar0_python_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with solar0_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = solar0_python_sdk.SolarApi(api_client)
    tenant = 'tenant_example' # str | Tenant
    request = [solar0_python_sdk.DataSolarMinDatapoint()] # List[DataSolarMinDatapoint] | Request

    try:
        # Add minute data to influxdb
        api_response = api_instance.solar_min_post(tenant, request)
        print("The response of SolarApi->solar_min_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SolarApi->solar_min_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant** | **str**| Tenant | 
 **request** | [**List[DataSolarMinDatapoint]**](DataSolarMinDatapoint.md)| Request | 

### Return type

[**List[DataSolarMinDatapoint]**](DataSolarMinDatapoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

