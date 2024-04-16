# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 04:45:41 2023

@author: AYOOLUWA-MAUTON
"""

std_scores = input("Input a list of student scores.").split()
print(std_scores)
highest_score = 0
for n in range(0, len(std_scores)):
    std_scores[n] = int(std_scores[n])
total_score = 0
for score in std_scores:
    total_score+= score
print (total_score)
no_of_std = 0
for std in std_scores:
    no_of_std+= 1
print(no_of_std)
average_score = total_score/no_of_std
print(f"The average score is: {average_score}")
for max_score in std_scores:
    if max_score > highest_score:
        highest_score = max_score
print(f"The highest score in the class is {highest_score}")
