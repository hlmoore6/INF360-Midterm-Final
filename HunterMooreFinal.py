# INF360 - Programming in Python
# Hunter Moore
# Midterm Project

"""
Welcome to Hunter Moore's randomly generated duengeon crawler.
To run this program just run py HunterMooreFinal.py in any terminal.
This is a randomly generated dungeon crawler game that runs in the terminal.
Instructions on how to play are displayed in the terminal when started.
"""


try:
    import logging
    logging.basicConfig(level=logging.DEBUG, filename="Log.txt",
    format='%(asctime)s -  %(levelname)s -  %(message)s')

except ImportError():
    print("Error importing logging library.")

try:
    from WorldGenerator import *
except ImportError():
    logging.critical("Could not import WorldGenerator. Please include WorldGenerator.py in this directory.")

try:
    import GameComponents
except ImportError():
    logging.critical("Could not import GameComponents. Please include GameComponents.py in this directory.")

try:
    import GameInput
except ImportError():
    logging.critical("Could not import GameInput. Please include GameInput.py in this directory.")

try:
    import sys
except ImportError():
    logging.critical("Could not import sys. Please make sure python has access to sys.")
import random

try:
    from World import *
except ImportError():
    logging.critical("Could not import World. Please include World.py in this directory.")

try:
    import time
except ImportError():
    logging.critical("Could not import time. Please make sure python has access to time.")
    
#This variable stores the intro text
intro = """You somehow find yourself inside a dungeon.
It's dark but you think that if you can just find the exit you can escape.
You notice that you are equiped with a bronze sword.
Maybe if you explore the rooms around you, you will be able to find the exit.
"""

#WorldGenerator variable that generates the world generator
generator = WorldGenderator()

#The global world variable that stores information about the rooms and enemies
world = None
# world.printAllRooms(world.currentRoom)

#Player variable that stores information about the player
player = None

#Prints our current world seed
def printSeed():
    print("This game's seed is: " + str(world.worldSeed))
    print("This games's dimensions are (" + str(world.worldWidth) + ", " + str(world.worldHeight) + ") (Width, Height)") 

#This function prints out the text when a player wins
def printWinText():
    print("The room you enter has a chest in the center full of treasure!")
    print("You can also see an exit just behind the chest!")
    print("Congratulations you've won!")

#attack() handels the code that deals with the player attacking
def attack():
    #global variable
    global player

    #playerAttackDamage is a variable that stores the randomized attack damage based on the player weapon
    playerAttackDamage = player.weapon.getAttackDamage()
    
    #Enemy takes damage based on playerAttackDamage
    world.currentRoom.enemy.takeDamage(playerAttackDamage)

    #Checks if the enemy should be dead
    if world.currentRoom.enemy.health <= 0:
        #Deletes the enemy from the current room
        world.currentRoom.enemy = None
        #Print text that notifies the player that the enemy has been defeated
        print("Congratulations you defeated the enemy! You can now move on.")
        print("Your health is restored fully")
        #Restore player health
        player.health = 100

        #This part of the code randomly generates a weapon drop
        itemChance = 35 #itemChance is the chance that a weapon will spawn
        #if itemChance is greater than a random integer between 0-100
        if itemChance > random.randint(0,100): #Then generate a random weapon
            print("You found a weapon!\n")
            #weaponIndex is used to pick a random weapon
            weaponIndex = random.randint(0, len(GameComponents.weapons) - 1)
            #weaponPickup is the randomized weapon we chose from the list of weapons
            weaponPickup = GameComponents.weapons[weaponIndex]

            #This block of code just prints the specs on the current weapon and the one we found
            print("Current Weapon")
            player.weapon.printWeaponStats()

            print('\n', end='')

            print("Found Weapon")
            weaponPickup.printWeaponStats()

            print('\n', end='')

            weaponInput = "" #This is used to store input from the user
            #while we don't have an input of yes or no
            while weaponInput.lower() != "yes" and weaponInput.lower() != "no":
                #set input to the input of the player
                weaponInput = input("Will you take this weapon (yes/no) >: ")

                #If the input is yes then set the player weapon to the one randomly generated
                if weaponInput.lower() == "yes":
                    print("You take the new weapon and discard your old one!")
                    player.weapon = weaponPickup
                
                #If the input is no then do nothing
                elif weaponInput.lower() == "no":
                    print("You discard the weapon you found and keep your old one.")
            
        #Because the enemy is dead there is no need to do anything else in this function
        return
    
    #If we reach this code then the enemy is still alive
    print("The enemy is still alive and it attacks!")

    #enemyAttackDamage is a randomized damage value from the enemy
    enemyAttackDamage = world.currentRoom.enemy.getDamage()
    
    #player then takes damage based on enemyAttackDamage
    player.takeDamage(enemyAttackDamage)

    #print the information on how much damage the enemy has done
    print("The enemy does " + str(enemyAttackDamage) + " damage to you.")
    
    #If the player should be dead
    if player.health < 0: #Then delete the player
        print("Oh no you died!")
        player = None
        return #Return because there is nothing else to do

    #Finally print the player stats
    player.printPlayerStats()


#move room changes the current room the player resides in (changes world.currentRoom)
#dir is an integer from 0-3 that notates the direction to go
def moveRoom(dir):
    #If there is an enemy in the current Room
    if world.currentRoom.enemy != None: #Then don't allow the player to leave
        print("You cannot leave the room until the enemy is dead.")
        return #gets us out of the function

    #get the room from the requested direction
    nextRoom = world.getRoomFromDirection(dir)

    #world.moveRoom(nextRoom) tries to change the room to nextRoom and returns False if it is not able to
    if not world.moveRoom(nextRoom):
        print("There is no room in that direction. Please try again")
        return #The move did not work so we return out of the function

    #If we get to this point then the room change was successful

    #If the room we moved into is the end room
    if world.currentRoom.isEnd: #Then we win
        printWinText()
        return #return out of function because we won
    
    #If there is an enemy in the room then notify the player
    if world.currentRoom.enemy != None:
        print("There's a " + world.currentRoom.enemy.name + " in the room!")
    
    #Finally print the new room options
    world.currentRoom.printRoomOptions()

# run receives a string as input an atempts a run
#dir is an integer from 0-3 that notates the direction to go
def run(dir):
    #global variable player
    global player

    #nextRoom is the room requested from dir
    nextRoom = world.getRoomFromDirection(dir)

    #If the nextRoom is not avaiable
    if not world.checkAvailability(nextRoom):
        #Notify the player
        print("There is no room in that direction")
        return #return out of function

    #runChance stores the chance that the player will get out of the room
    runChance = 10

    #if runChance is greater than a random integer between 0-100
    if runChance > random.randint(0,100):
        #Notify player that run atempt was successful
        print("You got away but the enemy is still there!")
        
        #Move room to next room
        world.moveRoom(nextRoom)
       
       #If there's an enemy in the new room
        if world.currentRoom.enemy != None:
            #Notify player
            print("There's a " + world.currentRoom.enemy.name + " in the room!")

        #Print all the room optinons of the new current room
        world.currentRoom.printRoomOptions()
       
        return #return out of function
    
    #If we get here then we did not escape
    print("Sadly you did not escape")

    #enemyAttackDamage store the damage that the enemy will do to the player
    enemyAttackDamage = world.currentRoom.enemy.getDamage()
    #The player then takes the damage
    player.takeDamage(enemyAttackDamage)

    #Notify player of how much damage was taken
    print("The enemy does " + str(enemyAttackDamage) + " damage to you.")
    
    #If player should be dead
    if player.health < 0: #Then kill the player
        print("Oh no you died!")
        player = None
        return

    #If we're alive print the player's stats
    player.printPlayerStats()

#This functions prints the room Options and the enemy stats if there is an enemy
def printRoom():
    #Print the room options
    world.currentRoom.printRoomOptions()
    
    #If theres an enemy in the room print the enemy's stats
    if world.currentRoom.enemy != None:
        world.currentRoom.enemy.printEnemyStats()
        return #return out of function
    #Notify the player that there is no enemy in the room
    print("No enemy in current room")


#This function notifies the player that the input was not recognized
def undefinedInput():
    print("Sorry I did not understand that request.")
    print("Please try and rephrase your input or refere to the help menu.")
    print('\n', end='')

#This function contains the main game loop that houses the gameplay
def gameLoop():
    #global variables
    global player
    global world

    #while the player still exists or the current room is not the end room
    while player != None and not world.currentRoom.isEnd:
        #Request input
        gameInputText = input("What will you do? >: ")
        #Parse the input and store the keywords into variable actions
        actions = GameInput.parseText(gameInputText)
        
        print('\n', end="")

        ##############Handle input###############
        ##############Handle input###############
        ##############Handle input###############

        #If no keywords were found
        if len(actions) == 0:
            #Notify player that no actions will be taken
            undefinedInput()
            continue
        try:
            #Help
            if actions[0] == "help":
                GameInput.printHelp()

            #Exit and Quit
            elif actions[0] == "exit" or actions[0] == "quit":
                #delete the player variable
                del player
                print("Print thank you for playing!")
                
                #this causes a SystemExit Exception
                quit()

            # Seed
            elif actions[0] == "seed":
                #prints player seed
                printSeed()

            # Attack
            elif actions[0] == "attack" or actions[0] == "fight":
                #If there is no enemy in the room
                if world.currentRoom.enemy == None:
                    print("There is not enemy in the room to attack!") #Notify player
                    continue #No other action needed
               
                #Otherwise attack
                attack()

            # Run
            elif actions[0] == "run":
                #If the player did not define a path to go along with the run command
                if len(actions) == 1:
                    #Notify player of the bad input
                    undefinedInput()
                    continue

                #If there is no enemy in the room
                if world.currentRoom.enemy == None:
                    #Notify player that the run command is not nessesary
                    print("There is no need to run!\n")
                    continue
                
                #If the direction is not a cardinal direction
                if actions[1] != "north" and actions[1] != "south" and actions[1] != "west" and actions[1] != "east":
                    #Notify player that they need to
                    undefinedInput()

                #Otherwise we are good
                run(actions[1])

            #These are just move commands in different directions
            #These are just move commands in different directions
            #These are just move commands in different directions

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
                #Print the enemy's info
                world.currentRoom.printEnemyInfo()

            # Stats
            elif actions[0] == "stats":
                #Print the player's stats
                player.printPlayerInfo()
                #Print the player's weapon stats
                player.weapon.printWeaponStats()

            #Surroundings and Room
            elif actions[0] == "surroundings" or actions[0] == "room":
                #Print the room options
                printRoom()

            else:
                undefinedInput()
                logging.info("Could not parse user input: " + gameInputText)
        
        #This is the quit() function exception. Everything is fine we just need to exit the loop
        except SystemExit:
            break
        
        #If this exception hits then we know something really bad has happened. This should never execute
        except:
            #Get exception info
            e = sys.exc_info()[0]
            #Print exception info
            print(e)
            #Print that the input was not recognized
            undefinedInput()
            logging.info("Could not parse user input: " + gameInputText)
        
        print('\n', end="")

#This function allows the user to generate the world map
def userCreateWorld():
    #global variable
    global world

    #These variables are used to store information that we will use to build the world
    worldWidth = None
    worldHeight = None
    worldSeed = None

    #while the worldWidth is not defined
    while worldWidth == None:
        #Get input for world width
        
        worldWidth = input("Please enter a map WIDTH (press enter for a width of 5) >: ")

        #If the input is empty then default to 5
        if worldWidth == "":
            worldWidth = 5
            break
        
        try:
            #try to cast variable into int
            worldWidth = int(worldWidth)
        except:
            #If we can't then we know the input was not an integer
            #Notify player
            print("Sorry I didn't understand that. Please try again")
            #undefine worldWidth so we loop again
            worldWidth = None 
    
    print('\n', end='')

    #We do the same procedure for world height as world width
    while worldHeight == None:
        worldHeight = input("Please enter a map HEIGHT (press enter for a height of 5) >: ")

        if worldHeight == "":
            worldHeight = 5
            break
        
        try:
            worldHeight = int(worldHeight)
        except:
            print("Sorry I didn't understand that. Please try again")
            worldHeight = None 

    print('\n', end='')

    #Get input for worldSeed
    worldSeed = input("Please enter a seed for the map (press enter for a random seed) >: ")
    
    #If the input was empty then randomize seed
    if worldSeed == "":
        #We seed random with the current time
        random.seed(int(time.time()))
        #Then we generate the seed from random that goes from 0 to the max size of an integer
        worldSeed = random.randint(0, sys.maxsize)

    #This is to make sure that if an integer was inputed that it stays an integer data type
    #If it's not an integer then random.seed() will not produce the same randomness
    try: #Try block
        intSeed = int(worldSeed) #Try to convert seed into an integer
        worldSeed = intSeed #Set the worldSeed equal to the integer conversion
    except: #If there's an exception
        pass #Just continue

    #Generate world using the variable we gather
    world = generator.generateWorld(worldWidth, worldHeight, seed=worldSeed)

    #Print the seed
    printSeed()

#userInput variable is used to store if the player want's to continue
userInput = ""

#while the input is not exit or quit play the game
while userInput.lower() != "exit" and userInput.lower() != "quit":

    #Create a new world
    userCreateWorld()

    #Create a new player
    player = GameComponents.Player("Player")
    print('\n', end='')
    
    # Prolouge
    GameInput.printHelp()
    print(intro)
    input("Press enter >: ")

    #Print the current room options
    world.currentRoom.printRoomOptions()

    #Main game loop
    gameLoop()

    #When gameLoop returns then the player either won or lost

    #Notify player that the game is done
    print("Sorry but the game is over :(")
    #Print the seed for the last time incase the player wants to replay
    printSeed()

    #Tell player how to quit or play again
    print("To play again please press enter")
    print("To quit please enter exit or quit\n")

    #Get the input
    userInput = input(">: ")



