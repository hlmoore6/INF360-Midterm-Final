import random
import World

#This class generates levels for the game and keeps


class WorldGenderator:
    def generateWorld(self, width, height, seed=0):
        self.worldSeed = seed
        random.seed(self.worldSeed)

        self.width = width
        self.height = height

        self.takenPositions = list()

        self.originRoom = self.generateRoomLayout()

        self.pickEndRoom(random.randrange(0,100))

        world = World.World(self.originRoom, self.worldSeed, self.width, self.height)

        return world

    def generateRoomLayout(self):
        #Set starting room in the middle of the rooms list
        startingRoom = World.Room.generateStartingRoom(self.width//2, self.height//2)

        #Add the starting room positions to the takenPositions tracker
        self.takenPositions.append((startingRoom.position_x, startingRoom.position_y))

        #This function recursivley calls itself to generate rooms adjacent to itself
        self.generateLocalRooms(startingRoom, 0, 5)
        
        return startingRoom

    #This function recursivley calls itself to generate rooms adjacent to itself
    #room is the current room
    #level is current recursion iteration
    #maxLevel is the max number of recursions allowed
    def generateLocalRooms(self, room, level, maxLevel):
        if level > maxLevel:
            return

        if room.isNone:
            return

        #Generate North

        request_y = room.position_y+1
        request_x = room.position_x
        if request_y < self.height and request_y >= 0 and not self.checkTaken((request_x,request_y), self.takenPositions):
            self.takenPositions.append((request_x,request_y))
            newRoom = World.Room.generateRoomFromSeed(random.randrange(0,100), request_x, request_y)
            room.northRoom = newRoom
            newRoom.southRoom = room
            if(not newRoom.isNone):
                self.generateLocalRooms(newRoom, level + 1, maxLevel)

        #Generate South

        request_y = room.position_y-1
        request_x = room.position_x

        if request_y < self.height and request_y >= 0 and not self.checkTaken((request_x,request_y), self.takenPositions):
            self.takenPositions.append((request_x,request_y))
            newRoom = World.Room.generateRoomFromSeed(random.randrange(0,100), request_x, request_y)
            room.southRoom = newRoom
            newRoom.northRoom = room
            if(not newRoom.isNone):
                self.generateLocalRooms(newRoom, level + 1, maxLevel)

        #Generate West

        request_y = room.position_y
        request_x = room.position_x - 1

        if request_x < self.width and request_x >= 0 and not self.checkTaken((request_x,request_y), self.takenPositions):
            self.takenPositions.append((request_x,request_y))
            newRoom = World.Room.generateRoomFromSeed(random.randrange(0,100), request_x, request_y)
            room.westRoom = newRoom
            newRoom.eastRoom = room
            if(not newRoom.isNone):
                self.generateLocalRooms(newRoom, level + 1, maxLevel)

        #Generate East

        request_y = room.position_y
        request_x = room.position_x + 1

        if request_x < self.width and request_x >= 0 and not self.checkTaken((request_x,request_y), self.takenPositions):
            self.takenPositions.append((request_x,request_y))
            newRoom = World.Room.generateRoomFromSeed(random.randrange(0,100), request_x, request_y)
            room.eastRoom = newRoom
            newRoom.westRoom = room
            if(not newRoom.isNone):
                self.generateLocalRooms(newRoom, level + 1, maxLevel)

    def pickEndRoom(self, seed):
        random.seed(seed)
        
        currRoom = self.originRoom

        minDistance = (self.width + self.height)//2

        originPos_x = self.originRoom.position_x
        originPos_y = self.originRoom.position_y

        while True:
            distance = 
            abs(currRoom.position_x - self.originRoom.position_x) + 
            abs(currRoom.position_y - self.originRoom.position_y)

            if distance => minDistance:
                



    #Returns True if a position was taken
    def checkTaken(self, positionRequest, takenPositions):
        #For every tuple in self.takenPositions
        for t in self.takenPositions:
            #We check if our requested position is already taken
            if positionRequest == t:
                return True #If it was taken then return True
        return False #If we pass all of the tests the we return False