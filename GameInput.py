# INF360 - Programming in Python
# Hunter Moore
# Midterm Project
try:
    import logging
except ImportError():
    print("Could not import logging. Something is terrible wrong!")

try:
    import re
except ImportError():
    logging.critical("Could not import the module re. Please make sure the regex module is installed")
    
#This variable is just the help menu
helpText = """Help Menu-

To move around the world just type where you want to go. It can even be as descriptive as you want!
To look at your stats just type \"Stats\".
To get your bearings and see what rooms surrond you type \"Surroundings\" or \"Room\".
To go into another room just type to direction you want to go ex. \"North\".
To get stats on an enemy type \"Enemy\".
To attack an enemy type \"Attack\" or \"Fight\".
To run type \"Run\" and the direction you want to go.
To exit the game type \"Exit\" or \"Quit\"
To get the seed for the current game type \"Seed\"
To read these instructions again just type \"Help\"
"""

#This array stores keywords that our program looks for in user input
#It's also in an order of precedence
keyWords = [
    "help", "exit", "quit", "seed",
    "attack", "fight" ,"run",
    "north","south","west","east",
    "enemy","stats","surroundings","room"
]

#Setup regex statement
regexStatement = r"\b(?:"

#Add all of the keywords into the regex
#For each word in keyWords
for word in keyWords:
    #Add the word along with the or regex operator
    regexStatement += word + r"|"

#Remove the last character (an extra | operator)
regexStatement = regexStatement[:-1]

#Add the end of the regex to the expression
regexStatement += r")\b"

#This function prints out the help text
def printHelp():
    print(helpText)
    input("Please press enter >: ")

#This function takes in a string(input) and returns any keywords
def parseText(text):
    #Convert the text all to lowercase
    text = text.lower()
    
    #Create variable keys and run regex to find all the keywords
    keys = re.findall(regexStatement, text)
    #Return the keyWords
    return keys