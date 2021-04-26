# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from openapi_client.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from openapi_client.model.clouds import Clouds
from openapi_client.model.coord import Coord
from openapi_client.model.main import Main
from openapi_client.model.model200 import Model200
from openapi_client.model.rain import Rain
from openapi_client.model.snow import Snow
from openapi_client.model.sys import Sys
from openapi_client.model.weather import Weather
from openapi_client.model.wind import Wind
