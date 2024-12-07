from itertools import product
def evaluate_expression_left_to_right(numbers, operators):
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == "+":
            result += numbers[i + 1]
        elif operators[i] == "*":
            result *= numbers[i + 1]
    return result

def can_match_target(test_value, numbers):
    num_operators = len(numbers) - 1
    for operators in product(["+", "*"], repeat=num_operators):
        if evaluate_expression_left_to_right(numbers, operators) == test_value:
            return True
    return False

def solve_bridge_repair(file_name):
    total_calibration_result = 0
    with open(file_name, "r") as f:
        input_lines = f.read().splitlines()
    for line in input_lines:
        test_value_str, numbers_str = line.split(": ")
        test_value = int(test_value_str)
        numbers = list(map(int, numbers_str.split()))
        if can_match_target(test_value, numbers):
            total_calibration_result += test_value
    return total_calibration_result

result = solve_bridge_repair("Datasets/dataset_day7.txt")
print(f"Total calibration result: {result}")