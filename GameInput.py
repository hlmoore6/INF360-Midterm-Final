import re

helpText = """Help Menu-

To move around the world just type where you want to go. It can even be a descriptive as you want!
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

keyWords = [
    "help", "exit", "quit", "seed",
    "attack","run",
    "north","south","west","east",
    "enemy","stats","surroundings","room"
]

#Setup regex statement
regexStatement = r"\b(?:"

for word in keyWords:
    regexStatement += word + r"|"

regexStatement = regexStatement[:-1]
regexStatement += r")\b"


def printHelp():
    print(helpText)
    input("Please press enter >: ")

def parseText(text):
    text = text.lower()
    keys = re.findall(regexStatement, text)
    return keys