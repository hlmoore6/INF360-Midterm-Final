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

        for x in range(0, self.width):
            rooms.append(list())
            for y in range(0, self.height):
                rooms[x].append(None)
                
        return 0



