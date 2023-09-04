# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 05:08:27 2023

@author: AYOOLUWA-MAUTON
"""

class Item:
    def __init__(self, name: str, sound: str, base_sound= "Hiss"):
        self.name = name.upper()
        self.sound = sound.upper()
        self.base_sound = base_sound.upper()
        
    def assign_animal_sound(self):

       Animals_in_a_zoo = ["Lion", "Giant Panda", "Tiger", "Cheetah", "Elephant", "Red panda", "Ostriches", "Wolf", "Komodo Dragon", "Orangutans", "Gila Monster", "Eagles", "Snakes", "Gorrillas", "Hippo", "Crocodiles", "Parrots", "Chickens", "Camels", "Giraffe", "Bobcat", "Hyenas", "Monkey", "Penguins", "Cow"].upper()
       Sounds_of_zoo_animals = ["Roar", "Honks", "Growl", "Gargles", "Trumpets", "Grunt", "Whistles", "Howl", "Hiss", "Long call", "Hiss", "Screech", "Hiss", "Hoot", "Growl", "Hiss", "Squawk", "Cluck", "Grunt", "Bleat", "Snarl", "Laugh", "Chatter", "Honk", "Moo"].upper()
       base_sound = "Hiss"
       animal_sounds = input("Which animal sound would you like to know?")
       if animal_sounds == Animals_in_a_zoo[8]:
           print(f"The animal you have selected makes the sound{base_sound}")
           
       
        
