import random

class World:

    def __init__(self, room, worldSeed, width, height):
        self.currentRoom = room
        self.worldSeed = worldSeed

        self.worldWidth = width
        self.worldHeight = height

    def printAllRooms(self, _currentRoom):
        _currentRoom.printRoomInfo()
        if _currentRoom.northRoom is not None or not _currentRoom.northRoom.isNone:
            self.printAllRooms(_currentRoom.northRoom)

        if _currentRoom.southRoom is not None or not _currentRoom.southRoom.isNone:
            self.printAllRooms(_currentRoom.northRoom)

        if _currentRoom.westRoom is not None or not _currentRoom.westRoom.isNone:
            self.printAllRooms(_currentRoom.northRoom)
        
        if _currentRoom.eastRoom is not None or not _currentRoom.eastRoom.isNone:
            self.printAllRooms(_currentRoom.northRoom)

class Room:

    #Constructor for Room
    #posx is the position x component
    #posy is the position y component
    def __init__(self, posx, posy):
        self.isNone = False
        self.isEnd = False

        self.position_x = posx
        self.position_y = posy

        self.northRoom = None
        self.southRoom = None
        self.westRoom = None
        self.eastRoom = None

    def printRoomInfo(self):
        print("Position X: " + str(self.position_x) + " Y: " + str(self.position_y))
        print("IsNone: " + str(self.isNone))
        print("IsEnd: " + str(self.isEnd))

    #This generates a random room based on a seed
    @staticmethod
    def generateRoomFromSeed(seed, posx, posy):
        room = Room(posx, posy)

        random.seed(seed)
        if random.randint(0,100) < 20:
            room.isNone = True
            return room

        return room

    @staticmethod
    def generateEndingRoom(posx, posy):
        room = Room(posx, posy)
        room.isEnd = True

        return room

    @staticmethod
    def generateStartingRoom(posx = 0, posy = 0):
        room = Room(posx, posy)
        
        return room