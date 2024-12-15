def parse_input(filepath):
    with open(filepath, 'r') as f:
        raw_data = f.read()
    machines = raw_data.strip().split("\n\n")
    parsed_machines = []

    for machine in machines:
        btn_a, btn_b, prize = machine.split("\n")

        btn_a = [int(i[2:]) for i in btn_a.split(": ")[1].split(", ")]
        btn_b = [int(i[2:]) for i in btn_b.split(": ")[1].split(", ")]
        prize = [int(i[2:]) for i in prize.split(": ")[1].split(", ")]

        parsed_machines.append((btn_a, btn_b, prize))

    return parsed_machines

def solve_claw_machine_part2(machines):
    OFFSET = 10**13
    total_tokens = 0

    for btn_a, btn_b, prize in machines:
        p_x, p_y = prize[0] + OFFSET, prize[1] + OFFSET

        determinant = btn_a[0] * btn_b[1] - btn_a[1] * btn_b[0]
        if determinant == 0:
            continue

        A = (p_x * btn_b[1] - p_y * btn_b[0]) / determinant
        B = (btn_a[0] * p_y - btn_a[1] * p_x) / determinant

        if A.is_integer() and B.is_integer() and A >= 0 and B >= 0:
            A, B = int(A), int(B)
            total_tokens += 3 * A + B

    return total_tokens

def main():
    filepath = "Datasets/dataset_day13.txt"
    machines = parse_input(filepath)
    part2_result = solve_claw_machine_part2(machines)
    print(f"Part 2: Total tokens required = {part2_result}")

if __name__ == "__main__":
    main()
