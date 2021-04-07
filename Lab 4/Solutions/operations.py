
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
    def get_priority(self) -> int:
        return 1

    def __str__(self):
        return "+"

    def calc(self, x: float, y: float) -> float:
        return x + y


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
