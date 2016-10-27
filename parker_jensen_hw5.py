#! /usr/bin/env pythons

pintries = 0

def getInput():
    """
    Attempts 3 times to receive the correct pin through user input
    Correct pin is 4 digits long
    """
    global pintries
    if pintries < 3:
        pin = input("Enter your pin...")
        if len(pin) != 4:
            print("Incorrect length for a pin. A pin is 4 digits long.")
            pintries += 1
            getInput()
        elif pin == "1234":
            print("Your pin is correct!")
            exit(0)
        else:
            print("Your pin is incorrect.")
            pintries += 1
            getInput()
    else:
        print("Your bank card is blocked!")
        exit(1)

def main():
    """
    test function
    """
    getInput()

if __name__=="__main__":
    main()
    exit(0)
