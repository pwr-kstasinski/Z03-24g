import os
import sys


def visit_sub_folders(path, depth):
    dirlist = [folder for folder in os.listdir(path) if os.path.isdir(os.path.join(path, folder))]
    for x in dirlist:
        print(depth * "    " + "├───", end=" ")
        print(x)
        visit_sub_folders(path + "\\" + x, depth + 1)


print(sys.argv[1])
visit_sub_folders(sys.argv[1], 0)