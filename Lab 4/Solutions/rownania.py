from collections import deque

def is_number(variable):
    try:
        float(variable)
        return True
    except ValueError:
        return False


class TreeNode:
    def __init__(self, **kwargs):
        value = kwargs.get('value')
        left_operand = kwargs.get('left_operand')
        operator = kwargs.get('operator')
        right_operand = kwargs.get('right_operand')
        if value is not None:
            self.set_value(value)
        elif left_operand is not None and operator is not None and right_operand is not None:
            self.set_operator(operator)
            self.set_left_child(left_operand)
            self.set_right_child(right_operand)
        else:
            raise AttributeError("Wrong arguments!")

    def set_value(self, value):
        if not hasattr(self, '__left_child__') and not hasattr(self, '__right_child__') :
            self.__value__ = value
        else:
            raise RuntimeError("This node is not a value!")  
    def set_operator(self, operator: chr):
        if not hasattr(self, '__value__'):
            self.__operator__ = operator
        else:
            raise RuntimeError("This node is not an operator!")  
    def set_left_child(self, left_child):
        if not hasattr(self, '__value__'):
            self.__left_child__ = left_child
        else:
            raise RuntimeError("This node is not an operator!")  
    def set_right_child(self, right_child):
        if not hasattr(self, '__value__'):
            self.__right_child__ = right_child
        else:
            raise RuntimeError("This node is not an operator!")  
    
    def get_operator(self):
        if hasattr(self, '__operator__'):
            return self.__operator__
        else:
            raise RuntimeError("This node is not an operator!")  
    def get_value(self):
        if hasattr(self, '__value__'):
            return self.__value__
        else:
            raise RuntimeError("This node is not a value!")  
    def get_left_child(self):
        if hasattr(self, '__left_child__'):
            return self.__left_child__
        else:
            raise RuntimeError("This node is not an operator!")
    def get_right_child(self):
        if hasattr(self, '__right_child__'):
            return self.__right_child__
        else:
            raise RuntimeError("This node is not an operator!")  
    def is_operator(self):
        if hasattr(self, '__operator__'):
            return True
        else:
                return False

class Tree:
    def __init__(self, reversed_polish_notation: [str]):
        stack = deque()
        for element in reversed_polish_notation:
            if is_number(element):
                new_node = TreeNode(value=element)
                stack.append(new_node)
            elif element in ["+", "-", "*", "/"]:
                right_child_node = stack.pop()
                left_child_node = stack.pop()
                new_node = TreeNode(left_operand=left_child_node, operator=element, right_operand=right_child_node)
                stack.append(new_node)
            else:
                raise TypeError("Invalid type of elements in reverse polish notation!")
        self.__root__ = stack.pop()
    def get_root_node(self):
        return self.__root__
    def __compute_expression__(self, tree_node):
        if (tree_node.is_operator()):
            left_subresult = self.__compute_expression__(tree_node.get_left_child())
            right_subresult = self.__compute_expression__(tree_node.get_right_child())
            operator = tree_node.get_operator()
            if operator == "+": 
                return float(float(left_subresult) + float(right_subresult))
            elif operator == "-": 
                return float(float(left_subresult) - float(right_subresult))
            elif operator == "*": 
                return float(float(left_subresult) * float(right_subresult))
            elif operator == "/": 
                return float(float(left_subresult) / float(right_subresult))
            else: 
                return 1
        else:
            return float(tree_node.get_value())
    def compute_expression(self):
        return self.__compute_expression__(self.__root__)
    def __make_list__(self, tree_node):
        if (tree_node.is_operator() == True):
            return "[" + str(self.__make_list__(tree_node.get_left_child())) + " " + str(tree_node.get_operator()) + " " + str(self.__make_list__(tree_node.get_right_child())) + "]"
        else:
            return tree_node.get_value()           
    def dfs_to_list(self):
        return self.__make_list__(self.__root__)

        







def priority(znak):
    if znak in ["+", "-"]:
        return 1
    if znak in ["*", "/", "%"]:
        return 2
    return -1 

def split_infix_expression(to_split):
    splitted = []
    strfloat_builder = ""
    for i in range (0, len(to_split)):
        if to_split[i] in ['(', '{', '[', ')', '}', ']', '+', '-', '*', '/'] :
            if len(strfloat_builder) > 0:
                splitted.append(strfloat_builder)
            strfloat_builder=""
            splitted.append(to_split[i])        
        elif to_split[i].isprintable() and to_split[i] != ' ':
            strfloat_builder += to_split[i]
    if len(strfloat_builder) > 0:
        splitted.append(strfloat_builder)
    return splitted

def infix_to_rpn(infix):
    infix = split_infix_expression(infix)
    operators_lifo = deque()
    rpn = []
    for i in range (len(infix)):
        actual_string = infix[i]
        if is_number(actual_string):
            rpn.append(actual_string)
        elif actual_string in ["(", "{", "["]:
            operators_lifo.append("(")
        elif actual_string in [")", "}", "]"]:
            while operators_lifo[len(operators_lifo)-1] not in ["(", "{", "["]:
                rpn.append(operators_lifo.pop())
            operators_lifo.pop()
        elif actual_string in ["+", "-", "*", "/"]:
            while len(operators_lifo)>0 and priority(actual_string) <= priority(operators_lifo[len(operators_lifo)-1]):
                rpn.append(operators_lifo.pop())
            operators_lifo.append(actual_string)
        else:
            print("found >" + actual_string + "<")
    while len(operators_lifo)>0:
        rpn.append(operators_lifo.pop())
    return rpn

normal = input("Podaj podstac normalna: ")
rpn = infix_to_rpn(normal)
tree = Tree(rpn)
print("Zawartosc grafu w kolejnosci infix depth-first: " + tree.dfs_to_list())
print("Wynik obliczenia wyrazenia: " + str(tree.compute_expression()))