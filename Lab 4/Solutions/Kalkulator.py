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
            or c == '/'):
        return True
    else:
        return False


def isNumber(c):
    if c in "0123456789" or c == ".":
        return True
    else:
        return False


def operatorOrder(c):
    if c == "+" or c == "-":
        return 1
    else:
        return 2


def convertToPostfix(expression):
    result = ""
    tempRes = " "
    space = " "
    stack = []
    topChar = 0
    sameSymbolsCounter = 0
    error = False
    for element in range(0, len(expression)):
        if expression[element] == space:
            continue
        elif isNumber(expression[element]):
            sameSymbolsCounter = 0
            tempRes += expression[element]
            if element < (len(expression)) - 1:
                if not isNumber(expression[element + 1]):
                    result += tempRes + space
                    tempRes = " "
            else:
                result += tempRes + space
        elif isOperator(expression[element]):
            if sameSymbolsCounter > 0:
                print("Wrong input - two operators in a row")
                error = True
            sameSymbolsCounter += 1
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
                result += popped
                popped = stack.pop()

    size = len(stack)
    for i in range(size - 1, -1, -1):
        test = stack[i]
        result += test + space
    return result,error



def constructTree(postfix):

    stack = []
    result = ""

    for element in range(0, len(postfix)):
        if postfix[element] == " ":
            continue


        if not isOperator(postfix[element]):

            result += postfix[element]

            if postfix[element + 1] == " ":
                t = Tree(result)
                stack.append(t)
                result = ""


        else:


            t = Tree(postfix[element])
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


def isLeaf(root):
    if root.left == None and root.right == None:
        return True
    else:
        return False


def count(root):
    if root is None:
        return 0

    if isLeaf(root):
        return float(root.value)

    x = count(root.left)
    y = count(root.right)

    return process(root.value, x, y)


def calc():
    while True:

        getUserInput = str(input("Insert calculation or press enter to quit "))
        if getUserInput == "":
            break
        else:
            test, error = convertToPostfix(getUserInput)
            if error:
                break
            else:
                tree = constructTree(test)
                print(f"Result is: {count(tree)}")
                displayTree = str(input("Do you want to see expression tree? [Y/N]"))
                if displayTree.upper() == "Y":
                    tree.display()


if __name__ == '__main__':
    calc()
