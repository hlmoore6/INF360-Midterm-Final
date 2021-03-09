import WorldGenerator
import GameComponents

generator = WorldGenerator.WorldGenderator()

world = generator.generateWorld(5,5, seed =0)

print("Please enter your name: ")
name = input()

player = Player(name)
player.position_x = world.currentRoom.position_x
player.position_y = world.currentRoom.position_y

#while(not world.currentRoom.isEnd):
