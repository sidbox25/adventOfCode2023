
#todo adjust input 
with open("day4/input.txt") as f:
    total = 0
    for line in f:
        line = line[:-1] # remove the /n

        gameNumber = line.split(":")[0]
        winningNumbers = line.split(":")[1].split("|")[0].split(" ")
        currentNumbers = line.split(":")[1].split("|")[1].split(" ")
        
        winningNumbers = list(filter(None, winningNumbers))
        currentNumbers = list(filter(None, currentNumbers))

        nrOfMatches = 0
        for currentNumber in currentNumbers:
            if currentNumber in winningNumbers:
                nrOfMatches += 1
                

        valToAdd = 0 if nrOfMatches == 0 else 2 ** (nrOfMatches-1)
        total += valToAdd
    
    print(total)