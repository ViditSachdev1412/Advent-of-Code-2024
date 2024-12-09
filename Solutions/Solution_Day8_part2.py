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
        n = len(locations)
        if n > 1:
            for i in range(n):
                x1, y1 = locations[i]
                for j in range(i + 1, n):
                    x2, y2 = locations[j]
                    dx, dy = x2 - x1, y2 - y1
                    antinodes.add((x1, y1))
                    antinodes.add((x2, y2))
                    for k in range(-1, 2, 2):
                        antinode_x, antinode_y = x1 + k * dx, y1 + k * dy
                        while 0 <= antinode_x < rows and 0 <= antinode_y < cols:
                            antinodes.add((antinode_x, antinode_y))
                            antinode_x += k * dx
                            antinode_y += k * dy
    return antinodes

def plot_map(map, antennas, antinodes):
    map_with_antinodes = [list(row) for row in map]
    for (x, y) in antinodes:
        if map_with_antinodes[x][y] == '.':
            map_with_antinodes[x][y] = '#'
        else:
            map_with_antinodes[x][y] = map_with_antinodes[x][y].upper()
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
