from tkinter import *
from graphviz import Source
import MyDreamIsToSeeATree


root = Tk()
root.title("Calculator")
calc = Frame(root)
calc.grid()

txtDisplay = Entry(calc, font =('Comic Sans MS', 20, 'bold'), bg = "#FA8072", bd=20, width=28, justify=RIGHT)
txtDisplay.grid(row = 0, column = 0, columnspan = 4, pady = 1)
txtDisplay.insert(0,"0")


def presentTree():
    MyDreamIsToSeeATree.ourGlouriousTreeOfLife.to_graphviz('dupa')
    s = Source.from_file(filename='dupa')
    s.view()

def GimmeYourSoul():
    temp = txtDisplay.get()
    txtDisplay.delete(0,END)
    return temp

def CheckMeTemp(temp):
    if len(temp) == 1 and temp == '0' :
        return TRUE
    else:
        return FALSE

# destroyer
def DestroyMeText():
    txtDisplay.delete(0,END)
    txtDisplay.insert(0, '0')
    MyDreamIsToSeeATree.stringOExpression[0] = ''


btnCE = (Button(calc,width = 6, height=2, font =('Comic Sans MS', 20, 'bold')
                , bg = "#FA8072",  bd=4,text = "CE", command = lambda:DestroyMeText())).grid(row=1,column=0,pady=1)


#  Numeric buttons and enabletor of the real numbers
def NumberCreator(value):
    temp = GimmeYourSoul()
    if CheckMeTemp(temp):
        txtDisplay.insert(0, str(value))
        MyDreamIsToSeeATree.stringOExpression[0] = str(value)

    else:
        txtDisplay.insert(0,temp + str(value))
        MyDreamIsToSeeATree.addToString(str(value))


btn0 = (Button(calc,width = 6, height=2, font =('Comic Sans MS', 20, 'bold')
               ,  bd=4,text = "0", command = lambda: NumberCreator(0))).grid(row=7,column=1,pady=1)
btn1 = (Button(calc,width = 6, height=2, font =('Comic Sans MS', 20, 'bold')
               ,  bd=4,text = "1", command = lambda: NumberCreator(1))).grid(row=6,column=0,pady=1)
btn2 = (Button(calc,width = 6, height=2, font =('Comic Sans MS', 20, 'bold')
               ,  bd=4,text = "2", command = lambda: NumberCreator(2))).grid(row=6,column=1,pady=1)
btn3 = (Button(calc,width = 6, height=2, font =('Comic Sans MS', 20, 'bold')
               ,  bd=4,text = "3", command = lambda: NumberCreator(3))).grid(row=6,column=2,pady=1)
btn4 = (Button(calc,width = 6, height=2, font =('Comic Sans MS', 20, 'bold')
               ,  bd=4,text = "4", command = lambda: NumberCreator(4))).grid(row=5,column=0,pady=1)
btn5 = (Button(calc,width = 6, height=2, font =('Comic Sans MS', 20, 'bold')
               ,  bd=4,text = "5", command = lambda: NumberCreator(5))).grid(row=5,column=1,pady=1)
btn6 = (Button(calc,width = 6, height=2, font =('Comic Sans MS', 20, 'bold')
               ,  bd=4,text = "6", command = lambda: NumberCreator(6))).grid(row=5,column=2,pady=1)
btn7 = (Button(calc,width = 6, height=2, font =('Comic Sans MS', 20, 'bold')
               ,  bd=4,text = "7", command = lambda: NumberCreator(7))).grid(row=4,column=0,pady=1)
btn8 = (Button(calc,width = 6, height=2, font =('Comic Sans MS', 20, 'bold')
               ,  bd=4,text = "8", command = lambda: NumberCreator(8))).grid(row=4,column=1,pady=1)
btn9 = (Button(calc,width = 6, height=2, font =('Comic Sans MS', 20, 'bold')
               ,  bd=4,text = "9", command = lambda: NumberCreator(9))).grid(row=4,column=2,pady=1)


def IsThisDotNetReference(value):
    temp = GimmeYourSoul()
    txtDisplay.insert(0, temp + value)
    if CheckMeTemp(temp):
        MyDreamIsToSeeATree.addToString('0' + str(value))
    else:
        MyDreamIsToSeeATree.addToString(str(value))

btnDot = (Button(calc,width = 6, height=2, font =('Comic Sans MS', 20, 'bold')
                 , bg = "#FA8072",  bd=4,text = ".", command = lambda:IsThisDotNetReference('.'))).grid(row=7,column=2,pady=1)

def OpenMeMiniExp(value):
    temp = GimmeYourSoul()
    if CheckMeTemp(temp):
        txtDisplay.insert(0, str(value))
        MyDreamIsToSeeATree.stringOExpression[0] = str(value) + ' '
    else:
        txtDisplay.insert(0, temp + str(value))
        MyDreamIsToSeeATree.addToString(str(value) + ' ')

def CloseMeMiniExp(value):
    temp = GimmeYourSoul()
    txtDisplay.insert(0, temp + str(value))
    MyDreamIsToSeeATree.addToString(' ' + str(value))

btnOpen = (Button(calc,width = 6, height=2, font =('Comic Sans MS', 20, 'bold')
                  , bg = "#FA8072",  bd=4,text = "(", command = lambda : OpenMeMiniExp('('))).grid(row=3,column=0,pady=1)
btnClose = (Button(calc,width = 6, height=2, font =('Comic Sans MS', 20, 'bold')
                   , bg = "#FA8072",  bd=4,text = ")", command = lambda : CloseMeMiniExp(')'))).grid(row=3,column=1,pady=1)

def IAmInNeedOfResult():
    if MyDreamIsToSeeATree.stringOExpression[0] == '':
        MyDreamIsToSeeATree.stringOExpression[0] = txtDisplay.get()

    MyDreamIsToSeeATree.eradicateCurrentGraph()
    exp = MyDreamIsToSeeATree.stringOExpression[0].split(' ')
    exptree = MyDreamIsToSeeATree.ToTree(MyDreamIsToSeeATree.ToPostfix(exp))
    result = MyDreamIsToSeeATree.Evaluate(exptree)
    txtDisplay.delete(0, END)
    txtDisplay.insert(0, result)
    MyDreamIsToSeeATree.stringOExpression[0] = str(result)

btnEq = (Button(calc,width = 6, height=2, font =('Comic Sans MS', 20, 'bold')
                , bg = "#FA8072",  bd=4,text = "=", command = lambda :IAmInNeedOfResult())).grid(row=7,column=3,pady=1)

def WeAreTheBasicGangMate(value):
    temp = GimmeYourSoul()
    txtDisplay.insert(0,temp +  str(value))
    if CheckMeTemp(temp):
        MyDreamIsToSeeATree.stringOExpression[0] =' ' + str(value) + ' '
    else:
        MyDreamIsToSeeATree.addToString(' ' + str(value) + ' ')


btnPlus = (Button(calc,width = 6, height=2, font =('Comic Sans MS', 20, 'bold')
                  , bg = "#FA8072",  bd=4,text = "+", command = lambda :WeAreTheBasicGangMate('+'))).grid(row=6,column=3,pady=1)
btnMinus = (Button(calc,width = 6, height=2, font =('Comic Sans MS', 20, 'bold')
                   , bg = "#FA8072",  bd=4,text = "-", command = lambda :WeAreTheBasicGangMate('-'))).grid(row=5,column=3,pady=1)
btnMult= (Button(calc,width = 6, height=2, font =('Comic Sans MS', 20, 'bold')
                 , bg = "#FA8072",  bd=4,text = "*", command = lambda :WeAreTheBasicGangMate('*'))).grid(row=4,column=3,pady=1)
btnDiv = (Button(calc,width = 6, height=2, font =('Comic Sans MS', 20, 'bold')
                 , bg = "#FA8072",  bd=4,text = "/", command = lambda :WeAreTheBasicGangMate('/'))).grid(row=3,column=3,pady=1)
btnExp = (Button(calc,width = 6, height=2, font =('Comic Sans MS', 20, 'bold')
                 , bg = "#FA8072",  bd=4,text = "x^y", command = lambda :WeAreTheBasicGangMate('^'))).grid(row=2,column=0,pady=1)
btnMod = (Button(calc,width = 6, height=2, font =('Comic Sans MS', 20, 'bold')
                 , bg = "#FA8072",  bd=4,text = "mod(x)",  command = lambda :WeAreTheBasicGangMate('mod ('))).grid(row=2,column=2,pady=1)

def FractaliusOmegalius(value):
    temp = GimmeYourSoul()
    txtDisplay.insert(0, temp + str(value))
    MyDreamIsToSeeATree.addToString(' ' + str(value))

btnFrac = (Button(calc,width = 6, height=2, font =('Comic Sans MS', 20, 'bold')
                  , bg = "#FA8072",  bd=4,text = "n!", command = lambda :FractaliusOmegalius('!'))).grid(row=3,column=2,pady=1)

def NoUCard():
    temp = GimmeYourSoul()
    if CheckMeTemp(temp):
        txtDisplay.insert(0,'1/(')
        MyDreamIsToSeeATree.stringOExpression[0] = ('1 / ( ')
    else:
        txtDisplay.insert(0, temp + '1/(')
        MyDreamIsToSeeATree.addToString('1 / ( ')


btnRev = (Button(calc,width = 6, height=2, font =('Comic Sans MS', 20, 'bold')
                 , bg = "#FA8072",  bd=4,text = "1/x", comman = lambda :NoUCard())).grid(row=7,column=0,pady=1)

def WeAreToImpotentToHaveTwoOperands(value):
    temp = GimmeYourSoul()
    if CheckMeTemp(temp):
        txtDisplay.insert(0, str(value) + '(')
        MyDreamIsToSeeATree.stringOExpression[0] = (str(value) + ' ( ')
    else:
        txtDisplay.insert(0, temp + str(value) + '(')
        MyDreamIsToSeeATree.addToString(str(value) + ' ( ')
btnLog = (Button(calc,width = 6, height=2, font =('Comic Sans MS', 20, 'bold')
                 , bg = "#FA8072",  bd=4,text = "log(x)", command = lambda : WeAreToImpotentToHaveTwoOperands('log'))).grid(row=1,column=3,pady=1)
btnSqrt = (Button(calc,width = 6, height=2, font =('Comic Sans MS', 20, 'bold')
                  , bg = "#FA8072",  bd=4,text = "sqrt(x)", command = lambda : WeAreToImpotentToHaveTwoOperands('sqrt'))).grid(row=2,column=1,pady=1)
btnAbs = (Button(calc,width = 6, height=2, font =('Comic Sans MS', 20, 'bold')
                 , bg = "#FA8072",  bd=4,text = "|x|", command = lambda : WeAreToImpotentToHaveTwoOperands('abs'))).grid(row=2,column=3,pady=1)


btnTree = (Button(calc,width = 13, height=2, font =('Comic Sans MS', 20, 'bold')
                  , bg = "#FA8072",  bd=4,text = "Make a tree", command = lambda:presentTree())).grid(row=1,column=1,columnspan =2,pady=1)

root.mainloop()



