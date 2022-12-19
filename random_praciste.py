# -*- coding: utf-8 -*-
  
import random

print("           Game name: Three chances")
print("*"*30)
print("Game rules: You have three chances to guess one number. Enjoy!")

status = True
chance = 1
while status:
    guess = int(input("Guess a number between 1-9: "))
    randomNumber = random.randint(1,9)
    if guess == randomNumber:
        print("Great you just guess a number")
        chance += 1
    elif guess > randomNumber:
        print("your number is too high")
        print("Right number is: {}".format(randomNumber))
        chance += 1
    elif guess < randomNumber:
        print("your number is too low")
        print("Right number is: {}".format(randomNumber))
        chance += 1
    if chance > 3: 
        check = int(input("""If you want to exit press: 1  
if you want to continue press: 2
Space for your decision: """))
    if check == 1:
        status = False
    elif check == 2:
        continue

  