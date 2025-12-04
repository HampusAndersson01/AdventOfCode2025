with open('Day 3\\input.txt', 'r') as file:
    Answer = 0
    for line in file:
        batteriesLeft = 12
        lineLength = len(line.strip())
        JoltageLevel = ""
        biggestFirstChar = -1
        biggestFirstPos = -1
        latestPos = -1
        
        for pos, char in enumerate(line.strip()):
            if int(char) > biggestFirstChar and lineLength - pos >= batteriesLeft:
                biggestFirstChar = int(char)
                biggestFirstPos = pos
        batteriesLeft -= 1
        latestPos = biggestFirstPos
        JoltageLevel += str(biggestFirstChar)
      
        while batteriesLeft > 0:
            biggestOtherChar = -1
            biggestOtherPos = -1
            for pos in range(latestPos+1, len(line)-1):
                char = line[pos]
                if int(char) > biggestOtherChar and lineLength - pos >= batteriesLeft:
                    biggestOtherChar = int(char)
                    biggestOtherPos = pos
            batteriesLeft -= 1
            latestPos = biggestOtherPos
            JoltageLevel += str(biggestOtherChar)
            if batteriesLeft == 0:
                Answer += int(JoltageLevel)     
        
    print(Answer)
                
            
        
       