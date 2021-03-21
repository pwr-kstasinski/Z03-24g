import random

print("Witaj w  paper rock scissorc")


wynikGraczaWRundzie = []                                # wygrana 1, przegrana 0, remis 0,5
liczbaWynikow = [0,0,0]                                 # [wygrana,remis,przegrana]


def liczbaRund():
    lRund = 0
    while lRund <= 0:
        lRund = int(input("podaj ile rund ( >0 ): "))

    return lRund


def wyborSymbolu():
    nrSymbolu = 0
    while nrSymbolu < 1 or nrSymbolu > 3:
        print("wybierz symbol (1,2,3)")
        print("1. PAPER")
        print("2. SCISSORS")
        print("3. ROCK")
        nrSymbolu = int(input("numer symbolu: "))

    return nrSymbolu


def losujSumbol():
    return random.randint(1,3)


def wynikGracza(symbolGracza,symbolBot):
    if symbolGracza == symbolBot:
        liczbaWynikow[1]+=1
        return 0.5

    elif symbolGracza == 1:                             # gracz ma papier
        if symbolBot == 2:                              # bot ma nozyczki
            liczbaWynikow[2]+=1
            return 0
        else:
            liczbaWynikow[0]+=1
            return 1

    elif symbolGracza == 2:                             # gracz ma nozyczki
        if symbolBot == 3:                              # bot ma kamien
            liczbaWynikow[2] += 1
            return 0
        else:
            liczbaWynikow[0] += 1
            return 0

    else:                                               # gracz ma kamien
        if symbolBot == 1:                              # bot ma papier
            liczbaWynikow[2] += 1
            return 0
        else:
            liczbaWynikow[0] += 1
            return 0


def wyswietlWyniki():
    print("wyniki gracza w kolejnych rundach: " + str(wynikGraczaWRundzie))
    print("wygranych: " + str(liczbaWynikow[0]))
    print("przegranych: " + str(liczbaWynikow[2]))
    print("remisow: " + str(liczbaWynikow[1]))



def graj():
    lRund = liczbaRund()
    for i in range(lRund):
        print("runda: " + str(i+1))
        symbolGracza = wyborSymbolu()
        symbolBot = losujSumbol()
        wynikGraczaWRundzie.append(wynikGracza(symbolGracza,symbolBot))

    print("------KONIEC GRY------")
    print("rozegranych rund: " + str(lRund))
    wyswietlWyniki()


graj()
