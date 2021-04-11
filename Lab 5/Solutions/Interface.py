import InputProcessing
import Evaluation
from tkinter import *
from graphviz import Source



root = Tk()
root.title("Calculator")
root.resizable(width=False, height=False)

root.geometry("540x720+0+0")

calc = Frame(root)
calc.grid()

#===============================MENU===================================

def presentTreeAction():
    InputProcessing.GTree.show()
    InputProcessing.GTree.to_graphviz('testy')
    s = Source.from_file(filename='testy')
    s.view()


menubar = Menu(calc)

treeMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Tree", menu=treeMenu)
treeMenu.add_command(label="Present Evaluation Tree", command=presentTreeAction)

#===========================DISPLAY====================================

display = Entry(calc, font=('arial', 20, 'bold'), bg="powder blue", bd=20, width=30, justify=RIGHT)
display.grid(row=0, column=0, columnspan=4, pady=1)
display.insert(0, "0")

def getStrZeroIfFirst(temp):
    if len(temp) == 1 and temp[0] == '0':
        return "0"

    else:
        return ""


#=======================NUMBER_BUTTONS=================================

def buttonNumAction(value):
    temp = display.get()
    if len(temp) == 1 and temp[0] == '0':
        display.delete(0, END)
        display.insert(0, str(value))
        InputProcessing.stringToProcess[0] = str(value)

    else:
        display.delete(0, END)
        display.insert(0, temp + str(value))
        InputProcessing.appendStringToProcess(str(value))


btn0 = Button(calc, width=7, height=2, font=('arial', 20, 'bold'), bd=4, text="0", command=lambda: buttonNumAction(0))
btn0.grid(row=7, column=1)

btn1 = Button(calc, width=7, height=2, font=('arial', 20, 'bold'), bd=4, text="1", command=lambda: buttonNumAction(1))
btn1.grid(row=6, column=0)

btn2 = Button(calc, width=7, height=2, font=('arial', 20, 'bold'), bd=4, text="2", command=lambda: buttonNumAction(2))
btn2.grid(row=6, column=1)

btn3 = Button(calc, width=7, height=2, font=('arial', 20, 'bold'), bd=4, text="3", command=lambda: buttonNumAction(3))
btn3.grid(row=6, column=2)

btn4 = Button(calc, width=7, height=2, font=('arial', 20, 'bold'), bd=4, text="4", command=lambda: buttonNumAction(4))
btn4.grid(row=5, column=0)

btn5 = Button(calc, width=7, height=2, font=('arial', 20, 'bold'), bd=4, text="5", command=lambda: buttonNumAction(5))
btn5.grid(row=5, column=1)

btn6 = Button(calc, width=7, height=2, font=('arial', 20, 'bold'), bd=4, text="6", command=lambda: buttonNumAction(6))
btn6.grid(row=5, column=2)

btn7 = Button(calc, width=7, height=2, font=('arial', 20, 'bold'), bd=4, text="7", command=lambda: buttonNumAction(7))
btn7.grid(row=4, column=0)

btn8 = Button(calc, width=7, height=2, font=('arial', 20, 'bold'), bd=4, text="8", command=lambda: buttonNumAction(8))
btn8.grid(row=4, column=1)

btn9 = Button(calc, width=7, height=2, font=('arial', 20, 'bold'), bd=4, text="9", command=lambda: buttonNumAction(9))
btn9.grid(row=4, column=2)

#=======================C_DOT_BRACKETS_BUTTONS==============================

def buttonCAction():
    display.delete(0, END)
    display.insert(0, '0')
    InputProcessing.stringToProcess[0] = ''
    InputProcessing.clearGraph()


def buttonDotAction(value):
    temp = display.get()
    display.delete(0, END)
    display.insert(0, temp + value)
    InputProcessing.appendStringToProcess(getStrZeroIfFirst(temp) + value)

def buttonLeftBracketAction(value):
    temp = display.get()
    if len(temp) == 1 and temp[0] == '0':
        display.delete(0,END)
        display.insert(0,str(value))
        InputProcessing.stringToProcess[0] = str(value) + ' '

    else:
        display.delete(0, END)
        display.insert(0, temp + str(value))
        InputProcessing.appendStringToProcess(str(value) + ' ')


def buttonRightBracketAction(value):
    temp = display.get()
    display.delete(0, END)
    display.insert(0, temp + value)
    InputProcessing.appendStringToProcess(getStrZeroIfFirst(temp) + ' '+value)


btnC = Button(calc, width=15, height=2, font=('arial', 20, 'bold'), bd=4, text="C", command=buttonCAction)
btnC.grid(row=1, column=0, columnspan=2)

btnDot = Button(calc, width=7, height=2, font=('arial', 20, 'bold'), bd=4, text=".", command=lambda: buttonDotAction('.'))
btnDot.grid(row=7, column=0)

btnLBracket = Button(calc, width=7, height=2, font=('arial', 20, 'bold'), bd=4, text="(", command=lambda: buttonLeftBracketAction('('))
btnLBracket.grid(row=3, column=1)

btnRBracket = Button(calc, width=7, height=2, font=('arial', 20, 'bold'), bd=4, text=")", command=lambda: buttonRightBracketAction(')'))
btnRBracket.grid(row=3, column=2)

#=======================BASIC_OPERATORS================================

def buttonBasicOperatorsAction(value):
    temp = display.get()
    display.delete(0, END)
    display.insert(0, temp + value)
    InputProcessing.appendStringToProcess(getStrZeroIfFirst(temp) + ' ' + str(value) + ' ')


def buttonEqlAction():
    if InputProcessing.stringToProcess[0] == '':
        InputProcessing.stringToProcess[0] = display.get()

    InputProcessing.clearGraph()
    temp = InputProcessing.stringToProcess[0].split(" ")
    tree = InputProcessing.postfix_to_tree(InputProcessing.infix_to_postfix(temp))
    result = Evaluation.evaluateExpressionTree(tree)
    display.delete(0, END)
    display.insert(0, str(result))
    InputProcessing.stringToProcess[0] = str(result)


btnEql = Button(calc, width=15, height=2, font=('arial', 20, 'bold'), bd=4, text="=", command=buttonEqlAction)
btnEql.grid(row=7, column=2, columnspan=2)

btnAdd = Button(calc, width=7, height=2, font=('arial', 20, 'bold'), bd=4, text="+", command=lambda: buttonBasicOperatorsAction('+'))
btnAdd.grid(row=3, column=3)

btnSub = Button(calc, width=7, height=2, font=('arial', 20, 'bold'), bd=4, text="-", command=lambda: buttonBasicOperatorsAction('-'))
btnSub.grid(row=5, column=3)

btnMult = Button(calc, width=7, height=2, font=('arial', 20, 'bold'), bd=4, text="*", command=lambda: buttonBasicOperatorsAction('*'))
btnMult.grid(row=4, column=3)

btnDiv = Button(calc, width=7, height=2, font=('arial', 20, 'bold'), bd=4, text="/", command=lambda: buttonBasicOperatorsAction('/'))
btnDiv.grid(row=6, column=3)

#=======================ADVANCED_OPERATORS================================

def buttonLogOperator():
    temp = display.get()
    if len(temp) == 1 and temp[0] == '0':
        display.delete(0, END)
        display.insert(0, 'log(')
        InputProcessing.stringToProcess[0] = 'log ( '

    else:
        temp = display.get()
        display.delete(0, END)
        display.insert(0, temp + 'log(')
        InputProcessing.appendStringToProcess('log ( ')


def buttonRev():
    temp = display.get()
    if len(temp) == 1 and temp[0] == '0':
        display.delete(0, END)
        display.insert(0, '(1/(')
        InputProcessing.stringToProcess[0] = '( 1 / ( '

    else:
        temp = display.get()
        display.delete(0, END)
        display.insert(0, temp + '(1/(')
        InputProcessing.appendStringToProcess('( 1 / ( ')


def buttonAbs():
    temp = display.get()
    if len(temp) == 1 and temp[0] == '0':
        display.delete(0, END)
        display.insert(0, 'abs(')
        InputProcessing.stringToProcess[0] = 'abs ( '

    else:
        temp = display.get()
        display.delete(0, END)
        display.insert(0, temp + 'abs(')
        InputProcessing.appendStringToProcess('abs ( ')


def buttonMod():
    temp = display.get()
    display.delete(0, END)
    display.insert(0, temp + 'mod(')
    InputProcessing.appendStringToProcess(getStrZeroIfFirst(temp) + ' mod ( ')


def buttonSqrt():
    temp = display.get()
    if len(temp) == 1 and temp[0] == '0':
        display.delete(0, END)
        display.insert(0, '\u221a(')
        InputProcessing.stringToProcess[0] = '\u221a ( '

    else:
        temp = display.get()
        display.delete(0, END)
        display.insert(0, temp + '\u221a(')
        InputProcessing.appendStringToProcess('\u221a ( ')


def buttonFact():
    temp = display.get()
    display.delete(0, END)
    display.insert(0, temp + '!')
    InputProcessing.appendStringToProcess(getStrZeroIfFirst(temp) + ' !')


btnPow = Button(calc, width=7, height=2, font=('arial', 20, 'bold'), bd=4, text="x^y", command=lambda: buttonBasicOperatorsAction('^'))
btnPow.grid(row=1, column=2)

btnFact = Button(calc, width=7, height=2, font=('arial', 20, 'bold'), bd=4, text="n!", command=buttonFact)
btnFact.grid(row=1, column=3)

btnRev = Button(calc, width=7, height=2, font=('arial', 20, 'bold'), bd=4, text="1/X", command=buttonRev)
btnRev.grid(row=3, column=0)

btnLog_10 = Button(calc, width=7, height=2, font=('arial', 20, 'bold'), bd=4, text="Log(x)", command=buttonLogOperator)
btnLog_10.grid(row=2, column=0)

btnMod = Button(calc, width=7, height=2, font=('arial', 20, 'bold'), bd=4, text="mod(x)", command=buttonMod)
btnMod.grid(row=2, column=1)

btnAbs = Button(calc, width=7, height=2, font=('arial', 20, 'bold'), bd=4, text="abs(x)", command=buttonAbs)
btnAbs.grid(row=2, column=2)

btnSqrt = Button(calc, width=7, height=2, font=('arial', 20, 'bold'), bd=4, text="\u221a", command=buttonSqrt)
btnSqrt.grid(row=2, column=3)

#======================================================================

root.config(menu=menubar)
root.mainloop()
