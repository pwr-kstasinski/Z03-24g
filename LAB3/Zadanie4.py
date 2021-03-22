import random

userWins = 0
computerWins = 0
rounds = 0
run = True

if(run):

    chosenRounds = int(input("Wpisz ile rund chcesz zagrac: ")) 

    while run: 

        print("Wybierz kamien, papier lub nozyce (wpisz liczbe) \n 1.Kamien \n 2.Papier \n 3.Nozyce \n") 

        choice = int((input("Wpisz swoj wybor: ")))

        while choice > 3 or choice < 1: 
            choice = int(input("Wpisz poprawna wartosc (1, 2 lub 3): ")) 

        if choice == 1: 
            choice_name = 'Kamien'
        elif choice == 2: 
            choice_name = 'Papier'
        else: 
            choice_name = 'Nozyce'
                       
        print("Wybor uzytkownika to: " + choice_name)
        print("\nTeraz wybiera komputer...")

        comp_choice = random.randint(1, 3) 

        while comp_choice == choice: 
            comp_choice = random.randint(1, 3) 

        if comp_choice == 1: 
            comp_choice_name = 'Kamien'
        elif comp_choice == 2: 
            comp_choice_name = 'Papier'
        else: 
            comp_choice_name = 'Nozyce'
            
        print("Wybor komputera to: " + comp_choice_name) 
    
        print("\n" + choice_name + " vs " + comp_choice_name) 

        if((choice == 1 and comp_choice == 2) or
        (choice == 2 and comp_choice == 1 )): 
            print("Papier wygrywa! ", end = "") 
            result = "Papier"
            
        elif((choice == 1 and comp_choice == 3) or
            (choice == 3 and comp_choice == 1)): 
            print("Kamien wygrywa! ", end = "") 
            result = "Kamien"
        else: 
            print("Nozyce wygrywaja! ", end = "") 
            result = "Nozyce"

        if result == choice_name: 
            print("!!!WYGRYWA UZYTKOWNIK!!!\n")
            userWins += 1
        else: 
            print("!!!WYGRYWA KOMPUTER!!!\n") 
            computerWins += 1

        rounds += 1

        if(rounds == chosenRounds):
            print("\nKoniec gry.")
            run = False
        
    if userWins < computerWins:
        print("\nWygral komputer z liczba zwyciestw: " + str(computerWins) + "\nUzytkownik wygral tylko: " + str(userWins) + " rund")
    elif userWins == computerWins:
        print("\nRemis!")
    else: 
        print("\nWygral uzytkownik z liczba zwyciestw: " + str(computerWins) + "\nKomputer wygral tylko: " + str(userWins) + " rund")   

else:
    print("\nGra sie jeszcze nie zaczela a juz sie skonczyla o.O") 




