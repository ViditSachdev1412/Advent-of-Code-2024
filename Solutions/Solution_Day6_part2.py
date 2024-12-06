def simulate_guard_with_obstruction(grid, start_r, start_c, start_dir, obstruction_r, obstruction_c):
   rows, cols = len(grid), len(grid[0])
   directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
   turn_order = ["^", ">", "v", "<"]
   grid[obstruction_r][obstruction_c] = "#"
   guard_pos = (start_r, start_c)
   guard_dir = start_dir
   visited_states = set()
   while True:
       state = (guard_pos[0], guard_pos[1], guard_dir)
       if state in visited_states:
           grid[obstruction_r][obstruction_c] = "."
           return True
       visited_states.add(state)
       dr, dc = directions[guard_dir]
       next_pos = (guard_pos[0] + dr, guard_pos[1] + dc)
       if not (0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols):
           grid[obstruction_r][obstruction_c] = "."
           return False
       if grid[next_pos[0]][next_pos[1]] == "#":
           guard_dir = turn_order[(turn_order.index(guard_dir) + 1) % 4]
       else:
           guard_pos = next_pos

def find_valid_obstructions_for_loop(grid):
   rows, cols = len(grid), len(grid[0])
   directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
   for r in range(rows):
       for c in range(cols):
           if grid[r][c] in directions:
               start_r, start_c = r, c
               start_dir = grid[r][c]
               break
   valid_positions = set()
   for r in range(rows):
       for c in range(cols):
           if grid[r][c] == "." and (r, c) != (start_r, start_c):
               if simulate_guard_with_obstruction(grid, start_r, start_c, start_dir, r, c):
                   valid_positions.add((r, c))
   return valid_positions

def read_grid_from_file(filename):
   with open(filename, "r") as file:
       return [list(line.strip()) for line in file.readlines()]

file_path = "Datasets/dataset_day6.txt"
grid = read_grid_from_file(file_path)
valid_obstructions = find_valid_obstructions_for_loop(grid)
print("Number of valid obstruction positions:", len(valid_obstructions))