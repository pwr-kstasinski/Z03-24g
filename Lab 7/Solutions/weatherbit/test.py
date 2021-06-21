import openapi_client
from pprint import pprint
from openapi_client.api import a16_day___daily_forecast_api
from openapi_client.api import a120_hour___hourly_forecast_api
from openapi_client.model.error import Error
from openapi_client.model.forecast_hourly import ForecastHourly



# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = a16_day___daily_forecast_api.a16DayDailyForecastApi()
    city_id = 4487042 # int | City ID. Example: 4487042
    key = "d4342a75711b4602af331e36b4d44595" # str | Your registered API key.pi
    try:
        # Returns a 120 hour (hourly) forecast - Given a City ID.
        api_response = api_instance.forecast_dailycity_idcity_id_get(city_id, key)
        #pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling 120HourHourlyForecastApi->forecast_hourlycity_idcity_id_get: %s\n" % e)
    api_instance = a120_hour___hourly_forecast_api.a120HourHourlyForecastApi()
    try:
        # Returns a 120 hour (hourly) forecast - Given a City ID.
        api_response = api_instance.forecast_hourlycity_idcity_id_get(city_id, key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling 120HourHourlyForecastApi->forecast_hourlycity_idcity_id_get: %s\n" % e)