import WorldGenerator
import GameComponents
import GameInput

intro = """You somehow find yourself inside a dungeon.
It's dark but you think that if you can just find the exit you can escape.
You notice that you are equiped with a bronze sword.
Maybe if you explore the rooms around you, you will be able to find the exit.
"""

generator = WorldGenerator.WorldGenderator()

world = generator.generateWorld(5,5, seed =0)
#world.printAllRooms(world.currentRoom)

playerName = input("Please enter your character's name >: ")
print('\n', end='')

player = GameComponents.Player(playerName)

#Prolouge
GameInput.printHelp()
input("Press enter >: ")
print(intro)

#Game Loop

while player != None:
    gameInputText = input("What will you do? >: ")
