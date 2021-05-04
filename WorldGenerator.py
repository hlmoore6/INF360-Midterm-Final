# INF360 - Programming in Python
# Hunter Moore
# Midterm Project

try:
    import logging
except:
    print("Could not import logging. Something is terrible wrong!")

try:
    import random
except:
    logging.critical("Could not import random. Please install the random module")

try:
    import World
except:
    logging.critical("Could not import module World.py. Please make sure World.py is in the same directroy as WorldGenerator.py")
#This class generates levels for the game and keeps
class WorldGenderator:

    #This is the main function of World Generator
    #This will take care of everything associated with the world generation
    def generateWorld(self, width, height, seed=0):
        #Debug statment to let the developer know what the generation parameters are
        logging.debug("Generating a world with a width of " + str(width) + " and a height of " + str(height) + " and a seed of " + str(seed))
        
        self.worldSeed = seed #This sets the seed that we will use for randomization
        random.seed(self.worldSeed) #This is where we set our random seed

        #Setting the world dimensions
        self.width = width 
        self.height = height

        #Taken positions are used to keep track of what positions have already been taken
        self.takenPositions = list()

        #Origin room is the first room we will spawn in
        self.originRoom = self.generateRoomLayout()

        #CurrRoom is to keep track of the current room we are playing in
        self.currRoom = self.originRoom

        #This allows us to pick our end room (the goal room)
        self.pickEndRoom(random.randrange(0,100))

        logging.debug("Number of rooms generated: " + str(len(self.takenPositions)))
        #This is where we initialize our world object
        world = World.World(self.originRoom, self.worldSeed, self.width, self.height)

        #We finnaly return the world
        return world

    def generateRoomLayout(self):
        #Set starting room in the middle of the rooms list
        startingRoom = World.Room.generateStartingRoom(self.width//2, self.height//2)

        #Add the starting room positions to the takenPositions tracker
        self.takenPositions.append((startingRoom.position_x, startingRoom.position_y))

        #Max recursion is how many times the function below will be able to call itself per call
        #The value of max recursion is 3/4 the average of width and hight
        maxRecursion = ((self.width + self.height)//2) * 0.75
        
        #This function recursivley calls itself to generate rooms adjacent to itself
        self.generateLocalRooms(startingRoom, 0, maxRecursion)
        
        return startingRoom

    def generateNorth(self, room):
        #First we calculate the position the we are going to request to generate a room
        request_y = room.position_y+1
        request_x = room.position_x

        #We check if the request is a valid position and if the position was already taken
        if request_y < self.height and request_y >= 0 and not self.checkTaken((request_x,request_y), self.takenPositions):
            #If the position is good and we are able to generate a room

            #We create a variable called newRoom and generate a Room from a random seed
            newRoom = World.Room.generateRoomFromSeed(random.randrange(0,100), request_x, request_y)
            
            #If the room we generated is None then we return
            if newRoom == None:
                return None

            #Append this position to the list of taken positions
            self.takenPositions.append((request_x,request_y))

            #Set our current room's north room to our newRoom that we generated
            room.northRoom = newRoom
            #Set the newRoom's south room to our current room
            newRoom.southRoom = room

            #Return the newly created room
            return newRoom
    
    #The rest of these functions work as the previous except with different directions
    def generateSouth(self, room):
        request_y = room.position_y-1
        request_x = room.position_x

        if request_y < self.height and request_y >= 0 and not self.checkTaken((request_x,request_y), self.takenPositions):
            self.takenPositions.append((request_x,request_y))
            newRoom = World.Room.generateRoomFromSeed(random.randrange(0,100), request_x, request_y)
            if newRoom == None:
                return None
            room.southRoom = newRoom
            newRoom.northRoom = room
            return newRoom

    def generateWest(self, room):
        request_y = room.position_y
        request_x = room.position_x - 1

        if request_x < self.width and request_x >= 0 and not self.checkTaken((request_x,request_y), self.takenPositions):
            self.takenPositions.append((request_x,request_y))
            newRoom = World.Room.generateRoomFromSeed(random.randrange(0,100), request_x, request_y)
            if newRoom == None:
                return None
            room.westRoom = newRoom
            newRoom.eastRoom = room
            return newRoom

    def generateEast(self, room):
        request_y = room.position_y
        request_x = room.position_x + 1

        if request_x < self.width and request_x >= 0 and not self.checkTaken((request_x,request_y), self.takenPositions):
            self.takenPositions.append((request_x,request_y))
            newRoom = World.Room.generateRoomFromSeed(random.randrange(0,100), request_x, request_y)
            if newRoom == None:
                return None
            room.eastRoom = newRoom
            newRoom.westRoom = room
            return newRoom

    #This function recursivley calls itself to generate rooms adjacent to itself
    #room is the current room
    #level is current recursion iteration
    #maxLevel is the max number of recursions allowed
    def generateLocalRooms(self, room, level, maxLevel):
        #This checks the current level iteration
        if level > maxLevel or room == None:
            #If our level is greater than the max iteration then we return out of the function
            return

        newRoom = self.generateNorth(room)
        if newRoom != None:
            self.generateLocalRooms(newRoom, level + 1, maxLevel)
       
        newRoom = self.generateSouth(room)
        if newRoom != None:
            self.generateLocalRooms(newRoom, level + 1, maxLevel)
        
        newRoom = self.generateWest(room)
        if newRoom != None:
            self.generateLocalRooms(newRoom, level + 1, maxLevel)
        
        newRoom = self.generateEast(room)
        if newRoom != None:
            self.generateLocalRooms(newRoom, level + 1, maxLevel)

        

    #This picks the end room
    def pickEndRoom(self, seed):
        #Setting the random seed
        random.seed(seed)

        #This is the minimum distance from the origin room
        minDistance = (self.width + self.height)//4

        #Loop to randomly pick end room
        while True:
            distance = abs(self.currRoom.position_x - self.originRoom.position_x) + abs(self.currRoom.position_y - self.originRoom.position_y)
            #If we find a room that is acceptable to be an end Room
            if distance >= minDistance:
                #We give a 10% chance that a room will be picked as an end room
                if random.randint(0,100) < 10:
                    #If we pick the room to be the ending room then this will take our currRoom and make is the endRoom
                    World.Room.generateEndingRoom(self.currRoom)
                    #Reset our currRoom to the originRoom
                    self.currRoom = self.originRoom           
                    #Return out of the function and out of the loop         
                    return

            #Create variable nextRoom and set it to None
            nextRoom = None

            #While the nextRoom is None then keep trying to pick the next room
            while nextRoom == None:
                #If we don't pick a room then try another randomly selected one
                dir = random.randint(0,4)

                #Pick North
                if(dir == 0):
                    #Set the nextRoom to the current room's north room
                    nextRoom = self.currRoom.northRoom
                    
                    #If the nextRoom is an acceptable room then...
                    if nextRoom != None:
                        #Set the currRoom into the northRoom
                        self.currRoom = self.currRoom.northRoom
                        #Break out of this first loop
                        break

                #This code is the same as the previous
                #This code is the same as the previous
                #This code is the same as the previous

                #Pick south
                if(dir == 1):
                    nextRoom = self.currRoom.southRoom
                    if nextRoom is not None:
                        if nextRoom != None:
                            self.currRoom = self.currRoom.southRoom
                            break

                #Pick west
                if(dir == 2):
                    nextRoom = self.currRoom.westRoom
                    if nextRoom is not None:
                        if nextRoom != None:
                            self.currRoom = self.currRoom.westRoom
                            break
                
                #Pick east
                if(dir == 3):
                    nextRoom = self.currRoom.eastRoom
                    if nextRoom is not None:
                        if nextRoom != None:
                            self.currRoom = self.currRoom.eastRoom
                            break


    #Returns True if a position was taken
    def checkTaken(self, positionRequest, takenPositions):
        #For every tuple in self.takenPositions
        for t in self.takenPositions:
            #We check if our requested position is already taken
            if positionRequest == t:
                return True #If it was taken then return True
        return False #If we pass all of the tests the we return False