# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 16:49:38 2023

@author: AYOOLUWA-MAUTON
"""

row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
t_map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}\n")
position =input("Where do you want to put the treasure?")
horizontal = int(position[0])
vertical = int(position[1])
sel_row = t_map[vertical -1]
sel_row[horizontal -1] ="X"
print(f"{row1}\n{row2}\n{row3}")