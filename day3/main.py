regex = r"/[^\d|\.|\n]/gm"

spechialChar = ["*","%","=","#",]

#ascii A-Z 65-90
#ascii a-z 97-122
#asii 0-9 48-57
#ascii . 46

whitelist = list()
whitelist.extend(list(range(65,91))) #A-Z
whitelist.extend(list(range(97,123))) #a-z
whitelist.extend(list(range(48,58))) #0-9
whitelist.extend([46])#.


#print(whitelist)

grid = []
with open("day3/input_copy.txt") as f:
    for line in f:
        line = line[:-1] # remove the /n
        list(line)
        rowList = list(line)
        
        localRow = []
        for rowItem in rowList:
            localRow.append(rowItem)
        
        grid.append(localRow)


y = 0
for row in grid:
    x = 0
    for char in row:
        if(ord(char) not in whitelist):
            print(f"y:{y} x:{x} ",char)
        x += 1
    y += 1


# do number finding logic 

    

for row in grid:
    print(row)
