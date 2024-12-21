def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    patterns = lines[0].strip().split(", ")
    designs = [line.strip() for line in lines[2:]]

    return patterns, designs

def count_ways_to_construct_design(patterns, design):
    dp = [0] * (len(design) + 1)
    dp[0] = 1

    for i in range(1, len(design) + 1):
        for pattern in patterns:
            if i >= len(pattern) and design[i - len(pattern):i] == pattern:
                dp[i] += dp[i - len(pattern)]

    return dp[len(design)]

def total_ways(patterns, designs):
    total = 0
    for design in designs:
        total += count_ways_to_construct_design(patterns, design)
    return total

file_path = 'Datasets/dataset_day19.txt'
patterns, designs = read_input(file_path)
total_ways_count = total_ways(patterns, designs)
print(f"Total number of different ways to construct each design: {total_ways_count}")