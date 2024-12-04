def count_x_mas(grid):
    rows = len(grid)
    cols = len(grid[0])
    x_mas_count = 0

    # Helper function to check if a cell is within bounds
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    # Check if "MAS" exists on a given diagonal
    def check_mas(x1, y1, x2, y2, x3, y3):
        if is_valid(x1, y1) and is_valid(x2, y2) and is_valid(x3, y3):
            # Check "MAS" forward
            if grid[x1][y1] == "M" and grid[x2][y2] == "A" and grid[x3][y3] == "S":
                return True
            # Check "MAS" backward
            if grid[x1][y1] == "S" and grid[x2][y2] == "A" and grid[x3][y3] == "M":
                return True
        return False

    # Iterate through the grid, treating each cell as the center of the "X"
    for row in range(rows):
        for col in range(cols):
            # Check diagonals forming an "X"
            if (
                check_mas(row - 1, col - 1, row, col, row + 1, col + 1) and  # Top-left to bottom-right
                check_mas(row - 1, col + 1, row, col, row + 1, col - 1)      # Top-right to bottom-left
            ):
                x_mas_count += 1

    return x_mas_count


# Read the input file
file_path = "Datasets/dataset_day4.txt"  # Update with your actual file path
with open(file_path, "r") as file:
    grid = [line.strip() for line in file]

# Find and print the result
result = count_x_mas(grid)
print("Total occurrences of 'X-MAS':", result)
