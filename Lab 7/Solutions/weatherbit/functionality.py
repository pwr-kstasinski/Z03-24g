from pprint import pprint
import requests
from PIL import ImageTk, Image
from io import BytesIO
from openapi_client.api import a16_day___daily_forecast_api
from openapi_client.api import a120_hour___hourly_forecast_api

key = "d4342a75711b4602af331e36b4d44595"
#city_id = 4487042

def get_weather(city_id=4487042):
    api_instance = a16_day___daily_forecast_api.a16DayDailyForecastApi()
    try:
        # Returns a 120 hour (hourly) forecast - Given a City ID.
        api_response = api_instance.forecast_dailycity_idcity_id_get(city_id, key)
        #pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling 120HourHourlyForecastApi->forecast_hourlycity_idcity_id_get: %s\n" % e)
    return api_response

#print(get_weather()["city_name"])

def get_hourly_weather(city_id=4487042, start=0, count=8):
    api_instance = a120_hour___hourly_forecast_api.a120HourHourlyForecastApi()
    try:
        # Returns a 120 hour (hourly) forecast - Given a City ID.
        api_response = api_instance.forecast_hourlycity_idcity_id_get(city_id, key)
        #pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling 120HourHourlyForecastApi->forecast_hourlycity_idcity_id_get: %s\n" % e)
    return api_response


def get_img(imgName, size):
    imgAddres = f'https://www.weatherbit.io/static/img/icons/{imgName}.png'
    response = requests.get(imgAddres)
    imgData = response.content
    img = Image.open(BytesIO(imgData)).resize((size, size))
    #img.show()
    return img