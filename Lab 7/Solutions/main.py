
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import *
from gui.window import *
from widgets import *


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


class WeatherProgram(Ui_MainWindow):
    def __init__(self):
        super(WeatherProgram, self).__init__()
        self.current_state = None

    def setupUi(self, MainWindow):
        super(WeatherProgram, self).setupUi(MainWindow)
        self.pushButton.clicked.connect(lambda: self.asyncLoadDays(self.lineEdit.text()))

    def asyncLoadDays(self, cityName):
        self.setLoadingScreen()
        p = ProcessRunnable(target=getDaysData, args=(cityName,))
        p.status.captureDataFinished.connect(lambda data: self.displayDaysWidgets(data["days"], cityName))
        p.start()

    def asyncLoadHours(self, date: str, cityName: str):
        self.setLoadingScreen()
        p = ProcessRunnable(target=getHoursData, args=(cityName,))

        def filterData(hours):
            filtered = list(filter(lambda hour: hour["timestamp_local"].find(date) != -1, hours["hours"]))
            self.displayHoursWidgets(date, filtered)

        p.status.captureDataFinished.connect(filterData)
        p.start()

    def setState(self, state):
        self.current_state = state
        state.loadState(self.contentLayout)

    def setLoadingScreen(self):
        label = QLabel()
        label.setAlignment(Qt.AlignCenter)
        q_movie = QMovie("gui/loading.gif")
        label.setMovie(q_movie)
        q_movie.start()
        state = State(label)
        self.setState(state)

    def displayDaysWidgets(self, days, cityName):
        widget = QWidget()
        horizontalLayout = QHBoxLayout()
        for day in days:
            one_day = self.loadDayWidget(day, cityName)
            horizontalLayout.addWidget(one_day)
        widget.setLayout(horizontalLayout)
        state = State(widget)
        self.setState(state)

    def displayHoursWidgets(self, date, hours):
        verticalWidget = QWidget()
        verticalWidget.setStyleSheet("background: white;")
        verticalLayout = QVBoxLayout()

        label = QLabel()
        label.setText(date)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size: 20px; font-weight: bold;")
        verticalLayout.addWidget(label)

        horizontalWidget = QWidget()
        horizontalLayout = QHBoxLayout()
        for hour in hours:
            one_hour = self.loadHourWidget(hour)
            horizontalLayout.addWidget(one_hour)
        horizontalWidget.setLayout(horizontalLayout)
        verticalLayout.addWidget(horizontalWidget)

        verticalWidget.setLayout(verticalLayout)
        state = State(verticalWidget)
        self.setState(state)

    def loadDayWidget(self, day, cityName):
        avgTemperature = day["temp"]
        minTemperature = day["min_temp"]
        temperature = Temperature(avgTemperature, minTemperature)
        precipitation = day["pop"]
        forecast = WeatherForecast(temperature, precipitation)
        iconName = day["weather"]["icon"]
        widget = DayWidget(day["datetime"], forecast)
        widget.asyncLoadImage(iconName)
        widget.mouseReleaseEvent = lambda _: self.asyncLoadHours(widget.day, cityName)
        return widget

    @staticmethod
    def loadHourWidget(hour):
        temperature = hour["temp"]
        timestampStr = hour["timestamp_local"]
        timeStr = timestampStr.split("T")[1]
        hourStr = timeStr[:timeStr.rfind(":")]
        return HourWidget(temperature, hourStr)

    def run(self) -> None:
        app = QtWidgets.QApplication(sys.argv)
        w = QtWidgets.QMainWindow()
        self.setupUi(w)
        w.show()
        sys.exit(app.exec_())


if __name__ == '__main__':
    weatherProgram = WeatherProgram()
    weatherProgram.run()
