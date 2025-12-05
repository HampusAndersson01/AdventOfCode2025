def read_input(filename):
    with open(filename, 'r') as f:
        content = f.read().strip()
    sections = content.split('\n\n')
    
    ranges = []
    ids = []
    
    for section in sections:
        lines = section.strip().split('\n')
        for line in lines:
            if '-' in line:
                start, end = line.split('-')
                ranges.append((int(start), int(end)))
            else:
                ids.append(int(line))
    
    return ranges, ids

def validateIds(ranges, ids):
    valid_ids = 0
    for id_ in ids:
        for start, end in ranges:
            if start <= id_ <= end:
                valid_ids += 1
                break
    return valid_ids

if __name__ == "__main__":
    ranges, ids = read_input('Day 5\\input.txt')
    valid_ids = validateIds(ranges, ids)
    print(f"Valid IDs: {valid_ids}")