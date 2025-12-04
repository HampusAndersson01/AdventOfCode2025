with open("Day 2\\input.txt", "r") as file:
    data = [line.strip().split(",") for line in file]
    data = data[0]
    answer = 0
    
    for range_str in data:
        low, high = map(int, range_str.split("-"))
        low, high = int(low), int(high)
        
        for number in range(low, high + 1):
            number_str = str(number)

            # split number into two halves
            mid = len(number_str) // 2
            first_half = number_str[:mid]
            second_half = number_str[mid:]
            if first_half == second_half:
                print(f"Match found: {number_str}")
                answer += number
                
    print(f"Final answer: {answer}")