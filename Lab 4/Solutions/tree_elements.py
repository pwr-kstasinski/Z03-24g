from typing import Set, List, Optional

from operations import *


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
        self.operation = operation
        self.x = x
        self.y = y

    def calc(self) -> float:
        return self.operation.calc(self.x.calc(), self.y.calc())

    def __str__(self):
        return f"({self.x} {self.operation} {str(self.y)})"


class EquationTree:
    def __init__(self, operations: Set[Operation]):
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
        if equation == "":
            return ValueElement(0)
        if self._can_delete_outer_brackets(equation):
            equation = equation[1:-1]
        blurred_equation = self._blur_brackets(equation)
        for same_priority_operations in self.operations:
            break_index, operation = self.get_break_index_with_operation(blurred_equation, same_priority_operations)
            if break_index != -1:
                first = equation[:break_index]
                second = equation[break_index + len(str(operation)):]
                x = self._read_equation(first)
                y = self._read_equation(second)
                return OperationElement(operation, x, y)
        return ValueElement(float(equation))

    @staticmethod
    def get_break_index_with_operation(blurred_equation, same_priority_operations) -> (int, Operation):
        break_indexes_with_operations = []
        for operation in same_priority_operations:
            break_indexes_with_operations.append((blurred_equation.rfind(str(operation)), operation))
        break_index, operation = max(break_indexes_with_operations, key=lambda i: i[0])
        return break_index, operation

    @staticmethod
    def _blur_brackets(equation: str) -> str:
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

    @staticmethod
    def _can_delete_outer_brackets(equation: str) -> bool:
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

    def equation_is_read(self) -> bool:
        return self._root is not None

    def __str__(self):
        if not self.equation_is_read():
            raise AttributeError("equation is not read")
        depth: int = self._get_depth(self._root)
        width: int = (2 ** depth) * 2
        queue: list = [self._root]
        next_queue: list = []
        result = ""
        while len(list(filter(lambda x: x is not None, queue))):
            for element in queue:
                to_add: str = ""
                if isinstance(element, ValueElement):
                    to_add = str(element)
                    next_queue.append(None)
                    next_queue.append(None)
                elif isinstance(element, OperationElement):
                    to_add = str(element.operation)
                    next_queue.append(element.x)
                    next_queue.append(element.y)
                result += to_add.center(width)
            result += "\n" * depth
            depth -= 1
            width //= 2
            queue = next_queue
            next_queue = []
        return result

    def _get_depth(self, tree_element: TreeElement) -> int:
        if isinstance(tree_element, ValueElement):
            return 1
        elif isinstance(tree_element, OperationElement):
            opr_elem: OperationElement = tree_element
            y_depth = self._get_depth(opr_elem.y)
            x_depth = self._get_depth(opr_elem.x)
            return 1 + max(x_depth, y_depth)
