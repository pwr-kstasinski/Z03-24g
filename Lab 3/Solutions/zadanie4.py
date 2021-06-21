import random


def game(rounds=3):
    elements = ['rock', 'paper', 'scissors']
    player_points = 0
    comp_points = 0

    for n in range(rounds):
        print('───────────Round ' + str(n) + ' ───────────')

        player_pick = ''

        while player_pick not in elements:
            player_pick = input('Input rock, paper or scissors: ')

        comp_pick = random.choice(elements)
        if player_pick == comp_pick:
            print('\nDraw...\n')
        elif (player_pick, comp_pick) in [('rock', 'scissors'), ('scissors', 'paper'), ('paper', 'rock')]:
            print('\nPlayer wins\n')
            player_points += 1
        else:
            print('\nComputer wins\n')
            comp_points += 1
    draws = rounds - comp_points - player_points
    print('┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
    print('┃{:16} {:^5} {:^5} {:^5}┃'.format('', 'Wins', 'Loses', 'Draws'))
    print('┃{:16} {:^5} {:^5} {:^5}┃'.format('Player', player_points, comp_points, draws))
    print('┃{:16} {:^5} {:^5} {:^5}┃'.format('Computer', comp_points, player_points, draws))
    print('┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛')
    if comp_points > player_points:
        print('\nComputer wins!')
    elif player_points > comp_points:
        print('\nPlayer wins!')
    else:
        print('\nDraw')


if __name__ == "__main__":
    pick = 0
    while pick < 1:
        pick = int(input('How many rounds do you want to play: '))

    game(pick)
