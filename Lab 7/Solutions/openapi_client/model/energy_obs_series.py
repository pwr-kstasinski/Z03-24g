"""
    Weatherbit.io - Swagger UI Weather API documentation

    This is the documentation for the Weatherbit Weather API.  The base URL for the API is [http://api.weatherbit.io/v2.0/](http://api.weatherbit.io/v2.0/) or [https://api.weatherbit.io/v2.0/](http://api.weatherbit.io/v2.0/). Below is the Swagger UI documentation for the API. All API requests require the `key` parameter.        An Example for a 5 day forecast for London, UK would be `http://api.weatherbit.io/v2.0/forecast/3hourly?city=London`&`country=UK`. See our [Weather API description page](https://www.weatherbit.io/api) for additional documentation.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)


class EnergyObsSeries(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'date': (str,),  # noqa: E501
            'cdd': (float,),  # noqa: E501
            'hdd': (float,),  # noqa: E501
            'rh': (int,),  # noqa: E501
            'dewpt': (float,),  # noqa: E501
            'wind_dir': (int,),  # noqa: E501
            'wind_speed': (float,),  # noqa: E501
            'temp': (float,),  # noqa: E501
            'clouds': (int,),  # noqa: E501
            't_ghi': (float,),  # noqa: E501
            't_dhi': (float,),  # noqa: E501
            't_dni': (float,),  # noqa: E501
            'sun_hours': (float,),  # noqa: E501
            'precip': (float,),  # noqa: E501
            'snow': (float,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'date': 'date',  # noqa: E501
        'cdd': 'cdd',  # noqa: E501
        'hdd': 'hdd',  # noqa: E501
        'rh': 'rh',  # noqa: E501
        'dewpt': 'dewpt',  # noqa: E501
        'wind_dir': 'wind_dir',  # noqa: E501
        'wind_speed': 'wind_speed',  # noqa: E501
        'temp': 'temp',  # noqa: E501
        'clouds': 'clouds',  # noqa: E501
        't_ghi': 't_ghi',  # noqa: E501
        't_dhi': 't_dhi',  # noqa: E501
        't_dni': 't_dni',  # noqa: E501
        'sun_hours': 'sun_hours',  # noqa: E501
        'precip': 'precip',  # noqa: E501
        'snow': 'snow',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """EnergyObsSeries - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            date (str): Date. [optional]  # noqa: E501
            cdd (float): Cooling degree days. [optional]  # noqa: E501
            hdd (float): Heating degree days. [optional]  # noqa: E501
            rh (int): Average Relative humidity (%). [optional]  # noqa: E501
            dewpt (float): Average dew point temperature - Default (C). [optional]  # noqa: E501
            wind_dir (int): Average wind direction (Degrees). [optional]  # noqa: E501
            wind_speed (float): Average wind speed - Default (m/s). [optional]  # noqa: E501
            temp (float): Average temperature - Default (C). [optional]  # noqa: E501
            clouds (int): Average cloud cover (%). [optional]  # noqa: E501
            t_ghi (float): Total global horizontal solar irradiance (W/m^2). [optional]  # noqa: E501
            t_dhi (float): Total diffuse horizontal solar irradiance (W/m^2). [optional]  # noqa: E501
            t_dni (float): Total direct normal solar irradiance (W/m^2). [optional]  # noqa: E501
            sun_hours (float): Average number of daily sun hours - # hours where Solar GHI > 1000 W/m^2. [optional]  # noqa: E501
            precip (float): Total precipitation in period - Default (mm). [optional]  # noqa: E501
            snow (float): Total snowfall in period - Default (mm). [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
