import random

class Weapon:

    def __init__(self, name, description, damage, maxOffset, critChance):
        self.name = name
        self.description = description
        self.damage = damage
        self.maxOffset = maxOffset
        self.critChance = critChance
    
    def getAttackDamage(self):
        offset = random.uniform(0, self.maxOffset)
        attackDamage = self.damage + offset
        
        if self.critChance < random.uniform(0,1):
            attackDamage *= 2
            print("You hit a critical hit!")
        
        return attackDamage
    
    def printWeaponStats(self):
        print("Weapon Name: " + self.name)
        print("Description: " + self.description)
        print("Average Damage: " + str(self.damage))
        print("Critical Hit Chance: " + str(100*self.critChance) + "%")

bronzeSword = Weapon("Bronze Sword", "Low tier sword.", 10, 5, 0.01)
ironSword = Weapon("Iron Sword", "A good sword.", 20, 5, 0.02)
steelSword = Weapon("Steel Sword", "A high class sword.", 35, 10, 0.05)

magicWand = Weapon("Magic Wand", "A \"magic\" wand.", 30, 10, 0.1)
excalibur = Weapon("Excalibur", "Pulled from a stone.", 40, 15, 0.15)

bow = Weapon("Bow and Arrow", "A regular ranged bow and arrow.", 5, 20, 0.07)

fists = Weapon("Fists", "Just regular old fists. Gets the job done.", 15, 10, 0.03)
brick = Weapon("Brick", "Seems a bit crude don't you think? I mean a brick isn't even that good. Why are you using a brick?!?", 40, 10, 0.2)

#Todo: Order these from worst to best so we can smartly randomize the chance of getting good items
weapons = [
    bronzeSword, ironSword, steelSword, magicWand, excalibur, bow, fists, brick
]

class Player:

    def __init__(self, name):
        self.name = name or "Player"

        self.position_x = 0
        self.position_y = 0

        self.weapon = bronzeSword

        self.health = 100

    def printPlayerInfo(self):
        print("Player: " + self.name)
        print("Health: " + str(self.health))
        print("Weapon: " + self.weapon.name)
        print("Weapon Description: " + self.weapon.description)
        print('\n', end='')

    def printPlayerStats(self):
        print("Health: " + str(self.health))
        print('\n', end='')

    def takeDamage(self, damageAmount):
        self.health -= damageAmount

class Enemy:

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

    minimumDamage = 5.0
    maxDamage = 30.0

    def __init__(self):
        self.name = ""
        self.description = ""
        self.health = 0
        self.damage = 0
        self.maxOffset = 5.0

    def printEnemyInfo(self):
        print("Name: " + self.name)
        print("Description: " + self.description)
        print("Health: " + str(self.health))
        print("Damage: " + str(self.damage))
        print("MaxOffset: " + str(self.maxOffset))
        print('\n', end='')
    
    def printEnemyStats(self):
        print("Name: " + self.name)
        print("Description: " + self.description)
        print("Health: " + str(self.health))

    def getDamage(self):
        offset = random.uniform(-self.maxOffset, self.maxOffset)
        return self.damage + offset

    def takeDamage(self, damageAmount):
        self.health -= damageAmount
        
        if self.health <= 0:
            del self        
        

    def randomizeEnemy(self, seed):
        random.seed(seed)
        nameIndex = random.randint(0, len(Enemy.EnemyTitles) - 1)
        self.name = list(Enemy.EnemyTitles.keys())[nameIndex]
        self.description = list(Enemy.EnemyTitles.values())[nameIndex]
        self.health = random.randint(50, 150)
        self.damage = random.uniform(Enemy.minimumDamage, Enemy.maxDamage)


