def parse_data(file_path):
    with open(file_path, 'r') as file:
        corrupted = [[*map(int, line.strip().split(","))] for line in file]

    if len(corrupted) == 25:  # test input
        size = 7
        corrupted_length = 12
    else:
        size = 71
        corrupted_length = 1024

    return corrupted, size, corrupted_length

def set_grid(corrupted, size, corrupted_length):
    grid = [["."] * size for _ in range(size)]
    for x, y in corrupted[:corrupted_length]:
        grid[y][x] = "#"
    return grid

def add_corrupted(grid, cx, cy):
    grid[cy][cx] = "#"

def get_shortest_path_steps(grid):
    size = len(grid)
    start = (0, 0)
    end = (size - 1, size - 1)

    # BFS
    queue = [(start, 0)]  # pos, length
    seen = set()
    while queue:
        pos, length = queue.pop(0)
        if pos == end:
            return length
        if pos in seen:
            continue
        seen.add(pos)
        x, y = pos
        for dx, dy in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < size and 0 <= ny < size and grid[ny][nx] == ".":
                queue.append(((nx, ny), length + 1))
    return -1  # no path

def part1(file_path):
    corrupted, size, corrupted_length = parse_data(file_path)
    grid = set_grid(corrupted, size, corrupted_length)
    steps = get_shortest_path_steps(grid)
    return steps

def part2(file_path):
    corrupted, size, corrupted_length = parse_data(file_path)

    start = corrupted_length
    end = len(corrupted)

    while end - start > 1:
        mid = (start + end) // 2
        grid = set_grid(corrupted, size, mid)
        steps = get_shortest_path_steps(grid)
        if steps == -1:
            end = mid
        else:
            start = mid

    return f"{corrupted[end-1][0]},{corrupted[end-1][1]}"

file_path = 'Datasets/dataset_day18.txt'

print("Part 1 Solution:", part1(file_path))
print("Part 2 Solution:", part2(file_path))
