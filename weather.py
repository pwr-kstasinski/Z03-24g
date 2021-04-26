import requests
import json
import tkinter as tk
from tkinter import Label, Entry, Button, PhotoImage, Frame
from PIL import ImageTk, Image
import pandas as pd
import matplotlib.pyplot as plt
import datetime

import os
api_key = '0a40e425199f402a947df243e3759420'

r = requests.get('https://api.weatherbit.io/v2.0/current?lat=38.123&lon=-78.543&key='+api_key)

today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
ttomorrow = tomorrow + datetime.timedelta(days=1)



def search():
    city = city_text.get()
    
    r = requests.get('https://api.weatherbit.io/v2.0//forecast/daily?city='+city+'&key='+api_key)
    
    d = json.loads(r.text)
      
    if d:       
        temperature_label['text'] = str(d['data'][0]['max_temp'])+"   °C"
        temperature_label_t['text'] = str(d['data'][1]['max_temp'])+"   °C"
        temperature_label_tt['text'] = str(d['data'][2]['max_temp'])+"   °C"

        temperature_label_min['text'] = str(d['data'][0]['min_temp'])+"   °C"
        temperature_label_t_min['text'] = str(d['data'][1]['min_temp'])+"   °C"
        temperature_label_tt_min['text'] = str(d['data'][2]['min_temp'])+"   °C"

        temperature_label_pop['text'] = str(d['data'][0]['pop'])+"   %"
        temperature_label_t_pop['text'] = str(d['data'][1]['pop'])+"   %"
        temperature_label_tt_pop['text'] = str(d['data'][2]['pop'])+"   %"

    else:
        print("GRUST")


def grafik(day):
    city = city_text.get()
    
    r = requests.get('https://api.weatherbit.io/v2.0/forecast/hourly?city='+city+'&key='+api_key+ '&hours=48')
    
    d = json.loads(r.text)

    temp_h = []
    hour = []
    current_hour = list(d['data'][0]['timestamp_local'])
    number = int(''.join(map(str, current_hour[11:13])))
    if day == "1":
        for i in range(25-number):
            temp_h.append(d['data'][i]['temp'])
            hour.append(i+number)
    elif day == "2":
        for i in range(24-number, 48-number):
            temp_h.append(d['data'][i]['temp'])
            hour.append(i-24+number)
    else :
         for i in range(48-number, 48):
            temp_h.append(d['data'][i]['temp'])
            hour.append(i-48 +number)
    df = pd.DataFrame({'hour_number':hour, 'temp':temp_h})
    df['hour_number'] = pd.to_numeric(df['hour_number'])

    plt.bar(df['hour_number'], df['temp'])
    plt.show()


    
def icon():
    city = city_text.get()
    
    r = requests.get('https://api.weatherbit.io/v2.0/forecast/daily?city='+city+'&key='+api_key)
    
    d = json.loads(r.text)
    
    icon_label['text'] = str(d['data'][0]['weather']['icon'])
    icon_label_t['text'] = str(d['data'][1]['weather']['icon'])
    icon_label_tt['text'] = str(d['data'][2]['weather']['icon'])
    
    

app = tk.Tk()
app.title("Weather App")
app.geometry("800x300")
city_text = tk.StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.grid(row=0, column=1)
  

Search_btn = Button(app, text="Search Weather",
                    width=12, command=lambda : [search(), icon()])
Search_btn.grid(row=0, column=2)
  
location_lbl = Label(app, text="Location", 
                     font={'bold', 20})
location_lbl.grid(row=0, column=0)
  
temperature_label = Label(app, text="")
temperature_label.grid(row=2, column=0)

temperature_label_t = Label(app, text="")
temperature_label_t.grid(row=2, column=1)

temperature_label_tt = Label(app, text="")
temperature_label_tt.grid(row=2, column=2)

temperature_label_min = Label(app, text="")
temperature_label_min.grid(row=3, column=0)

temperature_label_t_min = Label(app, text="")
temperature_label_t_min.grid(row=3, column=1)

temperature_label_tt_min = Label(app, text="")
temperature_label_tt_min.grid(row=3, column=2)

temperature_label_pop = Label(app, text="")
temperature_label_pop.grid(row=4, column=0)

temperature_label_t_pop = Label(app, text="")
temperature_label_t_pop.grid(row=4, column=1)

temperature_label_tt_pop = Label(app, text="")
temperature_label_tt_pop.grid(row=4, column=2)

icon_label = Label(app, text="")
icon_label.grid(row=5, column=0)

icon_label_t = Label(app, text="")
icon_label_t.grid(row=5, column=1)

icon_label_tt = Label(app, text="")
icon_label_tt.grid(row=5, column=2)




Grafik_btn = Button(app, text="Today",
                    width=12, command=lambda: grafik("1"))
Grafik_btn.grid(row=1, column=0)

tomorrow_btn = Button(app, text=tomorrow.strftime('%d.%m'),
                    width=12, command=lambda:grafik("2"))
tomorrow_btn.grid(row=1, column=1)

ttomorrow_btn = Button(app, text=ttomorrow.strftime('%d.%m'),
                    width=12, command=lambda:grafik("3"))
ttomorrow_btn.grid(row=1, column=2)



 



  
app.mainloop()
