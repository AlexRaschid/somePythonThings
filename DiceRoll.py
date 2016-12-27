import random

def rollDice():
    return random.randint(1,6)

x = 0
while (x != 6):
    x = rollDice()
    print(x)
