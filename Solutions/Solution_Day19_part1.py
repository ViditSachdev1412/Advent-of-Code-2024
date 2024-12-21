def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    patterns = lines[0].strip().split(", ")
    designs = [line.strip() for line in lines[2:]]  # assuming there's a blank line separating patterns and designs

    return patterns, designs

def can_construct_design(patterns, design):
    dp = [False] * (len(design) + 1)
    dp[0] = True

    for i in range(1, len(design) + 1):
        for pattern in patterns:
            if i >= len(pattern) and design[i - len(pattern):i] == pattern:
                dp[i] = dp[i] or dp[i - len(pattern)]

    return dp[len(design)]

def count_possible_designs(patterns, designs):
    count = 0
    for design in designs:
        if can_construct_design(patterns, design):
            count += 1
    return count

# File path to the input data
file_path = 'Datasets/dataset_day19.txt'

# Read input from the file
patterns, designs = read_input(file_path)

# Calculate the number of possible designs
possible_designs_count = count_possible_designs(patterns, designs)

# Print the result
print(f"Number of possible designs: {possible_designs_count}")
