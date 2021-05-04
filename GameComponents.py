# INF360 - Programming in Python
# Hunter Moore
# Midterm Project

import random

#This class stores information about a weapon
class Weapon:

    #Class construction
    def __init__(self, name, description, damage, maxOffset, critChance):
        self.name = name #Weapon name
        self.description = description #Weapon description
        self.damage = int(damage) #Weapon damage
        self.maxOffset = maxOffset #Max offset that the damage can deviate
        self.critChance = critChance #Critical hit chance of the weapon
    
    #This function will randomly generate a damage value based on the weapon
    def getAttackDamage(self):
        #Offset will store the offset that we will use for our damage
        offset = random.randint(-self.maxOffset, self.maxOffset)
        #Attack damage is the base damage plus the offset
        attackDamage = self.damage + offset
        
        #If our critChance is greater than a number between 0-1
        if self.critChance > random.uniform(0,1):
            #Our damage is doubled
            attackDamage *= 2
            #Notify player that a critical hit happened
            print("You hit a critical hit!")
        
        #Return the attackDamage
        return attackDamage
    
    #This function prints information about the weapon
    def printWeaponStats(self):
        print("Weapon Name: " + self.name)
        print("Description: " + self.description)
        print("Average Damage: " + str(self.damage))
        print("Critical Hit Chance: " + str(100*self.critChance) + "%")

#This is pre-defined weapons that we will be able to collect
bronzeSword = Weapon("Bronze Sword", "Low tier sword.", 10, 5, 0.01)
ironSword = Weapon("Iron Sword", "A good sword.", 20, 5, 0.02)
steelSword = Weapon("Steel Sword", "A high class sword.", 35, 10, 0.05)

magicWand = Weapon("Magic Wand", "A \"magic\" wand.", 30, 10, 0.1)
excalibur = Weapon("Excalibur", "Pulled from a stone.", 40, 15, 0.15)

bow = Weapon("Bow and Arrow", "A regular ranged bow and arrow.", 5, 20, 0.07)

fists = Weapon("Fists", "Just regular old fists. Gets the job done.", 15, 10, 0.03)
brick = Weapon("Brick", "Seems a bit crude don't you think? I mean a brick isn't even that good. Why are you using a brick?!?", 40, 10, 0.2)

#This is an array of all the weapons in the game
weapons = [
    bronzeSword, ironSword, steelSword, magicWand, excalibur, bow, fists, brick
]

#This is the player class
class Player:

    #Constructor (player name is basically obsolete)
    def __init__(self, name):
        #if name is not defined then it will default to player
        self.name = name or "Player"

        #Player's position
        self.position_x = 0
        self.position_y = 0

        #Player's weapon defaults to a bronze sword
        self.weapon = bronzeSword

        #Player health is defaulted to 100
        self.health = 100

    #This function prints basic information about the player
    def printPlayerInfo(self):
        print("Player: " + self.name)
        print("Health: " + str(self.health))
        print("Weapon: " + self.weapon.name)
        print("Weapon Description: " + self.weapon.description)
        print('\n', end='')

    #This function only prints out the player's health (the only stat)
    def printPlayerStats(self):
        print("Player Stats")
        print("Health: " + str(self.health))
        #print('\n', end='')

    #Take damage function takes a damageAmount and subtracts it from the player's health
    def takeDamage(self, damageAmount):
        self.health -= damageAmount

#Enemy class
class Enemy:

    #Enemy titles are names and descriptions for enemies
    EnemyTitles = {
        "Dragon": "A fire breathing lizzard!",
        "Goblin": "A small little green guy.",
        "Spider": "Scary!",
        "Knight": "He goes to knight school :D",
        "Werewolf": "Basically a dog.",
        "Bigfoot": "Wait he's real?!? Quick get your camera!",
        "Gnome": "Wait this might actually be a garden gnome.",
        "Troll": "Not the internet kind.",
        "Griffon": "Yeah it's a griffon.",
        "Tiger": "I hear he knows a great University!"
    }

    #Min and max damages achievable by an enemy
    minimumDamage = 5
    maxDamage = 20

    #Constructor (everything is set to default values)
    def __init__(self):
        self.name = ""
        self.description = ""
        self.health = 0
        self.damage = int(0)
        self.maxOffset = 5

    #This function prints out all information about the enemy
    def printEnemyInfo(self):
        print("Name: " + self.name)
        print("Description: " + self.description)
        print("Health: " + str(self.health))
        print("Damage: " + str(self.damage))
        print("MaxOffset: " + str(self.maxOffset))
    
    #This function only prints out stats the player needs to know
    def printEnemyStats(self):
        print("Name: " + self.name)
        print("Description: " + self.description)
        print("Health: " + str(self.health))

    #This function returns a randomly generated damage amount
    def getDamage(self):
        #Offset is a random number between -max and max
        offset = random.randint(-self.maxOffset, self.maxOffset)
        #Return damage plus the generated offset
        return self.damage + offset

    #Take damage takes damageAmount and subtracts it froms it's own health
    def takeDamage(self, damageAmount):
        #Remove health
        self.health -= damageAmount
        
        #If health is less than 0
        if self.health <= 0:
            del self #Delete itself       
        
    #This function randomizes it's own value
    def randomizeEnemy(self, seed):
        #Re-seed random (not nessissary)
        random.seed(seed)
        
        #Name index will be used to pick a title
        nameIndex = random.randint(0, len(Enemy.EnemyTitles) - 1)
        
        #Set the name to the key of enemy titles and index nameIndex
        self.name = list(Enemy.EnemyTitles.keys())[nameIndex]
        #Set the description to the the value of the key of name
        self.description = Enemy.EnemyTitles[self.name]

        #Randomize the health to be an integer from 25 to 150
        self.health = random.randint(25, 150)
        
        #Randomize the damage from minDamage to maxDamage
        self.damage = random.randint(Enemy.minimumDamage, Enemy.maxDamage)


