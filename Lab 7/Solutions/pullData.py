from weatherbit.api import Api
#print(hourly[0]['datetime'].hour)


def load_data(city):
    api_key = '42258c381e9f429a873751bc6e83acb6'

    api = Api(api_key)
    api.set_granularity('hourly')
    forecast = api.get_forecast(city=city, days=3)
    hourly = forecast.get_series(['temp'])
    api.set_granularity('daily')
    daily = api.get_forecast(city=city, days=3)
    daily = daily.get_series(['max_temp', 'min_temp', 'weather'])
    place = forecast.city_name + ', ' + forecast.country_code

    return daily, hourly, place
