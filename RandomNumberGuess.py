import random
from click import prompt

randNum = random.randint(1,5)
tries = 0
while True:
    num = prompt("Enter number")
    if(int(num) == randNum):
        print("You won")
        break
    else:
        tries = tries + 1
        print("Try again: %s"%tries)
        if(tries >= 5):
            print("Better luck next time")
            break