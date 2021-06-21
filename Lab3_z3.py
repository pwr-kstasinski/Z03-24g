import sys

def sortowanie(args):
    numbers = []
    numbers = args[1].split(" ")
    numbers = list(map( int, numbers))
    numbers.sort()
    return numbers

print(sortowanie(sys.argv))
