from queue import LifoQueue
from re import findall
from AST import AST

OPDICT = {"+": lambda a,b: a+b,"-": lambda a,b: a-b,"*": lambda a,b: a*b,"/": lambda a,b: a/b}

def is_operand(token):
    try:
        float(token)
        return True
    except (TypeError, ValueError):
        return False

def parse(expression):
    tokens = findall(r"[0-9]*[.]?[0-9]+|[+\-/*()]",expression)

    if(not tokens):
        raise RuntimeError(ERROR_MESSAGE)
    
    #print(tokens)
    ERROR_MESSAGE = 'Unable to parse \''+expression+'\''

    PRECEDENCE = {
        '(' : -1,
        ')' : -1,
        '*' : 1,
        '/' : 1,
        '+' : 0,
        '-' : 0
    }

    op_stack = LifoQueue()
    exp_stack = LifoQueue()
    
    for token in tokens:
        if is_operand(token):
            exp_stack.put(AST(float(token)))
        
        elif token == '(':
            op_stack.put(token)
        
        elif token == ')':
            while op_stack.qsize():
                op = op_stack.get()
                if op == '(':
                    break
                e2 = exp_stack.get()
                e1 = exp_stack.get()
                exp_stack.put(AST(op, e1, e2))
        
        elif token in PRECEDENCE:
            while op_stack.qsize():
                op = op_stack.get()
                if PRECEDENCE[op] < PRECEDENCE[token]:
                    op_stack.put(op)
                    break
                e2 = exp_stack.get()
                e1 = exp_stack.get()
                exp_stack.put(AST(op, e1, e2))

            op_stack.put(token)
        
        else:
            raise RuntimeError(ERROR_MESSAGE)
    
    while(op_stack.qsize()):
        op = op_stack.get()
        e2 = exp_stack.get()
        e1 = exp_stack.get()
        exp_stack.put(AST(op, e1, e2))
    
    # Return the root node
    return exp_stack.get()