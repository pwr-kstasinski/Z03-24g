import re
from typing import Set, Dict

from operations import *


class TreeElement:
    def calc(self) -> float:
        raise NotImplementedError


class ValueElement(TreeElement):
    def __init__(self, value: float):
        self.value = value

    def calc(self) -> float:
        return self.value


class OperationElement(TreeElement):
    def __init__(self, operation: Operation, x: TreeElement, y: TreeElement):
        self.operation = operation
        self.x = x
        self.y = y

    def calc(self) -> float:
        return self.operation.calc(self.x.calc(), self.y.calc())


class EquationsTree:
    def __init__(self, operations: Set[Operation]):
        self.operations = sorted(operations, key=lambda x: x.get_priority())

    def calc(self, equation_string: str) -> float:
        equation = equation_string.replace(" ", "")
        element: TreeElement = self._read_equation(equation)
        return element.calc()

    def _read_equation(self, equation: str) -> TreeElement:
        if self._can_delete_outer_brackets(equation):
            equation = equation[1:-1]
        blurred_equation = self._blur_brackets(equation)
        for operation in self.operations:
            opr_symbol = str(operation)
            break_index = blurred_equation.find(opr_symbol)
            if break_index != -1:
                first = equation[:break_index]
                x = self._read_equation(first)
                second = equation[break_index + len(opr_symbol):]
                y = self._read_equation(second)
                return OperationElement(operation, x, y)
        return ValueElement(float(equation))

    @staticmethod
    def _blur_brackets(equation: str) -> str:
        stack = []
        equation_list = list(equation)
        blurred_equation_list = list()
        for letter in equation_list:
            if letter == "(":
                stack.append(letter)
            blurred_equation_list.append("0" if len(stack) else letter)
            if letter == ")":
                stack.pop()
        return "".join(blurred_equation_list)

    @staticmethod
    def _can_delete_outer_brackets(equation: str) -> bool:
        stack = []
        if equation[0] != "(" or equation[-1] != ")":
            return False
        equation = equation[1:-1]
        for letter in equation:
            if letter == "(":
                stack.append(letter)
            elif letter == ")":
                if len(stack) == 0:
                    return False
                else:
                    stack.pop()
        return True


operations_set: Set[Operation] = {Add(), Subtract(), Multiply(), Divide()}
equations_tree: EquationsTree = EquationsTree(operations_set)


def calc(equation: str) -> float:
    return equations_tree.calc(equation)


if __name__ == '__main__':
    result = calc(input("Podaj równanie: "))
    print(f"Wynik: {result}")
