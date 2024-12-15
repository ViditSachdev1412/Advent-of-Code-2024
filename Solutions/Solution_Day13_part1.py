def find_min_tokens(A_x, A_y, B_x, B_y, prize_x, prize_y):
    min_tokens = float('inf')
    best_a_presses = None
    best_b_presses = None

    for a_presses in range(101):
        remaining_x = prize_x - (a_presses * A_x)
        remaining_y = prize_y - (a_presses * A_y)
        
        if remaining_x % B_x == 0 and remaining_y % B_y == 0:
            b_presses = remaining_x // B_x
            if b_presses >= 0 and remaining_y == b_presses * B_y:
                total_tokens = a_presses * 3 + b_presses * 1
                if total_tokens < min_tokens:
                    min_tokens = total_tokens
                    best_a_presses = a_presses
                    best_b_presses = b_presses

    if best_a_presses is None or best_b_presses is None:
        return None
    
    return min_tokens

file_path = "Datasets/dataset_day13.txt"
machines = []

with open(file_path, 'r') as file:
    lines = file.readlines()
    for i in range(0, len(lines), 4):
        A_line = lines[i].strip().split(': ')[1].split(', ')
        B_line = lines[i+1].strip().split(': ')[1].split(', ')
        prize_line = lines[i+2].strip().split(': ')[1].split(', ')
        
        A_x = int(A_line[0].split('+')[1])
        A_y = int(A_line[1].split('+')[1])
        B_x = int(B_line[0].split('+')[1])
        B_y = int(B_line[1].split('+')[1])
        prize_x = int(prize_line[0].split('=')[1])
        prize_y = int(prize_line[1].split('=')[1])
        
        machines.append({"A_x": A_x, "A_y": A_y, "B_x": B_x, "B_y": B_y, "prize_x": prize_x, "prize_y": prize_y})

total_tokens_needed = 0
prizes_won = 0

for machine in machines:
    min_tokens = find_min_tokens(machine["A_x"], machine["A_y"], machine["B_x"], machine["B_y"], machine["prize_x"], machine["prize_y"])
    if min_tokens is not None:
        total_tokens_needed += min_tokens
        prizes_won += 1

print(f'Total tokens needed: {total_tokens_needed}')
print(f'Total prizes won: {prizes_won}')
