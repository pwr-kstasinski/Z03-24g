import eel
import datetime
from datetime import date
import weather as w



eel.init("web")

def get_weather_conditions_for_n_days( how_many_days,place):
    location_name = ""
    location_name=place
    location_coordinates = (52.2319581, 21.0067249) #Warsaw is default city

    if location_name != "":
        location_coordinates = w.get_city_coordinates(location_name)

        json_weather_data = w.get_json_data(location_coordinates, 'daily')
        conditions = w.get_weather_conditions_for_n_days(how_many_days, json_weather_data)
        return conditions
    else:
        return


@eel.expose
def display_weather_conditions_for_n_days(how_many_days, place):
    conds = get_weather_conditions_for_n_days(how_many_days,place)
    
    return conds



eel.start("main.html",size=(770,500))
