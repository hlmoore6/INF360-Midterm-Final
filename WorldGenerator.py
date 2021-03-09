import random
import World

#This class generates levels for the game and keeps


class WorldGenderator:
    def generateWorld(self, width, height, seed=0):
        self.worldSeed = seed

        self.width = width
        self.height = height

        originRoom = self.generateRoomLayout()

        world = World.World(originRoom, self.worldSeed, self.width, self.height)

        return world

    def generateRoomLayout(self):
        random.seed(self.worldSeed)
        rooms_seed = random.randrange(0, 100)

        #Set starting room in the middle of the rooms list
        startingRoom = World.Room.generateStartingRoom(self.width//2, self.height//2)

        #This function recursivley calls itself to generate rooms adjacent to itself
        self.generateLocalRooms(startingRoom, 0, 10)
        
        return startingRoom

    #This function recursivley calls itself to generate rooms adjacent to itself
    #room is the current room
    #level is current recursion iteration
    #maxLevel is the max number of recursions allowed
    def generateLocalRooms(self, room, level, maxLevel):
        if level > maxLevel:
            return

        takenPositions = list()

        #Generate North

        request_y = room.position_y+1
        request_x = room.position_x

        if request_y < self.height or request_y >= 0 and not self.checkTaken((request_x,request_y), takenPositions):
            takenPositions.append((request_x,request_y))
            newRoom = World.Room.generateRoomFromSeed(random.randrange(0,100), request_x, request_y)
            room.northRoom = newRoom
            newRoom.southRoom = room
            if(newRoom.isNone):
                self.generateLocalRooms(newRoom, level + 1, maxLevel)

        #Generate South

        request_y = room.position_y-1
        request_x = room.position_x

        if request_y < self.height or request_y >= 0 and not self.checkTaken((request_x,request_y), takenPositions):
            takenPositions.append((request_x,request_y))
            newRoom = World.Room.generateRoomFromSeed(random.randrange(0,100), request_x, request_y)
            room.southRoom = newRoom
            newRoom.northRoom = room
            if(newRoom.isNone):
                self.generateLocalRooms(newRoom, level + 1, maxLevel)

        #Generate West

        request_y = room.position_y
        request_x = room.position_x - 1

        if request_x < self.width or request_x >= 0 and not self.checkTaken((request_x,request_y), takenPositions):
            takenPositions.append((request_x,request_y))
            newRoom = World.Room.generateRoomFromSeed(random.randrange(0,100), request_x, request_y)
            room.westRoom = newRoom
            newRoom.eastRoom = room
            if(newRoom.isNone):
                self.generateLocalRooms(newRoom, level + 1, maxLevel)

        #Generate East

        request_y = room.position_y
        request_x = room.position_x + 1

        if request_x < self.width or request_x >= 0 and not self.checkTaken((request_x,request_y), takenPositions):
            takenPositions.append((request_x,request_y))
            newRoom = World.Room.generateRoomFromSeed(random.randrange(0,100), request_x, request_y)
            room.eastRoom = newRoom
            newRoom.westRoom = room
            if(newRoom.isNone):
                self.generateLocalRooms(newRoom, level + 1, maxLevel)

    #Returns True if a position was taken
    def checkTaken(self, positionRequest, takenPositions):
        print(positionRequest)
        for t in takenPositions:
            print(t)
            if positionRequest == takenPositions:
                return True
        return False