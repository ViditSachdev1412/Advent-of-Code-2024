from collections import defaultdict

# Load the dataset from the file
with open('Datasets/dataset_day15.txt', 'r') as f:
    parts = f.read().split('\n\n')

# Process the grid (first part of the dataset)
parts[0] = parts[0].replace('#', '##') \
    .replace('O', '[]') \
    .replace('.', '..') \
    .replace('@', '@.')

# Create the grid using defaultdict to handle default values
g = defaultdict(lambda: "#") | {(i, j): c for i, line in enumerate(parts[0].splitlines()) for j, c in enumerate(line)}

# Find the initial position of the robot (@)
x, y = next(n for n in g if g[n] == '@')

# Define the function to check if the robot can move
def can_move(_x, _y, _dx, _dy):
    target = _x + _dx, _y + _dy
    if g[target] == '.':
        return True
    if g[target] == '#':
        return False
    if _dx == 0:
        return can_move(*target, _dx, _dy)
    else:
        lr = -1 if g[target] == ']' else 1
        return can_move(*target, _dx, _dy) and can_move(target[0], target[1] + lr, _dx, _dy)

# Define the function to move the robot
def move(_x, _y, _dx, _dy):
    target = _x + _dx, _y + _dy
    if g[target] != '.':
        if _dx == 0:
            move(*target, _dx, _dy)
        else:
            if g[target] in '[]':
                lr = -1 if g[target] == ']' else 1
                move(_x + _dx, _y + _dy + lr, _dx, _dy)
                move(_x + _dx, _y + _dy, _dx, _dy)
    g[target] = g[_x, _y]
    g[_x, _y] = '.'

# Process the moves from the second part of the dataset
for d in parts[1].replace('\n', ''):
    assert g[x, y] == '@'
    dx, dy = {'<': (0, -1), '>': (0, 1), '^': (-1, 0), 'v': (1, 0)}[d]
    nx, ny = x + dx, y + dy
    if can_move(x, y, dx, dy):
        move(x, y, dx, dy)
        x, y = nx, ny

# Print the result as the sum of coordinates for each object '['
print(sum(p[0] * 100 + p[1] for p in g if g[p] == '['))
