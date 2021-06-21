import os

path = str(input("Enter path "))

for dirpath, dirnames, filenames in os.walk(path):
    directory_level = dirpath.replace(path, "")
    directory_level = directory_level.count(os.sep)
    space = "  "*4
    underscore = "__" * 4
    for j in range(1,directory_level+1):
        print(space*j + "|",end="")
    if directory_level==0:
        print("|",end="")
    print(os.path.basename(dirpath))
    for f in filenames:

        for k in range(1, directory_level+1):
            print(space*k+"|", end="")
        if directory_level==0:
            print("|",end="")

        print(underscore, f)