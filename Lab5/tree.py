from tkinter import *

import math




class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

operators = ['+', '-', '/', '*', '^', '!', 'sqrt', 'log', 'mod']
priority = {'+': 0, '-': 0, '/': 1, '*': 1, '^': 2, 'mod': 3, '!': 3, 'sqrt': 3, 'log': 3, '(': -1, }


def construct_node(elem, postfix):
    if elem in operators:
        tmp = Node(elem)
        tmp.right = postfix.pop()
        if elem != '!' and elem != 'sqrt' and elem != 'log' and elem != '||':
            tmp.left = postfix.pop()

        postfix.append(tmp)

def create_tree(lista):
    
    list_operators = []
    new_list = []

    lista.insert(0, '(')
    lista.append(')')

    for ch in lista:
        if ch == '(':
            list_operators.append(ch)
        elif ch == ')':
            while list_operators[-1] != '(':
                construct_node(list_operators.pop(), new_list)
            list_operators.pop()

        elif ch in operators:
            while priority[ch] <= priority[str(list_operators[-1])]:
                construct_node(list_operators.pop(), new_list)
            list_operators.append(ch)
        else:
            new_list.append(Node(ch))

    for e in list_operators:
        construct_node(e, new_list)

    return new_list[0]

def post_order_traveller(root, lista):
    if root is not None:
        post_order_traveller(root.left, lista)
        post_order_traveller(root.right, lista)

        operation = root.value
        if operation in operators:
            if operation == "+":
                lista.append(float(lista.pop()) + float(lista.pop()))
            elif operation == "-":
                lista.append(-float(lista.pop()) + float(lista.pop()))
            elif operation == "*":
                lista.append(float(lista.pop()) * float(lista.pop()))
            elif operation == "/":
                e1 = float(lista.pop())
                e2 = float(lista.pop())
                lista.append(e2/e1)
            elif operation == "mod":
                e1 = float(lista.pop())
                e2 = float(lista.pop())
                lista.append(e2 % e1)
            elif operation == "^":
                e1 = float(lista.pop())
                e2 = float(lista.pop())
                lista.append(pow(e2, e1))
            elif operation == "!":
                lista.append(math.factorial(float(lista.pop())))
            elif operation == "sqrt":
                lista.append(math.sqrt(float(lista.pop())))
            elif operation == "log":
                lista.append(math.log(float(lista.pop()), 10))
        else:
            lista.append(operation)

def calculate(root):
    result = []
    post_order_traveller(root, result)
    return result[0]

