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
from openapi_client.model.sys import Sys


class TestSys(unittest.TestCase):
    """Sys unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSys(self):
        """Test Sys"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Sys()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
