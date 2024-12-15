def parse_robot_data(file_path):
    robots = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            p = tuple(map(int, parts[0][2:].split(',')))
            v = tuple(map(int, parts[1][2:].split(',')))
            robots.append((p, v))
    return robots

def simulate_motion(robots, time, width, height):
    positions = []
    for (px, py), (vx, vy) in robots:
        # Calculate new position after `time` seconds with wrap-around
        new_x = (px + vx * time) % width
        new_y = (py + vy * time) % height
        positions.append((new_x, new_y))
    return positions

def count_quadrants(positions, width, height):
    mid_x, mid_y = width // 2, height // 2
    quadrants = [0, 0, 0, 0]  # Top-left, Top-right, Bottom-left, Bottom-right

    for x, y in positions:
        if x == mid_x or y == mid_y:
            continue  # Ignore robots on the middle lines
        if x < mid_x and y < mid_y:
            quadrants[0] += 1  # Top-left
        elif x >= mid_x and y < mid_y:
            quadrants[1] += 1  # Top-right
        elif x < mid_x and y >= mid_y:
            quadrants[2] += 1  # Bottom-left
        else:
            quadrants[3] += 1  # Bottom-right

    return quadrants

def calculate_safety_factor(file_path, time, width, height):
    robots = parse_robot_data(file_path)
    positions = simulate_motion(robots, time, width, height)
    quadrants = count_quadrants(positions, width, height)
    safety_factor = 1
    for count in quadrants:
        safety_factor *= count
    return safety_factor

if __name__ == "__main__":
    file_path = "Datasets/dataset_day14.txt"  # Adjust the file path as needed
    width, height = 101, 103
    time = 100
    safety_factor = calculate_safety_factor(file_path, time, width, height)
    print(f"Safety Factor after {time} seconds: {safety_factor}")
