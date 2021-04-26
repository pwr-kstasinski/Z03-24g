from tkinter import *

from PIL import ImageTk, Image
import numpy as np
from pandas import read_csv
from openapi_client.api.day___daily_forecast_api import DayDailyForecastApi
from openapi_client.api.hour___hourly_forecast_api import HourHourlyForecastApi
import matplotlib.pyplot as plt
import datetime
from datetime import date
import time


def errorWindow(result):
    errorWindow = Toplevel(root)
    errorWindow.title("Error Message")
    changeTime()
    errorWindow.geometry("450x311")

    mainTextChooseDay = Label(errorWindow, text=result, bg='white',
                              font=("bold", 15), fg="blue")
    mainTextChooseDay.place(x=80, y=1)

    err = Image.open('errMeme2.png')
    err = err.resize((450, 280), Image.ANTIALIAS)
    errImage = ImageTk.PhotoImage(err)
    errPanel = Label(errorWindow, image=errImage, bg="white")
    errPanel.image = errImage
    errPanel.place(x=0, y=30)


def checkCity():
    city = city_entry.get()
    df = read_csv('cities_20000.csv')
    dataArray = np.array(df)
    dataDict = {}
    for i in dataArray:
        dataDict[i[1]] = i[0]

    result, flag = getIndex(city, dataDict)

    if flag:
        openNewWindow(result)
    else:
        errorWindow(result)


def getIndex(city_name, dataDict):
    try:
        flag = True

        return dataDict[city_name], flag

    except Exception as e:
        flag = False
        error = f"{city_name} doesn't exist in database"
        return error, flag


def partitionTemp(hourWeather):
    hourDict = hourWeather.to_dict()
    hourDict = hourDict['data']

    day = int(hourDict[0]['timestamp_local'][8:10])

    todayTemps = []
    tomorrowTemps = []
    dayAfterTomorrowTemps = []

    for i in hourDict:
        x = int(i['timestamp_local'][8:10])
        time = int(i['timestamp_local'][11:13])
        if x == day:
            todayTemps.append([time, i['temp']])
        elif x == day + 1:
            tomorrowTemps.append([time, i['temp']])
        else:
            dayAfterTomorrowTemps.append([time, i['temp']])

    return todayTemps, tomorrowTemps, dayAfterTomorrowTemps


def getData(result):
    key = '06efcc5d2264438ea61170657d9fd9b9'
    obj = DayDailyForecastApi()
    obj2 = HourHourlyForecastApi()
    time = 72
    day = obj.forecast_dailycity_idcity_id_get(result, key, days=3)
    hourlyWeather = obj2.forecast_hourlycity_idcity_id_get(result, key, hours=time)

    return day, hourlyWeather


def proceed3DaysData(dayWeather):
    weatherDict = dayWeather.to_dict()
    city = weatherDict['city_name']
    countryCode = weatherDict['country_code']
    weatherDict = weatherDict['data']
    db = [city, countryCode]
    for i in weatherDict:
        date = i['datetime']
        tempMax = i['app_max_temp']
        tempMin = i['app_min_temp']
        clouds = i['clouds']
        description = i['weather']['description']
        icon = i['weather']['icon']
        db.append([date, tempMax, tempMin, clouds, description, icon])

    return db


def displayPlot(hourTemps, newWindow):
    displayWindow = Toplevel(newWindow)
    displayWindow.title("TemperaturePlot")

    changeTime()
    displayWindow.geometry("1000x530")
    x = []
    y = []
    for i in hourTemps:
        y.append(i[0])
        x.append(i[1])

    def autolabel(rects, xpos='center'):
        """
        Attach a text label above each bar in rects, displaying its height.

        xpos indicates which side to place the text w.r.t. the center of
        the bar. It can be one of the following {'center', 'right', 'left'}.
        """

        xpos = xpos.lower()
        ha = {'center': 'center', 'right': 'left', 'left': 'right'}
        offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}

        for rect in rects:
            height = rect.get_height()
            plt.text(rect.get_x() + rect.get_width() * offset[xpos], 1.01 * height, '{}'.format(height), ha=ha[xpos],
                     va='bottom')

    plt.figure(figsize=(15, 8))
    ax = plt.bar(y, x, color='coral')
    plt.title('Weather by hour')
    plt.xlabel('Hour', loc='right')
    plt.ylabel('Tempreture [C]')
    plt.xticks(y)
    autolabel(ax)
    plt.tight_layout()
    plt.savefig('temperaturePlot.png')
    plt.close()

    tempPlot = Image.open('temperaturePlot.png')
    tempPlot = tempPlot.resize((1000, 530), Image.ANTIALIAS)
    tempPlotImage = ImageTk.PhotoImage(tempPlot)
    currTempPanel = Label(displayWindow, image=tempPlotImage, bg="white")
    currTempPanel.image = tempPlotImage
    currTempPanel.place(x=0, y=0)


def currentDate():
    weekDays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    months = (
        "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
        "December")

    today = date.today()
    d1 = today.strftime("%Y/%m/%d")

    year = int(d1[0:4])
    month = int(d1[5:7])
    day = int(d1[8:10])

    todaysDate = datetime.date(year, month, day)
    weekDay = todaysDate.weekday()
    returnWeekDay = weekDays[weekDay]
    returnMonth = months[month - 1]
    return returnWeekDay, returnMonth, d1[8:10]

def changeTime():
    now = time.localtime()
    currTime = time.strftime("%H:%M", now)

    hour = Label(root, text=currTime,
             bg='turquoise1', font=("Times", 25, "bold"), fg="black")
    hour.place(x=120, y=360)


def proceedWeekDay(weatherDict, whatDay):
    weekDays = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
    date = weatherDict[whatDay][0]
    year = int(date[0:4])
    month = int(date[5:7])
    day = int(date[8:10])

    tomorrowDate = datetime.date(year, month, day)
    weekDay = tomorrowDate.weekday()
    returnWeekDay = weekDays[weekDay]
    return returnWeekDay, date[8:10]


def createLabelsToday(weatherDict, newWindow, todayTemps):
    lable_day = Label(newWindow, text=("Today"), width=0,
                      bg='sky blue', font=("bold", 20))
    lable_day.place(x=60, y=50)

    lable_dayTemp = Label(newWindow, text=f'{weatherDict[2][1]}° ', width=0,
                          bg='sky blue', font=("bold", 20), fg="blue4")
    lable_dayTemp.place(x=70, y=90)

    lable_nightTemp = Label(newWindow, text=f'{weatherDict[2][2]}° ', width=0,
                            bg='sky blue', font=("bold", 10), fg="blue4")
    lable_nightTemp.place(x=80, y=120)

    cloudType = weatherDict[2][5]

    todayImage = Image.open(f'icons/{cloudType}.png')
    todayImage = todayImage.resize((150, 130), Image.ANTIALIAS)
    todayWeatherImage = ImageTk.PhotoImage(todayImage)
    currWeatherPanel = Label(newWindow, image=todayWeatherImage, bg="midnight blue")
    currWeatherPanel.image = todayWeatherImage
    currWeatherPanel.place(x=30, y=150)

    lable_weatherDescription = Label(newWindow, text=f'{weatherDict[2][4]}', width=0,
                                     bg='midnight blue', font=("bold", 10), fg="white")
    lable_weatherDescription.place(x=35, y=262)

    todayDetails = Button(newWindow, text=' Details ', fg='black', bg='spring green',
                          command=lambda: displayPlot(todayTemps, newWindow), height=1, width=21)
    todayDetails.place(x=28, y=290)


def createLabelsTomorrow(weatherDict, newWindow, tomorrowTemps):
    weekday, day = proceedWeekDay(weatherDict, 3)

    lable_NextDay = Label(newWindow, text=(f'{weekday} {day}'), width=0,
                          bg='sky blue', font=("bold", 20))
    lable_NextDay.place(x=260, y=50)

    lable_NextDayTemp = Label(newWindow, text=f'{weatherDict[3][1]}° ', width=0,
                              bg='sky blue', font=("bold", 20), fg="blue4")
    lable_NextDayTemp.place(x=270, y=90)
    #
    lable_NextNightTemp = Label(newWindow, text=f'{weatherDict[3][2]}° ', width=0,
                                bg='sky blue', font=("bold", 10), fg="blue4")
    lable_NextNightTemp.place(x=280, y=120)
    #
    cloudTypeTomorrow = weatherDict[3][5]

    tomorrowImage = Image.open(f'icons/{cloudTypeTomorrow}.png')
    tomorrowImage = tomorrowImage.resize((150, 130), Image.ANTIALIAS)
    tomorrowWeatherImage = ImageTk.PhotoImage(tomorrowImage)
    currWeatherPanel = Label(newWindow, image=tomorrowWeatherImage, bg="midnight blue")
    currWeatherPanel.image = tomorrowWeatherImage
    currWeatherPanel.place(x=230, y=150)
    #
    lable_weatherDescription = Label(newWindow, text=(f'{weatherDict[3][4]}'), width=0,
                                     bg='midnight blue', font=("bold", 10), fg="white")
    lable_weatherDescription.place(x=235, y=262)

    tomorrowDetails = Button(newWindow, text=' Details ', fg='black', bg='spring green',
                             command=lambda: displayPlot(tomorrowTemps, newWindow), height=1, width=21)
    tomorrowDetails.place(x=228, y=290)


def createLabelsDayAfterTomorrow(weatherDict, newWindow, dayAfterTomorrowTemps):
    weekday, day = proceedWeekDay(weatherDict, 4)

    lable_AfterNextDay = Label(newWindow, text=(f'{weekday} {day}'), width=0,
                               bg='sky blue', font=("bold", 20))
    lable_AfterNextDay.place(x=460, y=50)

    lable_AfterNextDayTemp = Label(newWindow, text=f'{weatherDict[4][1]}° ', width=0,
                                   bg='sky blue', font=("bold", 20), fg="blue4")
    lable_AfterNextDayTemp.place(x=470, y=90)
    #
    lable_AfterNextNightTemp = Label(newWindow, text=f'{weatherDict[4][2]}° ', width=0,
                                     bg='sky blue', font=("bold", 10), fg="blue4")
    lable_AfterNextNightTemp.place(x=480, y=120)
    #
    cloudTypeAfterTomorrow = weatherDict[4][5]

    AfterTomorrowImage = Image.open(f'icons/{cloudTypeAfterTomorrow}.png')
    AfterTomorrowImage = AfterTomorrowImage.resize((150, 130), Image.ANTIALIAS)
    AfterTomorrowWeatherImage = ImageTk.PhotoImage(AfterTomorrowImage)
    currWeatherPanel = Label(newWindow, image=AfterTomorrowWeatherImage, bg="midnight blue")
    currWeatherPanel.image = AfterTomorrowWeatherImage
    currWeatherPanel.place(x=430, y=150)
    #
    lable_weatherDescription = Label(newWindow, text=(f'{weatherDict[3][4]}'), width=0,
                                     bg='midnight blue', font=("bold", 10), fg="white")
    lable_weatherDescription.place(x=435, y=262)

    afterTommorowDetails = Button(newWindow, text=' Details ', fg='black', bg='spring green',
                                  command=lambda: displayPlot(dayAfterTomorrowTemps, newWindow), height=1, width=21)
    afterTommorowDetails.place(x=428, y=290)


def openNewWindow(result):
    city = city_entry.get()

    newWindow = Toplevel(root)

    newWindow.geometry("620x330")
    newWindow['background'] = "sky blue"
    # Getting data for current city
    dayWeather, hourWeather = getData(result)
    # proceeding daily weather for next 3 days
    weatherDict = proceed3DaysData(dayWeather)
    newWindow.title(f'{city} {weatherDict[1]}')
    # getting detailed temp weather for the next 48 hours
    todayTemps, tomorrowTemps, dayAfterTomorrowTemps = partitionTemp(hourWeather)

    mainTextChooseDay = Label(newWindow, text="Check out weather forecast of your choice", bg='sky blue',
                              font=("bold", 12), fg="gray1")
    mainTextChooseDay.place(x=140, y=1)

    createLabelsToday(weatherDict, newWindow, todayTemps)

    createLabelsTomorrow(weatherDict, newWindow, tomorrowTemps)

    createLabelsDayAfterTomorrow(weatherDict, newWindow, dayAfterTomorrowTemps)
    changeTime()

root = Tk()
root.title("Weather App")
root.geometry("335x430")
root['background'] = "turquoise1"
nameDay, month, day = currentDate()

date1 = Label(root, text=f' {nameDay}  ', bg='turquoise1', font=("Times", 25, "bold"), fg="black")
date1.place(x=25, y=300)
month1 = Label(root, text=f' {day} {month}', bg='turquoise1', font=("Times", 25, "bold"), fg="black")
month1.place(x=155, y=300)

changeTime()
mainText = Label(root, text="Enter your location in field above", bg='turquoise1', font=("Times", 12, "bold"),
                 fg="black")
mainText.place(x=55, y=100)

new = ImageTk.PhotoImage(Image.open('mainPhoto2.png'))
panel = Label(root, image=new)
panel.place(x=11, y=130)

city_name = StringVar()
city_entry = Entry(root, textvariable=city_name, width=24, font=("Times", 20, "bold"), bg="MediumPurple1")
city_entry.grid(row=1, column=0, ipady=20, stick=W + E + N + S)

city_nameButton = Button(root, text="Search", font=("bold", 10), command=checkCity, fg="black", bg="SeaGreen1")
city_nameButton.grid(row=20, column=0, padx=10, stick=W + E + N + S)

root.mainloop()
