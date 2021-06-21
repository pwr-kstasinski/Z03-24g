import math


class Function:
    def calc(self, x: float) -> float:
        raise NotImplementedError
    
    def check(self, equation: str):
        raise NotImplementedError

    def edit(self, equation: str):
        raise NotImplementedError


class Factorial(Function):
    def edit(self, equation: str):
        return equation[:-1]

    def check(self, equation: str):
        return equation[-1] == "!"

    def calc(self, x: float) -> float:
        return math.factorial(x)


class Logarithm(Function):
    def edit(self, equation: str):
        return equation[3:]

    def check(self, equation: str):
        return equation[:3] == "log"

    def calc(self, x: float) -> float:
        return math.log(x, 10)


class ModuloFunction(Function):
    def edit(self, equation: str):
        return equation[3:]

    def check(self, equation: str):
        return equation[:3] == "mod"

    def calc(self, x: float) -> float:
        return math.modf(x)[0]


class Absolute(Function):
    def edit(self, equation: str):
        return equation[3:]

    def check(self, equation: str):
        return equation[:3] == "abs"

    def calc(self, x: float) -> float:
        return math.fabs(x)


class Empty(Function):
    def calc(self, x: float) -> float:
        return x

    def check(self, equation: str):
        return equation == ""

    def edit(self, equation: str):
        return "0"


class SquareRoot(Function):
    def edit(self, equation: str):
        return equation[4:]

    def check(self, equation: str):
        return equation[:4] == "sqrt"

    def calc(self, x: float) -> float:
        return math.sqrt(x)


class Brackets(Function):
    def edit(self, equation: str):
        return equation[1:-1]

    def check(self, equation: str):
        counter = 0
        if equation[0] != "(" or equation[-1] != ")":
            return False
        equation = equation[1:-1]
        for letter in equation:
            if letter == "(":
                counter += 1
            elif letter == ")":
                if counter == 0:
                    return False
                else:
                    counter -= 1
        return True

    def calc(self, x: float) -> float:
        return x
