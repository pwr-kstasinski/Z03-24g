import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import tkinter.font as tkFont
import os
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import csv


from functionality import *

class Gui:
    def __init__(self, city='Slesin'):
        self.window = tk.Tk()
        self.window.resizable(False, False)
        self.curr_weather = None

        self.citiesdict = {}
        self.citieslist = []
        with open('cities_20000.csv',encoding="UTF-8") as citiescsv:
            citiesreader = csv.reader(citiescsv, delimiter=',', quotechar='@')
            for x in citiesreader:
                #print(x)
                if(x[0]=='city_id'):
                    continue
                citystr="{}, {}".format(x[1],x[4])
                self.citieslist.append(citystr)
                self.citiesdict[citystr]=int(x[0])
        self.citychosen = tk.StringVar()
        
        self.cityselect = ttk.Combobox(self.window, width = 30, textvariable = self.citychosen)
        self.cityselect['values']=tuple(self.citieslist)
        self.cityselect.grid(column=4, row=0)
        self.cityselect.current(2)

        self.imgdef = ImageTk.PhotoImage(get_img('t01d',20))

        self.todayB = tk.Button(self.window, text='Today', width=12, command=self.shToday)
        self.todayB.grid(column=0, row=0)
        self.todayT = tk.Label(self.window, text='xxC', width=12)
        self.todayT.grid(column=0, row=1)
        self.todayW = tk.Label(self.window, image=self.imgdef)
        self.todayW.grid(column=0, row=2)

        self.tomorrowB = tk.Button(self.window, text='Tomorrow', width=12, command=self.shTomorrow)
        self.tomorrowB.grid(column=1, row=0)
        self.tomorrowT = tk.Label(self.window, text='xxC', width=12)
        self.tomorrowT.grid(column=1, row=1)
        self.tomorrowW = tk.Label(self.window, image=self.imgdef)
        self.tomorrowW.grid(column=1, row=2)

        self.afterB = tk.Button(self.window, text='After', width=12, command=self.shAfter)
        self.afterB.grid(column=2, row=0)
        self.afterT = tk.Label(self.window, text='xxC', width=12)
        self.afterT.grid(column=2, row=1)
        self.afterW = tk.Label(self.window, image=self.imgdef)
        self.afterW.grid(column=2, row=2)

        self.update_interface()
        self.citychosen.trace('w',self.update_interface)

    def update_weather(self,city):
        try:
            self.curr_weather = get_weather(city)
            self.hourly_weather = get_hourly_weather(city)
            #self.curr_weather = get_weather()
            #self.hourly_weather = get_hourly_weather()
        except:
            print("data update problem")
    
    def update_interface(self,a=None,b=None,c=None):
        ct = self.citiesdict[self.citychosen.get()]
        self.update_weather(ct)
        self.window.title(f'Weather - {self.curr_weather["city_name"]}')
        self.todayT.configure(text=self.curr_weather['data'][0]['temp'])
        self.tomorrowT.configure(text=self.curr_weather['data'][1]['temp'])
        self.afterT.configure(text=self.curr_weather['data'][2]['temp'])

        self.todayI = ImageTk.PhotoImage(get_img(self.curr_weather['data'][0]['weather']['icon'], 30))
        self.tomorrowI = ImageTk.PhotoImage(get_img(self.curr_weather['data'][1]['weather']['icon'], 30))
        self.afterI = ImageTk.PhotoImage(get_img(self.curr_weather['data'][2]['weather']['icon'], 30))
        self.todayW.configure(image=self.todayI)
        self.tomorrowW.configure(image=self.tomorrowI)
        self.afterW.configure(image=self.afterI)
    def show_hours(self,offset):
        hours = range(0,24)
        temps = []
        for i in hours:
            temps.append(self.hourly_weather['data'][offset+i]['temp'])
        print(temps)

        fig, ax = plt.subplots()
        ind = np.arange(24)
        p1 = ax.bar(ind, tuple(temps), 0.9, label='temp')
        ax.set_xticks(ind)
        ax.bar_label(p1, label_type='center')
        ax.set_xticklabels(hours)
        ax.set_title('Temperatures')
        #fig.tight_layout()
        fig.set_size_inches((14,4))
        plt.show()
        
    def shToday(self):
        self.show_hours(0)
    def shTomorrow(self):
        self.show_hours(24)
    def shAfter(self):
        self.show_hours(48)
        

if __name__ == '__main__':
    top = Gui()
    tk.mainloop()