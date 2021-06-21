from PyQt5 import QtWidgets

from tree_elements import *
from window import Ui_MainWindow


class Calculator:
    def __init__(self, equationTree: EquationTree):
        self.equation_tree: EquationTree = equationTree

    def run(self) -> None:
        raise NotImplementedError


class ConsoleCalculator(Calculator):
    def run(self) -> None:
        self.read()
        self.calc()
        self.print()

    def read(self) -> None:
        equation = input("Podaj równanie: ").replace(",", ".")
        self.equation_tree.read(equation)

    def calc(self) -> None:
        result = self.equation_tree.calc()
        print(f"Wynik: {result}")

    def print(self) -> None:
        print(self.equation_tree)


class Observer:
    def update(self, value: str):
        raise NotImplementedError


class Display(Observer):
    def __init__(self, display: QtWidgets.QLabel):
        self.display = display

    def update(self, value: str):
        self.display.setText(value)


class TextOperation:
    def accept(self, string: str) -> str:
        raise NotImplementedError


class AddTextOperation(TextOperation):
    def __init__(self, value: str):
        self.value = value

    def accept(self, string: str) -> str:
        return string + self.value


class WrapTextOperation(TextOperation):
    def __init__(self, start: str, end: str):
        self.start = start
        self.end = end

    def accept(self, string: str) -> str:
        return self.start + string + self.end


class CalcOperation(AddTextOperation):
    def __init__(self, value: float):
        super().__init__(" = %.5f " % value)
        self.result = value


class ErrorOperation(AddTextOperation):
    pass


class EquationObservableStack:
    def __init__(self):
        self.text_operations: List[TextOperation] = []
        self.observers: List[Observer] = []

    def push(self, operation: TextOperation):
        if len(self.text_operations) > 0:
            last_operation = self.text_operations[-1]
            if isinstance(last_operation, CalcOperation):
                calc: CalcOperation = last_operation
                self.clear()
                self.push(AddTextOperation("%.5f" % calc.result))
            elif isinstance(last_operation, ErrorOperation):
                self.clear()
        self.text_operations.append(operation)
        self.notify()

    def pop(self) -> TextOperation:
        pop = self.text_operations.pop()
        self.notify()
        return pop

    def clear(self):
        self.text_operations = []
        self.notify()

    def __str__(self):
        text = ""
        for operation in self.text_operations:
            text = operation.accept(text)
        return text

    def notify(self):
        for i in self.observers:
            i.update(str(self))

    def add_observer(self, observer: Observer):
        self.observers.append(observer)


class WindowCalculator(Calculator, Ui_MainWindow):
    def __init__(self, equationTree: EquationTree):
        super().__init__(equationTree)
        self.equation_stack = EquationObservableStack()

    def read(self) -> None:
        pass

    def calc(self) -> None:
        if len(self.equation_stack.text_operations) > 0:
            last_operation = self.equation_stack.text_operations[-1]
            if isinstance(last_operation, CalcOperation):
                return
        operation: AddTextOperation
        try:
            self.equation_tree.read("".join(str(self.equation_stack)))
            try:
                value = self.equation_tree.calc()
                operation = CalcOperation(value)
            except:
                self.equation_stack.clear()
                operation = ErrorOperation("Not allowed operation")
        except:
            self.equation_stack.clear()
            operation = ErrorOperation("Syntax Error")
        self.equation_stack.push(operation)

    def setupUi(self, MainWindow):
        super(WindowCalculator, self).setupUi(MainWindow)

        number_buttons = [
            self.number_0_button,
            self.number_1_button,
            self.number_2_button,
            self.number_3_button,
            self.number_4_button,
            self.number_5_button,
            self.number_6_button,
            self.number_7_button,
            self.number_8_button,
            self.number_9_button
        ]
        for index, number_button in enumerate(number_buttons):
            self.add_text_on_click(number_button, str(index))

        self.add_text_on_click(self.comma_button, ".")
        self.add_text_on_click(self.power_button, "^")
        self.add_text_on_click(self.add_button, "+")
        self.add_text_on_click(self.subtract_button, "-")
        self.add_text_on_click(self.multiply_button, "*")
        self.add_text_on_click(self.divide_button, "/")
        self.add_text_on_click(self.factorial_button, "!")
        self.add_text_on_click(self.modulo_button, "%")
        self.add_text_on_click(self.left_bracket_button, "(")
        self.add_text_on_click(self.right_bracket_button, ")")

        self.wrap_text_on_click(self.square_power_button, "(", ")^2")
        self.wrap_text_on_click(self.square_root_button, "sqrt(", ")")
        self.wrap_text_on_click(self.absolute_button, "abs(", ")")
        self.wrap_text_on_click(self.inversion_button, "1/(", ")")
        self.wrap_text_on_click(self.modulo_f_button, "mod(", ")")
        self.wrap_text_on_click(self.brackets_button, "(", ")")
        self.wrap_text_on_click(self.logarithm_button, "log(", ")")

        self.clear_button.clicked.connect(self.equation_stack.clear)
        self.undo_button.clicked.connect(self.equation_stack.pop)
        self.calc_button.clicked.connect(self.calc)

        display = Display(self.equation_label)
        self.equation_stack.add_observer(display)

    def run(self) -> None:
        import sys

        app = QtWidgets.QApplication(sys.argv)
        w = QtWidgets.QMainWindow()
        self.setupUi(w)
        w.show()
        sys.exit(app.exec_())

    def add_text_on_click(self, button: QtWidgets.QPushButton, value: str):
        button.clicked.connect(lambda: self.equation_stack.push(AddTextOperation(value)))

    def wrap_text_on_click(self, button: QtWidgets.QPushButton, start: str, end: str):
        button.clicked.connect(lambda: self.equation_stack.push(WrapTextOperation(start, end)))


operations_set: Set[Operation] = {Add(), Subtract(), Multiply(), Divide(), Power(), ModuloOperation()}
functions_set: Set[Function] = {Brackets(), Factorial(), Logarithm(), ModuloFunction(), Absolute(), Empty(),
                                SquareRoot(), }

if __name__ == '__main__':
    tree = EquationTree(operations_set, functions_set)
    calculator = WindowCalculator(tree)
    calculator.run()
