from tkinter import *
from tree import calculate, create_tree
import math

numb = ['0','1','2','3','4','5','6','7','8','9']

class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.build()

    def build(self):
        self.formula = "0"
        self.lbl = Label(text=self.formula, font=("Times New Roman", 21, "bold"), bg="#000", foreground="#FFF")
        self.lbl.place(x=10, y=50)

        btns = [
            "C", "DEL", "^", "sqrt",
            "|x|", "mod", "log", "1/x",
            "(", ")", "!", "=", 
            "1", "2", "3", "/",
            "4", "5", "6", "*",
            "7", "8", "9", "-",
            "", "0", ".", "+"
        ]

        x = 10
        y = 140
        for bt in btns:
            com = lambda x=bt: self.calculate(x)
            Button(text=bt, bg="#FFF",
                   font=("Times New Roman", 15),
                   command=com).place(x=x, y=y,
                                      width=115,
                                      height=50)
            x += 117
            if x > 400:
                x = 10
                y += 55

    def calculate(self, operation):
        if operation == "C":
            self.formula = ""
        elif operation == "DEL":
            self.formula = self.formula[0:-1]
        elif operation == "1/x":
            self.formula = str(1 / float(self.formula))
        elif operation == "|x|":
            self.formula = str(math.fabs((float(self.formula))))

        elif operation == "=":
            listt = self.formula
            lista = list(listt.split())
            tree = create_tree(lista)
            self.formula = str(calculate(tree))
            print(calculate(tree))
            print(lista)
           
        else:
            if self.formula == "0":
                self.formula = ""
            if operation in numb or operation == ".":
                self.formula += operation
            else:
                self.formula +=" "
                self.formula += operation
                self.formula +=" "
        self.update()

    def update(self):
        if self.formula == "":
            self.formula = "0"
        self.lbl.configure(text=self.formula)


if __name__ == '__main__':
    root = Tk()
    root["bg"] = "#000"
    root.geometry("485x550")
    root.title("Calculator")
    root.resizable(False, False)
    app = Main(root)
    root.mainloop()