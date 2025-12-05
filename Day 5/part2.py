def read_input(filename):
    with open(filename, 'r') as f:
        content = f.read().strip()
    sections = content.split('\n\n')
    
    ranges = []
    
    for section in sections:
        lines = section.strip().split('\n')
        for line in lines:
            if '-' in line:
                start, end = line.split('-')
                ranges.append((int(start), int(end)))
    
    return ranges

def merge_ranges(ranges):
    if not ranges:
        return []
    ranges.sort(key=lambda x: x[0])
    
    merged = [ranges[0]]
    
    for current in ranges[1:]:
        last = merged[-1]
        if current[0] <= last[1] + 1: 
            merged[-1] = (last[0], max(last[1], current[1]))
        else:
            merged.append(current)
    
    return merged

def validIds(ranges):
    merged_ranges = merge_ranges(ranges)
    valid_ids = 0
    for start, end in merged_ranges:
        valid_ids += (end - start + 1)
        
    return valid_ids

if __name__ == "__main__":
    ranges = read_input('Day 5\\input.txt')
    valid_ids = validIds(ranges)
    print(f"Valid IDs: {valid_ids}")