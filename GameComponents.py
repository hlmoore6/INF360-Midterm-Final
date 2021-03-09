import random

class Player:

    def __init__(name):
        self.name = name

        self.position_x = 0
        self.position_y = 0

class Enemy:

    def __init__(name, health, damage, maxOffset = 0):
        self.name = name
        self.health = health
        self.damage = damage
        self.maxOffset = maxOffset

        self.description = ""

    def getDamage():
        offset = random.uniform(-maxOffset, maxOffset)
        return self.damage + offset

class Weapon:

    def __init__(name, damage):
        self.name = name
        self.damage = damage

        self.description = ""