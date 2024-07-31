'''
Jayati Samar
Last edited: 12/5/22
Associated with: CS 5001 - Lab09 - Epic Battle Simulator
Objective: This file creates a Character class originally created for use with the Epic Battle Simulator lab.
'''

import random as r
from weapon import Weapon

class Character:
    '''
    The Character class is used to setup and design characters with the attributes name, hit_points, strength, and weapon. 
    The created objects (characters) can take damage, fight, and be given a weapon.
    '''
    
    '''
    This is the constructor - it is used to set the initial values of a created Character.
    The character has the following parameters: name, hit_points, strength, alive, and weapon.
    All of the attributes can be sent in by the user except for alive - the character defaults to alive.
    name: name of the character, defaulting to "Ward"
    hit_points: hit_points of the character, defaulting to 5
    strength: strength of the character, defaulting to 5'
    alive: this defaults to true and indicates that the character is alive.
    weapon: the character's assigned weapon, if they have one. This defaults as none.
    '''
    def __init__(self,name="Ward",hit_points=5,strength=5,weapon=""):
        self.name = name
        self.hit_points = hit_points
        self.strength = strength
        self.alive = True
        self.weapon = weapon
    
    '''
    take_damage subtracts the amount of damage the character takes from the character's hit points, unless the character's hit points are 0 or would be less than 0.
    self refers to the character
    damage refers to how much the character's hit_points should be decreased by, so long as the end result isn't less than 0.
    take_damage decreases the character's hit_points by damage and returns that value for the hit_points. If less than 0, the hit_points are set to 0. Once the hit_points are 0 or less, the character is marked as dead.
    '''
    def take_damage(self,damage):
        self.hit_points -= damage
        # the character isn't allowed to have less than 0 hit_points, so this if statement remedies that. Additionally, hit_points <= 0 indicate the character is dead, so self.alive is set to False.
        if self.hit_points <= 0:
            self.alive = False
            self.hit_points = 0
    
    '''
    fight has two characters fight each other until one of them is no longer alive. It prints how much damage each character takes each round, how many rounds they fight, and who the winner is.
    self is the character
    opponent is the other character that is being fought
    In this method, self and opponent fight each other by each taking damage until one is no longer alive. Each iteration of the loop is treated as one round of the fight, and is printed as such, as is the amount of damage each character takes and the final winner.
    '''
    def fight(self,opponent):
        counter = 1

        # In this while loop, as long as both characters are alive, they will keep fighting
        while(self.alive and opponent.alive):
            print("Round",counter) # prints the number of the round, starting at 1
            self_attack = self.strength + Weapon.attack(self.weapon)
            opponent.take_damage(self_attack)
            print(opponent.name,"took",self_attack,"damage!")

            if not opponent.alive: break # If the opponent character is no longer alive, the loop breaks
            opponent_attack = opponent.strength + Weapon.attack(opponent.weapon)
            self.take_damage(opponent_attack)
            print(self.name,"took",opponent_attack,"damage!")
            counter += 1
        
        # Once one of the characters is dead, the while loop is broken and this method prints the number of rounds of combat and the winner.
        print("After",counter,"rounds of combat, the winner is:")
        if self.alive: print(self)
        else: print(opponent)


    '''
    set_weapon is used to assign a weapon to the character.
    self is the character
    weapon is the weapon being assigned from the Weapons class.
    In this method, a weapon is assigned to the character from the weapon's class and becomes part of its attributes
    '''        
    def set_weapon(self,weapon):
        self.weapon = weapon


    '''
    __str__ is the print method of this class. 
    In order, it prints the name, hit_points, strength, alive/dead status, and weapon of the character in question
    '''
    def __str__(self):
        return self.name + " " + str(self.hit_points) + " " + str(self.strength) + " " + str(self.alive) + " " + str(self.weapon)
        