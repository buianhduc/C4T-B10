import os, random
Map = [
    ['-','-','-','-',],
    ['-','-','-','-',],
    ['-','-','-','-',],
    ['-','-','-','-',]
] #genarate map
class coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

Door = coordinate(0,0)
Key = coordinate(0,0)
Player = coordinate(0,0)
Wall = coordinate(0,0)
Key2 = coordinate(0,0)
monster = coordinate(0,0)
PlayerHP = 100
MonsterHP = 100
# => define cordinate of elements

def same(coordinates):
    result = True
    for i in range(0,len(coordinates)-1):
        for j in range(0,len(coordinates)-1):
            if coordinates[i][0] == coordinates[i+1][0] and coordinates[i][1] == coordinates[i+1][1]:
                result = False
    return result
# => Check if there is a same coordinate of diffrent elements

def monster_move():
    command = random.randint(0,4)
    order = 0
    if command == 1:
        order = 'w'
    elif command == 2:
        order = 's'
    elif command == 3:
        order = 'd'
    elif command == 4:
        order = 'a'
    return order
# => monster movement

def genarateCordinate(): #generate elements' coordinate
    Door.x = random.randint(0,3)
    Door.y = random.randint(0,3)
    Key.x = random.randint(0,3)
    Key.y = random.randint(0,3)
    Player.x = random.randint(0,3)
    Player.y = random.randint(0,3)
    Wall.x = random.randint(0,3)
    Wall.y = random.randint(0,3)
    Key2.x = random.randint(0,3)
    Key2.y = random.randint(0,3)    
    monster.x = random.randint(0,3)
    monster.y = random.randint(0,3)
    coordinates = [[Door.x, Door.y], [Key.x,Key.y], [Player.x, Player.y], [Wall.x, Wall.y], [Key2.x,Key2.y], [monster.x, monster.y]]
    if(same(coordinates) == False):
        genarateCordinate()
# => Generate coordinate
def move(entry,kind): #update elements' coordinate
    if kind == 'p':
        if(entry == "w"):
            if(Player.x > 0):
                Player.x -= 1
        elif(entry == 's'):
            if(Player.x < 3):
                Player.x += 1
        elif(entry == 'd'):
            if(Player.y < 3):
                Player.y += 1
        elif(entry == 'a'):
            if(Player.y > 0):
                Player.y -= 1 
    if kind == 'm':
        if(entry == "w"):
            if(monster.x > 0):
                monster.x -= 1
        elif(entry == 's'):
            if(monster.x < 3):
                monster.x += 1
        elif(entry == 'd'):
            if(monster.y < 3):
                monster.y += 1
        elif(entry == 'a'):
            if(monster.y > 0):
                monster.y -= 1 
# update coordinate as the user type the move
def updateOldcoordinate(entry,kind):
    if kind == 'p':
        Map[Player.x][Player.y] = '-'
        move(entry,'p')
        Map[Player.x][Player.y] = 'P'
    else:
        Map[monster.x][monster.y] = '-'
        move(entry,'m')
        Map[monster.x][monster.y] = 'M'
# update coordinate on the map
    
def printMap():
    print("Your HP: {0}     {1} Monster's HP".format(PlayerHP, MonsterHP))
    for i in range(0, len(Map)):
        for j in range(0, len(Map)):
            print(Map[i][j], end =" ")
        print()
#print map
def convertEntry(entry):
    if(entry == 'w'):  
        return 's'
    elif(entry == 'a'): 
        return'd'
    elif(entry == 'd'):
        return 'a'
    elif(entry == 's'):
        return 'w'
# reverse user's order

def deal_w_monster():
    print('You have encontered with the monster!')
    print('You have 3 options:')
    print('1. Run')
    print('2. Fight')
    print('3. Defend')
    movement = input('What do you wanna do?')


if __name__ == "__main__":
    genarateCordinate()
    
    win = False
    HaveKey = False
    HaveKey2 = False
    Map[Door.x][Door.y] = 'D'
    Map[Player.x][Player.y] = 'P'
    Map[Key.x][Key.y] = 'K'
    Map[Wall.x][Wall.y] = 'W'
    Map[Key2.x][Key2.y] = 'K2'
    Map[monster.x][monster.y] = 'M'
    printMap()

    while(win == False):
        entry = input()
        updateOldcoordinate(entry,'p')
        monster_move()
        if (monster.x == Player.x and monster.y == Player.y):
            deal_w_monster()
        if(Player.x == Key.x and Player.y == Key.y):
            HaveKey = True
        if(Player.x == Key2.x and Player.y == Key2.y):
            HaveKey2 = True

        if(Player.x == Wall.x and Player.y == Wall.y):
            print("You have hit the frickin' wall")
            updateOldcoordinate(convertEntry(entry),'p')
            Map[Wall.x][Wall.y] = 'W'
        
        if(HaveKey == False or HaveKey2 == False):
            if(Player.x == Door.x and Player.y == Door.y):
                print("You haven't pick up enough keys")
                updateOldcoordinate(convertEntry(entry),'p')
                Map[Door.x][Door.y] = 'D'
        else:
            if(Player.x == Door.x and Player.y == Door.y):
                 win = True
        os.system('clear')
        printMap()
    print("You won ^^")