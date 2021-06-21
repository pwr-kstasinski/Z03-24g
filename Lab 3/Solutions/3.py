import os,sys,argparse

if len(sys.argv)>2:
    lis = argparse.ArgumentParser()
    lis.add_argument("nums",nargs="*",type=int)
    lis = lis.parse_args().nums
elif len(sys.argv)==2:
    lis = sys.argv[1].split(",")
    lis = list(map(int, lis))
else:
    lis = input("Enter comma-separated arguments: ").split(",")
    lis = list(map(int, lis))
lis.sort()
print(lis)