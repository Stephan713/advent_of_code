import itertools

with open(r"D:\Projects\advent_of_code\2024\inputs\D1207", 'r') as f:
    calibrations = f.readlines()

calibrations = [calibration.strip() for calibration in calibrations]
values = ['+','*','||']

calibration_result = 0
true_counts = 0

for calibration in calibrations:
    # print(calibration)
    test_value = int(calibration.split(':')[0])
    inputs = [int(num) for num in calibration.split(':')[1].split()]

    combinations = list(itertools.product(values, repeat=len(inputs)-1))

    for combination in combinations:
        result = 0
        for i, input in enumerate(inputs):
            if i == 0:
                result += input
            else:
                if combination[i-1] == '*':
                    result *= input
                elif combination[i-1] == '+':
                    result += input
                elif combination[i-1] == '||':
                    result = int(f"{result}{input}")

        if result == test_value:
            # print(result)
            calibration_result += result
            true_counts += 1
            break


print(calibration_result)
print(true_counts)
