import math
import sip
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QWidget
from apiCalls import *

from colour import Color

from gui.dayWidget import *
from gui.hourWidget import *


class Temperature:
    def __init__(self, avgTemperature: float, minTemperature: float):
        self.minT = minTemperature
        self.avgT = avgTemperature


class WeatherForecast:
    def __init__(self, temperature: Temperature, precipitationProbability: int):
        self.precipitationProbability = precipitationProbability
        self.temperature = temperature


class DayWidget(QWidget, Ui_DayWidget):
    def __init__(self, day, forecast: WeatherForecast):
        super().__init__()
        self.forecast = forecast
        self.day = day
        self.setupUi(self)

    def setupUi(self, Widget):
        super(DayWidget, self).setupUi(Widget)
        self.dayNameLabel.setText(self.day)
        self.dayAvgTemperatureLabel.setText(str(self.forecast.temperature.avgT) + "°C")
        self.nightAvgTemperatureLabel.setText(str(self.forecast.temperature.minT) + "°C")
        self.percentageLabel.setText(str(self.forecast.precipitationProbability) + "%")

    def asyncLoadImage(self, imageName: str):
        p = ProcessRunnable(target=getPixmapOfIcon, args=(imageName,))

        def set_pixmap(data):
            if not sip.isdeleted(self.label):
                self.label.setPixmap(data["pixmap"])

        p.status.captureDataFinished.connect(set_pixmap)
        p.start()


class HourWidget(QWidget, Ui_hourWidget):
    colors = list(Color("red").range_to(Color("blue"), 60))

    def __init__(self, temperature, hourStr):
        super().__init__()
        self.hourStr = hourStr
        self.temperature = temperature
        self.setupUi(self)

    def setupUi(self, widget):
        super(HourWidget, self).setupUi(widget)
        self.temperatureColumn.setText(str(self.temperature) + "°")
        height = int(math.fabs(int(self.temperature)))
        difference = 30 - height
        if self.temperature < 0:
            self.temperatureColumn.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        else:
            self.temperatureColumn.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignCenter)
        self.verticalLayout.setStretch(0, 30 if self.temperature < 0 else difference)
        self.verticalLayout.setStretch(1, height)
        self.verticalLayout.setStretch(2, 30 if self.temperature > 0 else difference)
        color_index = 0 - int(self.temperature) + 30
        if color_index >= 30:
            color_index = 29
        if color_index < 0:
            color_index = 0
        color = self.colors[color_index]
        self.temperatureColumn.setStyleSheet("background: " + str(color) + "; border-radius: 10px;")
        self.hourLabel.setText(self.hourStr)
        self.hourLabel.setAlignment(Qt.AlignCenter)



