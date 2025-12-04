startPoint=50
rangeOfDial=100 # Dial ranges from 0 to 99
counter=0



with open('Day 1\\input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if line[0] == 'R':
            startPoint += int(line[1:])
        elif line[0] == 'L':
            startPoint -= int(line[1:])
        startPoint = startPoint % rangeOfDial
        if startPoint == 0:
            counter += 1
print(counter)