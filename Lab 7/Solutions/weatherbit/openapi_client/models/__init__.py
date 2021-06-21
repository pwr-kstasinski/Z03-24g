# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from openapi_client.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from openapi_client.model.aq_current import AQCurrent
from openapi_client.model.aq_current_group import AQCurrentGroup
from openapi_client.model.aq_hour import AQHour
from openapi_client.model.aq_hourly import AQHourly
from openapi_client.model.current_obs import CurrentObs
from openapi_client.model.current_obs_group import CurrentObsGroup
from openapi_client.model.current_obs_weather import CurrentObsWeather
from openapi_client.model.energy_obs import EnergyObs
from openapi_client.model.energy_obs_group import EnergyObsGroup
from openapi_client.model.energy_obs_group_forecast import EnergyObsGroupForecast
from openapi_client.model.energy_obs_series import EnergyObsSeries
from openapi_client.model.error import Error
from openapi_client.model.forecast import Forecast
from openapi_client.model.forecast_day import ForecastDay
from openapi_client.model.forecast_hour import ForecastHour
from openapi_client.model.forecast_hour_weather import ForecastHourWeather
from openapi_client.model.forecast_hourly import ForecastHourly
from openapi_client.model.forecast_weather import ForecastWeather
from openapi_client.model.geo_ip_obj import GeoIPObj
from openapi_client.model.history import History
from openapi_client.model.history_day import HistoryDay
from openapi_client.model.history_day_obj import HistoryDayObj
from openapi_client.model.history_obj import HistoryObj
from openapi_client.model.history_obj_weather import HistoryObjWeather
from openapi_client.model.weather_alert import WeatherAlert
from openapi_client.model.weather_alert_group import WeatherAlertGroup
