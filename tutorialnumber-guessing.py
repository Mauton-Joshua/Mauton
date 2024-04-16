# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 17:34:03 2023

@author: AYOOLUWA-MAUTON
"""
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
    """Checks guess against answer and returns the number of turns remaining"""
    if guess > answer:
        print("Too high. \n Guess again")
        return turns -1
    elif guess < answer:
        print("Too low. \n Guess again")
        return turns -1
    else:
        print(f"You got it! The answer was {answer}")

#Make function sto set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
    
def game():
    print("Welcome to the number guessing game")
    print("I'm thinking of a number between 1 and 100.")
    #Choosing a random number between 1 and 100.
    answer = randint(1, 100)
    print(f"The answer is {answer}")

    turns = set_difficulty()
    
    guess = 0
    
#Repeat the guessing functionality if they got it wrong
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        #Let the user guess a number.
        guess = int(input("Make a guess: "))

        #Make a function to compare user's guess against actual answer

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses. Game over, you lose.")
            return

        

game()    
    

#Track the number of user's and reduce by 1 if user got it wrong.
