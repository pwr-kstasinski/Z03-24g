
import os



root = input("Enter directory :")

print(root)
def printTree(root,level):
    if level != 0:
        print(level*'    '+'|-----'+os.path.split(root)[1])
    
    if os.path.isdir(root):
        list = os.listdir(root)
        for i in range(len(list)):
            printTree(os.path.join(root, list[i]), level+1)


printTree(root,0)
