from treelib import Node
class AST:
    '''Data structure for an Abstract Syntax Tree'''

    def __init__(self, value, left=None, right=None):
        self.value = value

        # unary operators added
        #if left != None or right != None:
        #    assert left != None and right != None, \
        #        'Arguments left and right must both be either present or absent.'
                  
        self.left = None
        if left != None:
            if type(left) == AST:
                self.left = left
            else:
                self.left = AST(left)
        
        self.right = None
        if right != None:
            if type(right) == AST:
                self.right = right
            else:
                self.right = AST(right)

    def preOrder(self):
        # Value, Left, Right
        result = []
        result.append(self.value)
        if self.left:
            result += self.left.preOrder()
        if self.right:
            result += self.right.preOrder()
        return result

    def inOrder(self):
        # Left, Value, Right
        result = []
        if self.left:
            result += self.left.inOrder()
        result.append(self.value)
        if self.right:
            result += self.right.inOrder()
        return result

    def postOrder(self):
        # Left, Right, Value
        result = []
        if self.left:
            result += self.left.postOrder()
        if self.right:
            result += self.right.postOrder()
        result.append(self.value)
        return result
    def format(self, _padding=''):

        #line = '('+str(self.value) if type(self.value) is not float else "{:g}".format(self.value)+')\n'

        line = '('+str(self.value)+')\n'

        if self.left:
            line += _padding
            line += ' \u251C'

            # push
            _padding += ' |'

            line += self.left.format(_padding)

            # pop
            _padding = _padding[:-2]

        if self.right:
            line += _padding
            line += ' \u2514'
            
            # push
            _padding += '  '

            line += self.right.format(_padding)

            # pop
            _padding = _padding[:-2]
        return line

    def display(self):
        print(self.format())
    
    def evalAST(self,opDict):
        if self.value in opDict:
            return opDict[self.value](self.left.evalAST(opDict) if self.left else None,self.right.evalAST(opDict))
        else:
            return self.value
    def calc(self,opDict):
        print(self.evalAST(opDict))
    def createTreelibNode(self,tree,parent=None):
        #print(parent)
        #print(self.value)
        if parent:
            node = tree.create_node(parent=parent,tag=str(self.value))
        else:
            node = Node(tag=str(self.value))
            tree.add_node(node)
        if self.left:
            self.left.createTreelibNode(tree,node)
        if self.right:
            self.right.createTreelibNode(tree,node)
        return tree