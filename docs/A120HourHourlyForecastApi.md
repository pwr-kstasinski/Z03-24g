# openapi_client.A120HourHourlyForecastApi

All URIs are relative to *https://api.weatherbit.io/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**forecast_hourly_get**](A120HourHourlyForecastApi.md#forecast_hourly_get) | **GET** /forecast/hourly | Returns an 120 hour (hourly forecast) - Given City and/or State, Country.


# **forecast_hourly_get**
> ForecastHourly forecast_hourly_get(city, key)

Returns an 120 hour (hourly forecast) - Given City and/or State, Country.

 Returns an hourly forecast, where each point represents a one hour   period. Every point has a datetime string in the format \"YYYY-MM-DD:HH\". Time is UTC. Accepts a city in the format of City,ST or City. The state, and country parameters can be provided to make the search more accurate. 

### Example

```python
import time
import openapi_client
from openapi_client.api import a_120_hour___hourly_forecast_api
from openapi_client.model.error import Error
from openapi_client.model.forecast_hourly import ForecastHourly
from pprint import pprint
# Defining the host is optional and defaults to https://api.weatherbit.io/v2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.weatherbit.io/v2.0"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = a_120_hour___hourly_forecast_api.A120HourHourlyForecastApi(api_client)
    city = "city_example" # str | City search.. Example - &city=Raleigh,NC or &city=Berlin,DE or city=Paris&country=FR
    key = "key_example" # str | Your registered API key.
    state = "state_example" # str | Full name of state. (optional)
    country = "country_example" # str | Country Code (2 letter). (optional)
    units = "S" # str | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a> (optional)
    lang = "ar" # str | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a> (optional)
    param_callback = "callback_example" # str | Wraps return in jsonp callback. Example: callback=func (optional)
    hours = 1 # int | Number of hours to return. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns an 120 hour (hourly forecast) - Given City and/or State, Country.
        api_response = api_instance.forecast_hourly_get(city, key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling A120HourHourlyForecastApi->forecast_hourly_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns an 120 hour (hourly forecast) - Given City and/or State, Country.
        api_response = api_instance.forecast_hourly_get(city, key, state=state, country=country, units=units, lang=lang, param_callback=param_callback, hours=hours)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling A120HourHourlyForecastApi->forecast_hourly_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **city** | **str**| City search.. Example - &amp;city&#x3D;Raleigh,NC or &amp;city&#x3D;Berlin,DE or city&#x3D;Paris&amp;country&#x3D;FR |
 **key** | **str**| Your registered API key. |
 **state** | **str**| Full name of state. | [optional]
 **country** | **str**| Country Code (2 letter). | [optional]
 **units** | **str**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional]
 **lang** | **str**| Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt; | [optional]
 **param_callback** | **str**| Wraps return in jsonp callback. Example: callback&#x3D;func | [optional]
 **hours** | **int**| Number of hours to return. | [optional]

### Return type

[**ForecastHourly**](ForecastHourly.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A forecast object. |  -  |
**0** | No Data. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

