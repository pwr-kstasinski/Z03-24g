# openapi_client.AirQualityForecastApi

All URIs are relative to *https://api.weatherbit.io/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**forecast_airqualitycity_idcity_id_get**](AirQualityForecastApi.md#forecast_airqualitycity_idcity_id_get) | **GET** /forecast/airquality?city_id&#x3D;{city_id} | Returns 72 hour (hourly) Air Quality forecast - Given a City ID.
[**forecast_airqualitycitycitycountrycountry_get**](AirQualityForecastApi.md#forecast_airqualitycitycitycountrycountry_get) | **GET** /forecast/airquality?city&#x3D;{city}&amp;country&#x3D;{country} | Returns 72 hour (hourly) Air Quality forecast - Given City and/or State, Country.
[**forecast_airqualitylatlatlonlon_get**](AirQualityForecastApi.md#forecast_airqualitylatlatlonlon_get) | **GET** /forecast/airquality?lat&#x3D;{lat}&amp;lon&#x3D;{lon} | Returns 72 hour (hourly) Air Quality forecast - Given a lat/lon.
[**forecast_airqualitypostal_codepostal_code_get**](AirQualityForecastApi.md#forecast_airqualitypostal_codepostal_code_get) | **GET** /forecast/airquality?postal_code&#x3D;{postal_code} | Returns 72 hour (hourly) Air Quality forecast - Given a Postal Code.


# **forecast_airqualitycity_idcity_id_get**
> AQHourly forecast_airqualitycity_idcity_id_get(city_id, key)

Returns 72 hour (hourly) Air Quality forecast - Given a City ID.

Returns 72 hour (hourly) Air Quality forecast, where each point represents a one hour period.

### Example

```python
import time
import openapi_client
from openapi_client.api import air_quality_forecast_api
from openapi_client.model.error import Error
from openapi_client.model.aq_hourly import AQHourly
from pprint import pprint
# Defining the host is optional and defaults to https://api.weatherbit.io/v2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.weatherbit.io/v2.0"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = air_quality_forecast_api.AirQualityForecastApi(api_client)
    city_id = 1 # int | City ID. Example: 4487042
    key = "key_example" # str | Your registered API key.
    param_callback = "callback_example" # str | Wraps return in jsonp callback. Example - callback=func (optional)
    hours = 1 # int | Number of hours to return. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns 72 hour (hourly) Air Quality forecast - Given a City ID.
        api_response = api_instance.forecast_airqualitycity_idcity_id_get(city_id, key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AirQualityForecastApi->forecast_airqualitycity_idcity_id_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns 72 hour (hourly) Air Quality forecast - Given a City ID.
        api_response = api_instance.forecast_airqualitycity_idcity_id_get(city_id, key, param_callback=param_callback, hours=hours)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AirQualityForecastApi->forecast_airqualitycity_idcity_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **city_id** | **int**| City ID. Example: 4487042 |
 **key** | **str**| Your registered API key. |
 **param_callback** | **str**| Wraps return in jsonp callback. Example - callback&#x3D;func | [optional]
 **hours** | **int**| Number of hours to return. | [optional]

### Return type

[**AQHourly**](AQHourly.md)

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

# **forecast_airqualitycitycitycountrycountry_get**
> AQHourly forecast_airqualitycitycitycountrycountry_get(city, country, key)

Returns 72 hour (hourly) Air Quality forecast - Given City and/or State, Country.

Returns 72 hour (hourly) Air Quality forecast, where each point represents a one hour period.

### Example

```python
import time
import openapi_client
from openapi_client.api import air_quality_forecast_api
from openapi_client.model.error import Error
from openapi_client.model.aq_hourly import AQHourly
from pprint import pprint
# Defining the host is optional and defaults to https://api.weatherbit.io/v2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.weatherbit.io/v2.0"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = air_quality_forecast_api.AirQualityForecastApi(api_client)
    city = "city_example" # str | City search.. Example - &city=Raleigh,NC or &city=Berlin,DE or city=Paris&country=FR
    country = "country_example" # str | Country Code (2 letter).
    key = "key_example" # str | Your registered API key.
    state = "state_example" # str | Full name of state. (optional)
    param_callback = "callback_example" # str | Wraps return in jsonp callback. Example: callback=func (optional)
    hours = 1 # int | Number of hours to return. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns 72 hour (hourly) Air Quality forecast - Given City and/or State, Country.
        api_response = api_instance.forecast_airqualitycitycitycountrycountry_get(city, country, key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AirQualityForecastApi->forecast_airqualitycitycitycountrycountry_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns 72 hour (hourly) Air Quality forecast - Given City and/or State, Country.
        api_response = api_instance.forecast_airqualitycitycitycountrycountry_get(city, country, key, state=state, param_callback=param_callback, hours=hours)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AirQualityForecastApi->forecast_airqualitycitycitycountrycountry_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **city** | **str**| City search.. Example - &amp;city&#x3D;Raleigh,NC or &amp;city&#x3D;Berlin,DE or city&#x3D;Paris&amp;country&#x3D;FR |
 **country** | **str**| Country Code (2 letter). |
 **key** | **str**| Your registered API key. |
 **state** | **str**| Full name of state. | [optional]
 **param_callback** | **str**| Wraps return in jsonp callback. Example: callback&#x3D;func | [optional]
 **hours** | **int**| Number of hours to return. | [optional]

### Return type

[**AQHourly**](AQHourly.md)

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

# **forecast_airqualitylatlatlonlon_get**
> AQHourly forecast_airqualitylatlatlonlon_get(lat, lon, key)

Returns 72 hour (hourly) Air Quality forecast - Given a lat/lon.

Returns 72 hour (hourly) Air Quality forecast, where each point represents a one hour period.

### Example

```python
import time
import openapi_client
from openapi_client.api import air_quality_forecast_api
from openapi_client.model.error import Error
from openapi_client.model.aq_hourly import AQHourly
from pprint import pprint
# Defining the host is optional and defaults to https://api.weatherbit.io/v2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.weatherbit.io/v2.0"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = air_quality_forecast_api.AirQualityForecastApi(api_client)
    lat = 3.14 # float | Latitude component of location.
    lon = 3.14 # float | Longitude component of location.
    key = "key_example" # str | Your registered API key.
    param_callback = "callback_example" # str | Wraps return in jsonp callback. Example - callback=func (optional)
    hours = 1 # int | Number of hours to return. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns 72 hour (hourly) Air Quality forecast - Given a lat/lon.
        api_response = api_instance.forecast_airqualitylatlatlonlon_get(lat, lon, key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AirQualityForecastApi->forecast_airqualitylatlatlonlon_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns 72 hour (hourly) Air Quality forecast - Given a lat/lon.
        api_response = api_instance.forecast_airqualitylatlatlonlon_get(lat, lon, key, param_callback=param_callback, hours=hours)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AirQualityForecastApi->forecast_airqualitylatlatlonlon_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lat** | **float**| Latitude component of location. |
 **lon** | **float**| Longitude component of location. |
 **key** | **str**| Your registered API key. |
 **param_callback** | **str**| Wraps return in jsonp callback. Example - callback&#x3D;func | [optional]
 **hours** | **int**| Number of hours to return. | [optional]

### Return type

[**AQHourly**](AQHourly.md)

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

# **forecast_airqualitypostal_codepostal_code_get**
> AQHourly forecast_airqualitypostal_codepostal_code_get(postal_code, key)

Returns 72 hour (hourly) Air Quality forecast - Given a Postal Code.

Returns 72 hour (hourly) Air Quality forecast, where each point represents a one hour period.

### Example

```python
import time
import openapi_client
from openapi_client.api import air_quality_forecast_api
from openapi_client.model.error import Error
from openapi_client.model.aq_hourly import AQHourly
from pprint import pprint
# Defining the host is optional and defaults to https://api.weatherbit.io/v2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.weatherbit.io/v2.0"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = air_quality_forecast_api.AirQualityForecastApi(api_client)
    postal_code = 1 # int | Postal Code. Example: 28546
    key = "key_example" # str | Your registered API key.
    country = "country_example" # str | Country Code (2 letter). (optional)
    param_callback = "callback_example" # str | Wraps return in jsonp callback. Example - callback=func (optional)
    hours = 1 # int | Number of hours to return. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns 72 hour (hourly) Air Quality forecast - Given a Postal Code.
        api_response = api_instance.forecast_airqualitypostal_codepostal_code_get(postal_code, key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AirQualityForecastApi->forecast_airqualitypostal_codepostal_code_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns 72 hour (hourly) Air Quality forecast - Given a Postal Code.
        api_response = api_instance.forecast_airqualitypostal_codepostal_code_get(postal_code, key, country=country, param_callback=param_callback, hours=hours)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AirQualityForecastApi->forecast_airqualitypostal_codepostal_code_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **postal_code** | **int**| Postal Code. Example: 28546 |
 **key** | **str**| Your registered API key. |
 **country** | **str**| Country Code (2 letter). | [optional]
 **param_callback** | **str**| Wraps return in jsonp callback. Example - callback&#x3D;func | [optional]
 **hours** | **int**| Number of hours to return. | [optional]

### Return type

[**AQHourly**](AQHourly.md)

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

