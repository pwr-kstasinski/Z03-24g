import time
import openapi_client
from pprint import pprint
from openapi_client.api import a_120_hour___hourly_forecast_api
from openapi_client.model.error import Error
from openapi_client.model.forecast_hourly import ForecastHourly
# Defining the host is optional and defaults to https://api.weatherbit.io/v2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.weatherbit.io/v2.0"
)



# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = a_120_hour___hourly_forecast_api.a120HourHourlyForecastApi(api_client)
    city = "city_example" # str | City search.. Example - &city=Raleigh,NC or &city=Berlin,DE or city=Paris&country=FR
    key = "key_example" # str | Your registered API key.
    state = "state_example" # str | Full name of state. (optional)
    country = "country_example" # str | Country Code (2 letter). (optional)
    units = "S" # str | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a> (optional)
    lang = "ar" # str | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a> (optional)
    param_callback = "callback_example" # str | Wraps return in jsonp callback. Example: callback=func (optional)
    hours = 1 # int | Number of hours to return. (optional)

    try:
        # Returns an 120 hour (hourly forecast) - Given City and/or State, Country.
        api_response = api_instance.forecast_hourly_get(city, key, state=state, country=country, units=units, lang=lang, param_callback=param_callback, hours=hours)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling 120HourHourlyForecastApi->forecast_hourly_get: %s\n" % e)
