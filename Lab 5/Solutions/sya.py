from queue import LifoQueue
from re import findall
from AST import AST
from math import factorial,log10,sqrt,fabs

OPDICT = {
    "+": lambda a,b: a+b,
    "-": lambda a,b: a-b,
    "*": lambda a,b: a*b,
    "/": lambda a,b: a/b,
    "%": lambda a,b: a%b,
    "^": lambda a,b: a**b,
    "!": lambda a,b: factorial(b),
    "abs": lambda a,b: fabs(b),
    "log": lambda a,b: log10(b),
    "sqrt": lambda a,b: sqrt(b)
    }


def is_operand(token):
    try:
        float(token)
        return True
    except (TypeError, ValueError):
        return False

def parse(expression):
    tokens = findall(r"[0-9]*[.]?[0-9]+|[+\-/*()!%^]|log|abs|sqrt",expression)

    if(not tokens):
        raise RuntimeError(ERROR_MESSAGE)
    
    print(tokens)
    ERROR_MESSAGE = 'Unable to parse \''+expression+'\''
    
    PRECEDENCE = {
        '(': -1,
        '!': 4,
        'sqrt' : 3,
        'log' : 3,
        'abs' : 3,
        '^': 2,
        '*' : 1,
        '/' : 1,
        '%': 1,
        '+' : 0,
        '-' : 0
    }
    # ASSOCIATIVITY is either 0 (right-associative) or 0.5 (left-associative) because it serves as a modifier to precedence
    # unary operators all have 0
    ASSOCIATIVITY = {
        '!': 0,
        'sqrt' : 0,
        'log' : 0,
        'abs' : 0,
        '^': 0,
        '*' : 0.5,
        '/' : 0.5,
        '%': 0.5,
        '+' : 0.5,
        '-' : 0.5
    }
    UNARY = ['!','sqrt','log','abs']

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
                e1 = None if(op in UNARY) else exp_stack.get()
                exp_stack.put(AST(op, e1, e2))
        
        elif token in PRECEDENCE:
            while op_stack.qsize():
                op = op_stack.get()
                if PRECEDENCE[op] <= PRECEDENCE[token] - ASSOCIATIVITY[token]:
                    op_stack.put(op)
                    break
                e2 = exp_stack.get()
                e1 = None if(op in UNARY) else exp_stack.get()
                exp_stack.put(AST(op, e1, e2))

            op_stack.put(token)
        
        else:
            raise RuntimeError(ERROR_MESSAGE)
    
    while(op_stack.qsize()):
        op = op_stack.get()
        e2 = exp_stack.get()
        e1 = None if(op in UNARY) else exp_stack.get()
        exp_stack.put(AST(op, e1, e2))
    assert(exp_stack.qsize()==1)
    return exp_stack.get()