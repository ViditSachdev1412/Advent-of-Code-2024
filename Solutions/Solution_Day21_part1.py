from itertools import permutations, product

numeric_keys = {
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),
    "0": (3, 1),
    "A": (3, 2)
}

direction_keys = {
    "^": (0, 1),
    "A": (0, 2),
    "<": (1, 0),
    "v": (1, 1),
    ">": (1, 2)
}

dd = {
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1),
    "^": (-1, 0)
}

def generate_paths(code, keypad):
    """Generate all valid paths to press a code on the given keypad."""
    all_combos = []
    cur_loc = keypad["A"]

    for char in code:
        target_loc = keypad[char]
        di = target_loc[0] - cur_loc[0]
        dj = target_loc[1] - cur_loc[1]

        moves = ""
        if di > 0:
            moves += "v" * di
        elif di < 0:
            moves += "^" * -di
        if dj > 0:
            moves += ">" * dj
        elif dj < 0:
            moves += "<" * -dj

        raw_combos = list(set(permutations(moves)))
        valid_combos = []

        for combo in raw_combos:
            path = "".join(combo) + "A"
            ci, cj = cur_loc
            valid = True
            for move in path[:-1]:
                di, dj = dd[move]
                ci, cj = ci + di, cj + dj
                if (ci, cj) not in keypad.values():
                    valid = False
                    break
            if valid:
                valid_combos.append(path)

        all_combos.append(valid_combos)
        cur_loc = target_loc 
    return ["".join(p) for p in product(*all_combos)]

def shortest_path(code):
    """Get the shortest path by combining the three levels."""
    level1 = generate_paths(code, numeric_keys)
    level2 = [path for l1_path in level1 for path in generate_paths(l1_path, direction_keys)]
    level3 = [path for l2_path in level2 for path in generate_paths(l2_path, direction_keys)]

    return min(len(path) for path in level3)

with open("Datasets/dataset_day21.txt") as fin:
    lines = fin.read().strip().split("\n")

total_complexity = 0
for line in lines:
    code_complexity = shortest_path(line) * int(line[:-1])
    print(shortest_path(line), int(line[:-1]))
    total_complexity += code_complexity

print(total_complexity)
