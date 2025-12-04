with open("Day 2\\input.txt", "r") as file:
    data = [line.strip().split(",") for line in file]
    data = data[0]
    answer = 0
    
    for range_str in data:
        low, high = map(int, range_str.split("-"))
        low, high = int(low), int(high)
        
        for number in range(low, high + 1):
            number_str = str(number)
            length = len(number_str)
            
            for i in range(length, 1, -1):
                # Split number into i parts
                parts = [number_str[j:j + length // i] for j in range(0, length, length // i)]
                if all(part == parts[0] for part in parts):
                    print(f"Match found: {number_str} with {i} parts")
                    answer += number
                    break
                
                
                
    print(f"Final answer: {answer}")