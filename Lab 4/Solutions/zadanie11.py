import math as dupa

class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.value = data
tree = Node("")
OPERATORS = set(['+','-','*','/','(',')','^', 'mod','!','sqrt','log','abs'])
PRIORITY = {'+': 1, '-': 1, '*': 2, '/': 2,'^':3,'mod':2, 'sqrt': 4, 'abs': 4, 'log': 4,}
ONEARGUMENTOPERATORS = set(['!','sqrt','log','abs'])
def ToPostfix(exp):

    stack = []
    postfix = []

    for symbol in exp:

        if symbol not in OPERATORS:

            postfix.append(symbol)

        elif symbol == '(':

            stack.append(symbol)

        elif symbol in ONEARGUMENTOPERATORS:

            if symbol == '!':

                postfix.append(symbol)

            else:

                stack.append(symbol)

        elif symbol == ')':

            while stack and stack[-1] != '(':
                postfix.append(stack.pop())

            stack.pop()

        else:
            while  stack and stack[-1] != '(' and PRIORITY[symbol] <= PRIORITY[stack[-1]]:
                postfix.append(stack.pop())

            stack.append(symbol)


    while stack:
        postfix.append(stack.pop())

    return postfix

def ToTree(postfix):

    stack = []

    for symbol in postfix:
        if symbol not in OPERATORS:
            stack.append(Node(symbol))

        else:
            if symbol in ONEARGUMENTOPERATORS:

                temp = Node(symbol)
                temp.left = stack.pop()
                stack.append(temp)

            else:

                temp = Node(symbol)
                temp.right= stack.pop()
                temp.left = stack.pop()
                stack.append(temp)

    return stack.pop()

def Evaluate(root):
    if root is None:
        return 0
    if root.left is None and root.right is  None:
        try:
            temp = float(root.value)
            return temp
        except:
            print("wrong format of exspresion")
            raise SystemExit

    leftVal = Evaluate(root.left)
    rightVal = Evaluate(root.right)

    if root.value == '+':
        return leftVal + rightVal

    elif root.value == '-':
        return leftVal - rightVal

    elif root.value == '*':
        return leftVal * rightVal

    elif root.value == '^':
        return leftVal ** rightVal

    elif root.value == 'mod':
        return leftVal % rightVal

    elif root.value == '!':
        return dupa.factorial(leftVal)

    elif root.value == 'abs':
        return abs(leftVal)

    elif root.value == 'sqrt':
        return dupa.sqrt(leftVal)

    elif root.value == "log":
        return dupa.log10(leftVal)

    else:
        try:
            temp = leftVal/rightVal
            return temp
        except:
            print(" cannot divade by 0")
            raise SystemExit


def printLevelOrder(root):
    h = height(root)
    for i in range(1, h + 1):
        printGivenLevel(root, i)
        print()


def printGivenLevel(root, level):

    if root is None:
        return root
    if level == 1:
        print(root.value, end = ' ')
    elif level > 1:
        printGivenLevel(root.left, level - 1)
        printGivenLevel(root.right, level - 1)


def height(node):
    if node is None:
        return 0
    else:
        lh = height(node.left)
        rh = height(node.right)
        if lh > rh:
            return lh + 1
        else:
            return rh + 1

def menu():
    result = 0
    while result not in range(1,4):
        print("Options:")
        print("1. calculate")
        print("2. make a tree")
        print("3. quit")
        result = int(input())

    return result
def start():
    print("give me expression:")
    exp = input("separate operators and operands with space")
    exp = exp.split(" ")

    if len(exp) > 1:
        temp = ToPostfix(exp)
        print(temp)
        tree=ToTree(ToPostfix(exp))
        printLevelOrder(tree)
        while True:
            temp = menu()
            if temp == 1:
                print(Evaluate(tree))
            elif temp ==2:
                printLevelOrder(tree)
            else:
                raise SystemExit

start()
