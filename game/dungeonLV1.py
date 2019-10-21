import os, random
Map = [
    ['-','-','-','-',],
    ['-','-','-','-',],
    ['-','-','-','-',],
    ['-','-','-','-',]
]
class condinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

Door = condinate(0,0)
Key = condinate(0,0)
Player = condinate(0,0)
Wall = condinate(0,0)

def same(condinates):
    result = True
    for i in range(0,3):
        for j in range(0,3):
            if condinates[i][0] == condinates[i+1][0] and condinates[i][1] == condinates[i+1][1]:
                result = False
    return result

def genarateCordinate(): #generate elements' condinate
    Door.x = random.randint(0,3)
    Door.y = random.randint(0,3)
    Key.x = random.randint(0,3)
    Key.y = random.randint(0,3)
    Player.x = random.randint(0,3)
    Player.y = random.randint(0,3)
    Wall.x = random.randint(0,3)
    Wall.y = random.randint(0,3)
    condinates = [[Door.x, Door.y], [Key.x,Key.y], [Player.x, Player.y], [Wall.x, Wall.y]]
    if(same(condinates) == False):
        genarateCordinate()

def move(entry): #update elements' condinate
    if(entry == "w"):
        if(Player.x >= 0):
            Player.x -= 1
    elif(entry == 's'):
        if(Player.x <= 3):
            Player.x += 1
    elif(entry == 'd'):
        if(Player.y <= 3):
            Player.y += 1
    elif(entry == 'a'):
        if(Player.y >= 0):
            Player.y -= 1

def updateOldCondinate(entry):
    Map[Player.x][Player.y] = '-'
    move(entry)
    Map[Player.x][Player.y] = 'P'

def printMap():
    for i in range(0, len(Map)):
        for j in range(0, len(Map)):
            print(Map[i][j], end =" ")
        print()

def convertEntry(entry):
    if(entry == 'w'):  
        return 's'
    elif(entry == 'a'): 
        return'd'
    elif(entry == 'd'):
        return 'a'
    elif(entry == 's'):
        return 'w'

if __name__ == "__main__":
    genarateCordinate()
    
    win = False
    HaveKey = False
    Map[Door.x][Door.y] = 'D'
    Map[Player.x][Player.y] = 'P'
    Map[Key.x][Key.y] = 'K'
    Map[Wall.x][Wall.y] = 'W'

    printMap()

    while(win == False):
        entry = input()
        updateOldCondinate(entry)
        if(Player.x == Key.x and Player.y == Key.y):
            HaveKey = True
        if(Player.x == Wall.x and Player.y == Wall.y):
            print("You have hit the frickin' wall")
            updateOldCondinate(convertEntry(entry))
            Map[Wall.x][Wall.y] = 'W'
        if(HaveKey == False):
            if(Player.x == Door.x and Player.y == Door.y):
                print("You haven't pick up the key")
                updateOldCondinate(convertEntry(entry))
                Map[Door.x][Door.y] = 'D'
        else:
            if(Player.x == Door.x and Player.y == Door.y):
                 win = True
        os.system('clear')
        printMap()
    print("You won ^^")