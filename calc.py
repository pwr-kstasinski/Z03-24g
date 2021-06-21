from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import math
import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def new_node(elem, lista_node):
    if elem in operators:
        tmp = Node(elem)
        tmp.right = lista_node.pop()
        tmp.left = lista_node.pop()
        lista_node.append(tmp)

operators = ['+', '-', '/', '*']
priority = {'+': 1, '-': 1, '/': 2, '*': 2, '(': 0}

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







root = Tk() 
root.title("Calculator")

bttn_list = [
"7", "8", "9", "+", "*", 
"4", "5", "6", "-", "/",
"1", "2", "3",  "=", "xⁿ",
"0", ".",  "C","Exit",
"(", ")","n!","√2",
"1/x","|x|","mod","log(x)"]

r = 2
c = 0
for i in bttn_list:
    rel = ""
    cmd=lambda x=i: calc(x)
    ttk.Button(root, text=i, command = cmd, width = 20).grid(row=r, column = c)
    c += 1
    if c > 4:
        c = 0
        r += 1

calc_entry = Entry(root, width = 30)
calc_entry2 = Entry(root, width = 30)
calc_entry.grid(row=0, column=0, columnspan=2)
calc_entry2.grid(row=1, column=0, columnspan=2)


def calc(key):
    global memory
    if key == "=":

        try:
            calc_entry2.delete(0, END)
            if '**' or ' % ' in calc_entry.get():
                res = eval(calc_entry.get())
            else:
                tree = make_tree(calc_entry.get())
                res=str(calculate(tree))
            calc_entry2.insert(END,  res)
        except:
            calc_entry2.insert(END, "Error!")
            messagebox.showerror("Error!", "Check the correctness of data")
    elif key in "1234567890":
        calc_entry.insert(END, str(key))
    elif key == ".":
        calc_entry.insert(END, ".")
    elif key in "/*+-":
         calc_entry.insert(END, " " +str(key)+" ")
    elif key == "C":
        calc_entry.delete(0, END)
        calc_entry2.delete(0, END)
    elif key == "xⁿ":
        calc_entry.insert(END, "**")
    elif key in "()":
        calc_entry.insert(END, " "+str(key)+" ")
    elif key == "mod":
        calc_entry.insert(END, " % ")
    elif key == "|x|":
        calc_entry2.delete(0, END)
        calc_entry2.insert(END, str(math.fabs(eval(calc_entry.get()))))
    elif key == "log(x)":
        calc_entry2.delete(0, END)
        calc_entry2.insert(END, str(math.log10(int(calc_entry.get()))))
    elif key == "√2":
        calc_entry2.delete(0, END)
        calc_entry2.insert(END, str(math.sqrt(int(calc_entry.get()))))
    elif key == "n!":
        calc_entry2.delete(0, END)
        calc_entry2.insert(END, str(math.factorial(int(calc_entry.get()))))
    elif key == "1/x":
        calc_entry2.delete(0, END)
        calc_entry2.insert(END, str(1/(int(calc_entry.get()))))
    root.mainloop()

    

