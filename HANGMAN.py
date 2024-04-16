# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 09:21:45 2023

@author: AYOOLUWA-MAUTON
"""

import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
display = []
word_length = len(chosen_word)
lives = 6




for _ in range(word_length):
    display.append("_")
print(f'Pssst, the solution is {chosen_word}.')


end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
       
        letter = chosen_word[position]
        if letter == guess:
          display[position] = letter
    
    if guess not in chosen_word:
        lives -=1
        if lives == 0:
            end_of_game = True
        print(lives)
        print("You lose")
    
    
    print(display)
    
    print(f"{' '.join(display)}")
    
    if "_" not in display:
        end_of_game = True
        print("You win.")
        
        
    print(stages[lives])






