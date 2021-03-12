import random

class Player:

    def __init__(self, name):
        self.name = name

        self.position_x = 0
        self.position_y = 0

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
    maxDamaage = 30.0

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

    def getDamage(self):
        offset = random.uniform(-self.maxOffset, self.maxOffset)
        return self.damage + offset

    def randomizeEnemy(self, seed):
        random.seed(seed)
        nameIndex = random.randint(0, len(Enemy.EnemyTitles) - 1)
        self.name = list(Enemy.EnemyTitles.keys())[nameIndex]
        self.description = list(Enemy.EnemyTitles.values())[nameIndex]
        self.health = random.randint(50, 150)
        self.damage = random.uniform(Enemy.minimumDamage, Enemy.maxDamaage)


class Weapon:

    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

        self.description = ""