from typing import List, Dict, Set

def read_input_from_file(filename: str) -> str:
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        return ""
    except IOError:
        print(f"Error: Could not read file {filename}.")
        return ""

def parse_input(input_text: str) -> tuple:
    sections = input_text.strip().split('\n\n')
    
    rules = {}
    for line in sections[0].split('\n'):
        before, after = map(int, line.split('|'))
        if before not in rules:
            rules[before] = set()
        if after not in rules:
            rules[after] = set()
        rules[before].add(after)
    
    updates = [list(map(int, line.split(','))) for line in sections[1].split('\n')]
    
    return rules, updates

def is_valid_order(sequence: List[int], rules: Dict[int, Set[int]]) -> bool:
    page_positions = {page: index for index, page in enumerate(sequence)}
    
    for before, after_set in rules.items():
        if before in page_positions and any(
            after in page_positions and 
            page_positions[before] >= page_positions[after] 
            for after in after_set
        ):
            return False
    
    return True

def topological_sort(pages: List[int], rules: Dict[int, Set[int]]) -> List[int]:
    graph = {page: set() for page in pages}
    in_degree = {page: 0 for page in pages}
    
    for before, after_set in rules.items():
        if before in pages and any(after in pages for after in after_set):
            for after in after_set:
                if after in pages and before in pages:
                    if after not in graph[before]:
                        graph[before].add(after)
                        in_degree[after] += 1
    
    queue = [page for page in pages if in_degree[page] == 0]
    sorted_pages = []
    
    while queue:
        current = queue.pop(0)
        sorted_pages.append(current)
        
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return sorted_pages if len(sorted_pages) == len(pages) else pages

def solve_part1(input_text: str) -> int:
    rules, updates = parse_input(input_text)
    
    valid_middle_pages = []
    
    for update in updates:
        if is_valid_order(update, rules):
            mid_index = len(update) // 2
            valid_middle_pages.append(update[mid_index])
    
    return sum(valid_middle_pages)

def solve_part2(input_text: str) -> int:
    rules, updates = parse_input(input_text)
    
    incorrect_middle_pages = []
    
    for update in updates:
        if not is_valid_order(update, rules):
            sorted_update = topological_sort(update, rules)
            
            mid_index = len(sorted_update) // 2
            incorrect_middle_pages.append(sorted_update[mid_index])
    
    return sum(incorrect_middle_pages)

def main():
    filename = 'Datasets/dataset_day5.txt'
    input_text = read_input_from_file(filename)
    
    if input_text:
        part1_result = solve_part1(input_text)
        part2_result = solve_part2(input_text)
        
        print(f"Part 1 Result: {part1_result}")
        print(f"Part 2 Result: {part2_result}")

if __name__ == "__main__":
    main()