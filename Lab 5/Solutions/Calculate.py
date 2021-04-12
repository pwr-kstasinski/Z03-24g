import math


class Node:

    # Constructor
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


operators = ['+', '-', '/', '*', '^', '!', 'sqrt', 'log', 'mod', 'abs']
order = {'+': 0, '-': 0, '/': 1, '*': 1, '^': 2, 'mod': 1, '!': 2, 'sqrt': 2, 'log': 2, 'abs': 2, '(': -1}


def construct_node(elem, postfix):
    if elem in operators:
        tmp = Node(elem)
        tmp.right = postfix.pop()
        if elem != '!' and elem != 'sqrt' and elem != 'log' and elem != 'abs':
            tmp.left = postfix.pop()

        postfix.append(tmp)


def equation_to_tree(equation):
    elements = equation.split()
    stack = []
    result = []
    elements.insert(0, '(')
    elements.append(')')

    for e in elements:
        if e == '(':
            stack.append(e)
        elif e == ')':
            while stack[-1] != '(':
                construct_node(stack.pop(), result)
            stack.pop()
        elif e in operators:
            while order[e] <= order[str(stack[-1])]:
                construct_node(stack.pop(), result)
            stack.append(e)
        else:
            result.append(Node(e))

    for e in stack:
        construct_node(e, result)

    return result[0]


# traveling tree post order to evaluate tree of expression
def post_order(root, stack):
    if root is not None:
        post_order(root.left, stack)
        post_order(root.right, stack)
        if root.value in operators:
            if root.value == '+':
                stack.append(float(stack.pop()) + float(stack.pop()))
            elif root.value == '-':
                stack.append(-float(stack.pop()) + float(stack.pop()))
            elif root.value == '*':
                stack.append(float(stack.pop()) * float(stack.pop()))
            elif root.value == '/':
                stack.append(1 / float(stack.pop()) * float(stack.pop()))
            elif root.value == 'mod':
                stack.append(float(stack.pop()) % float(stack.pop()))
            elif root.value == '^':
                val1 = float(stack.pop())
                val2 = float(stack.pop())
                stack.append(pow(val2, val1))
            elif root.value == 'log':
                stack.append(math.log(float(stack.pop()), 10))
            elif root.value == 'sqrt':
                stack.append(math.sqrt(float(stack.pop())))
            elif root.value == '!':
                stack.append(math.factorial(float(stack.pop())))
            elif root.value == 'abs':
                stack.append(math.fabs(float(stack.pop())))
        else:
            stack.append(root.value)


# calling post order traversal to calculate tree and returning evaluated value
def evaluate(root):
    if root is None:
        print('So lonely... There\'s no tree to evaluate')
        return 0
    else:
        stack = []
        post_order(root, stack)
        return stack.pop()


def print_generator(root: Node, lvl=0, path='', is_right=False):
    if root is not None:
        for i in range(len(path)-1):
            if path[i] == 'l':
                yield '    '
            elif path[i] == 'r':
                yield '│   '

        if lvl != 0:
            if is_right:
                yield '├───'
            else:
                yield '└───'

        yield '('+str(root.value)+')' + '\n'
        yield from print_generator(root.right, lvl + 1, path + 'r', True)
        yield from print_generator(root.left, lvl + 1, path + 'l', False)


def print_string_return(tree: Node):
    result = ''
    for p in print_generator(tree):
        result = result + p

    return result
