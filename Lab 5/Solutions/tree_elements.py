import math
from typing import Set, Optional, List

from operations import *
from functions import *


class TreeElement:
    def calc(self) -> float:
        raise NotImplementedError


class ValueElement(TreeElement):
    def __init__(self, value: float):
        self.value = value

    def calc(self) -> float:
        return self.value

    def __str__(self):
        return str(self.value)


class OperationElement(TreeElement):
    def __init__(self, operation: Operation, x: TreeElement, y: TreeElement):
        self.x = x
        self.y = y
        self.operation = operation

    def calc(self) -> float:
        return self.operation.calc(self.x.calc(), self.y.calc())

    def __str__(self):
        return f"{self.x} {self.operation} {self.y}"


class FunctionElement(TreeElement):
    def __init__(self, function: Function, x: TreeElement):
        self.function = function
        self.x = x

    def calc(self) -> float:
        return self.function.calc(self.x.calc())


class EquationTree:
    def __init__(self, operations: Set[Operation], functions: Set[Function]):
        self.functions: List[Function] = list(functions)
        self.operations: List[List[Operation]] = self._transform_operations(operations)
        self._root: Optional[TreeElement] = None

    @staticmethod
    def _transform_operations(operations) -> List[List[Operation]]:
        transformed = []
        operations_dict = dict()
        for operation in operations:
            priority = operation.get_priority()
            if priority not in operations_dict:
                operations_dict[priority] = []
            operations_dict[priority].append(operation)
        for key in sorted(operations_dict.keys()):
            transformed.append(operations_dict[key])
        return transformed

    def read(self, equation: str) -> None:
        equation = equation.replace(" ", "")
        self._root = self._read_equation(equation)

    def calc(self) -> float:
        if self._root is not None:
            return self._root.calc()
        else:
            raise AttributeError("equation not found")

    def _read_equation(self, equation: str) -> TreeElement:
        blurred_equation = self._blur_functions(equation)
        for same_priority_operations in self.operations:
            break_index, operation = self.get_break_index_with_operation(blurred_equation, same_priority_operations)
            if break_index != -1:
                first = equation[:break_index]
                second = equation[break_index + len(str(operation)):]
                x = self._read_equation(first)
                y = self._read_equation(second)
                return OperationElement(operation, x, y)
        for function in self.functions:
            if function.check(equation):
                return FunctionElement(function, self._read_equation(function.edit(equation)))
        return ValueElement(float(equation))

    @staticmethod
    def get_break_index_with_operation(blurred_equation, same_priority_operations) -> (int, Operation):
        break_indexes_with_operations = []
        for operation in same_priority_operations:
            break_indexes_with_operations.append((blurred_equation.rfind(str(operation)), operation))
        break_index, operation = max(break_indexes_with_operations, key=lambda i: i[0])
        return break_index, operation

    @staticmethod
    def _blur_functions(equation: str) -> str:
        counter = 0
        equation_list = list(equation)
        blurred_equation_list = list()
        for letter in equation_list:
            if letter == "(":
                counter += 1
            blurred_equation_list.append("0" if counter else letter)
            if letter == ")":
                counter -= 1
        return "".join(blurred_equation_list)

    def equation_is_read(self) -> bool:
        return self._root is not None
