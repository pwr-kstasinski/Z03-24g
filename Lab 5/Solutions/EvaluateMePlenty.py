import math
import MyDreamIsToSeeATree

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