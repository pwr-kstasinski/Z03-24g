import sys
import os


class Node:

    # Constructor
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


operators = ['+', '-', '/', '*']
order = {'+': 0, '-': 0, '/': 1, '*': 1, '(': -1}


# converting equation to ONP notation
def to_onp(equation: str):
    elements = equation.split()
    stack = []
    result = ''
    elements.insert(0, '(')
    elements.append(')')
    for e in elements:
        if e == '(':
            stack.append('(')
        elif e == ')':
            while stack[-1] != '(':
                result += stack.pop() + ' '
            stack.pop()
        elif e in operators:
            while order[e] <= order[str(stack[-1])]:
                result += stack.pop() + ' '
            stack.append(e)
        else:
            result += e + ' '

    for e in stack:
        result += e + ' '

    return result


# make tree based on ONP notated equation
def make_tree(onp: str):
    stack = []
    elements = onp.split()
    for e in elements:
        if e not in operators:
            stack.append(Node(e))
        else:
            node = Node(e)
            node.left = stack.pop()
            node.right = stack.pop()
            stack.append(node)

    return stack.pop()


# traveling tree post order to evaluate tree of expression
def post_order(root, stack):
    if root is not None:
        post_order(root.left, stack)
        post_order(root.right, stack)
        if root.value in operators:
            if root.value == '+':
                stack.append(float(stack.pop()) + float(stack.pop()))
            if root.value == '-':
                stack.append(float(stack.pop()) - float(stack.pop()))
            if root.value == '*':
                stack.append(float(stack.pop()) * float(stack.pop()))
            if root.value == '/':
                stack.append(1 / float(stack.pop()) * float(stack.pop()))
        else:
            stack.append(root.value)


# calling post order traversal to calculate tree and returning evaluated value
def evaluate(root):
    if root is None:
        print("So lonely... There's no tree to evaluate")
        return 0
    else:
        stack = []
        post_order(root, stack)
        return stack.pop()


def print_tree(root: Node, lvl=0, path='', is_right=False):
    if root is not None:
        for i in range(len(path)-1):
            if path[i] == 'l':
                print('    ', end='')
            elif path[i] == 'r':
                print('│   ', end='')

        if lvl != 0:
            if is_right:
                print('├───', end='')
            else:
                print('└───', end='')

        print('('+str(root.value)+')')
        print_tree(root.right, lvl + 1, path + 'r', True)
        print_tree(root.left, lvl + 1, path + 'l', False)


def main(args):
    if '--help' in args or '-h' in args:
        print_help()
        return
    if args.__len__() == 2:
        print(args[1] + ' = ' + str(evaluate(make_tree(to_onp(args[1])))))
    elif args.__len__() == 1:
        s = input('Equation: ')
        print(' = ' + str(evaluate(make_tree(to_onp(s)))))
    else:
        if '-p' in args:
            tree = make_tree(to_onp(args[2]))
            print_tree(tree)
            print(args[2] + ' = ' + str(evaluate(tree)))
        else:
            print(args[2] + ' = ' + str(evaluate(make_tree(to_onp(args[2])))))


def print_help():
    print(f'\nUsage: {os.path.basename(__file__)} [Options]... "equation"')
    print('Script to evaluate equation including parentheses, every element must be separated by space')
    print('\n   -p      print tree of expression')


if __name__ == "__main__":
    main(sys.argv)
