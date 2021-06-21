#infix to postfix conversion form https://cppsecrets.com/users/2582658986657266505064717765737646677977/INFIX-TO-POSTFIX-CONVERSION-USING-STACK.php

class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


tree = Node("")
OPERATORS = set(['+', '-', '*', '/', '(', ')'])
PRIORITY = {'+': 1, '-': 1, '*': 2, '/': 2}


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

    #print(stack)

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
    print("")


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


def evaluateExpressionTree(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        try:
            temp = float(root.data)
            return temp
        except:
            print("Error during conversion to float. Next time type data correctly!")
            raise SystemExit

    leftEv = evaluateExpressionTree(root.left)
    rightEv = evaluateExpressionTree(root.right)

    if root.data == '+':
        return leftEv + rightEv

    elif root.data == '-':
        return leftEv - rightEv

    elif root.data == '*':
        return leftEv * rightEv

    else:
        try:
            temp = leftEv / rightEv
            return temp
        except ZeroDivisionError:
            print("Error during Division.")
            raise SystemExit


def whatToDo():
    result = -1
    while result < 1 or result > 3:
        print("Enter what you want me to do:")
        print("1. get result")
        print("2. print tree")
        print("3. exit")
        result = int(input())

    return result


def work():
    print("Welcome in Calculator")
    exp = input("Enter expresion(use space to separate brackets, operands and operators)")
    exp = exp.split(" ")

    if len(exp) > 1:
        tree = postfix_to_tree(infix_to_postfix(exp))
        while True:
            temp = whatToDo()
            if temp == 1:
                print(evaluateExpressionTree(tree))

            elif temp == 2:
                printLevelOrder(tree)

            else:
                raise SystemExit



    else:
        print("Next time do what I say.")


work()
