"""
    OpenWeatherMap API

    Get current weather, daily forecast for 16 days, and 3-hourly forecast 5 days for your city. Helpful stats, graphics, and this day in history charts are available for your reference. Interactive maps show precipitation, clouds, pressure, wind around your location stations. Data is available in JSON, XML, or HTML format. **Note**: This sample Swagger file covers the `current` endpoint only from the OpenWeatherMap API. <br/><br/> **Note**: All parameters are optional, but you must select at least one parameter. Calling the API by city ID (using the `id` parameter) will provide the most precise location results.  # noqa: E501

    The version of the OpenAPI document: 2.5.2
    Contact: some_email@gmail.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.clouds import Clouds
from openapi_client.model.coord import Coord
from openapi_client.model.main import Main
from openapi_client.model.rain import Rain
from openapi_client.model.snow import Snow
from openapi_client.model.sys import Sys
from openapi_client.model.weather import Weather
from openapi_client.model.wind import Wind
globals()['Clouds'] = Clouds
globals()['Coord'] = Coord
globals()['Main'] = Main
globals()['Rain'] = Rain
globals()['Snow'] = Snow
globals()['Sys'] = Sys
globals()['Weather'] = Weather
globals()['Wind'] = Wind
from openapi_client.model.model200 import Model200


class TestModel200(unittest.TestCase):
    """Model200 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testModel200(self):
        """Test Model200"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Model200()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
