import math

n=int(input("list size: "))

lst=[]
for i in range(0,n):
    lst.append(int(input('Enter number: ')))

lst.sort()
print(lst)

