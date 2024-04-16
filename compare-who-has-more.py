# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 18:58:13 2023

@author: AYOOLUWA-MAUTON
"""

import random
from game_data import data
from art import logo, vs






def format_data(account):
    """Takes the account data and returns into printable format."""
    account_name = account["name"]
    account_desp = account["description"]
    account_country = account["country"]
    followers = data["follower_count"]
    return f"{account_name}, a {account_desp}, from {account_country}"


    
    




print(logo)


score = 0
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
  account_b = random.choice(data)

print(f"Compare A: {format_data(account_a)}.")
print(vs)
print(f"Against B: {format_data(account_b)}.")

guess = input("\n Who has the most followers on tiktok?").lower()