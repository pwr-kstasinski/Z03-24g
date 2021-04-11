from treelib import Node, Tree

stringToProcess = [""]
GTree = Tree()


def clearGraph():
    global GTree
    GTree = Tree()


def updateGraph(root):
    global GTree
    if root is not None:
        GTree.create_node(str(root.data), root)

        updateGraphHelper(root, root.left)
        updateGraphHelper(root, root.right)


def updateGraphHelper(parent, child):
    global GTree
    if child is not None:
        GTree.create_node(str(child.data), child, parent=parent)
        updateGraphHelper(child, child.left)
        updateGraphHelper(child, child.right)


def appendStringToProcess(value):
     stringToProcess[0] = stringToProcess[0] + value
     print(str(stringToProcess))


class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


tree = Node("")
OPERATORS = set(['+', '-', '*', '/', '(', ')', '^', 'mod', '!', '\u221a', 'log', 'abs'])
PRIORITY = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, 'mod': 2, '\u221a': 4, 'abs': 4, 'log': 4}
ONEARGUMENTOPERATORS = set(['!', '\u221a', 'log', 'abs'])

def infix_to_postfix(expression):
    stack = []
    postfix = []

    for symbol in expression:

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
            while stack and stack[-1] != '(' and PRIORITY[symbol] <= PRIORITY[stack[-1]]:
                postfix.append(stack.pop())

            stack.append(symbol)

    while stack:
        postfix.append(stack.pop())

    return postfix


def postfix_to_tree(postfix):
    global tree
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
                temp.right = stack.pop()
                temp.left = stack.pop()
                stack.append(temp)

    t = stack.pop()
    updateGraph(t)
    return t


