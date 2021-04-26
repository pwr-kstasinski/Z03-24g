"""
    OpenWeatherMap API

    Get current weather, daily forecast for 16 days, and 3-hourly forecast 5 days for your city. Helpful stats, graphics, and this day in history charts are available for your reference. Interactive maps show precipitation, clouds, pressure, wind around your location stations. Data is available in JSON, XML, or HTML format. **Note**: This sample Swagger file covers the `current` endpoint only from the OpenWeatherMap API. <br/><br/> **Note**: All parameters are optional, but you must select at least one parameter. Calling the API by city ID (using the `id` parameter) will provide the most precise location results.  # noqa: E501

    The version of the OpenAPI document: 2.5.2
    Contact: some_email@gmail.com
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "openapi-client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
]

setup(
    name=NAME,
    version=VERSION,
    description="OpenWeatherMap API",
    author="OpenWeatherMap API",
    author_email="some_email@gmail.com",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "OpenWeatherMap API"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="CC Attribution-ShareAlike 4.0 (CC BY-SA 4.0)",
    long_description="""\
    Get current weather, daily forecast for 16 days, and 3-hourly forecast 5 days for your city. Helpful stats, graphics, and this day in history charts are available for your reference. Interactive maps show precipitation, clouds, pressure, wind around your location stations. Data is available in JSON, XML, or HTML format. **Note**: This sample Swagger file covers the &#x60;current&#x60; endpoint only from the OpenWeatherMap API. &lt;br/&gt;&lt;br/&gt; **Note**: All parameters are optional, but you must select at least one parameter. Calling the API by city ID (using the &#x60;id&#x60; parameter) will provide the most precise location results.  # noqa: E501
    """
)
