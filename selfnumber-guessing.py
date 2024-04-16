# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 22:50:22 2023

@author: AYOOLUWA-MAUTON
"""
import random
from random import randint
EASY = 7
HARD = 3
end_of_game = False
print("Welcome to the number guessing game")
print("I'm thinking of a number between 1 and 100.")

def easy_mode():
    ran_number_guess = randint(1, 100)
    print(ran_number_guess)
    end_easy = False
    _lives = 7
    while not end_easy:
        guess_easy = int(input("Guess a number between '1' and '100': "))
        
        if guess_easy > ran_number_guess:
            _lives -=1
            print(f"You have {_lives} lives left ")
            print(" Too high, pick a lower number")
        elif guess_easy < ran_number_guess:
            _lives -=1
            print(f"You have {_lives} lives left ")
            print("Too low, pick a higher number")
        elif guess_easy == ran_number_guess:
            end_easy = True
            return "You have guessed the number correctly"
        
        elif _lives == 0:
            print(f"You have {_lives} lives left, game has ended")
            end_easy = True
        
            


def hard_mode():
    ran_number_guess = randint(1, 100)
    print(ran_number_guess)
    end_hard = False
    h_lives = 3
    while not end_hard:
        guess_hard = int(input("Guess a number between '1' and '100': "))
        if guess_hard > ran_number_guess:
            h_lives -=1
            print(f"You have {h_lives} lives left")
            print("Too high, pick a lower number")
        elif guess_hard < ran_number_guess:
            h_lives -=1
            print(f"You have {h_lives} lives left")
            print("Too low, pick a higher number")
        elif guess_hard == ran_number_guess:
            return "You have guessed the number correctly"
            end_hard = True
        elif h_lives == 0:
            print(f"You have {h_lives} lives left, game has ended")
            end_hard = True
            



def number_guessing_game():
    difficulty_level = input("Choose a difficulty, type 'easy' or 'hard': ")
    if difficulty_level == "hard":
        return hard_mode()
        
    else:
        return easy_mode()
        
        
        
    

    
    

    
    

        
    
    
number_guessing_game()   
    
    