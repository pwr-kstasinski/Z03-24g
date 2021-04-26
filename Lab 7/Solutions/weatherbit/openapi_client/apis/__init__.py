
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.120_hour___hourly_forecast_api import 120HourHourlyForecastApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from openapi_client.api.120_hour___hourly_forecast_api import 120HourHourlyForecastApi
from openapi_client.api.16_day___daily_forecast_api import 16DayDailyForecastApi
from openapi_client.api.5_day___3_hour_forecast_api import 5Day3HourForecastApi
from openapi_client.api.air_quality_forecast_api import AirQualityForecastApi
from openapi_client.api.alerts_api import AlertsApi
from openapi_client.api.bulk_downloads_api import BulkDownloadsApi
from openapi_client.api.current_air_quality_api import CurrentAirQualityApi
from openapi_client.api.current_weather_data_api import CurrentWeatherDataApi
from openapi_client.api.daily_historical_weather_data_api import DailyHistoricalWeatherDataApi
from openapi_client.api.forecast_degree_day_api_api import ForecastDegreeDayAPIApi
from openapi_client.api.forecast_solar_irradiance_api_api import ForecastSolarIrradianceAPIApi
from openapi_client.api.historical_air_quality_api import HistoricalAirQualityApi
from openapi_client.api.historical_degree_day_api_api import HistoricalDegreeDayAPIApi
from openapi_client.api.historical_solar_irradiance_api_api import HistoricalSolarIrradianceAPIApi
from openapi_client.api.historical_weather_energy_api_api import HistoricalWeatherEnergyAPIApi
from openapi_client.api.hourly_historical_weather_data_api import HourlyHistoricalWeatherDataApi
