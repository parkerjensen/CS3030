#! /usr/bin/env pythons

pintries = 0

def getInput(pintries):
    if pintries < 3:
        pin = input("Enter your pin...")
        if len(pin) != 4:
            print("Incorrect length for a pin. A pin is 4 digits long.")
            pintries += 1
            getInput(pintries)
        elif pin == "1234":
            print("Your pin is correct!")
            exit(0)
        else:
            print("Your pin is incorrect.")
            pintries += 1
            getInput(pintries)
    else:
        print("Your bank card is blocked!")
        exit(1)

if __name__=="__main__":
    pintries = 0
    getInput(pintries)
    exit(0)
