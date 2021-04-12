import math
from tkinter import *


class Tree:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):

        if self.right is None and self.left is None:
            line = '%s' % self.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        left, lwidth, lheight, lmiddle = self.left._display_aux()
        right, rwidth, rheight, rmiddle = self.right._display_aux()
        s = '%s' % self.value
        u = len(s)
        first_line = (lmiddle + 1) * ' ' + (lwidth - lmiddle - 1) * '' + s + rmiddle * '' + (rwidth - rmiddle) * ' '
        second_line = lmiddle * ' ' + '/' + (lwidth - lmiddle - 1 + u + rmiddle) * ' ' + '\\' + (
                rwidth - rmiddle - 1) * ' '
        if lheight < rheight:
            left += [lwidth * ' '] * (rheight - lheight)
        elif rheight < lheight:
            right += [rwidth * ' '] * (lheight - rheight)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, lwidth + rwidth + u, max(lheight, rheight) + 2, lwidth + u // 2


def isOperator(c):
    if (c == '+' or c == '-' or c == '*'
            or c == '/' or c == '^' or c == '%'):
        return True
    else:
        return False


def specialOperator(c):
    if c == "!" or c == '√' or c == 'l':
        return True


def isNumber(c):
    if c in "0123456789" or c == ".":
        return True
    else:
        return False


def operatorOrder(c):
    if c == "!":
        return 3
    if c == "^" or c == '√' or c == "l":
        return 2
    elif c == "*" or c == "/" or c == "%":
        return 1
    else:
        return 0


def convertToPostfix(expression):
    result = ""
    tempRes = " "
    space = " "
    stack = []
    topChar = 0

    for element in range(0, len(expression)):
        if expression[element] == space:
            continue
        elif isNumber(expression[element]):
            tempRes += expression[element]
            if element < (len(expression)) - 1:
                if not isNumber(expression[element + 1]):
                    result += tempRes + space
                    tempRes = " "
            else:
                result += tempRes + space
        elif isOperator(expression[element]) or specialOperator(expression[element]):

            while True:

                size = len(stack)
                if size != 0:
                    topChar = stack[size - 1]
                if len(stack) == 0 or topChar == '(':
                    stack.append(expression[element])
                    break
                else:
                    pc = operatorOrder(expression[element])
                    tc = operatorOrder(topChar)

                    if pc > tc:
                        stack.append(expression[element])
                        break
                    else:
                        result += stack.pop()



        elif expression[element] == '(':
            stack.append(expression[element])
        elif expression[element] == ')':
            popped = stack.pop()

            while popped != '(':
                result += popped + space
                popped = stack.pop()

    size = len(stack)
    for i in range(size - 1, -1, -1):
        test = stack[i]
        result += test + space
    return result


def singleOperator(op, x):
    x = float(x)
    if op == "!":
        return math.factorial(x)
    if op == '√':
        return math.sqrt(x)
    if op == 'l':
        return math.log(x, 10)


def constructTree(postfix):
    stack = []
    result = ""

    for element in range(0, len(postfix)):
        if postfix[element] == " ":
            continue

        if not isOperator(postfix[element]) and not specialOperator(postfix[element]):

            result += postfix[element]

            if postfix[element + 1] == " " and not specialOperator(postfix[element + 2]):
                t = Tree(result)
                stack.append(t)
                result = ""
            elif specialOperator(postfix[element + 2]):
                result = singleOperator(postfix[element + 2], result)
                result = str(result)
                counter = element + 4
                while counter < len(postfix):
                    if specialOperator(postfix[counter]):
                        result = singleOperator(postfix[counter], result)
                        result = str(result)
                        counter += 2
                    else:
                        break
                t = Tree(result)
                stack.append(t)
                result = ""

        elif specialOperator(postfix[element]):
            print()
        else:
            temp = postfix[element]
            if element + 2 < len(postfix):
                if specialOperator(postfix[element + 2]):
                    temp = ""
                    temp = postfix[element] + postfix[element + 2]

            t = Tree(temp)
            t1 = stack.pop()
            t2 = stack.pop()

            t.right = t1
            t.left = t2

            stack.append(t)

    t = stack.pop()

    return t


def process(op, x, y):
    if op == '+':
        return x + y
    if op == '-':
        return x - y
    if op == '*':
        return x * y
    if op == '/':
        return x / y
    if op == '^':
        return x ** y
    if op == '%':
        return x % y


def isLeaf(root):
    if root.left == None and root.right == None:
        return True
    else:
        return False


def specialProcessing(op, x, y):
    result = 0.
    for i in range(0, len(op)):
        if not specialOperator(op[i]):
            if op[i] == '+':
                result = x + y
            if op[i] == '-':
                result = x - y
            if op[i] == '*':
                result = x * y
            if op[i] == '/':
                result = x / y
            if op[i] == '^':
                result = x ** y
            if op[i] == '%':
                result = x % y
        else:
            result = singleOperator(op[i], result)
            return result


def count(root):
    if root is None:
        return 0

    if isLeaf(root):
        return float(root.value)

    x = count(root.left)
    y = count(root.right)

    if len(root.value) > 1:
        return specialProcessing(root.value, x, y)
    else:
        return process(root.value, x, y)


expression = ""


def press(num):
    global expression

    expression = expression + str(num)

    equation.set(expression)


def equalPress():
    global expression
    exp = convertToPostfix(expression)
    tree = constructTree(exp)
    result = count(tree)
    equation.set(result)


def dis():

    global expression
    exp = convertToPostfix(expression)
    tree = constructTree(exp)
    tree.display()



def btn_clear():
    global expression
    expression = ""
    equation.set("")

def back():
    global expression
    newExpression = ""
    for char in range(0, len(expression)-1):
        newExpression += expression[char]
    expression = newExpression
    equation.set(expression)

if __name__ == "__main__":

    gui = Tk()


    gui.title("Calculator")

    gui.geometry("312x431")


    equation = StringVar()

    input_frame = Frame(gui, width=312, height=70, bd=0, highlightbackground="black", highlightcolor="black",
                        highlightthickness=1)
    input_frame.pack(side=TOP)

    input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=equation, width=70, bg="#eee", bd=0,
                        justify=RIGHT)
    input_field.grid(row=0, column=0)
    input_field.pack(ipady=10)

    btns_frame = Frame(gui, width=500, height=400, bg="grey")
    btns_frame.pack()

    power = Button(btns_frame, text="x^y", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                   command=lambda: press("^")).grid(row=0, column=0, padx=1, pady=1)
    factorial = Button(btns_frame, text="x!", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                       command=lambda: press("!")).grid(row=0, column=1, padx=1, pady=1)
    sqr = Button(btns_frame, text="sqrt(x)", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                 command=lambda: press("√")).grid(row=0, column=2, padx=1, pady=1)
    backspace = Button(btns_frame, text="<--", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                      command=lambda: back()).grid(row=0, column=3, padx=1, pady=1)

    modulo = Button(btns_frame, text="mod(x)", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                    command=lambda: press("%")).grid(row=1, column=0, padx=1, pady=1)
    reverse = Button(btns_frame, text="1/x", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                     command=lambda: press("1/")).grid(row=1, column=1, padx=1, pady=1)
    log = Button(btns_frame, text="log(x)", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                 command=lambda: press("l")).grid(row=1, column=2, padx=1, pady=1)
    divide = Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                    command=lambda: press("/")).grid(row=1, column=3, padx=1, pady=1)

    seven = Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                   command=lambda: press(7)).grid(row=2, column=0, padx=1, pady=1)
    eight = Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                   command=lambda: press(8)).grid(row=2, column=1, padx=1, pady=1)
    nine = Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                  command=lambda: press(9)).grid(row=2, column=2, padx=1, pady=1)
    multiply = Button(btns_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                      command=lambda: press("*")).grid(row=2, column=3, padx=1, pady=1)

    four = Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                  command=lambda: press(4)).grid(row=3, column=0, padx=1, pady=1)
    five = Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                  command=lambda: press(5)).grid(row=3, column=1, padx=1, pady=1)
    six = Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                 command=lambda: press(6)).grid(row=3, column=2, padx=1, pady=1)
    minus = Button(btns_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                   command=lambda: press("-")).grid(row=3, column=3, padx=1, pady=1)

    one = Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                 command=lambda: press(1)).grid(row=4, column=0, padx=1, pady=1)
    two = Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                 command=lambda: press(2)).grid(row=4, column=1, padx=1, pady=1)
    three = Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                   command=lambda: press(3)).grid(row=4, column=2, padx=1, pady=1)
    plus = Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                  command=lambda: press("+")).grid(row=4, column=3, padx=1, pady=1)

    clear = Button(btns_frame, text="Clear", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                   command=lambda: btn_clear()).grid(row=5, column=0, padx=1, pady=1)
    zero = Button(btns_frame, text="0", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                  command=lambda: press(0)).grid(row=5, column=1, padx=1, pady=1)
    point = Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                   command=lambda: press(".")).grid(row=5, column=2, padx=1, pady=1)
    equals = Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                    command=lambda: equalPress()).grid(row=5, column=3, padx=1, pady=1)

    leftPar = Button(btns_frame, text="(", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                     command=lambda: press("(")).grid(row=6, column=0, padx=1, pady=1)
    rightPar = Button(btns_frame, text=")", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                      command=lambda: press(")")).grid(row=6, column=1, padx=1, pady=1)

    display = Button(btns_frame, text="Display", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                     command=lambda: dis()).grid(row=6, column=2, padx=1, pady=1)
    gui.mainloop()
