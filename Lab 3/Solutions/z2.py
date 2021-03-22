import os

def prt(src,offset):
    fl=os.listdir(src)
    for f in fl:
        s=""
        for i in range(0,offset):
            s+="    "
        print(s+f)
        if(os.path.isdir(src+'\\'+f)):
            prt(src+'\\'+f,offset+1)

prt(input("path: "),0)
