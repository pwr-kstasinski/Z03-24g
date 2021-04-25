import math
import urllib.request

from PyQt5.QtCore import Qt, QRunnable, QThreadPool, QObject, pyqtSignal
from PyQt5.QtGui import QPixmap, QMovie
from PyQt5.QtWidgets import *

from gui.dayWidget import *
from gui.hourWidget import *
from weatherApi.openapi_client.api.sixteen_day___daily_forecast_api import *
from weatherApi.openapi_client.api.hundred_twenty_hour___hourly_forecast_api import *
from gui.window import *
from colour import Color


class Temperature:
    def __init__(self, avgTemperature: float, minTemperature: float):
        self.minT = minTemperature
        self.avgT = avgTemperature


class Precipitation:
    def __init__(self, precipitationProbability: int):
        self.probabilityP = precipitationProbability


class WeatherForecast:
    def __init__(self, temperature: Temperature, precipitation: Precipitation):
        self.precipitation = precipitation
        self.temperature = temperature


class DayWidget(Ui_DayWidget):
    def __init__(self, day, forecast: WeatherForecast, icon_pixmap):
        self.icon_pixmap = icon_pixmap
        self.forecast = forecast
        self.day = day

    def setupUi(self, Widget):
        super(DayWidget, self).setupUi(Widget)
        self.dayNameLabel.setText(self.day)
        self.dayAvgTemperatureLabel.setText(str(self.forecast.temperature.avgT) + "°C")
        self.nightAvgTemperatureLabel.setText(str(self.forecast.temperature.minT) + "°C")
        self.label.setPixmap(self.icon_pixmap)
        self.percentageLabel.setText(str(self.forecast.precipitation.probabilityP) + "%")

    def generateWidget(self):
        w = QWidget()
        self.setupUi(w)
        return w


class HourWidget(Ui_hourWidget):
    colors = list(Color("red").range_to(Color("blue"), 60))

    def __init__(self, temperature):
        self.temperature = temperature

    def setupUi(self, widget):
        super(HourWidget, self).setupUi(widget)
        self.temperatureColumn.setText(str(self.temperature) + "°")
        height = int(math.fabs(int(self.temperature)))
        difference = 30 - height
        if self.temperature < 0:
            self.temperatureColumn.setAlignment(QtCore.Qt.AlignTop)
        else:
            self.temperatureColumn.setAlignment(QtCore.Qt.AlignBottom)
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

    def generateWidget(self):
        w = QWidget()
        self.setupUi(w)
        return w


class State:
    def __init__(self, widget):
        self.widget = widget

    @staticmethod
    def _clearLayout(layout: QLayout):
        for i in reversed(range(layout.count())):
            layout.itemAt(i).widget().deleteLater()

    def loadState(self, contentLayout: QLayout):
        self._clearLayout(contentLayout)
        contentLayout.addWidget(self.widget)


class ReversibleState(State):
    def __init__(self, widget, lastState: State):
        super().__init__(widget)
        self.lastState = lastState

    def unloadState(self, contentLayout: QLayout):
        self.lastState.loadState(contentLayout)


class ProcessRunnableStatus(QObject):
    captureDataFinished = pyqtSignal(list)


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


class WeatherProgram(Ui_MainWindow):
    def __init__(self):
        super(WeatherProgram, self).__init__()
        self.current_state = None

    def setupUi(self, MainWindow):
        super(WeatherProgram, self).setupUi(MainWindow)
        self.pushButton.clicked.connect(self.async_load_days)

    def async_load_days(self):
        self.set_loading_screen()
        p = ProcessRunnable(target=self.get_days_data, args=())
        p.status.captureDataFinished.connect(self.display_days_widgets)
        p.start()

    def async_load_hours(self, data: str):
        self.set_loading_screen()
        p = ProcessRunnable(target=self.get_hours_data, args=())

        def filter_data(hours):
            filtered = filter(lambda hour: hour["datetime"].find(data) != -1, hours)
            self.display_hours_widgets(filtered)

        p.status.captureDataFinished.connect(filter_data)
        p.start()

    def set_loading_screen(self):
        label = QLabel()
        label.setAlignment(Qt.AlignCenter)
        q_movie = QMovie("gui/loading.gif")
        label.setMovie(q_movie)
        q_movie.start()
        state = State(label)
        self.set_state(state)

    def display_days_widgets(self, days):
        widget = QWidget()
        horizontalLayout = QHBoxLayout()
        for day in days:
            one_day = self.loadDayWidget(day)
            day_widget = one_day.generateWidget()
            day_widget.mouseReleaseEvent = lambda _: self.async_load_hours(one_day.day)
            horizontalLayout.addWidget(day_widget)
        widget.setLayout(horizontalLayout)
        state = State(widget)
        self.set_state(state)

    def set_state(self, state):
        self.current_state = state
        state.loadState(self.contentLayout)

    def display_hours_widgets(self, hours):
        widget = QWidget()
        horizontalLayout = QHBoxLayout()
        for hour in hours:
            one_hour = self.loadHourWidget(hour)
            hour_widget = one_hour.generateWidget()
            horizontalLayout.addWidget(hour_widget)
        widget.setLayout(horizontalLayout)
        state = ReversibleState(widget, self.current_state)
        self.set_state(state)

    def get_days_data(self):
        cityName = str(self.lineEdit.text())
        api = SixteenDayDailyForecastApi()
        forecast_daily = api.forecast_daily_get(cityName, days=3, key="f8c636b607224c2c8fc99a19443584df")
        days = forecast_daily["data"]
        return days

    def get_hours_data(self):
        cityName = str(self.lineEdit.text())
        api = HundredTwentyHourHourlyForecastApi()
        forecast_hourly = api.forecast_hourly_get(cityName, hours=120, key="f8c636b607224c2c8fc99a19443584df")
        hours = forecast_hourly["data"]
        return hours

    def loadDayWidget(self, day):
        avgTemperature = day["temp"]
        minTemperature = day["min_temp"]
        temperature = Temperature(avgTemperature, minTemperature)
        precipitationProbability = day["pop"]
        precipitation = Precipitation(precipitationProbability)
        forecast = WeatherForecast(temperature, precipitation)
        iconName = day["weather"]["icon"]
        icon_pixmap = self.get_Pixmap_of_icon(iconName)
        return DayWidget(day["datetime"], forecast, icon_pixmap)

    def loadHourWidget(self, hour):
        temperature = hour["temp"]
        return HourWidget(temperature)

    @staticmethod
    def get_Pixmap_of_icon(iconName):
        url = f'https://www.weatherbit.io/static/img/icons/{iconName}.png'
        url_data = urllib.request.urlopen(url).read()
        pixmap = QPixmap()
        pixmap.loadFromData(url_data)
        return pixmap

    def run(self) -> None:
        import sys

        app = QtWidgets.QApplication(sys.argv)
        w = QtWidgets.QMainWindow()
        self.setupUi(w)
        w.show()
        sys.exit(app.exec_())


if __name__ == '__main__':
    weatherProgram = WeatherProgram()
    weatherProgram.run()
