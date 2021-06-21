from treelib import Node, Tree
import math

ourGlouriousTreeOfLife = Tree()
stringOExpression = [""]

def eradicateCurrentGraph():
    global ourGlouriousTreeOfLife
    ourGlouriousTreeOfLife=Tree()

def createGraph(root):
    global  ourGlouriousTreeOfLife
    if root is not None:
        ourGlouriousTreeOfLife.create_node(str(root.value),root)

        populateTheGraph(root,root.left)
        populateTheGraph(root, root.right)

def populateTheGraph(parent, child):
    global ourGlouriousTreeOfLife
    if child is not None:
        ourGlouriousTreeOfLife.create_node(str(child.value), child, parent=parent)
        populateTheGraph(child, child.left)
        populateTheGraph(child, child.right)

def addToString(value):
    stringOExpression[0] = stringOExpression[0] + str(value)

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

    t = stack.pop()
    createGraph(t)
    return t



def Evaluate(root):

    if root is None:
        return 0

    if root.left is None and root.right is None:
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
        return math.factorial(leftVal)

    elif root.value == 'abs':
        return abs(leftVal)

    elif root.value == 'sqrt':
        return math.sqrt(leftVal)

    elif root.value == "log":
        return math.log10(leftVal)

    else:
        try:
            temp = leftVal/rightVal
            return temp
        except:
            print(" cannot divade by 0")
            raise SystemExit