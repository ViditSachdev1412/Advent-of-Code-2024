import re

def parse_corrupted_memory(memory):
    # Regular expression to find valid mul() instructions
    mul_pattern = r'mul\((\d+),(\d+)\)'
    
    # Regular expressions for do() and don't() instructions
    do_pattern = r'do\(\)'
    dont_pattern = r'don\'t\(\)'
    
    # Initialize variables
    total_sum = 0
    mul_enabled = True
    
    # Find all matches in the memory
    mul_matches = list(re.finditer(mul_pattern, memory))
    do_matches = list(re.finditer(do_pattern, memory))
    dont_matches = list(re.finditer(dont_pattern, memory))
    
    # Combine and sort all matches by their position
    all_matches = sorted(
        mul_matches + do_matches + dont_matches, 
        key=lambda m: m.start()
    )
    
    # Process matches in order
    for match in all_matches:
        if match.group(0).startswith('mul'):
            # If multiplication is enabled, calculate and add
            if mul_enabled:
                x, y = map(int, match.groups())
                total_sum += x * y
        elif match.group(0) == 'do()':
            # Enable multiplications
            mul_enabled = True
        elif match.group(0) == 'don\'t()':
            # Disable multiplications
            mul_enabled = False
    
    return total_sum

# Read the input from the file
with open('Datasets/dataset_day3.txt', 'r') as file:
    corrupted_memory = file.read()

# Calculate the sum of multiplications
result = parse_corrupted_memory(corrupted_memory)
print(f"Sum of multiplications: {result}")