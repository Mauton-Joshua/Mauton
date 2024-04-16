# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 04:00:28 2023

@author: AYOOLUWA-MAUTON
"""

print("Welcome to  ASH THERAPY")
FB =5000
BSN =3500
NS =3000
Massage_pick = input("Which of our massage therapies would you like? FB, BSN, or NS")

if Massage_pick =="FB":
    bill =FB
elif Massage_pick =="BSN":
    bill =BSN
elif Massage_pick =="NS":
    bill =NS
time_ext = input("Would you like to extend your time? Y or N")
if time_ext =="Y":
    ext_time1 =500
    ext_time2 =1000
    ext_time3 =1500
    ext_time4 =2000
    ext = input("How long will your session extend? 5, 10, 15")
    if ext =="5":
        bill +=ext_time1
    elif ext =="10":
        bill +=ext_time2
    elif ext =="15":
        bill +=ext_time3
    print(f"Your bill is {bill}")
else:
    print(f"Your bill is {bill}")
        

    

    
    
    