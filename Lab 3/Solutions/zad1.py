import os

path = input("enter path: ")
ext = input("enter extension: ")



for file in os.listdir(path):
    if file.endswith(ext):
        print(os.path.join(path, file))    #os.path.join() ladnie skleja sciezke