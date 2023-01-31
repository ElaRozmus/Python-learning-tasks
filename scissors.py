# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 08:47:37 2023

@author: rozmu
"""
import random
import time
import sys

user_choice = input("Enter your weapon: 'rock', 'paper', 'scissors' \n>>>").lower()

comp_list = ["rock", "paper", "scissors"]
comp_choice = random.choice(comp_list)
# print(comp_choice)

print(f'You chose {user_choice} \nComputer chose {comp_choice}')



if user_choice == comp_choice:
    print('Tie,you both select same')
elif user_choice == "rock" and comp_choice == "paper":
    print("You win")
elif user_choice == "rock" and comp_choice == "scissors":
    print("You win")
elif user_choice == "paper" and comp_choice == "rock":
    print("You loose")
elif user_choice == "paper" and comp_choice == "scissors":
    print("You loose")
elif user_choice == "scissors" and comp_choice == "rock":
    print("You loose")
elif user_choice == "scissors" and comp_choice == "paper":
    print("You win")
# %%

user_choice = input("Enter your weapon: 'rock', 'paper', 'scissors' \n>>>").lower()

comp_list = ["rock", "paper", "scissors"]
comp_choice = random.choice(comp_list)
#time.sleep(1)
print("\n")
print(f'You chose {user_choice} \nComputer chose {comp_choice}')
print("\n")

while True:
    if user_choice == comp_choice:
        time.sleep(1)
        print('Tie,you both select same')
    elif user_choice == "rock":
        if comp_choice == "paper":
            time.sleep(1)
            print("You win")
        elif comp_choice == "scissors":
            time.sleep(1)
            print("You win")
    elif user_choice == "paper":
        if comp_choice == "rock":
            time.sleep(1)
            print("You lose")
    elif comp_choice == "scissors":
        time.sleep(1)
        print("You lose")
    elif user_choice == "scissors":
        if comp_choice == "rock":
            time.sleep(1)
            print("You lose")
    elif comp_choice == "paper":
        time.sleep(1)
        print("You win")

    play_again = input("Do you want to play again? y/n \n>>>")
    if play_again !="y":
        sys.exit()
        
        
        






