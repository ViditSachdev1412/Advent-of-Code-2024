def count_xmas_occurrences(grid, word="XMAS"):
    rows = len(grid)
    cols = len(grid[0])
    word_length = len(word)
    total_count = 0

    directions = [
        (0, 1),   
        (1, 0),   
        (1, 1),   
        (1, -1),  
        (0, -1),  
        (-1, 0),  
        (-1, -1), 
        (-1, 1),  
    ]

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def check_direction(x, y, dx, dy):
        for i in range(word_length):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid(nx, ny) or grid[nx][ny] != word[i]:
                return 0
        return 1

    for row in range(rows):
        for col in range(cols):
            for dx, dy in directions:
                total_count += check_direction(row, col, dx, dy)

    return total_count

file_path = "Datasets/dataset_day4.txt" 
with open(file_path, "r") as file:
    grid = [line.strip() for line in file]

result = count_xmas_occurrences(grid)

print("Total occurrences of 'XMAS':", result)