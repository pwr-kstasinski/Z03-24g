import tkinter as tk
import math


class Node:
    def __init__(self, data, leftChild = None, rightChild=None):
        self.left = leftChild
        self.right = rightChild
        self.data = data
    
    def prt(self):
        if(self.left):   self.left.prt()
        print(self.data,end='')
        if(self.right):  self.right.prt()

    def calc(self):
        if(not self.left):      return self.data
        elif(self.data=='+'):   return self.left.calc()+self.right.calc()
        elif(self.data=='-'):   return self.left.calc()-self.right.calc()
        elif(self.data=='*'):   return self.left.calc()*self.right.calc()
        elif(self.data=='/'):   return self.left.calc()/self.right.calc()
        elif(self.data=='%'):   return self.left.calc()%self.right.calc()
        elif(self.data=='^'):   return math.pow(self.left.calc(),self.right.calc())

    def prtTree(self,offset=""):
        if(offset==""):
            print(self.data)
            if(self.left!=None):
                self.left.prtTree("├── ")
                self.right.prtTree("└── ")
        else:                   
            print(offset,self.data,sep='')
            if(self.left!=None):
                if(offset[-4]=='├'):    
                    self.left.prtTree(offset[:-4]+"|   ├── ")
                    self.right.prtTree(offset[:-4]+"|   └── ")
                else:                   
                    self.left.prtTree(offset[:-4]+"    ├── ")
                    self.right.prtTree(offset[:-4]+"    └── ")

def makeNode(postfix):
    stack=[]
    for elem in postfix:
        if((elem=='+') or (elem=='-') or(elem=='*') or(elem=='/') or (elem=='^') or(elem == '%')):
            a=stack.pop()
            b=Node(0)
            if (len(stack)>0):
                b=stack.pop()
            stack.append(Node(elem,b,a))
        else:   stack.append(Node(elem))
    return stack[0]

def infixToPostfix(infix):
    precedance={'+':1,'-':1,'*':2,'/':2,'m':2,'^':3}    #m - mod - modulo
    postfix=[]
    stack=[]
    i=0
    while(i<len(infix)):
        if(infix[i].isdigit()):
            j=i+1
            while((j<len(infix)) and (infix[j].isdigit())):     j+=1
            if((j<len(infix)) and (infix[j]=='.')):     
                j+=1
                while((j<len(infix)) and (infix[j].isdigit())):     j+=1
                postfix.append(float(infix[i:j]))
            else:   postfix.append(int(infix[i:j]))
            i=j-1
        elif(infix[i]=='('):
            stack.append('(')
        elif(infix[i]==')'):
            while(stack[-1]!='('):      postfix.append(stack.pop())
            stack.pop()
        else:
            while((len(stack)>0) and (stack[-1]!='(') and (precedance[stack[-1]]>=precedance[infix[i]])):
                postfix.append(stack.pop())
            if(infix[i]!='m'):
                stack.append(infix[i])
            else:
                stack.append('%')
                i+=2        #mod pominiecie 'mo'
        i+=1
    while(len(stack)>0):        postfix.append(stack.pop())
    return postfix





class CalculatorButton(tk.Button):
    def __init__(self,master, target, text,row,column,command=None):
        super().__init__(master,text=text,command=command)
        self.target=target
        self.text=text
        self["height"]=3
        self["width"]=5
        if (command==None):  
            self["command"]=self.onClick
        self.grid(row=row,column=column)

    def onClick(self):
        self.target["text"] +=self.text


class Gui(tk.Frame):
    def __init__(self, master=tk.Tk()):
        super().__init__(master)
        self.master = master
        self.pack()
        self.buttonLayout=[("=",5,4,self.clickEqual),("c",0,0,self.clickClear),
            ("sqrt",0,1,self.clickSqrt),("|x|",0,2,self.clickAbs),
            ("1/x",0,3,self.clickNegativePower),("n!",1,0,self.clickSilnia),
            ("log",0,4,self.clicklog),("<-",5,0,self.clickBackspace),
            ("0",5,1),("1",2,0),("2",2,1),("3",2,2),("4",3,0),
            ("5",3,1),("6",3,2),("7",4,0),("8",4,1),("9",4,2),
            ("+",5,3),("-",4,3),("*",3,3),("/",2,3),("^",1,3),
            ("mod",1,4),("(",1,1),(")",1,2),(".",5,2)]
        self.create_widgets()

    def create_widgets(self):
        self.history=tk.Label(self,text="")
        self.history.pack(side="top")

        self.display=tk.Label(self,text="")
        self.display.pack(side="top")

        self.buttonMenu=tk.Frame(self)
        self.buttonMenu.pack(side="bottom")

        self.buttons=[]
        for b in self.buttonLayout:
            if(len(b)>3):
                self.buttons.append(CalculatorButton(self.buttonMenu,self.display,b[0],b[1],b[2],b[3]))
            else:
                self.buttons.append(CalculatorButton(self.buttonMenu,self.display,b[0],b[1],b[2]))
        
    def clickEqual(self):
        self.history["text"]=self.display["text"]+"="
        self.display["text"]="{0}".format(makeNode(infixToPostfix(self.display["text"])).calc())
    
    def clickClear(self):
        self.history["text"]=""
        self.display["text"]=""
    
    def clickSqrt(self):
        self.clickEqual()
        self.history["text"]="sqrt("+self.history["text"][:-1]+")="
        self.display["text"]="{0}".format(math.sqrt(float(self.display["text"])))
    
    def clickAbs(self):
        self.clickEqual()
        self.history["text"]="|"+self.history["text"][:-1]+"|="
        if (self.display["text"][0]=='-'):
            self.display["text"]=self.display["text"][1:]

    def clickNegativePower(self):
        self.clickEqual()
        self.history["text"]="("+self.history["text"][:-1]+")^-1="
        self.display["text"]="{0}".format(1/float(self.display["text"]))

    def clickSilnia(self):
        self.clickEqual()
        self.history["text"]="("+self.history["text"][:-1]+")!="
        mul=1
        for i in range(2,math.floor(float(self.display["text"]))+1):
            mul=mul*i
        self.display["text"]="%d"%(mul)

    def clicklog(self):
        self.clickEqual()
        self.history["text"]="log("+self.history["text"][:-1]+")="
        self.display["text"]="{0}".format(math.log10(float(self.display["text"])))

    def clickBackspace(self):
        self.display["text"]=self.display["text"][:-1]


Gui().mainloop()


"""
try:
    while(True):
        rownanie=input("podaj rownanie: ")
        expr=makeNode(infixToPostfix(rownanie))
        expr.prtTree()
        print(rownanie,'=',expr.calc())
except EOFError:
    print("")
"""


"""
t1=makeNode(infixToPostfix("2"))
t1.prtTree()
t1.prt()
print(" =",t1.calc())
t1=makeNode(infixToPostfix("(2)"))
t1.prtTree()
t1.prt()
print(" =",t1.calc())
t1=makeNode(infixToPostfix("2+3"))
t1.prtTree()
t1.prt()
print(" =",t1.calc())
t1=makeNode(infixToPostfix("(2+3)"))
t1.prtTree()
t1.prt()
print(" =",t1.calc())
t1=makeNode(infixToPostfix("(2+3)*4"))
t1.prtTree()
t1.prt()
print(" =",t1.calc())
t1=makeNode(infixToPostfix("3*(4+5)"))
t1.prtTree()
t1.prt()
print(" =",t1.calc())
t1=makeNode(infixToPostfix("(2+3)*(4)"))
t1.prtTree()
t1.prt()
print(" =",t1.calc())
t1=makeNode(infixToPostfix("(3)*(4+5)"))
t1.prtTree()
t1.prt()
print(" =",t1.calc())
t1=makeNode(infixToPostfix("(2+3)*(4/5)"))
t1.prtTree()
t1.prt()
print(" =",t1.calc())
t1=makeNode(infixToPostfix("1+2*3"))
t1.prtTree()
t1.prt()
print(" =",t1.calc())
t1=makeNode(infixToPostfix("0.5*2"))
t1.prtTree()
t1.prt()
print(" =",t1.calc())
print(infixToPostfix("0.5*2"))
t1=makeNode(infixToPostfix("2^2"))
t1.prtTree()
t1.prt()
print(" =",t1.calc())
print(infixToPostfix("2^2"))
"""
