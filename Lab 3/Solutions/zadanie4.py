#!/usr/bin/env python

import random

vals = 'R P S'.split(' ')
msg_win = "You win this round."
msg_lose = "You lose this round."
msg_tie = "Tie! You both picked "
help = "Enter R for rock, P for paper, S for scissor."


def fight(userval):
    compval = vals[random.randint(0, len(vals) - 1)]
    print "Computer picked %s." % compval
    if compval == userval:
        return 0, '%s%s.' % (msg_tie, compval)
    elif (userval == vals[0] and compval == vals[1]) or (userval == vals[1] and compval == vals[2]) or (
            userval == vals[2] and compval == vals[0]):
        return -1, '%s %s beats %s.' % (msg_lose, compval, userval)
    else:
        return 1, '%s %s beats %s.' % (msg_win, userval, compval)


def loop():
    i = 0
    score = [0, 0]
    print help
    print ""
    print "Numbers of rounds:"
    numberofrounds = raw_input()

    while i < int(numberofrounds):
        userval = raw_input("-->")
        userval = userval.upper()
        i += 1
        if userval in vals:
            result, message = fight(userval)
            print message
            if result == 1:
                score[0] += 1
            elif result == -1:
                score[1] += 1
            print "Score: %s to %s." % (score[0], score[1])
            print ""
        else:
            print "%s is not a valid command." % userval
            print ""
            exit()

        print "Final Score: %s to %s" % (score[0], score[1])
        if score[0] > score[1]:
            print "You win!"
        elif score[0] < score[1]:
            print "You Lose!"
        else:
            print "You tied."


if __name__ == '__main__':
    loop()
