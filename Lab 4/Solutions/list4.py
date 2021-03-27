#infix to postfix conversion form https://cppsecrets.com/users/2582658986657266505064717765737646677977/INFIX-TO-POSTFIX-CONVERSION-USING-STACK.php


OPERATORS = set(['+', '-', '*', '/', '(', ')', '^'])
PRIORITY = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}


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
    print("")
    



def work():
    print("Welcome in Calculator")
    exp=input("Enter expresion(use space to separate brackets, operands and operators)")
    exp = exp.split(" ")
    print(exp)
    if len(exp) > 1:
        print("supa")
        print(infix_to_postfix(exp))

    else:
        print("next time do what I say")






work()
