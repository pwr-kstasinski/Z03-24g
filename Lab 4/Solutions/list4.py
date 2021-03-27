#infix to postfix conversion form https://cppsecrets.com/users/2582658986657266505064717765737646677977/INFIX-TO-POSTFIX-CONVERSION-USING-STACK.php


OPERATORS = set(['+', '-', '*', '/', '(', ')'])
PRIORITY = {'+': 1, '-': 1, '*': 2, '/': 2}

class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

def infix_to_postfix(expression):

    stack = []
    postfix = []

    for ch in expression:

        if ch not in OPERATORS:

            postfix.append(ch)

        elif ch == '(':

            stack.append('(')

        elif ch == ')':

            while stack and stack[-1] != '(':
                postfix.append(stack.pop())

            stack.pop()

        else:
            while stack and stack[-1] != '(' and PRIORITY[ch] <= PRIORITY[stack[-1]]:
                postfix.append(stack.pop())

            stack.append(ch)

    print(stack)

    while stack:
        postfix.append(stack.pop())

    return postfix


def postfix_to_tree(postfix):
    stack = []

    for ch in postfix:
        if ch not in OPERATORS:
          stack.append(Node(ch))

        else:
            print()
            temp = Node(ch)
            temp.right = stack.pop()
            temp.left = stack.pop()
            stack.append(temp)

    return  stack.pop()


def printLevelOrder(root):
    h = height(root)

    for i in range(h):
        helperPrintLevelOrder(root, i+1)


def helperPrintLevelOrder(root, level):
    if root is None:
        return
    if level == 1:
        print(root.data, end=" ")
    elif level > 1:
        helperPrintLevelOrder(root.left, level - 1)
        helperPrintLevelOrder(root.right, level - 1)


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


def work():
    print("Welcome in Calculator")
    exp=input("Enter expresion(use space to separate brackets, operands and operators)")
    exp = exp.split(" ")
    print(exp)
    if len(exp) > 1:
        print("supa")
        temp = infix_to_postfix(exp)
        print(temp)
        printLevelOrder(postfix_to_tree(temp))

    else:
        print("next time do what I say")






work()
