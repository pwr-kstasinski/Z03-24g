# openapi_client.HistoricalDegreeDayAPIApi

All URIs are relative to *https://api.weatherbit.io/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**history_energy_bboxlat1lat1lon1lon1lat2lat2lon2lon2_get**](HistoricalDegreeDayAPIApi.md#history_energy_bboxlat1lat1lon1lon1lat2lat2lon2lon2_get) | **GET** /history/energy/bbox?lat1&#x3D;{lat1}&amp;lon1&#x3D;{lon1}&amp;lat2&#x3D;{lat2}&amp;lon2&#x3D;{lon2} | Returns multiple locations given a bounding box. 
[**history_energylatlatlonlon_get**](HistoricalDegreeDayAPIApi.md#history_energylatlatlonlon_get) | **GET** /history/energy?lat&#x3D;{lat}&amp;lon&#x3D;{lon} | Returns Energy API response  - Given a single lat/lon. 


# **history_energy_bboxlat1lat1lon1lon1lat2lat2lon2lon2_get**
> EnergyObsGroup history_energy_bboxlat1lat1lon1lon1lat2lat2lon2lon2_get(lat1, lon1, lat2, lon2, start_date, end_date, key)

Returns multiple locations given a bounding box. 

Returns aggregate energy specific historical weather fields, over a specified time period. Supply a bounding box ex: lat1=40&lon1=-78&lat2=38&lon2=-80. This API will return UP TO 150 stations, aggregated by the specified time period start_date to end_date. 

### Example

```python
import time
import openapi_client
from openapi_client.api import historical_degree_day_api_api
from openapi_client.model.energy_obs_group import EnergyObsGroup
from openapi_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.weatherbit.io/v2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.weatherbit.io/v2.0"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = historical_degree_day_api_api.HistoricalDegreeDayAPIApi(api_client)
    lat1 = 3.14 # float | Latitude of upper left corner.
    lon1 = 3.14 # float | Longitude of upper left corner.
    lat2 = 3.14 # float | Latitude of lower right corner.
    lon2 = 3.14 # float | Longitude of lower right corner.
    start_date = "start_date_example" # str | Start Date (YYYY-MM-DD or YYYY-MM-DD:HH).
    end_date = "end_date_example" # str | End Date (YYYY-MM-DD or YYYY-MM-DD:HH).
    key = "key_example" # str | Your registered API key.
    threshold = 3.14 # float | Temperature threshold to use to calculate degree days (default 18 C)  (optional)
    units = "S" # str | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a> (optional)
    param_callback = "callback_example" # str | Wraps return in jsonp callback. Example: callback=func (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns multiple locations given a bounding box. 
        api_response = api_instance.history_energy_bboxlat1lat1lon1lon1lat2lat2lon2lon2_get(lat1, lon1, lat2, lon2, start_date, end_date, key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling HistoricalDegreeDayAPIApi->history_energy_bboxlat1lat1lon1lon1lat2lat2lon2lon2_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns multiple locations given a bounding box. 
        api_response = api_instance.history_energy_bboxlat1lat1lon1lon1lat2lat2lon2lon2_get(lat1, lon1, lat2, lon2, start_date, end_date, key, threshold=threshold, units=units, param_callback=param_callback)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling HistoricalDegreeDayAPIApi->history_energy_bboxlat1lat1lon1lon1lat2lat2lon2lon2_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lat1** | **float**| Latitude of upper left corner. |
 **lon1** | **float**| Longitude of upper left corner. |
 **lat2** | **float**| Latitude of lower right corner. |
 **lon2** | **float**| Longitude of lower right corner. |
 **start_date** | **str**| Start Date (YYYY-MM-DD or YYYY-MM-DD:HH). |
 **end_date** | **str**| End Date (YYYY-MM-DD or YYYY-MM-DD:HH). |
 **key** | **str**| Your registered API key. |
 **threshold** | **float**| Temperature threshold to use to calculate degree days (default 18 C)  | [optional]
 **units** | **str**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional]
 **param_callback** | **str**| Wraps return in jsonp callback. Example: callback&#x3D;func | [optional]

### Return type

[**EnergyObsGroup**](EnergyObsGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An Energy Data Object. |  -  |
**0** | No Data. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **history_energylatlatlonlon_get**
> EnergyObsGroup history_energylatlatlonlon_get(lat, lon, start_date, end_date, key)

Returns Energy API response  - Given a single lat/lon. 

Returns aggregate energy specific historical weather fields, over a specified time period.

### Example

```python
import time
import openapi_client
from openapi_client.api import historical_degree_day_api_api
from openapi_client.model.energy_obs_group import EnergyObsGroup
from openapi_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.weatherbit.io/v2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.weatherbit.io/v2.0"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = historical_degree_day_api_api.HistoricalDegreeDayAPIApi(api_client)
    lat = 3.14 # float | Latitude component of location.
    lon = 3.14 # float | Longitude component of location.
    start_date = "start_date_example" # str | Start Date (YYYY-MM-DD or YYYY-MM-DD:HH).
    end_date = "end_date_example" # str | End Date (YYYY-MM-DD or YYYY-MM-DD:HH).
    key = "key_example" # str | Your registered API key.
    tp = "hourly" # str | Time period to aggregate by (daily, monthly) (optional)
    threshold = 3.14 # float | Temperature threshold to use to calculate degree days (default 18 C)  (optional)
    units = "S" # str | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a> (optional)
    param_callback = "callback_example" # str | Wraps return in jsonp callback. Example: callback=func (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns Energy API response  - Given a single lat/lon. 
        api_response = api_instance.history_energylatlatlonlon_get(lat, lon, start_date, end_date, key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling HistoricalDegreeDayAPIApi->history_energylatlatlonlon_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns Energy API response  - Given a single lat/lon. 
        api_response = api_instance.history_energylatlatlonlon_get(lat, lon, start_date, end_date, key, tp=tp, threshold=threshold, units=units, param_callback=param_callback)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling HistoricalDegreeDayAPIApi->history_energylatlatlonlon_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lat** | **float**| Latitude component of location. |
 **lon** | **float**| Longitude component of location. |
 **start_date** | **str**| Start Date (YYYY-MM-DD or YYYY-MM-DD:HH). |
 **end_date** | **str**| End Date (YYYY-MM-DD or YYYY-MM-DD:HH). |
 **key** | **str**| Your registered API key. |
 **tp** | **str**| Time period to aggregate by (daily, monthly) | [optional]
 **threshold** | **float**| Temperature threshold to use to calculate degree days (default 18 C)  | [optional]
 **units** | **str**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional]
 **param_callback** | **str**| Wraps return in jsonp callback. Example: callback&#x3D;func | [optional]

### Return type

[**EnergyObsGroup**](EnergyObsGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An Energy Data Object. |  -  |
**0** | No Data. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

