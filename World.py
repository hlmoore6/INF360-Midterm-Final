import random
import GameComponents

#The world class handles the storage of Rooms and holds data about the world
class World:

    #Constructor
    def __init__(self, room, worldSeed, width, height):
        self.currentRoom = room
        self.worldSeed = worldSeed

        self.worldWidth = width
        self.worldHeight = height

    #This is a debug function that prints every room's room information
    def printAllRooms(self, _currentRoom, parentRoom = None):
        #Print the _currentRoom(parameter) info
        _currentRoom.printRoomInfo()

        #If theres a north room
        if _currentRoom.northRoom is not None:
            #If the north room is not the parentRoom(parameter)
            if _currentRoom.northRoom != parentRoom:
                #Recursivley print the northroom with current room as parent
                self.printAllRooms(_currentRoom.northRoom, _currentRoom)
        
        #The rest of these if statements are the same except with different cardinal directions
        #The rest of these if statements are the same except with different cardinal directions
        #The rest of these if statements are the same except with different cardinal directions

        if _currentRoom.southRoom is not None:
            if not _currentRoom.southRoom.isNone and _currentRoom.southRoom != parentRoom:
                self.printAllRooms(_currentRoom.southRoom, _currentRoom)

        if _currentRoom.westRoom is not None:
            if not _currentRoom.westRoom.isNone and _currentRoom.westRoom != parentRoom:
                self.printAllRooms(_currentRoom.westRoom, _currentRoom)
        
        if _currentRoom.eastRoom is not None:
            if not _currentRoom.eastRoom.isNone and _currentRoom.eastRoom != parentRoom:
                self.printAllRooms(_currentRoom.eastRoom, _currentRoom)

    #This function returns a room from the current room in direction dir
    def getRoomFromDirection(self, dir):
        
        #Theses if statments just compare from 0-3 and return the respective room cardinal direction
        if dir == 0:
            return self.currentRoom.northRoom
        elif dir == 1:
            return self.currentRoom.southRoom
        elif dir == 2:
            return self.currentRoom.westRoom
        elif dir == 3:
            return self.currentRoom.eastRoom

        #These if statments do the same thing as the ones before except they compare with strings
        if dir == "north":
            return self.currentRoom.northRoom
        elif dir == "south":
            return self.currentRoom.southRoom
        elif dir == "west":
            return self.currentRoom.westRoom
        elif dir == "east":
            return self.currentRoom.eastRoom
        
        #If dir did not match any of the above just return none
        return None

    #This is a helper method that just compares if the room is equal to None
    @staticmethod
    def checkAvailability(room):
        #Return the opposite of room == None
        #If room is none then return false
        #If room is a real room then return true
        return not room == None
    
    #This changes the current room to parameter room
    def moveRoom(self, room):
        #If the room is not a real room then return false
        if not World.checkAvailability(room):
            return False
        
        #Otherwise change the current room
        self.currentRoom = room
        return True #Return false
    
class Room:

    #NoneChance is the chance that a room when created will not be a room
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

    #This is a debug function that just prints details about the current room
    def printRoomInfo(self):
        print("Position X: " + str(self.position_x) + " Y: " + str(self.position_y))
        print("IsEnd: " + str(self.isEnd))
        print('\n', end='')

    #This function prints information about the enemy in the room
    def printEnemyInfo(self):
        #If there is an enemy
        if self.enemy is not None:
            #Print the enemy's info
            self.enemy.printEnemyStats()
            return #Return out of function
        
        #Otherwise there is no enemy
        print("There is no enemy in the room!")

    #This function prints the current path's the player can take in the current room
    def printRoomOptions(self):
        #This is a list that contains the cardinal directions a player can go
        options = list()

        #This block of if statements will add cardinal directions to options if they're availble
        #If northRoom is a room
        if self.northRoom != None:
            #Append the cardinal direction to the list of directions
            options.append("North")
        
        if self.southRoom != None:
            options.append("South")

        if self.westRoom != None:
            options.append("West")
        
        if self.eastRoom != None:
            options.append("East")

        #Print out the beginning
        print("There is a room to the ", end='')
        
        #For every direction in options
        for dir in options:
            #Add that direction to the message
            print(dir + " ", end='')

        print('\n', end='')

    #This generates a random room based on a seed
    @staticmethod
    def generateRoomFromSeed(seed, posx, posy):
        #Re-seed random just to add more randomness (not nessissarily needed)
        random.seed(seed)
        
        #If a random integer between 0-100 is less than NoneChance
        if random.randint(0,100) < Room.NoneChance:
            #Return nothing
            return None

        #Create variable room and initialize it's position
        room = Room(posx, posy)
        
        #Add an enemy to the room
        room.enemy = GameComponents.Enemy()
        #Randomize that enemy
        room.enemy.randomizeEnemy(random.randint(0,100))

        #Return the newly created room
        return room

    #This function makes a room the end room
    @staticmethod
    def generateEndingRoom(room):
        room.isEnd = True

    #This function returns a room that has no enemy and is not the ending room
    @staticmethod
    def generateStartingRoom(posx = 0, posy = 0):
        room = Room(posx, posy)
        
        return room