#12 red, 13 green, 14 blue

maxRed = 12
maxGreen = 13
maxBlue = 14


with open("day2/input.txt") as f:
    total = 0
    for line in f:
        validGame = True
        minRed = 0
        minGreen = 0
        minBlue = 0


        split1 = line.split(":")
        game = split1[0]
        pulls = split1[1].split(";")
        pulls[-1] = pulls[-1][:-1]

        for pull in pulls:
            colors = pull.split(",")
            #colors = list(map(lambda color:color.strip().split(" "),colors))

            for color in colors:
                color = color.strip().split(" ")

                """
                #part 1
                if (color[1] == "red"):
                    if (int(color[0]) > maxRed):
                        validGame = False
                        print(f"too much red in {game} , {colors}")
                if (color[1] == "green"):
                    if (int(color[0]) > maxGreen):
                        validGame = False
                        print(f"too much green in {game} , {colors}")
                if (color[1] == "blue"):
                    if (int(color[0]) > maxBlue):
                        validGame = False
                        print(f"too much blue in {game} , {colors}")
                """

                if (color[1] == "red"):
                    if(int(color[0])>minRed):
                        minRed = int(color[0])
                if (color[1] == "green"):
                    if(int(color[0])>minGreen):
                        minGreen = int(color[0])
                if (color[1] == "blue"):
                    if(int(color[0])>minBlue):
                        minBlue = int(color[0])

        """
        #part 1
        if (validGame):
            
            total += int(game.split(" ")[1])
        """

        # part 2
        valToAdd = minRed * minGreen * minBlue
        print(valToAdd, " ",total)
        total += (minRed * minGreen * minBlue)
    print(total)





                

        #print(game, allPulls)

        
        

