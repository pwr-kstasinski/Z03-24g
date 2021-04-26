
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.current_weather_data_api import CurrentWeatherDataApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from openapi_client.api.current_weather_data_api import CurrentWeatherDataApi
from openapi_client.api.a_120_hour___hourly_forecast_api import A120HourHourlyForecastApi
from openapi_client.api.a_16_day___daily_forecast_api import A16DayDailyForecastApi
