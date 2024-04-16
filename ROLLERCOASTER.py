# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 04:42:38 2023

@author: AYOOLUWA-MAUTON
"""

print("Hello welcome to the rollercoaster ride!")
H = int(input("What is your current height in centimetres?"))
bill =0
if H >=120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your current age?"))
    if age <=12:
        bill +=5
        print("Child tickets are $5")
    elif age <=18:
        bill +=7
        print("Youth tickets are $7")
    elif age >=45 and age <=55:
        print("Everything is going to be okay, have a fun ride! It's on the house!")
    else:
        bill +=12
        print("Adult tickets are $12")
        
    wants_photos =input("Do you want pictures taken? Y, or N?")
    if wants_photos =="Y":
        bill +=3
        print(f"Your final bill is ${bill}")
    else:
        print(f"Your final bill is {bill}")
else:
    print("You are not elligible to ride the rollercoaster!")