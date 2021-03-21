import os

path = input("enter path to start: ")
command = "tree "+ path +" /f"
os.system(command)