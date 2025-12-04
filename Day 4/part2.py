with open('Day 4/input.txt', 'r') as f:
    answer = 0
    matrix = [list(line.strip()) for line in f]
    rows = len(matrix)
    cols = len(matrix[0])
    removedRolls = -1
    
    while removedRolls != 0:
        removedRolls = 0
        oldMatrix = [row.copy() for row in matrix]
        for col in range(cols):
            for row in range(rows):
                count = 0
                current = oldMatrix[row][col]
                if current == '@':
                    for dr in [-1, 0, 1]:
                        for dc in [-1, 0, 1]:
                            if dr == 0 and dc == 0:
                                continue
                            r, c = row + dr, col + dc
                            if 0 <= r < rows and 0 <= c < cols:
                                if oldMatrix[r][c] == '@':
                                    count += 1                   
                    if count < 4:
                        answer += 1
                        removedRolls += 1
                        matrix[row][col] = '.'
      
    print(answer)