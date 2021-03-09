import WorldGenerator

generator = WorldGenerator.WorldGenderator()

world = generator.generateWorld(10,10)

world.printAllRooms(world.currentRoom)

world.currentRoom.printRoomInfo()