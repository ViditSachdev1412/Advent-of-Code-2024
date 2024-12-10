from collections import deque

def parse_map(file_path):
    with open(file_path, 'r') as file:
        return [list(map(int, line.strip())) for line in file]

def find_trailheads(height_map):
    trailheads = []
    for r, row in enumerate(height_map):
        for c, value in enumerate(row):
            if value == 0:
                trailheads.append((r, c))
    return trailheads

def dfs_trailhead(height_map, start):
    rows, cols = len(height_map), len(height_map[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    stack = [(start[0], start[1], 0)]  # (row, col, current height)
    visited_paths = set()
    distinct_trails = 0

    def dfs(r, c, height, path):
        nonlocal distinct_trails
        # Add current position to the path
        path = path + ((r, c),)

        # If height reaches 9, we found a valid trail
        if height_map[r][c] == 9:
            visited_paths.add(path)
            distinct_trails += 1
            return

        # Explore neighbors
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and height_map[nr][nc] == height + 1:
                if path + ((nr, nc),) not in visited_paths:
                    dfs(nr, nc, height + 1, path)

    # Start DFS from the trailhead
    dfs(start[0], start[1], 0, ())
    return distinct_trails

def calculate_total_rating(file_path):
    height_map = parse_map(file_path)
    trailheads = find_trailheads(height_map)
    total_rating = 0

    for trailhead in trailheads:
        rating = dfs_trailhead(height_map, trailhead)
        total_rating += rating

    return total_rating

# Path to the dataset file
file_path = 'Datasets/dataset_day10.txt'

# Calculate and print the total rating
print(calculate_total_rating(file_path))
