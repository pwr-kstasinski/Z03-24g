# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from openapi_client.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from openapi_client.model.error import Error
from openapi_client.model.forecast import Forecast
from openapi_client.model.forecast_day import ForecastDay
from openapi_client.model.forecast_hour import ForecastHour
from openapi_client.model.forecast_hour_weather import ForecastHourWeather
from openapi_client.model.forecast_hourly import ForecastHourly
from openapi_client.model.forecast_weather import ForecastWeather
