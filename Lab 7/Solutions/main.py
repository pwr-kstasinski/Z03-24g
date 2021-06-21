import requests
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
from datetime import datetime
from PIL import ImageTk, Image
from io import BytesIO


def get_weather(city='slesin', index=0):
    key = 'dfc2cb2adfed32b31e8e6c4217b27a0c'
    try:
        weather_json = requests.get(
            f'http://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={key}').json()
        #print(weather_json)
    except:
        return

    weatherDict = {
        "weather_state_name": weather_json['list'][index]['weather'][0]['main'],
        "weather_state_abbr": weather_json['list'][index]['weather'][0]['icon'],
        "wind_direction_compass": weather_json['list'][index]['wind']['deg'],
        "wind_speed": weather_json['list'][index]['wind']['speed'],
        "the_temp": weather_json['list'][index]['main']['temp'],
        "min_temp": weather_json['list'][index]['main']['temp_min'],
        "max_temp": weather_json['list'][index]['main']['temp_max'],
        "feels_temp": weather_json['list'][index]['main']['feels_like'],
        "air_pressure": weather_json['list'][index]['main']['pressure'],
        "humidity": weather_json['list'][index]['main']['humidity'],
        "visibility": weather_json['list'][index]['visibility'] / 1000,
        "country": weather_json['city']['country'],
        "city": weather_json['city']['name'],
        "time": datetime.fromtimestamp(weather_json['list'][index]['dt'] - 3600).strftime('%H:%M:%S'),
        "sun_rise": datetime.fromtimestamp(
            weather_json['city']['sunrise'] + weather_json['city']['timezone'] - 3600).strftime('%H:%M:%S'),
        "sun_set": datetime.fromtimestamp(
            weather_json['city']['sunset'] + weather_json['city']['timezone'] - 3600).strftime('%H:%M:%S'),
        "date": datetime.fromtimestamp(weather_json['list'][index]['dt'] - 3600).strftime('%d-%m-%Y'),
    }

    return weatherDict


def get_hourly_weather(city='slesin', start=0, count=8):
    key = 'dfc2cb2adfed32b31e8e6c4217b27a0c'
    try:
        weather_json = requests.get(
            f'http://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={key}').json()
    except:
        return

    weatherData = []

    for i in range(count):
        weatherData.append({
            "hour": datetime.fromtimestamp(
                weather_json['list'][i + start]['dt'] + weather_json['city']['timezone'] - 3600).strftime('%H:%M'),
            "temp": weather_json['list'][i + start]['main']['temp'],
            "gen": weather_json['list'][i + start]['weather'][0]['main'],
            "icon": weather_json['list'][i + start]['weather'][0]['icon']
        })

    return weatherData


def get_img(img_symbol, size):
    imgAddres = f'http://openweathermap.org/img/wn/{img_symbol}@2x.png'
    response = requests.get(imgAddres)
    imgData = response.content
    img = ImageTk.PhotoImage(Image.open(BytesIO(imgData)).resize((size, size), Image.ANTIALIAS))
    return img, imgData


def get_temp_color(temperature):
    if temperature > 30:
        return "#e74c3c"
    elif temperature > 20:
        return "#f39c12 "
    elif temperature > 15:
        return "#f1c40f"
    elif temperature > 10:
        return "#58d68d"
    elif temperature > 5:
        return "#5dade2"
    elif temperature > 0:
        return "#aed6f1"
    elif temperature > -5:
        return "#a9cce3"
    elif temperature > -10:
        return "WHITE"
    elif temperature > -15:
        return "#e5e8e8"
    else:
        return "#d5d8dc"


class WeatherApp:
    def __init__(self, city='Slesin'):
        self.window = tk.Tk()
        self.master = tk.Frame(self.window, bg='#abebc6')
        self.window.resizable(False, False)
        self.curr_weather = None

        self.mainColor = '#abebc6'


        #----------------------------------TEMPERATURE FRAME------------------------------------------------------------

        self.label_frame_temp = tk.LabelFrame(self.master, text='Temperature', bg=self.mainColor)
        self.label_frame_temp.columnconfigure(0, weight=1)
        self.label_frame_temp.columnconfigure(1, weight=1)

        self.the_temp_label = tk.Label(self.label_frame_temp, anchor=tk.E, text='Now: ', width=12, bg=self.mainColor)
        self.the_temp_label.grid(column=0, row=0)
        self.the_temp = tk.Label(self.label_frame_temp, width=12, anchor=tk.W, bg=self.mainColor)
        self.the_temp.grid(column=1, row=0)

        self.min_temp_label = tk.Label(self.label_frame_temp, anchor=tk.E, text='Lowest today: ', width=12,
                                       bg=self.mainColor)
        self.min_temp_label.grid(column=0, row=1)
        self.min_temp = tk.Label(self.label_frame_temp, width=12, anchor=tk.W, bg=self.mainColor)
        self.min_temp.grid(column=1, row=1)

        self.max_temp_label = tk.Label(self.label_frame_temp, anchor=tk.E, text='Highest today: ', width=12,
                                       bg=self.mainColor)
        self.max_temp_label.grid(column=0, row=2)
        self.max_temp = tk.Label(self.label_frame_temp, width=12, anchor=tk.W, bg=self.mainColor)
        self.max_temp.grid(column=1, row=2)

        #-------------------------------CONDITIONS FRAME----------------------------------------------------------------

        self.label_frame_conditions = tk.LabelFrame(self.master, text='Conditions', bg=self.mainColor)
        self.label_frame_conditions.columnconfigure(0, weight=1)
        self.label_frame_conditions.columnconfigure(1, weight=1)

        self.air_pressure_label = tk.Label(self.label_frame_conditions, anchor=tk.E, text='Air pressure: ', width=12,
                                           bg=self.mainColor)
        self.air_pressure_label.grid(column=0, row=0)
        self.air_pressure = tk.Label(self.label_frame_conditions, width=12, anchor=tk.W, bg=self.mainColor)
        self.air_pressure.grid(column=1, row=0)

        self.visibility_label = tk.Label(self.label_frame_conditions, anchor=tk.E, text='Visibility: ', width=12,
                                         bg=self.mainColor)
        self.visibility_label.grid(column=0, row=1)
        self.visibility = tk.Label(self.label_frame_conditions, width=12, anchor=tk.W, bg=self.mainColor)
        self.visibility.grid(column=1, row=1)

        self.humidity_label = tk.Label(self.label_frame_conditions, anchor=tk.E, text='Humidity: ', width=12,
                                       bg=self.mainColor)
        self.humidity_label.grid(column=0, row=4, rowspan=2)
        self.humidity = tk.Scale(self.label_frame_conditions, orient=tk.VERTICAL, from_=100, to=0,
                                 troughcolor='LIGHTBLUE', sliderlength=5, length=50, bg='#abebc6')
        self.humidity.grid(column=1, row=4, rowspan=2, sticky=tk.W)

        #----------------------------------WIND FRAME-------------------------------------------------------------------

        self.label_frame_wind = tk.LabelFrame(self.master, text='Wind', bg=self.mainColor)
        self.label_frame_wind.columnconfigure(0, weight=1)
        self.label_frame_wind.columnconfigure(1, weight=1)

        self.wind_direction_compass_label = tk.Label(self.label_frame_wind, anchor=tk.E, text='Direction: ', width=12,
                                                     bg=self.mainColor)
        self.wind_direction_compass_label.grid(column=0, row=0)
        self.wind_direction_compass = tk.Label(self.label_frame_wind, width=12, anchor=tk.W, bg=self.mainColor)
        self.wind_direction_compass.grid(column=1, row=0)

        self.wind_speed_label = tk.Label(self.label_frame_wind, anchor=tk.E, text='Speed: ', width=12, bg=self.mainColor)
        self.wind_speed_label.grid(column=0, row=1)
        self.wind_speed = tk.Label(self.label_frame_wind, width=12, anchor=tk.W, bg=self.mainColor)
        self.wind_speed.grid(column=1, row=1)

        #---------------------------LOCALIZATION FRAME------------------------------------------------------------------

        self.label_frame_localization = tk.LabelFrame(self.master, text='Localization', bg=self.mainColor)
        self.label_frame_localization.columnconfigure(0, weight=1)
        self.label_frame_localization.columnconfigure(1, weight=1)

        self.country_label = tk.Label(self.label_frame_localization, anchor=tk.E, text='Country: ', width=12,
                                      bg=self.mainColor)
        self.country_label.grid(column=0, row=0)
        self.country = tk.Label(self.label_frame_localization, width=12, anchor=tk.W, bg=self.mainColor)
        self.country.grid(column=1, row=0)

        self.city_label = tk.Label(self.label_frame_localization, anchor=tk.E, text='City: ', width=12,
                                   bg=self.mainColor)
        self.city_label.grid(column=0, row=1)
        self.city = tk.Label(self.label_frame_localization, width=12, anchor=tk.W, bg=self.mainColor)
        self.city.grid(column=1, row=1)

        self.time_label = tk.Label(self.label_frame_localization, anchor=tk.E, text='Data time: ', width=12,
                                   bg=self.mainColor)
        self.time_label.grid(column=0, row=2)
        self.time = tk.Label(self.label_frame_localization, width=12, anchor=tk.W, bg=self.mainColor)
        self.time.grid(column=1, row=2)

        #-------------------------------------SUN FRAME-----------------------------------------------------------------

        self.label_frame_sun = tk.LabelFrame(self.master, text='Sun today', bg=self.mainColor)
        self.label_frame_sun.columnconfigure(0, weight=1)
        self.label_frame_sun.columnconfigure(1, weight=1)

        self.sun_rise_label = tk.Label(self.label_frame_sun, anchor=tk.E, text='Sun rise: ', width=12, bg=self.mainColor)
        self.sun_rise_label.grid(column=0, row=0)
        self.sun_rise = tk.Label(self.label_frame_sun, width=12, bg=self.mainColor)
        self.sun_rise.grid(column=1, row=0)

        self.sun_set_label = tk.Label(self.label_frame_sun, anchor=tk.E, text='Sun set: ', width=12, bg=self.mainColor)
        self.sun_set_label.grid(column=0, row=1)
        self.sun_set = tk.Label(self.label_frame_sun, width=12, bg=self.mainColor)
        self.sun_set.grid(column=1, row=1)

        #------------------------------------OVERALL FRAME--------------------------------------------------------------

        self.label_frame_overall = tk.LabelFrame(self.master, text='Weather', bg=self.mainColor)
        self.label_frame_overall.columnconfigure(0, weight=1)
        self.label_frame_overall.columnconfigure(1, weight=1)

        self.date = tk.Label(self.label_frame_overall, width=24, font=tkFont.Font(weight='bold'), bg=self.mainColor)
        self.date.grid(column=0, row=0)

        self.weather_state_name = tk.Label(self.label_frame_overall, width=24, font=tkFont.Font(weight='bold'),
                                           bg=self.mainColor)
        self.weather_state_name.grid(column=0, row=1)

        self.image = tk.Label(self.label_frame_overall, width=240, bg=self.mainColor)
        self.image.grid(column=0, row=2)

        self.temp_main = tk.Label(self.label_frame_overall, width=24, font=tkFont.Font(weight='bold'),
                                  bg=self.mainColor)
        self.temp_main.grid(column=0, row=3)

        #----------------------------------------ENTRY FRAME------------------------------------------------------------

        self.frame_entry = tk.Frame(self.master, bg=self.mainColor)
        self.frame_entry.columnconfigure(0, weight=1)
        self.frame_entry.columnconfigure(1, weight=1)

        self.info_text = tk.Label(self.frame_entry,
                                  text='Data from \nhttps://www.openweathermapmetaweather.org/',
                                  bg=self.mainColor)
        self.info_text.grid(column=1, row=0, columnspan=1, rowspan=2)

        self.city_entry_label = tk.Label(self.frame_entry, anchor=tk.E, text='City: ', bg=self.mainColor)
        self.city_entry_label.grid(column=4, row=0)
        self.city_entry = tk.Entry(self.frame_entry)
        self.city_entry.insert(0, city)
        self.city_entry.grid(column=5, row=0)

        self.search_button = tk.Button(self.frame_entry,
                                       command=lambda: self.update_interface(self.city_entry.get()),
                                       text="Search", width=24, bg='SILVER')
        self.search_button.grid(column=4, row=1, columnspan=2)

        #-----------------------------------MAIN GRID PLACEMENT---------------------------------------------------------

        self.label_frame_temp.grid(row=0, column=0, rowspan=4, sticky=tk.NW)
        self.label_frame_conditions.grid(row=4, column=0, rowspan=6, sticky=tk.SW)

        self.label_frame_overall.grid(row=0, column=1, rowspan=10, sticky=tk.NSEW)

        self.label_frame_wind.grid(row=0, column=2, rowspan=3, sticky=tk.NE)
        self.label_frame_sun.grid(row=3, column=2, rowspan=3, sticky=tk.E)
        self.label_frame_localization.grid(row=6, column=2, rowspan=4, sticky=tk.SE)

        self.frame_entry.grid(row=10, column=0, columnspan=3, sticky=tk.NSEW)

        #-------------------------------------DAY SELECT -------------------------------------------------------

        self.frame_date_selector = tk.Frame(self.window)
        self.today_button = tk.Button(self.frame_date_selector, text='Today',
                                      command=lambda: self.update_interface(self.curr_weather['city']),
                                      width=25, bg='#f5b7b1')
        self.tomorrow_button = tk.Button(self.frame_date_selector, text='Tomorrow',
                                         command=lambda: self.update_interface(self.curr_weather['city'], 8),
                                         width=45, bg='#f5b7b1')
        self.atomorrow_button = tk.Button(self.frame_date_selector, text='After Tomorrow',
                                          command=lambda: self.update_interface(self.curr_weather['city'], 16),
                                          width=25, bg='#f5b7b1')
        self.today_button.grid(column=0, row=0, sticky=tk.W)
        self.tomorrow_button.grid(column=1, row=0)
        self.atomorrow_button.grid(column=2, row=0, sticky=tk.E)

        self.frame_date_selector.grid(column=0, row=0, columnspan=3, sticky=tk.EW)

        #-------------------------------------HOURLY PARTITION-----------------------------------------------------------

        self.hours = tk.Frame(self.window)
        hour1 = self.HourFrame(self.hours)
        hour1.grid(column=0, row=0)
        hour2 = self.HourFrame(self.hours)
        hour2.grid(column=1, row=0)
        hour3 = self.HourFrame(self.hours)
        hour3.grid(column=2, row=0)
        hour4 = self.HourFrame(self.hours)
        hour4.grid(column=3, row=0)
        hour5 = self.HourFrame(self.hours)
        hour5.grid(column=4, row=0)
        hour6 = self.HourFrame(self.hours)
        hour6.grid(column=5, row=0)
        hour7 = self.HourFrame(self.hours)
        hour7.grid(column=6, row=0)
        hour8 = self.HourFrame(self.hours)
        hour8.grid(column=7, row=0)

        self.hours_widget = [hour1, hour2, hour3, hour4, hour5, hour6, hour7, hour8]

        self.hours.grid(column=0, row=1, columnspan=3)
        self.master.grid(column=0, row=2, columnspan=3)

        self.update_interface(city)

    class HourFrame(tk.LabelFrame):
        def __init__(self, parent, primary_color='#abebc6'):
            super().__init__(parent, bg=primary_color)

            self.configure(text='hh:mm')
            self.gen_label = tk.Label(self, width=11, text='Weather', bg=primary_color)
            self.temp_label = tk.Label(self, width=11, text='-273', bg=primary_color)
            self.image_label = tk.Label(self, width=50, text='image', bg=primary_color)
            self.temp_scale = tk.Scale(self, width=74, length=40, bg='LEMONCHIFFON', sliderlength=5, showvalue=0, bd=0)

            self.gen_label.grid(column=0, row=0)
            self.image_label.grid(column=0, row=1)
            self.temp_label.grid(column=0, row=2)
            self.temp_scale.grid(column=0, row=3)

        def update_hour(self, weather_stats, min_temp, max_temp):
            self.configure(text=weather_stats['hour'])
            self.temp_label.configure(text=f"{weather_stats['temp']} °C")
            self.gen_label.configure(text=weather_stats['gen'])
            self.temp_scale.configure(state=tk.NORMAL)
            self.temp_scale.configure(to=min_temp, from_=max_temp, troughcolor=get_temp_color(weather_stats['temp']))
            self.temp_scale.set(weather_stats['temp'])
            self.temp_scale.configure(state=tk.DISABLED)

            self.img, self.img_data = get_img(weather_stats['icon'], 50)
            self.image_label.configure(image=self.img)

    def update_weather(self, city, index=0):
        temp_weather = self.curr_weather
        try:
            self.curr_weather = get_weather(city, index)
            self.hours = get_hourly_weather(city, index)
        except:
            self.curr_weather = temp_weather
            tk.messagebox.showwarning('Incorrect city', 'Type correct city!')

    def update_interface(self, city, index=0):
        self.update_weather(city, index)
        self.window.title(f'Weather - {self.curr_weather["city"]}')
        self.weather_state_name.configure(text=self.curr_weather['weather_state_name'])
        self.wind_direction_compass.configure(text=self.curr_weather['wind_direction_compass'])
        self.wind_speed.configure(text=f'{self.curr_weather["wind_speed"]} km/h')
        self.temp_main.configure(text=f'Feels like {self.curr_weather["feels_temp"]} °C')
        self.the_temp.configure(text=f'{self.curr_weather["the_temp"]} °C')
        self.min_temp.configure(text=f'{self.curr_weather["min_temp"]} °C')
        self.max_temp.configure(text=f'{self.curr_weather["max_temp"]} °C')
        self.air_pressure.configure(text=f'{self.curr_weather["air_pressure"]} hPa')
        self.visibility.configure(text=f'{self.curr_weather["visibility"]} km')
        self.country.configure(text=self.curr_weather['country'])
        self.city.configure(text=self.curr_weather['city'])
        self.time.configure(text=self.curr_weather['time'])
        self.sun_rise.configure(text=self.curr_weather['sun_rise'])
        self.sun_set.configure(text=self.curr_weather['sun_set'])
        self.humidity.set(self.curr_weather['humidity'])
        self.humidity.configure(state=tk.DISABLED)
        self.date.configure(text=self.curr_weather['date'])

        min_temp = self.hours[0]['temp']
        max_temp = self.hours[0]['temp']

        for i in range(len(self.hours_widget)):
            if self.hours[i]['temp'] > max_temp:
                max_temp = self.hours[i]['temp']
            elif self.hours[i]['temp'] < min_temp:
                min_temp = self.hours[i]['temp']

        min_temp = min_temp - 2
        max_temp = max_temp + 2

        for i in range(len(self.hours_widget)):
            self.hours_widget[i].update_hour(self.hours[i], min_temp, max_temp)

        self.img, self.img_data = get_img(self.curr_weather['weather_state_abbr'], 100)
        self.image.configure(image=self.img)


if __name__ == '__main__':
    top = WeatherApp()
    tk.mainloop()
