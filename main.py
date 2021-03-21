import WorldGenerator
import GameComponents
import GameInput
import sys
import random
from World import *

intro = """You somehow find yourself inside a dungeon.
It's dark but you think that if you can just find the exit you can escape.
You notice that you are equiped with a bronze sword.
Maybe if you explore the rooms around you, you will be able to find the exit.
"""

generator = WorldGenerator.WorldGenderator()

world = None
# world.printAllRooms(world.currentRoom)

player = None

def printSeed():
    print("This game's seed is: " + str(world.worldSeed))

def win():
    print("The room you enter has a chest in the center full of treasure!")
    print("Congratulations you've won!")

def attack():
    global player

    playerAttackDamage = player.weapon.getAttackDamage()
    world.currentRoom.enemy.takeDamage(playerAttackDamage)

    if world.currentRoom.enemy.health <= 0:
        world.currentRoom.enemy = None
        print("Congratulations you defeated the enemy! You can now move on.")
        print("Your health is restored fully")
        player.health = 100

        itemChance = 5
        if itemChance < random.randint(0,100):
            print("You found a weapon!\n")
            weaponIndex = random.randint(0, len(GameComponents.weapons))
            weaponPickup = GameComponents.weapons[weaponIndex]

            print("Current Weapon")
            player.weapon.printWeaponStats()

            print('\n', end='')

            print("Found Weapon")
            weaponPickup.printWeaponStats()

            print('\n', end='')

            weaponInput = ""
            while weaponInput.lower() != "yes" and weaponInput.lower() != "no":
                weaponInput = input("Will you take this weapon (yes/no) >: ")

                if weaponInput.lower() == "yes":
                    print("You take the new weapon and discard your old one!")
                    player.weapon = weaponPickup
                    return
                
                elif weaponInput.lower() == "no":
                    print("You discard the weapon you found and keep your old one.")
                    return
    
    print("The enemy is still alive and it attacks!")

    enemyAttackDamage = world.currentRoom.enemy.getDamage()
    player.takeDamage(enemyAttackDamage)

    print("The enemy does " + str(enemyAttackDamage) + " damage to you.")
    
    if player.health < 0:
        print("Oh no you died!")
        player = None
        return

    player.printPlayerStats()


def moveRoom(dir):
    if world.currentRoom.enemy != None:
        print("You cannot leave the room until the enemy is dead.")
        return

    nextRoom = world.getRoomFromDirection(dir)

    if not world.moveRoom(nextRoom):
        print("There is no room in that direction. Please try again")
        return

    if world.currentRoom.isEnd:
        win()
        return
    
    if world.currentRoom.enemy != None:
        print("There's a " + world.currentRoom.enemy.name + " in the room!")
    
    world.currentRoom.printRoomOptions()

# run receives a string as input an atempts a run
def run(dir):
    global player

    nextRoom = world.getRoomFromDirection(dir)

    if not world.checkAvailability(nextRoom):
        print("There is no room in that direction")
        return

    runChance = 10

    if runChance > random.randint(0,100):
        print("You got away but the enemy is still there!")
        world.moveRoom(nextRoom)
        world.currentRoom.printRoomOptions()
       
        if world.currentRoom.enemy != None:
            print("There's a " + world.currentRoom.enemy.name + " in the room!")
       
        return
    
    print("Sadly you did not escape")

    enemyAttackDamage = world.currentRoom.enemy.getDamage()
    player.takeDamage(enemyAttackDamage)

    print("The enemy does " + str(enemyAttackDamage) + " damage to you.")
    
    if player.health < 0:
        print("Oh no you died!")
        player = None
        return

    player.printPlayerStats()


def printRoom():
    world.currentRoom.printRoomOptions()
    
    if world.currentRoom.enemy != None:
        world.currentRoom.enemy.printEnemyStats()
        return
    
    print("No enemy in current room")


def undefinedInput():
    print("Sorry I did not understand that request.")
    print("Please try and rephrase your input or refere to the help menu.")
    print('\n', end='')

def gameLoop():
    global player
    global world

    while player != None and not world.currentRoom.isEnd:
        gameInputText = input("What will you do? >: ")
        actions = GameInput.parseText(gameInputText)
        
        print('\n', end="")

        ##############Handle input###############
        ##############Handle input###############
        ##############Handle input###############

        if len(actions) == 0:
            undefinedInput()
            continue
        try:
            #Help
            if actions[0] == "help":
                GameInput.printHelp()

            #Exit and Quit
            elif actions[0] == "exit" or actions[0] == "quit":
                del player
                print("Print thank you for playing!")
                quit()

            # Seed
            elif actions[0] == "seed":
                printSeed()

            # Attack
            elif actions[0] == "attack":
                if world.currentRoom.enemy == None:
                    print("There is not enemy in the room to attack!")
                    continue
                attack()

            # Run
            elif actions[0] == "run":
                if len(actions) == 1:
                    undefinedInput()
                    continue

                if world.currentRoom.enemy == None:
                    print("There is no need to run!\n")
                    continue
                
                if actions[1] != "north" and actions[1] != "south" and actions[1] != "west" and actions[1] != "east":
                    undefinedInput()

                run(actions[1])

            # North
            elif actions[0] == "north":
                moveRoom(0)

            # South
            elif actions[0] == "south":
                moveRoom(1)

            # West
            elif actions[0] == "west":
                moveRoom(2)

            # East
            elif actions[0] == "east":
                moveRoom(3)

            # Enemy
            elif actions[0] == "enemy":
                world.currentRoom.printEnemyInfo()

            # Stats
            elif actions[0] == "stats":
                player.printPlayerInfo()
                player.weapon.printWeaponStats()

            #Surroundings and Room
            elif actions[0] == "surroundings" or actions[0] == "room":
                printRoom()

            else:
                undefinedInput()
        except SystemExit:
            break
        except:
            e = sys.exc_info()[0]
            print(e)
            undefinedInput()
        
        print('\n', end="")

def userCreateWorld():
    global world

    worldWidth = None
    worldHeight = None
    worldSeed = None

    while worldWidth == None:
        worldWidth = input("Please enter a map WIDTH (press enter for a width of 5) >: ")

        if worldWidth == "":
            worldWidth = 5
            break
        
        try:
            worldWidth = int(worldWidth)
        except:
            print("Sorry I didn't understand that. Please try again")
            worldWidth = None 

    while worldHeight == None:
        worldHeight = input("Please enter a map HEIGHT (press enter for a width of 5) >: ")

        if worldHeight == "":
            worldHeight = 5
            break
        
        try:
            worldHeight = int(worldHeight)
        except:
            print("Sorry I didn't understand that. Please try again")
            worldHeight = None 


    worldSeed = input("Please enter a seed for the map (press enter for a seed of 0) >: ")
    
    if worldSeed == "":
        worldSeed = 0
    
    world = generator.generateWorld(worldWidth, worldHeight, seed=worldSeed)

userInput = ""

while userInput.lower() != "exit" and userInput.lower() != "quit":

    userCreateWorld()

    player = GameComponents.Player("Player")
    print('\n', end='')
    
    # Prolouge
    GameInput.printHelp()
    print(intro)
    input("Press enter >: ")

    world.currentRoom.printRoomOptions()

    #Main game loop
    gameLoop()

    print("Sorry but the game is over :(")
    printSeed()
    print("To play again please press enter")
    print("To quit please enter exit or quit\n")

    userInput = input(">: ")



