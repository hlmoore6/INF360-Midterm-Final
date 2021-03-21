import random
import GameComponents

#The world class handles the storage of Rooms and holds data about the world
class World:

    def __init__(self, room, worldSeed, width, height):
        self.currentRoom = room
        self.worldSeed = worldSeed

        self.worldWidth = width
        self.worldHeight = height

    def printAllRooms(self, _currentRoom, parentRoom = None):
        _currentRoom.printRoomInfo()

        if _currentRoom.northRoom is not None:
            if not _currentRoom.northRoom.isNone and _currentRoom.northRoom != parentRoom:
                self.printAllRooms(_currentRoom.northRoom, _currentRoom)
        
        if _currentRoom.southRoom is not None:
            if not _currentRoom.southRoom.isNone and _currentRoom.southRoom != parentRoom:
                self.printAllRooms(_currentRoom.southRoom, _currentRoom)

        if _currentRoom.westRoom is not None:
            if not _currentRoom.westRoom.isNone and _currentRoom.westRoom != parentRoom:
                self.printAllRooms(_currentRoom.westRoom, _currentRoom)
        
        if _currentRoom.eastRoom is not None:
            if not _currentRoom.eastRoom.isNone and _currentRoom.eastRoom != parentRoom:
                self.printAllRooms(_currentRoom.eastRoom, _currentRoom)

    def getRoomFromDirection(self, dir):
        if dir == 0:
            return self.currentRoom.northRoom
        elif dir == 1:
            return self.currentRoom.southRoom
        elif dir == 2:
            return self.currentRoom.westRoom
        elif dir == 3:
            return self.currentRoom.eastRoom

        if dir == "north":
            return self.currentRoom.northRoom
        elif dir == "south":
            return self.currentRoom.southRoom
        elif dir == "west":
            return self.currentRoom.westRoom
        elif dir == "east":
            return self.currentRoom.eastRoom
        
        return None

    @staticmethod
    def checkAvailability(room):
        if room == None:
            return False
        
        return True
    
    def moveRoom(self, room):
        if not World.checkAvailability(room):
            return False
        
        self.currentRoom = room
        return True
    
class Room:

    NoneChance = 20

    #Constructor for Room
    #posx is the position x component
    #posy is the position y component
    def __init__(self, posx, posy):
        self.isEnd = False

        self.position_x = posx
        self.position_y = posy

        self.northRoom = None
        self.southRoom = None
        self.westRoom = None
        self.eastRoom = None

        self.enemy = None

    def printRoomInfo(self):
        print("Position X: " + str(self.position_x) + " Y: " + str(self.position_y))
        print("IsEnd: " + str(self.isEnd))
        print('\n', end='')

    def printEnemyInfo(self):
        if self.enemy is not None:
            self.enemy.printEnemyInfo()
        else:
            print("There is no enemy in the room!")

    def printRoomOptions(self):
        options = list()

        if self.northRoom != None:
            options.append("North")
        
        if self.southRoom != None:
            options.append("South")

        if self.westRoom != None:
            options.append("West")
        
        if self.eastRoom != None:
            options.append("East")

        print("There is a room to the ", end='')
        for dir in options:
            print(dir + " ", end='')
        print('\n', end='')

    #This generates a random room based on a seed
    @staticmethod
    def generateRoomFromSeed(seed, posx, posy):
        room = Room(posx, posy)

        random.seed(seed)
        
        if random.randint(0,100) < Room.NoneChance:
            return None
        
        room.enemy = GameComponents.Enemy()
        room.enemy.randomizeEnemy(random.randint(0,100))

        return room

    @staticmethod
    def generateEndingRoom(room):
        room.isEnd = True

    @staticmethod
    def generateStartingRoom(posx = 0, posy = 0):
        room = Room(posx, posy)
        
        return room