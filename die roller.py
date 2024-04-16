# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 18:37:17 2023

@author: AYOOLUWA-MAUTON
"""
import random
random_int = random.randint(1, 1000000000)
print(random_int)
import random
random_float = random.random()
print(random_float *12)
import random
random_dice = random.randint(1, 6)
if random_dice ==6:
    print("You may roll the die again")
elif random_dice ==5:
    print("Move up the ladder 5 times.")
elif random_dice ==4:
    print("Move up the ladder 4 times.")
elif random_dice ==3:
    print("Move up the ladder 3 times.")
elif random_dice ==2:
    print("Move up the ladder 2 times.")
else:
    print("Move up the ladder Once!.")