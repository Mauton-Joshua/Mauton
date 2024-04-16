# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 13:38:37 2023

@author: AYOOLUWA-MAUTON
"""

import random
R= "rock"
P= "paper"
S= "scissors"
game_RPS = [R, P, S]
user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for Scissors.\n"))
if user_choice >= 3 or user_choice <0:
    print("Invalid number. You lose!")
else:
    print("You chose:")
    print (game_RPS[user_choice])
    comp_choice = random.randint(0, 2)
    print("Computer chose:")
    print (game_RPS[comp_choice])
    
    if user_choice == comp_choice:
        print("It is a draw!")
    elif user_choice == 0 and comp_choice == 2:
        print("You chose rock. You win!")
    elif comp_choice ==0 and user_choice == 2:
        print("You chose scissors. You lose!")
    elif user_choice > comp_choice:
        print("You win!")
    elif comp_choice > user_choice:
        print("You lose!")
        
        