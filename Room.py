import random

class Room:

    def __init__(self):
        self.isNone = False
        self.isEnd = False

    @staticmethod
    def generateRoomFromSeed(seed):
        room = Room()

        random.seed(seed)
        if random.randint(0,100) < 20:
            room.isNone = True
            return room

        return room

    @staticmethod
    def generateEndingRoom():
        room = Room()
        room.isEnd = True

        return room

    @staticmethod
    def generateStartingRoom():
        room = Room()
        
        return room