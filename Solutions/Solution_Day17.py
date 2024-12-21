def get_combo_value(operand, A, B, C):
    if operand == 4:
        return A
    elif operand == 5:
        return B
    elif operand == 6:
        return C
    return operand

def run_program(A, B, C, program):
    output = []
    ip = 0

    while ip < len(program):
        opcode = program[ip]
        if ip + 1 < len(program):
            operand = program[ip + 1]
        else:
            operand = 0

        if opcode == 0:  
            denominator = 2 ** get_combo_value(operand, A, B, C)
            A //= denominator
        elif opcode == 1:
            B ^= operand
        elif opcode == 2:
            B = get_combo_value(operand, A, B, C) % 8
        elif opcode == 3:
            if A != 0:
                ip = operand
                continue
        elif opcode == 4:
            B ^= C
        elif opcode == 5:
            output_value = get_combo_value(operand, A, B, C) % 8
            output.append(output_value)
        elif opcode == 6:
            denominator = 2 ** get_combo_value(operand, A, B, C)
            B = A // denominator
        elif opcode == 7:
            denominator = 2 ** get_combo_value(operand, A, B, C)
            C = A // denominator

        ip += 2

    return output

def part1(registers, program):
    output = run_program(registers[0], registers[1], registers[2], program)
    return ",".join(map(str, output))

def part2(program):
    A = sum(7 * 8**i for i in range(len(program) - 1)) + 1

    while True:
        result = run_program(A, 0, 0, program)

        if len(result) > len(program):
            raise ValueError("The output is too long")

        if result == program:
            return A

        add = 0
        for i in range(len(result) - 1, -1, -1):
            if result[i] != program[i]:
                add = 8**i
                A += add
                break

initial_registers = [30886132, 0, 0]
program = [2, 4, 1, 1, 7, 5, 0, 3, 1, 4, 4, 4, 5, 5, 3, 0]

part1_solution = part1(initial_registers, program)
print(f"Part 1 Solution: {part1_solution}")

part2_solution = part2(program)
print(f"Part 2 Solution: {part2_solution}")
