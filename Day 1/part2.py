startPoint = 50
rangeOfDial = 100
counter = 0

with open('Day 1\\input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        direction = line[0]
        distance = int(line[1:])
        
        if direction == 'R':
            for i in range(1, distance + 1):
                if (startPoint + i) % rangeOfDial == 0:
                    counter += 1
            startPoint = (startPoint + distance) % rangeOfDial
            
        elif direction == 'L':
            for i in range(1, distance + 1):
                if (startPoint - i) % rangeOfDial == 0:
                    counter += 1
            startPoint = (startPoint - distance) % rangeOfDial

print(counter)