def is_safe_report(report_line):
    levels = list(map(int, report_line.split()))
    trend = None

    for i in range(len(levels) - 1):
        diff = levels[i+1] - levels[i]

        if abs(diff) not in {1, 2, 3}:
            return False
        
        if trend is None:
            if diff > 0:
                trend = True
            elif diff < 0:
                trend = False

        if trend is True and diff < 0:
            return False
        elif trend is False and diff > 0:
            return False

    return True

file_path = "Datasets/dataset_day2.txt"
safe_reports = []

with open(file_path, "r") as file:
    for line in file:
        if is_safe_report(line.strip()):
            safe_reports.append(line.strip())

print("Number of Safe Reports:", len(safe_reports))
