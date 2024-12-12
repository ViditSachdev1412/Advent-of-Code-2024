from collections import Counter

def transform_stone_batch(stone, count):
    transformations = Counter()
    if stone == 0:
        transformations[1] += count
    elif len(str(stone)) % 2 == 0:
        digits = str(stone)
        mid = len(digits) // 2
        left = int(digits[:mid])
        right = int(digits[mid:])
        transformations[left] += count
        transformations[right] += count
    else:
        transformations[stone * 2024] += count
    return transformations

def simulate_blinks_optimized(stones, blinks):

    stone_counts = Counter(stones)
    for _ in range(blinks):
        new_counts = Counter()
        for stone, count in stone_counts.items():
            new_counts.update(transform_stone_batch(stone, count))
        stone_counts = new_counts
    return sum(stone_counts.values())

initial_stones = [5, 127, 680267, 39260, 0, 26, 3553, 5851995]
blinks = 25

# Part 1 Calculate the number of stones after 25 blinks
result = simulate_blinks_optimized(initial_stones, blinks)
print(f"Number of stones after 25 blinks: {result}")

# Part 2 Calculate the number of stones after 75 blinks
blinks2 = 75
result2 = simulate_blinks_optimized(initial_stones, blinks2)
print(f"Number of stones after 75 blinks: {result2}")