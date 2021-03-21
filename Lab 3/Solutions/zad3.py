import sys

listOfInputs = []

for value in sys.argv:
    listOfInputs.append(value)

listOfInputs.remove('zad3.py')

print(sorted(listOfInputs))
