import os
import string

src=input("path: ")
exten=input("extension: ")

fl=os.listdir(src)

def chkExten(file):
    return '.'+str.split(file,'.')[-1]==exten

fl=filter(chkExten,fl)

for f in fl:
    print(f)
