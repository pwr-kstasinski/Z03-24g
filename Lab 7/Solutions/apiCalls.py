from PyQt5.QtCore import QObject, pyqtSignal, QRunnable, QThreadPool
from PyQt5.QtGui import QPixmap

from weatherApi.openapi_client.api.hundred_twenty_hour___hourly_forecast_api import *
from weatherApi.openapi_client.api.sixteen_day___daily_forecast_api import *
import urllib.request


class ProcessRunnableStatus(QObject):
    captureDataFinished = pyqtSignal(dict)


class ProcessRunnable(QRunnable):
    def __init__(self, target, args):
        QRunnable.__init__(self)
        self.t = target
        self.args = args
        self.status = ProcessRunnableStatus()

    def run(self):
        t = self.t(*self.args)
        self.status.captureDataFinished.emit(t)

    def start(self):
        QThreadPool.globalInstance().start(self)


def getDaysData(cityName):
    api = SixteenDayDailyForecastApi()
    forecast_daily = api.forecast_daily_get(cityName, days=3, key="f8c636b607224c2c8fc99a19443584df")
    days = forecast_daily["data"]
    return {"days": days}


def getHoursData(cityName):
    api = HundredTwentyHourHourlyForecastApi()
    forecast_hourly = api.forecast_hourly_get(cityName, hours=120, key="f8c636b607224c2c8fc99a19443584df")
    hours = forecast_hourly["data"]
    return {"hours": hours}


def getPixmapOfIcon(iconName):
    url = f'https://www.weatherbit.io/static/img/icons/{iconName}.png'
    url_data = urllib.request.urlopen(url).read()
    pixmap = QPixmap()
    pixmap.loadFromData(url_data)
    return {"pixmap": pixmap}
