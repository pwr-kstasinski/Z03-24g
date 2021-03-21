import sys
import random


playerwins, computerwins, draws = 0, 0, 0


def playerwin():
    print(playerwinmes)
    global playerwins
    playerwins = playerwins + 1


def computerwin():
    print(cpuwinmes)
    global computerwins
    computerwins = computerwins + 1


possibilities = ["kamien", "papier", "nozyce"]
cpuwinmes = "komputer wygrywa"
playerwinmes = "gracz wygrywa"
for x in range(int(sys.argv[1])):
    choice = -1
    while choice < 0 or choice > 2:
        choice = int(input("1 - kamien \n2 - papier \n3 - nozyce\n")) - 1
        if choice < 0 or choice > 2:
            print("Wybrano liczbe spoza zak")
    print("gracz wybral: " + possibilities[choice])
    computerchoice = random.randrange(3)
    print("komputer wybral: " + possibilities[computerchoice])
    if computerchoice == choice:
        print("remis!")
        draws = draws + 1
    else:
        if computerchoice == 0:
            if choice == 1:
                playerwin()
            else:
                computerwin()
        elif computerchoice == 1:
            if choice == 0:
                computerwin()
            else:
                playerwin()
        else:
            if choice == 0:
                playerwin()
            else:
                computerwin()
    print("====================================")
    print("====================================")
print("/////////////////////////////////////////")
print("Zwyciestwa komputera: " + str(computerwins))
print("Zwyciestwa gracza: " + str(playerwins))
print("Remisy: " + str(draws))
print("/////////////////////////////////////////")
