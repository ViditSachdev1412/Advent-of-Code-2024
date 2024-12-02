def is_safe_report(report_line):
    levels = list(map(int, report_line.split()))

    def check_safety(levels):
        for i in range(len(levels) - 1):
            diff = levels[i+1] - levels[i]
            if abs(diff) not in {1,2,3}:  
                return False
            if i > 0:  
                prev_diff = levels[i] - levels[i-1]
                if (prev_diff > 0 and diff < 0) or (prev_diff < 0 and diff > 0):
                    return False
        return True

    if check_safety(levels):
        return True

    for i in range(len(levels)):
        new_levels = levels[:i] + levels[i+1:]
        if check_safety(new_levels):
            return True

    return False

file_path = "Datasets/dataset_day2.txt"  
safe_reports = []

with open(file_path, "r") as file:
    for line in file:
        if is_safe_report(line.strip()):
            safe_reports.append(line.strip())

print("Number of Safe Reports:", len(safe_reports))
