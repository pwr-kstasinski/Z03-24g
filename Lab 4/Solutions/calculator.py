from tree_elements import *


class Calculator:
    def __init__(self, operations: Optional[Set[Operation]] = None):
        self.operations = operations
        self.equation_tree: Optional[EquationTree] = None

    def read(self) -> None:
        if self.operations is None:
            raise AttributeError("operations set not found")
        else:
            self._read()

    def calc(self) -> None:
        if self.equation_tree is None:
            raise AttributeError("equation not found")
        elif self.operations is None:
            raise AttributeError("operations set not found")
        else:
            self._calc()

    def print(self) -> None:
        if self.equation_tree is None:
            raise AttributeError("equation not found")
        elif self.operations is None:
            raise AttributeError("operations set not found")
        else:
            self._print()

    def _read(self) -> None:
        raise NotImplementedError

    def _calc(self) -> None:
        raise NotImplementedError

    def _print(self) -> None:
        raise NotImplementedError


class ConsoleCalculator(Calculator):
    def __init__(self, operations: Set[Operation]):
        super().__init__(operations)

    def _read(self) -> None:
        self.equation_tree = EquationTree(self.operations)
        equation = input("Podaj równanie: ")
        self.equation_tree.read(equation)

    def _calc(self) -> None:
        result = self.equation_tree.calc()
        print(f"Wynik: {result}")

    def _print(self) -> None:
        print(self.equation_tree)


operations_set: Set[Operation] = {Add(), Subtract(), Multiply(), Divide()}

if __name__ == '__main__':
    calculator = ConsoleCalculator(operations_set)
    calculator.read()
    calculator.print()
    calculator.calc()
