"""
    Weatherbit.io - Swagger UI Weather API documentation

    This is the documentation for the Weatherbit Weather API.  The base URL for the API is [http://api.weatherbit.io/v2.0/](http://api.weatherbit.io/v2.0/) or [https://api.weatherbit.io/v2.0/](http://api.weatherbit.io/v2.0/). Below is the Swagger UI documentation for the API. All API requests require the `key` parameter.        An Example for a 5 day forecast for London, UK would be `http://api.weatherbit.io/v2.0/forecast/3hourly?city=London`&`country=UK`. See our [Weather API description page](https://www.weatherbit.io/api) for additional documentation.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.geo_ip_obj import GeoIPObj


class TestGeoIPObj(unittest.TestCase):
    """GeoIPObj unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGeoIPObj(self):
        """Test GeoIPObj"""
        # FIXME: construct object with mandatory attributes with example values
        # model = GeoIPObj()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
