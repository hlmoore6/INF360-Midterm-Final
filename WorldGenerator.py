import random
import World
import Room

#This class generates levels for the game and keeps
class WorldGenderator:
    def generateWorld(self, width, height, seed = 0):
        self.worldSeed = seed

        self.width = width
        self.height = height

        self.rooms = self.generateRoomLayout()

    def generateRoomLayout(self):
        random.seed(self.worldSeed)
        rooms_seed = random.randrange(0, 100)

        startingRoom = Room.Room.generateRoomFromSeed(rooms_seed)
        endingRoom = Room.Room.generateEndingRoom()

        rooms = list()
        
        #Initialize rooms layout
        for x in range(0, self.width):
            rooms.append(list())
            for y in range(0, self.height):
                rooms[x].append(None)

        #Rooms generation code

        #Set starting room in the middle of the rooms list
        rooms[self.width//2][self.height//2] = startingRoom
                
        return 0

    def generateLocalRooms(room):




