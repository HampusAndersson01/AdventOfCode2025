with open('Day 3\\input.txt', 'r') as file:
    Answer = 0
    for line in file:
        line = line.strip()
        biggestFirstChar = -1
        biggestFirstPos = -1
        BiggestSecondChar = -1
        BiggestSecondPos = -1
        for pos, char in enumerate(line):
            if int(char) > biggestFirstChar:
                biggestFirstChar = int(char)
                biggestFirstPos = pos
        
        for pos in range(biggestFirstPos+1, len(line)):
            char = line[pos]
            if int(char) > BiggestSecondChar:
                BiggestSecondChar = int(char)
                BiggestSecondPos = pos
        
        #combine both into one number
        Answer += biggestFirstChar * 10 + BiggestSecondChar
    print(Answer)
       