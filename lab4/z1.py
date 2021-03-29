lista = list(input('Input list: ').split())

class Tree:
    def __init__(tree):
        tree.left = None
        tree.right = None
        tree.data = None
        
def create(lista,ind):
        root = Tree()
        root.data = lista[ind]
        root.left = Tree()
        root.left.data = lista[ind-1]
        root.right = Tree()
        root.right.data = lista[ind+1]

        return root
def createTree(lista):            
    while len(lista)>1:
        try: 
            ind = lista.index(next(x for x in lista if x=="/" or x=="*"))
            if lista[ind]=="*":
                
                root = create(lista,ind)
            else:
                root = create(lista,ind)
            lista.insert(ind-1,root)
            
            del lista[ind]
            del lista[ind]
            del lista[ind]
        except:
            ind = lista.index(next(x for x in lista if x=="-" or x=="+"))
            if lista[ind]=="-":
                
                root = create(lista,ind)
            else:
                
                root = create(lista,ind)
            lista.insert(ind-1,root)
            del lista[ind]
            del lista[ind]
            del lista[ind]

    return  lista[0]
           


def calculate(tree):
    try:
        result = float(tree.data)
        return result
    except:
        try:
            l = float(calculate(tree.left))
            r = float(calculate(tree.right))
            if tree.data == "+":
                return l + r
            elif tree.data == "-":
                return l - r
            elif tree.data == "*":
                return l * r
            elif tree.data == "/":
                return l / r
        except:
            return calculate(tree.data)


        
       
def printTree(node, level):
    if node != None:
        if isinstance(node.data,str):
            printTree(node.left, level + 1)
            print(' ' * 4 * level + '->', node.data)
            printTree(node.right, level + 1)
        else:
            printTree(node.data.left, level + 1)
            print(' ' * 4 * level + '->', node.data.data)
            printTree(node.data.right, level + 1)


tree = createTree(lista)
print(calculate(tree))

printTree(tree,0)


       
    
       
 