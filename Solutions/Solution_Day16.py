class Solution:
    def part1(self, data):
        possible_routes = self.find_routes(data)
        min_score = min(r[1] for r in possible_routes)
        return min_score

    def part2(self, data):
        possible_routes = self.find_routes(data)
        min_score = min(r[1] for r in possible_routes)
        best_routes = [r for r in possible_routes if r[1] == min_score]
        tiles = {tile for route in best_routes for tile in route[0]}
        return len(tiles)

    def find_routes(self, data):
        grid = []
        start = None
        end = None
        for y, row in enumerate(data):
            grid_row = []
            for x, cell in enumerate(row):
                grid_row.append(cell)
                if cell == "S":
                    start = (y, x)
                elif cell == "E":
                    end = (y, x)
            grid.append(grid_row)

        dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        routes = []
        visited = {}

        queue = [(start, [start], 0, 0)]
        while queue:
            (y, x), history, curr_score, curr_dir = queue.pop(0)

            if (y, x) == end:
                routes.append((history, curr_score))
                continue

            if ((y, x), curr_dir) in visited and visited[((y, x), curr_dir)] < curr_score:
                continue

            visited[((y, x), curr_dir)] = curr_score

            for _dir, (dy, dx) in enumerate(dirs):
                if (curr_dir + 2) % 4 == _dir:
                    continue

                ny, nx = y + dy, x + dx
                if grid[ny][nx] != "#" and (ny, nx) not in history:
                    if _dir == curr_dir:
                        queue.append(((ny, nx), history + [(ny, nx)], curr_score + 1, _dir))
                    else:
                        queue.append(((y, x), history, curr_score + 1000, _dir)) 

        return routes


if __name__ == "__main__":
    try:
        with open("Datasets/dataset_day16.txt", "r") as f:
            input_data = [line.strip() for line in f.readlines() if line.strip()] 

        solution = Solution()

        part1_result = solution.part1(input_data)
        print("Part 1:", part1_result)

        part2_result = solution.part2(input_data)
        print("Part 2:", part2_result)

    except FileNotFoundError:
        print("The file 'Datasets/dataset_day16.txt' was not found. Please ensure the file exists.")
    except Exception as e:
        print(f"An error occurred: {e}")
