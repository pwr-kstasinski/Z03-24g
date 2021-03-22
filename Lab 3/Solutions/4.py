import random

choices = ["papier","kamień","nożyce"]
wins=loses=ties=0
rounds = int(input("Enter rounds count:\n"))
while rounds>0:
    player = input("Enter \"papier\",\"kamień\" or \"nożyce\":\n")
    if player in choices:
        computer = random.choice(choices)
        print(computer)
        pi = choices.index(player)
        ci = choices.index(computer)
        if pi<ci:
            if pi==0 and ci==2:
                loses+=1
            else:
                wins+=1
        elif pi>ci:
            if pi==2 and ci==0:
                wins+=1
            else:
                loses+=1
        print("%i:%i"%(wins,loses))
        rounds-=1
    else:
        print("Wrong symbol")
if wins>loses:
    print("You won")
elif wins<loses:
    print("You lost")
else:
    print("Tie")
print("Wins:%i, Ties:%i, Loses:%i"%(wins,ties,loses))