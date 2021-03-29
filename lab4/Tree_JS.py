import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


operators = ['+', '-', '/', '*']
priority = {'+': 1, '-': 1, '/': 2, '*': 2, '(': 0}

def new_node(elem, lista_node):
    if elem in operators:
        tmp = Node(elem)
        tmp.right = lista_node.pop()
        tmp.left = lista_node.pop()
        lista_node.append(tmp)


def make_tree(dane):
    dane_array = dane.split()
    lista_oper = []
    lista_node = []

    dane_array.insert(0, '(')
    dane_array.append(')')

    for ch in dane_array:
        if ch == '(':
            lista_oper.append(ch)
        elif ch == ')':
            while lista_oper[-1] != '(':
                new_node(lista_oper.pop(), lista_node)
            lista_oper.pop()
        elif ch in operators:
            while priority[ch] <= priority[str(lista_oper[-1])]:
                new_node(lista_oper.pop(), lista_node)
            lista_oper.append(ch)
        else:
            lista_node.append(Node(ch))

    for e in lista_oper:
        new_node(e, lista_node)
    return lista_node[0]





def calculate(root):
    result = []
    calculate_tree(root, result)
    return result[0]


def calculate_tree(root, list):
    if root is not None:
        calculate_tree(root.left, list)
        calculate_tree(root.right, list)
        if root.value in operators:
            if root.value == "+":
                list.append(float(list.pop()) + float(list.pop()))
            if root.value == "-":
                list.append(-float(list.pop()) + float(list.pop()))
            if root.value == "*":
                list.append(float(list.pop()) * float(list.pop()))
            if root.value == "/":
                list.append(1/float(list.pop()) * float(list.pop()))
        else:
            list.append(root.value)




args=sys.argv
tree = make_tree(args[1])
print(args[1]+" = "+str(calculate(tree)))