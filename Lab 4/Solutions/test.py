import unittest

from parameterized import parameterized

from calculator import *


class TestCalcEquationWithoutBrackets(unittest.TestCase):
    @parameterized.expand([
        ["2", 2.0],
        [" 2 ", 2.0],
        ["2.0", 2.0],
        [" 2.0 ", 2.0],
        [" 1.3 ", 1.3]
    ])
    def test_number(self, equation: str, expecting: float):
        self.assertAlmostEqual(expecting, calc(equation), 3)

    @parameterized.expand([
        ["2+3", 5.0],
        ["2.0+3.0", 5.0],
        ["2-3", -1.0],
        ["2.0-3.0", -1.0],
        ["2*3", 6.0],
        ["2.0*3.0", 6.0],
        ["6/3", 2.0],
        ["6.0/3.0", 2.0],
        ["3.0/2.0", 1.5],
    ])
    def test_simple_equation(self, equation: str, expecting: float):
        self.assertAlmostEqual(expecting, calc(equation), 3)

    @parameterized.expand([
        ["1+2*3", 7.0],
        ["2*3+1", 7.0],
        ["2-6/2", -1.0],
    ])
    def test_double_equation(self, equation: str, expecting: float):
        self.assertAlmostEqual(expecting, calc(equation), 3)


class TestCalcEquationWithBrackets(unittest.TestCase):
    @parameterized.expand([
        ["(1)", 1.0],
        ["(1+2)", 3.0],
        ["(2-6)/2", -2.0],
        ["(2*3)+(6/3)", 8.0],
        ["(2*3)/(6/3)", 3.0],
        ["(0-6)/2+2", -1.0],
        ["((2-6)/(2+2))-2*(6/3)", -5.0]
    ])
    def test_bracket_equation(self, equation: str, expecting: float):
        self.assertAlmostEqual(expecting, calc(equation), 3)

    @parameterized.expand([
        ["1(239)", "100000"],
        ["1(3)4(67)8", "1000400008"],
    ])
    def test_blur_brackets(self, equation: str, expecting: str):
        self.assertEqual(expecting, EquationsTree._blur_brackets(equation))

    @parameterized.expand([
        ["(2)", True],
        ["(2*3)", True],
        ["(2*3)+6", False],
        ["(2*3)+(6/3)", False],
        ["(2*3)+(6/3)+(2+7)", False],
        ["((2*3)+(6/3))", True],
    ])
    def test_can_delete_brackets_brackets(self, equation: str, expecting: bool):
        self.assertEqual(expecting, EquationsTree._can_delete_outer_brackets(equation))


class TestOperations(unittest.TestCase):
    @parameterized.expand([
        [Add(), ValueElement(2.0), ValueElement(3.0), 5.0],
        [Subtract(), ValueElement(2.0), ValueElement(3.0), -1.0],
        [Multiply(), ValueElement(2.0), ValueElement(3.0), 6.0],
        [Divide(), ValueElement(6.0), ValueElement(3.0), 2.0]
    ])
    def test_calc(self, operation: Operation, x: TreeElement, y: TreeElement, expecting: float):
        operation_element = OperationElement(operation, x, y)
        self.assertAlmostEqual(expecting, operation_element.calc(), 3)

    @parameterized.expand([
        [Add(), "+"],
        [Subtract(), "-"],
        [Multiply(), "*"],
        [Divide(), "/"]
    ])
    def test_symbol(self, operation: Operation, expecting: str):
        self.assertEqual(expecting, str(operation))

    @parameterized.expand([
        [Add(), 1],
        [Subtract(), 1],
        [Multiply(), 2],
        [Divide(), 2]
    ])
    def test_priority(self, operation: Operation, expecting: int):
        self.assertEqual(expecting, operation.get_priority())


if __name__ == '__main__':
    unittest.main()
