
keyWords = [
    "Help",
    "North","South","West","East",
    "Attack","Run",
    "Enemy","Stats","Surroundings","Room"
]

def printHelp():
    helpText = """Help Menu-

To move around the world just type where you want to go. It can even be a descriptive as you want!
To look at your stats just type \"Stats\".
To get your bearings and see what rooms surrond you type \"Surroundings\" or \"Room\".
To go into another room just type to direction you want to go ex. \"North\".
To get stats on an enemy type \"Enemy\".
To attack an enemy type \"Attack\" or \"Fight\".
To run type \"Run\" and the direction you want to go.
To read these instructions again just type \"Help\"
"""

    print(helpText)
    input("Please press enter >: ")

def parseText(text):
    return