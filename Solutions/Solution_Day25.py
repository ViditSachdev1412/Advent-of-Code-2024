def parse_schematics(input_data):
    schematics = input_data.strip().split("\n\n")
    locks = []
    keys = []
    
    for schematic in schematics:
        rows = schematic.splitlines()
        top_row = rows[0]
        bottom_row = rows[-1]
        
        # Identify locks
        if top_row == '#' * len(top_row) and bottom_row == '.' * len(bottom_row):
            locks.append(rows)
        
        # Identify keys
        elif top_row == '.' * len(top_row) and bottom_row == '#' * len(bottom_row):
            keys.append(rows)
    
    print("Parsed Locks:", len(locks))
    print("Parsed Keys:", len(keys))
    return locks, keys

def convert_to_heights(schematic, is_lock=True):
    columns = zip(*schematic)
    heights = []
    for column in columns:
        if is_lock:
            heights.append(sum(1 for cell in column if cell == '#'))
        else:
            heights.append(sum(1 for cell in reversed(column) if cell == '#'))
    return heights

def count_valid_pairs(locks, keys):
    lock_heights = [convert_to_heights(lock, is_lock=True) for lock in locks]
    key_heights = [convert_to_heights(key, is_lock=False) for key in keys]
    
    total_pairs = 0
    for lock_idx, lock in enumerate(lock_heights):
        for key_idx, key in enumerate(key_heights):
            if all(l + k <= len(locks[0]) for l, k in zip(lock, key)):
                print(f"Lock {lock_idx} fits with Key {key_idx}")
                total_pairs += 1
    
    return total_pairs

# Main Execution
if __name__ == "__main__":
    with open("Datasets/dataset_day25.txt", "r") as file:
        input_data = file.read()

    locks, keys = parse_schematics(input_data)
    result = count_valid_pairs(locks, keys)
    print("Number of valid lock/key pairs:", result)
