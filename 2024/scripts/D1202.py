report_file = open(r"D:\Projects\advent_of_code\2024\inputs\D1202", 'r')

reports = report_file.readlines()
reports = [[int(num) for num in report.split()] for report in reports]

def strictly_increasing(L):
    return [x<y and (1 <= abs(x-y) <= 3)  for x, y in zip(L, L[1:])]

def strictly_decreasing(L):
    return [x>y and (1 <= abs(x-y) <= 3) for x, y in zip(L, L[1:])]

def strictly_monotonic(L):
    return all(strictly_increasing(L)) or all(strictly_decreasing(L))

safe_reports = 0

for report in reports:
    if strictly_monotonic(report):
        safe_reports += 1
    else:
        for i in range(len(report)):
            if strictly_monotonic(report[:i] + report[i + 1:]):
                safe_reports += 1
                break

print(safe_reports)

# print(reports)