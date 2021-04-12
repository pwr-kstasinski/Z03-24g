import tkinter as tk
from sya import parse,OPDICT as opdict
from treelib import Tree
from graphviz import Source
import os

class Gui:
    ExpressionInput = None
    ResultOutput = None
    def __init__(self, root):
        root.title("Calculator")
        width=330
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.ExpressionInput = tk.Entry(root)
        self.ExpressionInput["borderwidth"] = "1px"
        self.ExpressionInput["justify"] = "center"
        self.ExpressionInput["text"] = ""
        self.ExpressionInput.place(x=10,y=10,width=310,height=30)
		
        self.ResultOutput=tk.Label(root)
        self.ResultOutput["justify"] = "center"
        self.ResultOutput["text"] = "= ?"
        self.ResultOutput.place(x=10,y=40,width=310,height=30)
		
        GButton_305=tk.Button(root)
        GButton_305["justify"] = "center"
        GButton_305["text"] = "+"
        GButton_305.place(x=250,y=100,width=70,height=25)
        GButton_305["command"] = lambda: self.appendToInput("+")

        GButton_215=tk.Button(root)
        GButton_215["justify"] = "center"
        GButton_215["text"] = "-"
        GButton_215.place(x=250,y=140,width=70,height=25)
        GButton_215["command"] = lambda: self.appendToInput("-")

        GButton_55=tk.Button(root)
        GButton_55["justify"] = "center"
        GButton_55["text"] = "1"
        GButton_55.place(x=10,y=100,width=70,height=25)
        GButton_55["command"] = lambda: self.appendToInput("1")

        GButton_793=tk.Button(root)
        GButton_793["justify"] = "center"
        GButton_793["text"] = "2"
        GButton_793.place(x=90,y=100,width=70,height=25)
        GButton_793["command"] = lambda: self.appendToInput("2")

        GButton_92=tk.Button(root)
        GButton_92["justify"] = "center"
        GButton_92["text"] = "3"
        GButton_92.place(x=170,y=100,width=70,height=25)
        GButton_92["command"] = lambda: self.appendToInput("3")

        GButton_670=tk.Button(root)
        GButton_670["justify"] = "center"
        GButton_670["text"] = "4"
        GButton_670.place(x=10,y=140,width=70,height=25)
        GButton_670["command"] = lambda: self.appendToInput("4")

        GButton_503=tk.Button(root)
        GButton_503["justify"] = "center"
        GButton_503["text"] = "5"
        GButton_503.place(x=90,y=140,width=70,height=25)
        GButton_503["command"] = lambda: self.appendToInput("5")

        GButton_744=tk.Button(root)
        GButton_744["justify"] = "center"
        GButton_744["text"] = "6"
        GButton_744.place(x=170,y=140,width=70,height=25)
        GButton_744["command"] = lambda: self.appendToInput("6")

        GButton_360=tk.Button(root)
        GButton_360["justify"] = "center"
        GButton_360["text"] = "7"
        GButton_360.place(x=10,y=180,width=70,height=25)
        GButton_360["command"] = lambda: self.appendToInput("7")

        GButton_152=tk.Button(root)
        GButton_152["justify"] = "center"
        GButton_152["text"] = "8"
        GButton_152.place(x=90,y=180,width=70,height=25)
        GButton_152["command"] = lambda: self.appendToInput("8")

        GButton_730=tk.Button(root)
        GButton_730["justify"] = "center"
        GButton_730["text"] = "9"
        GButton_730.place(x=170,y=180,width=70,height=25)
        GButton_730["command"] = lambda: self.appendToInput("9")

        GButton_10=tk.Button(root)
        GButton_10["justify"] = "center"
        GButton_10["text"] = "0"
        GButton_10.place(x=10,y=220,width=70,height=25)
        GButton_10["command"] = lambda: self.appendToInput("0")

        GButton_709=tk.Button(root)
        GButton_709["justify"] = "center"
        GButton_709["text"] = "."
        GButton_709.place(x=90,y=220,width=70,height=25)
        GButton_709["command"] = lambda: self.appendToInput(".")

        GButton_451=tk.Button(root)
        GButton_451["justify"] = "center"
        GButton_451["text"] = "*"
        GButton_451.place(x=250,y=180,width=70,height=25)
        GButton_451["command"] = lambda: self.appendToInput("*")

        GButton_962=tk.Button(root)
        GButton_962["justify"] = "center"
        GButton_962["text"] = "/"
        GButton_962.place(x=250,y=220,width=70,height=25)
        GButton_962["command"] = lambda: self.appendToInput("/")

        GButton_702=tk.Button(root)
        GButton_702["justify"] = "center"
        GButton_702["text"] = "("
        GButton_702.place(x=10,y=260,width=70,height=25)
        GButton_702["command"] = lambda: self.appendToInput("(")

        GButton_177=tk.Button(root)
        GButton_177["justify"] = "center"
        GButton_177["text"] = ")"
        GButton_177.place(x=90,y=260,width=70,height=25)
        GButton_177["command"] = lambda: self.appendToInput(")")

        GButton_3=tk.Button(root)
        GButton_3["justify"] = "center"
        GButton_3["text"] = "%"
        GButton_3.place(x=250,y=260,width=70,height=25)
        GButton_3["command"] = lambda: self.appendToInput("%")

        GButton_746=tk.Button(root)
        GButton_746["justify"] = "center"
        GButton_746["text"] = "="
        GButton_746.place(x=250,y=340,width=70,height=25)
        GButton_746["command"] = self.calculateResult

        GButton_738=tk.Button(root)
        GButton_738["justify"] = "center"
        GButton_738["text"] = "!"
        GButton_738.place(x=170,y=260,width=70,height=25)
        GButton_738["command"] = lambda: self.appendToInput("!")

        GButton_949=tk.Button(root)
        GButton_949["justify"] = "center"
        GButton_949["text"] = "sqrt"
        GButton_949.place(x=170,y=300,width=70,height=25)
        GButton_949["command"] = lambda: self.appendToInput("sqrt(")

        GButton_369=tk.Button(root)
        GButton_369["justify"] = "center"
        GButton_369["text"] = "log"
        GButton_369.place(x=90,y=300,width=70,height=25)
        GButton_369["command"] = lambda: self.appendToInput("log(")

        GButton_655=tk.Button(root)
        GButton_655["justify"] = "center"
        GButton_655["text"] = "|x|"
        GButton_655.place(x=90,y=340,width=70,height=25)
        GButton_655["command"] = lambda: self.appendToInput("abs(")

        GButton_107=tk.Button(root)
        GButton_107["justify"] = "center"
        GButton_107["text"] = "^"
        GButton_107.place(x=250,y=300,width=70,height=25)
        GButton_107["command"] = lambda: self.appendToInput("^")

        GButton_160=tk.Button(root)
        GButton_160["justify"] = "center"
        GButton_160["text"] = "1/x"
        GButton_160.place(x=10,y=340,width=70,height=25)
        GButton_160["command"] = lambda: self.surroundInput("1/(",")")

        GButton_108=tk.Button(root)
        GButton_108["justify"] = "center"
        GButton_108["text"] = "TT"
        GButton_108.place(x=170,y=340,width=70,height=25)
        GButton_108["command"] = self.showTree
    
    def appendToInput(self,arg):
        self.ExpressionInput.insert("end",arg)
    def surroundInput(self,left,right):
        self.ExpressionInput.insert(0,left)
        self.ExpressionInput.insert("end",right)
    def calculateResult(self):
        tree = parse(self.ExpressionInput.get())
        self.ResultOutput["text"]="= {:g}".format(tree.evalAST(opdict))
    def showTree(self):
        tree = parse(self.ExpressionInput.get())
        treelibtree = tree.createTreelibNode(Tree())
        treelibtree.to_graphviz("tree")
        s = Source.from_file(filename="tree")
        os.remove("tree")
        s.view()
    def clearExpression(self):
        self.ExpressionInput.delete(0,'end')
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = Gui(root)
    root.mainloop()
