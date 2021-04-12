from graphviz import Graph
from BinaryTree import BinaryTree as binaryTree
import math


def is_binary_operator(operator):
    return operator in ['+', '-', '*', '/', '^', "mod"]


class BetterEquation:
    def __init__(self, equation):
        self.equation = equation
        self.infix = equation.split()
        self.postfix = []
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, "abs": 3, '^': 3, "sqrt": 3, "mod": 3, "log": 3}
        self.tree = None

    def convert_infix_to_postfix(self):
        stack = []
        for x in self.infix:
            if x[0].isdigit():
                self.postfix.append(x)
            elif x == '(':
                stack.append(x)
            elif x == ')':
                while stack and stack[-1] != '(':
                    self.postfix.append(stack.pop())
                if not stack and stack[-1] != '(':
                    return -1
                else:
                    stack.pop()

            else:
                while stack and stack[-1] != '(' and self.precedence.get(x) <= self.precedence.get(stack[-1]):
                    self.postfix.append(stack.pop())
                stack.append(x)
        while stack:
            self.postfix.append(stack.pop())

    def convert_postfix_to_binarytree(self):
        stack = []
        for x in self.postfix:
            if is_binary_operator(x):
                t = binaryTree(x)
                t.right = stack.pop()
                t.left = stack.pop()
                stack.append(t)
            elif not x[0].isdigit():
                t = binaryTree(x)
                t.left = stack.pop()
                t.right = None
                stack.append(t)
            else:
                stack.append(binaryTree(float(x)))
        self.tree = stack.pop()


def inorder(tree):
    if tree is not None:
        inorder(tree.left)
        inorder(tree.right)
        print(tree.value, end=' ')


def evaluate_tree(tree):
    if tree is None:
        return 0
    if tree.left is None and tree.right is None:
        return tree.value
    left_value = evaluate_tree(tree.left)
    right_value = evaluate_tree(tree.right)

    if tree.value == '+':
        return left_value + right_value
    elif tree.value == '-':
        return left_value - right_value
    elif tree.value == '*':
        return left_value * right_value
    elif tree.value == '/':
        return left_value / right_value
    elif tree.value == '^':
        return left_value ** right_value
    elif tree.value == "mod":
        return math.fmod(left_value, right_value)
    elif tree.value == "sqrt":
        return math.sqrt(left_value)
    elif tree.value == "abs":
        return math.fabs(left_value)
    elif tree.value == "log":
        return math.log(left_value)


def calculate(expression):
    b = BetterEquation(expression)
    try:
        b.convert_infix_to_postfix()
    except TypeError:
        return "Error"
    try:
        b.convert_postfix_to_binarytree()
    except (IndexError, ValueError):
        return "Wrong usage of operators"
    try:
        result = evaluate_tree(b.tree)
    except ValueError:
        return "Function argument error"
    if math.modf(result)[0] == 0:
        result = math.trunc(result)
    visualize_tree(b.tree)
    return result


def tree_depth(tree):
    if tree is None:
        return 0
    else:
        return max(tree_depth(tree.left), tree_depth(tree.right)) + 1


def visualize_tree(tree):
    def add_nodes_edges(tree, dot=None):
        if dot is None:
            dot = Graph()
            dot.node(name=str(tree), label=str(tree.value))

        if tree.left:
            dot.node(name=str(tree.left), label=str(tree.left.value))
            dot.edge(str(tree), str(tree.left))
            dot = add_nodes_edges(tree.left, dot=dot)

        if tree.right:
            dot.node(name=str(tree.right), label=str(tree.right.value))
            dot.edge(str(tree), str(tree.right))
            dot = add_nodes_edges(tree.right, dot=dot)

        return dot

    dot = add_nodes_edges(tree)
    dot.format = 'png'
    dot.render('img', view=True)
