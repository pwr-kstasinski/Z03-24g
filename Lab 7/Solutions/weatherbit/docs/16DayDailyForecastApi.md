# openapi_client.16DayDailyForecastApi

All URIs are relative to *https://api.weatherbit.io/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**forecast_dailycity_idcity_id_get**](16DayDailyForecastApi.md#forecast_dailycity_idcity_id_get) | **GET** /forecast/daily?city_id&#x3D;{city_id} | Returns a daily forecast - Given a City ID.
[**forecast_dailycitycitycountrycountry_get**](16DayDailyForecastApi.md#forecast_dailycitycitycountrycountry_get) | **GET** /forecast/daily?city&#x3D;{city}&amp;country&#x3D;{country} | Returns a daily forecast - Given City and/or State, Country.
[**forecast_dailylatlatlonlon_get**](16DayDailyForecastApi.md#forecast_dailylatlatlonlon_get) | **GET** /forecast/daily?lat&#x3D;{lat}&amp;lon&#x3D;{lon} | Returns a daily forecast - Given Lat/Lon.
[**forecast_dailypostal_codepostal_code_get**](16DayDailyForecastApi.md#forecast_dailypostal_codepostal_code_get) | **GET** /forecast/daily?postal_code&#x3D;{postal_code} | Returns a daily forecast - Given a Postal Code.


# **forecast_dailycity_idcity_id_get**
> ForecastDay forecast_dailycity_idcity_id_get(city_id, key)

Returns a daily forecast - Given a City ID.

Returns a daily forecast, where each point represents one day (24hr) period. Every point has a datetime string in the format \"YYYY-MM-DD\". One day begins at 00:00 UTC, and ends at 23:59 UTC. 

### Example

```python
import time
import openapi_client
from openapi_client.api import 16_day___daily_forecast_api
from openapi_client.model.error import Error
from openapi_client.model.forecast_day import ForecastDay
from pprint import pprint
# Defining the host is optional and defaults to https://api.weatherbit.io/v2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.weatherbit.io/v2.0"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = 16_day___daily_forecast_api.16DayDailyForecastApi(api_client)
    city_id = 1 # int | City ID. Example: 4487042
    key = "key_example" # str | Your registered API key.
    days = 3.14 # float | Number of days to return. Default 16. (optional)
    units = "S" # str | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a> (optional)
    lang = "ar" # str | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a> (optional)
    param_callback = "callback_example" # str | Wraps return in jsonp callback. Example: callback=func (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a daily forecast - Given a City ID.
        api_response = api_instance.forecast_dailycity_idcity_id_get(city_id, key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling 16DayDailyForecastApi->forecast_dailycity_idcity_id_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a daily forecast - Given a City ID.
        api_response = api_instance.forecast_dailycity_idcity_id_get(city_id, key, days=days, units=units, lang=lang, param_callback=param_callback)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling 16DayDailyForecastApi->forecast_dailycity_idcity_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **city_id** | **int**| City ID. Example: 4487042 |
 **key** | **str**| Your registered API key. |
 **days** | **float**| Number of days to return. Default 16. | [optional]
 **units** | **str**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional]
 **lang** | **str**| Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt; | [optional]
 **param_callback** | **str**| Wraps return in jsonp callback. Example: callback&#x3D;func | [optional]

### Return type

[**ForecastDay**](ForecastDay.md)

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

# **forecast_dailycitycitycountrycountry_get**
> ForecastDay forecast_dailycitycitycountrycountry_get(city, country, key)

Returns a daily forecast - Given City and/or State, Country.

Returns a daily forecast, where each point represents one day (24hr) period. Every point has a datetime string in the format \"YYYY-MM-DD\". One day begins at 00:00 UTC, and ends at 23:59 UTC. Accepts a city in the format of City,ST or City. The state, and country parameters can be provided to make the search more accurate. 

### Example

```python
import time
import openapi_client
from openapi_client.api import 16_day___daily_forecast_api
from openapi_client.model.error import Error
from openapi_client.model.forecast_day import ForecastDay
from pprint import pprint
# Defining the host is optional and defaults to https://api.weatherbit.io/v2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.weatherbit.io/v2.0"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = 16_day___daily_forecast_api.16DayDailyForecastApi(api_client)
    city = "city_example" # str | City search.. Example - &city=Raleigh,NC or &city=Berlin,DE or city=Paris&country=FR
    country = "country_example" # str | Country Code (2 letter).
    key = "key_example" # str | Your registered API key.
    state = "state_example" # str | Full name of state. (optional)
    days = 3.14 # float | Number of days to return. Default 16. (optional)
    units = "S" # str | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a> (optional)
    lang = "ar" # str | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a> (optional)
    param_callback = "callback_example" # str | Wraps return in jsonp callback. Example - callback=func (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a daily forecast - Given City and/or State, Country.
        api_response = api_instance.forecast_dailycitycitycountrycountry_get(city, country, key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling 16DayDailyForecastApi->forecast_dailycitycitycountrycountry_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a daily forecast - Given City and/or State, Country.
        api_response = api_instance.forecast_dailycitycitycountrycountry_get(city, country, key, state=state, days=days, units=units, lang=lang, param_callback=param_callback)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling 16DayDailyForecastApi->forecast_dailycitycitycountrycountry_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **city** | **str**| City search.. Example - &amp;city&#x3D;Raleigh,NC or &amp;city&#x3D;Berlin,DE or city&#x3D;Paris&amp;country&#x3D;FR |
 **country** | **str**| Country Code (2 letter). |
 **key** | **str**| Your registered API key. |
 **state** | **str**| Full name of state. | [optional]
 **days** | **float**| Number of days to return. Default 16. | [optional]
 **units** | **str**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional]
 **lang** | **str**| Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt; | [optional]
 **param_callback** | **str**| Wraps return in jsonp callback. Example - callback&#x3D;func | [optional]

### Return type

[**ForecastDay**](ForecastDay.md)

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

# **forecast_dailylatlatlonlon_get**
> ForecastDay forecast_dailylatlatlonlon_get(lat, lon, key)

Returns a daily forecast - Given Lat/Lon.

Returns a daily forecast, where each point represents one day (24hr) period. Every point has a datetime string in the format \"YYYY-MM-DD\". One day begins at 00:00 UTC, and ends at 23:59 UTC.  

### Example

```python
import time
import openapi_client
from openapi_client.api import 16_day___daily_forecast_api
from openapi_client.model.error import Error
from openapi_client.model.forecast_day import ForecastDay
from pprint import pprint
# Defining the host is optional and defaults to https://api.weatherbit.io/v2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.weatherbit.io/v2.0"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = 16_day___daily_forecast_api.16DayDailyForecastApi(api_client)
    lat = 3.14 # float | Latitude component of location.
    lon = 3.14 # float | Longitude component of location.
    key = "key_example" # str | Your registered API key.
    days = 3.14 # float | Number of days to return. Default 16. (optional)
    units = "S" # str | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a> (optional)
    lang = "ar" # str | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a> (optional)
    param_callback = "callback_example" # str | Wraps return in jsonp callback. Example: callback=func (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a daily forecast - Given Lat/Lon.
        api_response = api_instance.forecast_dailylatlatlonlon_get(lat, lon, key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling 16DayDailyForecastApi->forecast_dailylatlatlonlon_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a daily forecast - Given Lat/Lon.
        api_response = api_instance.forecast_dailylatlatlonlon_get(lat, lon, key, days=days, units=units, lang=lang, param_callback=param_callback)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling 16DayDailyForecastApi->forecast_dailylatlatlonlon_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lat** | **float**| Latitude component of location. |
 **lon** | **float**| Longitude component of location. |
 **key** | **str**| Your registered API key. |
 **days** | **float**| Number of days to return. Default 16. | [optional]
 **units** | **str**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional]
 **lang** | **str**| Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt; | [optional]
 **param_callback** | **str**| Wraps return in jsonp callback. Example: callback&#x3D;func | [optional]

### Return type

[**ForecastDay**](ForecastDay.md)

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

# **forecast_dailypostal_codepostal_code_get**
> ForecastDay forecast_dailypostal_codepostal_code_get(postal_code, key)

Returns a daily forecast - Given a Postal Code.

Returns a daily forecast, where each point represents one day (24hr) period. Every point has a datetime string in the format \"YYYY-MM-DD\". One day begins at 00:00 UTC, and ends at 23:59 UTC. 

### Example

```python
import time
import openapi_client
from openapi_client.api import 16_day___daily_forecast_api
from openapi_client.model.error import Error
from openapi_client.model.forecast_day import ForecastDay
from pprint import pprint
# Defining the host is optional and defaults to https://api.weatherbit.io/v2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.weatherbit.io/v2.0"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = 16_day___daily_forecast_api.16DayDailyForecastApi(api_client)
    postal_code = 1 # int | Postal Code. Example: 28546
    key = "key_example" # str | Your registered API key.
    country = "country_example" # str | Country Code (2 letter). (optional)
    days = 3.14 # float | Number of days to return. Default 16. (optional)
    units = "S" # str | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a> (optional)
    lang = "ar" # str | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a> (optional)
    param_callback = "callback_example" # str | Wraps return in jsonp callback. Example: callback=func (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a daily forecast - Given a Postal Code.
        api_response = api_instance.forecast_dailypostal_codepostal_code_get(postal_code, key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling 16DayDailyForecastApi->forecast_dailypostal_codepostal_code_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a daily forecast - Given a Postal Code.
        api_response = api_instance.forecast_dailypostal_codepostal_code_get(postal_code, key, country=country, days=days, units=units, lang=lang, param_callback=param_callback)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling 16DayDailyForecastApi->forecast_dailypostal_codepostal_code_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **postal_code** | **int**| Postal Code. Example: 28546 |
 **key** | **str**| Your registered API key. |
 **country** | **str**| Country Code (2 letter). | [optional]
 **days** | **float**| Number of days to return. Default 16. | [optional]
 **units** | **str**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional]
 **lang** | **str**| Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt; | [optional]
 **param_callback** | **str**| Wraps return in jsonp callback. Example: callback&#x3D;func | [optional]

### Return type

[**ForecastDay**](ForecastDay.md)

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

