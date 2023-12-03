regex = r"/[^\d|\.|\n]/gm"

spechialChar = ["*","%","=","#",]

#ascii A-Z 65-90
#ascii a-z 97-122
#asii 0-9 48-57
#ascii . 46

isReguarCharWhitelist = list()
isReguarCharWhitelist.extend(list(range(65,91))) #A-Z
isReguarCharWhitelist.extend(list(range(97,123))) #a-z
isReguarCharWhitelist.extend(list(range(48,58))) #0-9
isReguarCharWhitelist.extend([46])#.

grid = [] #input file as grid

with open("day3/input_copy.txt") as f:
    for line in f:
        line = line[:-1] # remove the /n
        list(line)
        rowList = list(line)
        
        localRow = []
        for rowItem in rowList:
            localRow.append(rowItem)
        
        grid.append(localRow)


yMax = len(grid)
xMax = len(grid[0])

girdStatus = [[0 for col in range(xMax)] for row in range(yMax)]

Status = {
    "spechialChar": 1,
    "unconfirmedNum": 2,
    "confirmedNum": 3,
    "inProcessCheckedNum": 4
}
             

def printMatrix(matrix):
    for row in matrix:
        print(row)
    print("--------------")

y = 0
for row in grid:
    x = 0
    for char in row:
        if(ord(char) not in isReguarCharWhitelist):
            #print(f"y:{y} x:{x} ",char)
            girdStatus[y][x] = Status["spechialChar"]
        if(char.isdigit()):
            girdStatus[y][x] = Status["unconfirmedNum"]
        x += 1
    y += 1

def ValidCoords(y,x):
    yValid = True
    if (y > yMax):
        yValid = False
    if (y < 0):
        yValid = False
        
    xValid = True
    if (x > xMax):
        xValid = False
    if (x < 0):
        xValid = False
    
    return yValid, xValid



# the recurtion is doubbeling back and overwriting it self
def flagNumbers(y,x,base = girdStatus):
    for yMod in [1,0,-1]:
        for xMod in [1,-1]:
            
            yLocal, xLocal = y+yMod,x+xMod
            yValid, xValid = ValidCoords(yLocal, xLocal)

            if (yValid):
                if (base[yLocal][xLocal] not in isReguarCharWhitelist or base[yLocal][xLocal]==Status["confirmedNum"]):
                    base[y][x] = Status["confirmedNum"]
                    
                    printMatrix(girdStatus)
                    
                #print(f"y:{yLocal} x:{xLocal} ",base[yLocal][xLocal])
            if (xValid):
                if (base[yLocal][xLocal] == Status["unconfirmedNum"]):
                    base[y][x] = Status["inProcessCheckedNum"]
                    printMatrix(girdStatus)
                    
                    flagNumbers(yLocal,xLocal)

            
   
y = 0
for row in girdStatus:
    x = 0
    for char in row:
        if(char == 2):
            flagNumbers(y,x)
        x += 1
    y += 1



#for row in grid:
 #   print(row)

for row in girdStatus:
    print(row)



    

