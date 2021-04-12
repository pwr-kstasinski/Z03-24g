import math


class Operation:
    def calc(self, x: float, y: float) -> float:
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError

    def __hash__(self):
        return hash(str(self))

    def get_priority(self) -> int:
        raise NotImplementedError


class Add(Operation):
    def calc(self, x: float, y: float) -> float:
        return x + y

    def get_priority(self) -> int:
        return 1

    def __str__(self):
        return "+"


class Subtract(Operation):
    def get_priority(self) -> int:
        return 1

    def __str__(self):
        return "-"

    def calc(self, x: float, y: float) -> float:
        return x - y


class Multiply(Operation):
    def get_priority(self) -> int:
        return 2

    def __str__(self):
        return "*"

    def calc(self, x: float, y: float) -> float:
        return x * y


class Divide(Operation):
    def get_priority(self) -> int:
        return 2

    def __str__(self):
        return "/"

    def calc(self, x: float, y: float) -> float:
        return x / y


class Power(Operation):
    def calc(self, x: float, y: float) -> float:
        return x ** y

    def __str__(self):
        return "^"

    def get_priority(self) -> int:
        return 3


class ModuloOperation(Operation):
    def calc(self, x: float, y: float) -> float:
        return math.fmod(x, y)

    def __str__(self):
        return "%"

    def get_priority(self) -> int:
        return 2
