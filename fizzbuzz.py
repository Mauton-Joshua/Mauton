# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 08:23:59 2023

@author: AYOOLUWA-MAUTON
"""

for number in range(1, 101):
    if number % 5 ==0 and number % 3 ==0:
        print("Fizz Buzz")
    elif number % 5 ==0:
        print("Buzz")
    elif number % 3 ==0:
        print("Fizz")
    else:
        print(number)