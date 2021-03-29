
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
        if(not self.left):  return self.data
        elif(self.data=='+'):   return self.left.calc()+self.right.calc()
        elif(self.data=='-'):   return self.left.calc()-self.right.calc()
        elif(self.data=='*'):   return self.left.calc()*self.right.calc()
        elif(self.data=='/'):   return self.left.calc()/self.right.calc()



def makeNode(postfix):
    stack=[]
    for elem in postfix:
        if((elem=='+') or (elem=='-') or(elem=='*') or(elem=='/')):
            a=stack.pop()
            b=stack.pop()
            stack.append(Node(elem,b,a))
        else:   stack.append(Node(elem))
    return stack[0]

def infixToPostfix(infix):
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
        elif(infix[i]=='('):
            stack.append('(')
        elif(infix[i]==')'):
            while(stack[-1]!='('):      postfix.append(stack.pop())
            stack.pop()
        elif((len(stack)==0) or (stack[-1]=='(')):          stack.append(infix[i])
        elif((infix[i]=='*' or infix[i]=='/') and (stack[-1]=='+' or stack[-1]=='-')):    
            stack.append(infix[i])
        else:
            while((len(stack)>0) and (stack[-1]=='*' or stack[-1]=='/')):
                postfix.append(stack.pop())
            if(infix[i]=='+' or infix[i]=='-'):
                while((len(stack>0)) and (stack[-1]=='-' or stack[-1]=='+')):
                    postfix.append(stack.pop())
            stack.append(infix[i])
        i+=1
    while(len(stack)>0):        postfix.append(stack.pop())
    return postfix


"""
t1=makeNode(infixToPostfix("2"))
t1.prt()
print(" =",t1.calc())
t1=makeNode(infixToPostfix("(2)"))
t1.prt()
print(" =",t1.calc())
t1=makeNode(infixToPostfix("2+3"))
t1.prt()
print(" =",t1.calc())
t1=makeNode(infixToPostfix("(2+3)"))
t1.prt()
print(" =",t1.calc())
t1=makeNode(infixToPostfix("(2+3)*4"))
t1.prt()
print(" =",t1.calc())
t1=makeNode(infixToPostfix("3*(4+5)"))
t1.prt()
print(" =",t1.calc())
t1=makeNode(infixToPostfix("(2+3)*(4)"))
t1.prt()
print(" =",t1.calc())
t1=makeNode(infixToPostfix("(3)*(4+5)"))
t1.prt()
print(" =",t1.calc())
t1=makeNode(infixToPostfix("(2+3)*(4/5)"))
t1.prt()
print(" =",t1.calc())
t1=makeNode(infixToPostfix("1+2*3"))
t1.prt()
print(" =",t1.calc())
"""

try:
    while(True):
        print(makeNode(infixToPostfix(input("podaj rownanie: "))).calc())
except EOFError:
    print("")

