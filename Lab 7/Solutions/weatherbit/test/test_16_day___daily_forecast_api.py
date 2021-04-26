"""
    Weatherbit.io - Swagger UI Weather API documentation

    This is the documentation for the Weatherbit Weather API.  The base URL for the API is [http://api.weatherbit.io/v2.0/](http://api.weatherbit.io/v2.0/) or [https://api.weatherbit.io/v2.0/](http://api.weatherbit.io/v2.0/). Below is the Swagger UI documentation for the API. All API requests require the `key` parameter.        An Example for a 5 day forecast for London, UK would be `http://api.weatherbit.io/v2.0/forecast/3hourly?city=London`&`country=UK`. See our [Weather API description page](https://www.weatherbit.io/api) for additional documentation.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.a16_day___daily_forecast_api import a16DayDailyForecastApi  # noqa: E501


class Test16DayDailyForecastApi(unittest.TestCase):
    """16DayDailyForecastApi unit test stubs"""

    def setUp(self):
        self.api = a16DayDailyForecastApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_forecast_dailycity_idcity_id_get(self):
        """Test case for forecast_dailycity_idcity_id_get

        Returns a daily forecast - Given a City ID.  # noqa: E501
        """
        pass

    def test_forecast_dailycitycitycountrycountry_get(self):
        """Test case for forecast_dailycitycitycountrycountry_get

        Returns a daily forecast - Given City and/or State, Country.  # noqa: E501
        """
        pass

    def test_forecast_dailylatlatlonlon_get(self):
        """Test case for forecast_dailylatlatlonlon_get

        Returns a daily forecast - Given Lat/Lon.  # noqa: E501
        """
        pass

    def test_forecast_dailypostal_codepostal_code_get(self):
        """Test case for forecast_dailypostal_codepostal_code_get

        Returns a daily forecast - Given a Postal Code.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
