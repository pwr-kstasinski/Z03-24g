import time
import openapi_client
from pprint import pprint
from openapi_client.api import a_120_hour___hourly_forecast_api
from openapi_client.api import a_16_day___daily_forecast_api
from openapi_client.api import current_weather_data_api
from openapi_client.model.error import Error
from openapi_client.model.forecast_hourly import ForecastHourly

import tkinter as tk
import tkinter.font as font
# Defining the host is optional and defaults to https://api.weatherbit.io/v2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.weatherbit.io/v2.0"
)


"""
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = a_16_day___daily_forecast_api.A16DayDailyForecastApi(api_client)
    #api_instance = a_120_hour___hourly_forecast_api.A120HourHourlyForecastApi(api_client)
    city = "756135" # str | City search.. Example - &city=Raleigh,NC or &city=Berlin,DE or city=Paris&country=FR
    key = "30c4cec00f85498a928a09be2f62043e" # str | Your registered API key.
    state = "state_example" # str | Full name of state. (optional)
    country = "country_example" # str | Country Code (2 letter). (optional)
    units = "S" # str | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a> (optional)
    lang = "ar" # str | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a> (optional)
    param_callback = "callback_example" # str | Wraps return in jsonp callback. Example: callback=func (optional)
    hours = 1 # int | Number of hours to return. (optional)

    try:
        # Returns an 120 hour (hourly forecast) - Given City and/or State, Country.
        api_response = api_instance.forecast_daily_get(city_id=city, key=key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling A120HourHourlyForecastApi->forecast_hourly_get: %s\n" % e)
    except Exception as e:
        print(e)
"""

class Gui(tk.Frame):
    def __init__(self, master=tk.Tk()):
        super().__init__(master)
        master.title("WeatherApp")
        self.api_client=openapi_client.ApiClient(configuration)
        self.key="30c4cec00f85498a928a09be2f62043e"
        self.chkHour=False
        self.pack()
        self.createWidgets()
        
    def createWidgets(self):
        self.cityLabel=tk.Label(self,text="city:")
        self.cityLabel.grid(row=0,column=0)

        self.cityInput=tk.Entry(self)
        self.cityInput.insert(0,"756135")
        self.cityInput.grid(row=0,column=1)

        self.getWeather=tk.Button(self,text="getWeather",command=self.getDailyWeather)
        self.getWeather.grid(row=0,column=2)

        self.dailyWeather=tk.Frame(self)
        self.dailyWeather.grid(row=1)
        self.createDailyWeather()
        
        self.hourlyWeather=tk.Frame(self)
        self.hourlyWeather.grid(row=2)

        self.getDailyWeather()
        #self.createHourlyWeather()

    def createDailyWeather(self):
        self.dailyWeather.label=tk.Label(self.dailyWeather,text="Daily forecast:")
        self.dailyWeather.label.grid(row=0)
        self.dailyWeather.days=[]
        for i in range(5):
            self.dailyWeather.days.append({"date":"","temp":"","tempMin":"","clouds":"","humidity":""})
            self.dailyWeather.days[i]["date"]=tk.Button(self.dailyWeather,text="a",command=self.getHourlyWeather)
            self.dailyWeather.days[i]["date"].grid(row=1,column=i+1)
            self.dailyWeather.days[i]["temp"]=tk.Button(self.dailyWeather,text="s",command=self.getHourlyWeather)
            self.dailyWeather.days[i]["temp"]["font"]=font.Font(size=20)
            self.dailyWeather.days[i]["temp"].grid(row=2,column=i+1)
            self.dailyWeather.days[i]["tempMin"]=tk.Button(self.dailyWeather,text="d",command=self.getHourlyWeather)
            self.dailyWeather.days[i]["tempMin"].grid(row=3,column=i+1)
            self.dailyWeather.days[i]["clouds"]=tk.Button(self.dailyWeather,text="f",command=self.getHourlyWeather)
            self.dailyWeather.days[i]["clouds"].grid(row=4,column=i+1)
            self.dailyWeather.days[i]["humidity"]=tk.Button(self.dailyWeather,text="0",command=self.getHourlyWeather)
            self.dailyWeather.days[i]["humidity"].grid(row=5,column=i+1)
        

    def createHourlyWeather(self):
        self.chkHour=True
        self.hourlyWeather.label=tk.Label(self.hourlyWeather,text="Hourly weather:")
        self.hourlyWeather.label.grid(row=0)
        self.hourlyWeather.hours=[]
        for i in range(1):
           self.hourlyWeather.hours.append(tk.Canvas(self.hourlyWeather))
           self.hourlyWeather.hours[-1]["height"]=120
           self.hourlyWeather.hours[-1]["width"]=30
           self.hourlyWeather.hours[-1].create_rectangle(0, 0, 30, 10, fill="red")
           self.hourlyWeather.hours[-1].create_text(8,50,anchor=tk.SW,text="0",fill="black")
           self.hourlyWeather.hours[-1].grid(row=1,column=i+1)


    def setDailyWeather(self,apiResponse):
        i=0
        for day in self.dailyWeather.days:
            day["date"]["text"]=apiResponse.data[i]["datetime"]
            day["temp"]["text"]="{0}°".format(apiResponse.data[i]["temp"])
            day["tempMin"]["text"]="{0}°".format(apiResponse.data[i]["min_temp"])
            day["clouds"]["text"]="cloud: {0}%".format(apiResponse.data[i]["clouds"])
            #day["humidity"]["text"]=apiResponse.data[i]
            i+=1
        self.dailyWeather.update()
        
    def setHourlyWeather(self,apiResponse):
        if not self.chkHour:    self.createHourlyWeather()
        i=0
        for hour in self.hourlyWeather.hours:
            hour.create_rectangle(0, 0, 30, int(apiResponse.data[i]["temp"]*10), fill="red")
            hour.create_text(6,int(apiResponse.data[i]["temp"]*10),
                            anchor=tk.SW,text=apiResponse.data[i]["temp"],fill="black")
            i+=1
            hour.update()
        self.hourlyWeather.update()


    def getDailyWeather(self):
        api_instance = a_16_day___daily_forecast_api.A16DayDailyForecastApi(self.api_client)
        apiResponse = api_instance.forecast_daily_get(city_id=self.cityInput.get(), key=self.key)
        self.setDailyWeather(apiResponse)

    def getHourlyWeather(self):
        api_instance = current_weather_data_api.CurrentWeatherDataApi(self.api_client)
        apiResponse = api_instance.currentcity_idcity_id_get(city_id=self.cityInput.get(), key=self.key)
        self.setHourlyWeather(apiResponse)
    


Gui().mainloop()


