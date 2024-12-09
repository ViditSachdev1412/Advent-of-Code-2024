def find_antennas(map):
    antennas = {}
    for i, row in enumerate(map):
        for j, char in enumerate(row):
            if char != '.':
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((i, j))
    return antennas

def find_antinodes(antennas, rows, cols):
    antinodes = set()
    for freq, locations in antennas.items():
        for i, (x1, y1) in enumerate(locations):
            for j, (x2, y2) in enumerate(locations):
                if i != j:
                    dx, dy = x2 - x1, y2 - y1
                    antinode1 = (x1 - dx, y1 - dy)
                    antinode2 = (x2 + dx, y2 + dy)
                    if 0 <= antinode1[0] < rows and 0 <= antinode1[1] < cols:
                        antinodes.add(antinode1)
                    if 0 <= antinode2[0] < rows and 0 <= antinode2[1] < cols:
                        antinodes.add(antinode2)
    return antinodes

def plot_map(map, antennas, antinodes):
    map_with_antinodes = [list(row) for row in map]
    for (x, y) in antinodes:
        if map_with_antinodes[x][y] == '.':
            map_with_antinodes[x][y] = '#'

    for row in map_with_antinodes:
        print(''.join(row))

with open('Datasets/dataset_day8.txt', 'r') as file:
    map = file.read().splitlines()

rows = len(map)
cols = len(map[0])

antennas = find_antennas(map)
antinodes = find_antinodes(antennas, rows, cols)
plot_map(map, antennas, antinodes)

print("Number of unique antinode locations:", len(antinodes))
