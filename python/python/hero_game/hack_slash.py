'''

Python 2

Author: Santiago Beltran

Going to make a text game where there is a hero
fighting off an infinante amount of monsters
'''
import random, hero_class

def start(hero = "", health = 10, attack = 3):
    hero = intro_game(hero, health, attack)
    smonster = intro_monsters(smonster = "", smhealth = 3, smattack = 1)

def intro_game(hero, health, attack):
    if hero != "": #if statment
        print('Welcome back hereo {}!'.format(hero)) #Printing out a value with .format
        print('Your current stats are (health:{}, attack{})').format(health,attack)
    else:
        new_hero= True
        while new_hero:
            if hero == "":
                hero = raw_input('\nWhat is your name hero?').capitalize()
                print('\nWelcome Hero {}!').format(hero)
                print('\nThis world is filled with monsters that require slaying')
                print('\nThe world looks to you for your stragnth')
                print('\nYou have {} health and {} attack').format(health,attack)
                print('\nThe further you get, the stronger you will become')
                new_hero = False
                
    return hero

monster_tuple = ("Bat", "Cub", "Grunt", "Goblin"); # Tuple

def intro_monsters(smonster, smhealth, smattack):
    for smonster in monster_tuple:
        print("\nAt your current state you can only handle these foes: "+smonster)
    


'''
This is a tuple that contain the name of the monsters you will fight.
I have an idea of having diffrent dificulties of monsters. but for now
just this one set until i have more time and figure out how to do this.
'''


'''monster_tuple = ("Bat", "Cub", "Grunt", "Goblin"); # Tuple

def fight(hero, health, attack):
    for monster in monster_tuple:
        print('\nYou are attacked by a {}.').format(random.choice(monster_tuple))
        battle_option = raw_input("Do you wish to fight? y/n: ")

        if battle_option == ('y'):
            print('\nYou strike the {} and do {} damage').format(random.choice(monster_tuple),attack)
            print('\nBut you also substain 1 damage')

        elif battle_option == ('n'):
            print('\nYou flee the scene')
'''


bob = hero_class.hero("bob")
print jim.name
jim.get_name()
print jim.health



