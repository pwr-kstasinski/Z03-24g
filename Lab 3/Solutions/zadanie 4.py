import random as rnd

def play_round():
    #wybor gracza:
    player_selection = 0
    while True:
        player_selection = input("Wprowadz papier/kamien/nozyce: ")
        if player_selection == "papier" or player_selection == "kamien" or player_selection == "nozyce":
            break
        else:
            print("   nieprawidlowy wybor! Sprobuj jeszcze raz")
    #wybor komputera:
    computer_selection = rnd.randint(0, 2)
    if computer_selection == 0:
        computer_selection = "papier"
    elif computer_selection == 1:
        computer_selection = "kamien"
    else:
        computer_selection = "nozyce"
    print("Komputer wybral " + computer_selection)
    #sedzia:
    if (player_selection == computer_selection):
        return (0, 0)
    elif ((player_selection, computer_selection) == ("papier", "kamien") or (player_selection, computer_selection) == ("kamien", "nozyce") or (player_selection, computer_selection) == ("nozyce", "papier")):
        return (1, 0)
    else:
        return (0, 1)

def show_stats(player_score, computer_score, number_of_rounds):
    if player_score > computer_score:
        print("Wygrales!")
    elif player_score < computer_score:
        print("Przegrales!")
    else:
        print("Remis!")
    print("   punkty: " + str(player_score) + "-" + str(computer_score))
    print("   liczba remisow: " + str(number_of_rounds - (player_score + computer_score)))

def start_game(number_of_rounds):
    total_player_score = 0
    total_computer_score = 0
    for i in range(number_of_rounds):
        (player_score, computer_score) = play_round()
        total_player_score += player_score
        total_computer_score += computer_score
    show_stats(total_player_score, total_computer_score, number_of_rounds)

number_of_round = int(input("Ile rund chcesz zagrac?: "))
start_game(number_of_round)