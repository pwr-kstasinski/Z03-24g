def checkCorrectInput(equation):
    correctInput = (' ', '+', '-', '/', '*', '.', '(', ')', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    correct = True

    for character in equation:
        if not character in correctInput:
            return not correct
    return correct

def doYourJob(equation):
    try:
            print(str(equation) + " = " + str(eval(equation)))
    except: 
        print("Cos poszlo nie tak o.O\nWpisz to wyrazenie normalnie...")
        main()
    
def main():
        equation = input("\nZdefiniuj swoje rownanie: ")

        if checkCorrectInput(equation):
            doYourJob(equation)
        else:
            print("\nNiepoprawnie wprowadzone znaki. Wez sie zastanow, a nie w testera sie bawisz.")

main()