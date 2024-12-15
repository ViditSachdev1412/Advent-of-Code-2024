with open("Datasets/dataset_day14.txt") as file:
    lines = []
    for line in file:
        line = line.strip()
        pos_part, vel_part = line.split(' v=')  # Split into position and velocity
        x, y = map(int, pos_part.split('=')[1].split(','))  # Extract position x, y
        dx, dy = map(int, vel_part.split(','))  # Extract velocity dx, dy
        lines.append([[x, y], [dx, dy]])  # Append as [[position], [velocity]]

width, height = 101, 103
seconds = 1

while True:
    robots = set()
    for robot in lines:
        robot[0][0] = (robot[0][0] + robot[1][0]) % width  # Update x position
        robot[0][1] = (robot[0][1] + robot[1][1]) % height  # Update y position
        robots.add(tuple(robot[0]))

    while len(robots) > 0:
        dirs = [[0, +1], [0, -1], [+1, 0], [-1, 0]]
        locations = [next(iter(robots))]  # Start BFS with one robot position
        i = 0
        while i < len(locations):
            for dir in dirs:
                t = (locations[i][0] + dir[0], locations[i][1] + dir[1])
                if t in robots and t not in locations:
                    locations.append(t)
            robots.remove(locations[i])  # Remove visited position
            i += 1

        if len(locations) >= 15:  # Check if cluster of size >= 15 exists
            print("PART 2 SOLUTION PERHAPS - CHECK", seconds)
            exit()
    seconds += 1
