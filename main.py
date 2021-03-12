import WorldGenerator
import GameComponents
import GameInput
import sys

intro = """You somehow find yourself inside a dungeon.
It's dark but you think that if you can just find the exit you can escape.
You notice that you are equiped with a bronze sword.
Maybe if you explore the rooms around you, you will be able to find the exit.
"""

generator = WorldGenerator.WorldGenderator()

world = generator.generateWorld(5, 5, seed=0)
# world.printAllRooms(world.currentRoom)

playerName = input("Please enter your character's name >: ")
print('\n', end='')

player = GameComponents.Player(playerName)

def printSeed():
    print("This game's seed is: " + str(world.worldSeed))

def attack():
    return

# run receives a string as input an atempts a run


def run(dir):
    return


def moveRoom(dir):
    return


def printRoom():
    return


def undefinedInput():
    print("Sorry I did not understand that request.")
    print("Please try and rephrase your input or refere to the help menu.")
    print('\n', end='')

# Prolouge
GameInput.printHelp()
print(intro)
input("Press enter >: ")

# Game Loop

while player != None:
    gameInputText = input("What will you do? >: ")
    actions = GameInput.parseText(gameInputText)

    ##############Handle input###############
    ##############Handle input###############
    ##############Handle input###############

    if len(actions) == 0:
        undefinedInput()
        continue
    try:
        #Help
        if actions[0] == GameInput.keyWords[0]:
            GameInput.printHelp()

        #Exit and Quit
        elif actions[0] == GameInput.keyWords[1] or actions[0] == GameInput.keyWords[2]:
            printSeed()
            print("Print thank you for playing!")
            break

        # Seed
        elif actions[0] == GameInput.keyWords[3]:
            printSeed()

        # Attack
        elif actions[0] == GameInput.keyWords[4]:
            attack()

        # Run
        elif actions[0] == GameInput.keyWords[5]:
            if len(actions) == 1:
                undefinedInput()
                continue

            if world.currentRoom.enemy == None:
                print("There is no need to run!")
                continue
            
            if actions[1] != "north" or actions[1] != "south" or actions[1] != "west" or actions[1] != "east":
                undefinedInput()

            run(actions[1])

        # North
        elif actions[0] == GameInput.keyWords[6]:
            moveRoom(0)

        # South
        elif actions[0] == GameInput.keyWords[7]:
            moveRoom(1)

        # West
        elif actions[0] == GameInput.keyWords[8]:
            moveRoom(2)

        # East
        elif actions[0] == GameInput.keyWords[9]:
            moveRoom(3)

        # Enemy
        elif actions[0] == GameInput.keyWords[10]:
            world.currentRoom.printEnemyInfo()

        # Stats
        elif actions[0] == GameInput.keyWords[11]:
            player.printPlayerInfo()

        #Surroundings and Room
        elif actions[0] == GameInput.keyWords[12] or actions[0] == GameInput.keyWords[13]:
            printRoom()

        else:
            undefinedInput()
    except:
        e = sys.exc_info()[0]
        print(e)
        undefinedInput()
        player = None

