def simulate_guard_path(grid):
   rows, cols = len(grid), len(grid[0])
   directions = {
       "^": (-1, 0),
       ">": (0, 1),
       "v": (1, 0),
       "<": (0, -1),
   }
   turn_order = ["^", ">", "v", "<"]
   for r in range(rows):
       for c in range(cols):
           if grid[r][c] in "^>v<":
               guard_pos = (r, c)
               guard_dir = grid[r][c]
               break
   visited_positions = set()
   visited_positions.add(guard_pos)
   while True:
       dr, dc = directions[guard_dir]
       next_pos = (guard_pos[0] + dr, guard_pos[1] + dc)
       if not (0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols):
           break
       if grid[next_pos[0]][next_pos[1]] == "#":
           guard_dir = turn_order[(turn_order.index(guard_dir) + 1) % 4]
       else:
           guard_pos = next_pos
           visited_positions.add(guard_pos)
   return len(visited_positions)

def read_grid_from_file(filename):
   with open(filename, "r") as file:
       return [list(line.strip()) for line in file.readlines()]

file_path = "Datasets/dataset_day6.txt"
grid = read_grid_from_file(file_path)
result = simulate_guard_path(grid)
print("Distinct positions visited:", result)