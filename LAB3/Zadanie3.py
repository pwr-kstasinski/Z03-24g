lst = []  
n = int(input("Wpisz ile chcesz dodac liczb do tablicy: ")) 
  
for i in range(0, n): 
    ele = int(input())
    lst.append(ele)
   
print(lst)
lst.sort()
print(lst)


