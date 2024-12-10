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

def bfs_trailhead(height_map, start):
    rows, cols = len(height_map), len(height_map[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = set()
    queue = deque([(start[0], start[1], 0)])  # (row, col, current height)
    reachable_nines = set()
    
    while queue:
        r, c, height = queue.popleft()
        
        if (r, c) in visited:
            continue
        visited.add((r, c))
        
        # If we've reached a height of 9, record it
        if height_map[r][c] == 9:
            reachable_nines.add((r, c))
            continue
        
        # Explore neighbors
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and height_map[nr][nc] == height + 1:
                queue.append((nr, nc, height + 1))
    
    return len(reachable_nines)

def calculate_total_score(file_path):
    height_map = parse_map(file_path)
    trailheads = find_trailheads(height_map)
    total_score = 0
    
    for trailhead in trailheads:
        score = bfs_trailhead(height_map, trailhead)
        total_score += score
    
    return total_score

# Path to the dataset file
file_path = 'Datasets/dataset_day10.txt'

# Calculate and print the total score
print(calculate_total_score(file_path))
