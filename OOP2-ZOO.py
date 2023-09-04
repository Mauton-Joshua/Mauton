# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 07:11:27 2023

@author: AYOOLUWA-MAUTON
"""

class Animals:
    def __init__(self, name, respiratory, childbirth):
        self.name = name
        self.respiratory = respiratory
        self.childbirth = childbirth
        
    def view(self):
        print(self.name, self.respiratory, self.childbirth)
        
class Mammals(Animals):
    def __init__(self,name, respiratory, childbirth):
        Animals.__init__(self, name, respiratory, childbirth)
        self.name = "Mammal"
        self.respiratory = "Lungs"
        self.childbirth = "Viviparous"
        print("This is a mammalian animal")
        
class Reptiles(Animals):
    def __init__(self, name, respiratory, childbirth):
        Animals.__init__(self, name, respiratory, childbirth)
        self.name = "Reptile"
        self.respiratory = "Lungs"
        self.childbirth = "Oviparous"
        print("This is a reptile")
        
class Amphibians(Animals):
    def __init__(self, name, respiratory, childbirth):
        Animals.__init__(name, respiratory, childbirth)
        self.name = "Amphibian"
        self.respiratory = "Lungs and skiin"
        self.childbirth = "Viviparous"
        print("This is an amphibian")

       