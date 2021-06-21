import random

n = int(input ('Liczba rund:'))
i=1
choice = ['','Kamien','Nozyce','Papier']
results=[0,0,0]
while i <= n:

    player = int(input('Wybierz :\n 1.Kamien \n 2.Nozyce \n 3.Papier \n'))
    computer = random.randint(1,3)
    print('\nMatch:\n '+choice[player]+':'+choice[computer]+'\n')
    if player == computer:
        results[2]+=1
        print('REMIS')

    elif player == 1:
        if computer == 2:
            results[0]+=1
            print('ZWYCIENSTWO')
        else:
            results[2]+=1
            print('PORAZKA')
    elif player == 2:
        if computer == 1:
            results[2]+=1
            print('PORAZKA')
        else:
            results[0]+=1
            print('ZWYCIENSTWO')
    else :
        if computer == 1:
            results[2]+=1
            print('PORAZKA')
        else:
            results[0]+=1
            print('ZWYCIENSTWO')

    i=i+1


print('\nliczba zwycięstw : ' + str(results[0]))
print('liczba porazek : ' + str(results[1]))
print('liczba remisów : ' + str(results[2]))
