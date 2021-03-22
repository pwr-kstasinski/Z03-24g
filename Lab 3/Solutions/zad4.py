import random
from enum import IntEnum


class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2


def printStatistics(wins, draws, losses):
    print("End!!\nNow it is time for some statistics: ")
    print(f'Your wins: {wins} , your draws: {draws} and your losses:{losses}  ')

    if wins > losses:
        print("Based on statistic you are the winnner !!\n Congratulations!!!")
    elif losses > wins:
        print("Based on statistic you are the looser!!\n Better luck next time")
    else:
        print("Based on statistic it is a draw!!")
    exit()


def determineWinner(yourPick, computersPick, wins, draws, losses):
    if yourPick == computersPick:
        print("It's a draw!!")
        draws += 1
    elif ((yourPick == 0 and computersPick == 1) or (yourPick == 1 and computersPick == 2) or (
            yourPick == 2 and computersPick == 0)):

        print("You lost!")
        losses += 1
    else:
        print("You won!!!")
        wins += 1
    print("_________________________________________________________________")
    return wins, draws, losses


def displayCountdown():
    for j in range(3, 0, -1):
        print(j)


def play():
    numberOfRounds = int(input("Enter how many rounds do you wanna play: "))

    if numberOfRounds > 0:

        wins = draws = losses = 0
        for i in range(0, numberOfRounds):
            print("Let's play!")
            displayCountdown()
            print(f"Round {i + 1}:")
            yourPick = int(input("Write Rock[0] , Paper[1] or Scissors[2]. Enter your choice: "))
            if yourPick > 2 or yourPick < 0:
                print("Wrong input, lets start over")
                play()

            else:
                computersPick = random.randint(0, 2)
                print(f"You chose: {Action(yourPick).name} ")
                print(f"Computer chose: {Action(computersPick).name} ")

                (wins, draws, losses) = determineWinner(yourPick, computersPick, wins, draws, losses)

        printStatistics(wins, draws, losses)


    else:
        print("Wrong input")


play()
