'''
Jayati Samar
Last edited: 12/5/22
CS 5001 - Lab09 - Epic Battle Simulator
Objective: This program creates a simple menu-driven battle simulator that has the user equip characters with weapons and then fight to the death against each other until there is a final winner.
'''

from character import Character
from weapon import Weapon
import copy as c

 
def main ():
    # Assign all characters their attributes
    c1 = Character("Juniper",40,5)
    c2 = Character("Foxglove",30,8)
    c3 = Character("Nightshade",45,3)
    c4 = Character("Oleander",35,7)
    # all_characters is used during weapon selection
    all_characters = [c1,c2,c3,c4]
    # character_menu is used when actually fighting
    character_menu = [c1,c2,c3,c4]

    # Assign all weapons their attributes
    w1 = Weapon("garrote",2,5)
    w2 = Weapon("glaive",3,3)
    w3 = Weapon("mace",2,4)
    w4 = Weapon("scythe",4,1)
    # all_weapons is used during weapon selection
    all_weapons = [w1,w2,w3,w4]

    # The following while loop is used to help assign weapons to all the characters - it continues until all_characters and all_weapons each have only element left
    while len(all_characters) != 1:
        print("Let's assign weapons to your characters! \nThe following is your choice of characters: \n") 
        
        # This for loop prints all the available characters without weapons assigned to them
        for character in all_characters:
            print((all_characters.index(character) + 1),") ",(character))
        
        character_choice = int(input("Please select the number of the character you'd like to start with.\n "))
        print("Great! Now let's decide what weapon you'd like to assign to ",all_characters[character_choice - 1])
        print("The following is your choice of weapons: \n")
        
        # This for loop prints all the available, unassigned weapons
        for weapon in all_weapons:
            print((all_weapons.index(weapon) + 1),") ",(weapon))
        
        weapon_choice = int(input("Please select the number of the weapon you'd like to assign. \n"))
        all_characters[character_choice - 1].set_weapon(all_weapons[weapon_choice - 1])
        print("Great! Here is your equipped character:",all_characters[character_choice - 1])
        all_characters.pop((character_choice - 1))
        all_weapons.pop((weapon_choice - 1))
    all_characters[0].set_weapon(all_weapons[0])
    print("By process of elimination, your final character is",all_characters[0])

    # This while loop is used to have the characters fight against each other - when the loop ends, only the winning character is in character_menu
    while len(character_menu) != 1:
        print("Now, let's have our characters fight each other! \nRemember: the character you choose first goes first, and weapons do NOT reset after every round, unlike the characters. \nHere are the available characters: \n")
        
        # This for loop prints all the characters that are not dead
        for character in character_menu:
            print((character_menu.index(character) + 1),") ",(character))
        selection1 = int(input("What number is your first choice?\n "))
        selection2 = int(input("What number is your second choice?\n "))
        
        # In the event that both selections are the same, the program prints a snarky message
        if selection1 == selection2:
            print("The rules of this game don't allow for angsty person vs. self battles at this time. This is a PvP arena only. Moving on!")
            continue

        # Copy the selections so that the character's hitpoints reset before each fight.
        first_fighter = c.copy(character_menu[selection1 - 1])
        second_fighter = c.copy(character_menu[selection2 - 1])
        first_fighter.fight(second_fighter)

        # The following if/else is used to only remove the character that actually lost
        if first_fighter.alive == True:
            character_menu.pop(selection2 - 1)
        else: character_menu.pop(selection1 - 1)
    print("The final winner is",character_menu[0])





main()