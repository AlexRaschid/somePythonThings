import random


def rollDice():
    return random.randint(1,6)

x = rollDice()
userInput = input("There is a random number between 1-6, guess it: ")
print(userInput)



answer = False


while(answer == False):
    
    if(x == userInput):
        print("You got it correct!")
        answer = True
    else:
        print("Try again")
        userInput = input("What number is it?" )
