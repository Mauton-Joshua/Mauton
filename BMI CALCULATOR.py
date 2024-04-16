# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 03:30:45 2023

@author: AYOOLUWA-MAUTON
"""

print("Hello there!, Welcome to the bmi calculator!")
weight = float(input("What is your current weight in kilograms?"))
height = float(input("What is your current height in metres?"))
bmi = round(weight/height**2)
if bmi <18.5:
    print(f"Your bmi is {bmi}, you are UNDERWEIGHT")
elif bmi <25:
    print(f"Your bmi is {bmi}, you have a NORMAL WEIGHT")
elif bmi <30:
    print(f"Your bmi is {bmi}, you are OVERWEIGHT")
elif bmi <35:
    print(f"Your bmi is {bmi}, you are OBESE")
else:
    print(f"Your bmi is {bmi}, you are CLINICALLY OVERWEIGHT")