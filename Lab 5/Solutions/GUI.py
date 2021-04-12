import kivy
from BetterEquation import calculate
from kivy.app import App
from kivy.config import Config
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
kivy.require('2.0.0')

Builder.load_file('calcGUI.kv')
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')


class CalcGridLayout(GridLayout):
    def calculate(self, expression):
        self.display.text = str(calculate(expression))


class CalculatorApp(App):
    def build(self):
        return CalcGridLayout()


if __name__ == '__main__':
    calcApp = CalculatorApp()
    calcApp.run()