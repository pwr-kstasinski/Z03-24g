import random as ran
import sys


lista_elementow = ["papier", "kamień", "nożyce"]
def game(rounds):
    point_p = 0
    point_c = 0
    player = ""
    comp = ""
    for i in range(rounds):
        i=i+1
        print("Round " + str(i))
        player = input("Wybierz element: ")
        comp = ran.choice(lista_elementow)

        if (player, comp)==("papier", "kamień") or (player, comp)==("kamień", "nożyce") or (player, comp)==("nożyce", "papier"):
            point_p += 1
            print("Zwycięstwo")
        elif player == comp:
            print("Remis")
        else:
            point_c += 1
            print("Porażka")
        player = ""
        print("")

    draws = rounds - point_c - point_p

    print("---------------")
    print("           ", "Z", "P", "R")
    print("Player     ", point_p, point_c, draws)
    print("Computer   ", point_c, point_p, draws)


def main(arg):
    if (len(arg) > 1):
        rounds = int(arg[1])
        game(rounds)
    else:
        game(3)


main(sys.argv)
