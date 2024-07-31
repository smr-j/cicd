'''
Jayati Samar
Last edited: 12/5/22
Associated with: CS 5001 - Lab09 - Epic Battle Simulator
Objective: This file creates a Weapon class originally created for use with the Epic Battle Simulator lab.
'''

import random as r

class Weapon:
    '''
    The Weapon class is used to setup and design weapons with the attributes name, strength, and durability. 
    The created objects (weapons) can attack.
    '''
    
    '''
    This is the constructor - it is used to set the initial values of a created Weapon.
    The Weapon has the following parameters: name, strength, and durability.
    All of the attributes can be sent in by the user.
    name: name of the Weapon, defaulting to "generic dagger"
    strength: strength of the Weapon, defaulting to 1
    durability: the durability of the Weapon - decides how much it can be used. This defaults to 2
    The constructor creates a Weapon with name, strength, and durability
    '''
    def __init__(self,name="generic dagger",strength=1,durability=2):
        self.name = name
        self.strength = strength
        self.durability = durability
        
    '''
    with attack, the weapon returns a value between one and its strength value, with the durability decreasing by 1 every time the weapon is used. Once durability is 0, the weapon returns 0.
    self is the weapon
    While the weapon's durability is not 0, attack returns a random value between 1 and the strength of the weapon. Once the weapon's durability is 0, attack returns a value of 0.
    '''
    def attack(self):
        if self.durability > 0:
            self.durability -= 1
            return r.randint(1,self.strength)
        else: return 0
            
    '''
    __str__ is the print method of this class and prints the name, strength, and durability of the weapon in that order
    '''
    def __str__(self):
        return self.name + " " + str(self.strength) + " " + str(self.durability)