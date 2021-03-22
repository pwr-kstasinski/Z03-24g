import random
import math

n=int(input("ilosc rund: "))

w=0
l=0
r=0
while((w+l+r<n) and (w<=l+ n-r-w)):
    player=int(input("wybiez:\n0. kamien\n1. papier\n2. nozyce\ntwoj wybor: "))
    pc=random.choice([1,2,3])
    if(player==pc):
        r+=1
        print("remis")
    elif((player+1)%3==pc):
        l+=1
        print("przegrana")
    else:
        w+=1
        print("wygrana")

print(f"twoj wynik(win,los,tie): {w} {l} {r}")



