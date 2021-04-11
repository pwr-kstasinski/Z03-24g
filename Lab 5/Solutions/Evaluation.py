import InputProcessing
import math


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

    elif root.data == '^':
        return leftEv ** rightEv

    elif root.data == 'mod':
        return leftEv % rightEv

    elif root.data == '!':
        return math.factorial(leftEv)

    elif root.data == 'abs':
        return abs(leftEv)

    elif root.data == '\u221a':
        return math.sqrt(leftEv)

    elif root.data == 'log':
        return math.log10(leftEv)

    else:
        try:
            temp = leftEv / rightEv
            return temp
        except ZeroDivisionError:
            print("Error during Division.")
            raise SystemExit