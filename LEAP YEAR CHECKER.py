# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 03:09:12 2023

@author: AYOOLUWA-MAUTON
"""

print("Hello!, Welcome to the leap year and number of days  checker")
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
  
# TODO: Add more code here 👇
def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  
  
  if year == True and month == 2:
    return 29
  elif month > index(month_days):
    return "Invalid input, please input the correct month number."
  else:
    return month_days[month - 1]
    

  
#🚨 Do NOT change any of the code below 
year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)

    
    