import re

with open(r"D:\Projects\advent_of_code\2024\inputs\D1203", 'r') as f:
    memory = f.read()

pattern = r'(mul\(\d{1,3},\s*\d{1,3}\))'

func_calls = re.findall(pattern, memory)

num_pattern = r'(\d{1,3})'
total_sum = 0
for func_call in func_calls:
    num1, num2 = re.findall(num_pattern, func_call)

    total_sum += int(num1) * int(num2)
    # print(num1, num2)

print(total_sum)

memory = r"do()" + memory
# memory =r"do()xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

dont_pattern = r"(don't\(\))"
dont_matches = [match.start() for match in re.finditer(dont_pattern, memory)]

do_pattern = r"(do\(\))"
do_matches = [match.start() for match in re.finditer(do_pattern, memory)]
corrected_memory = ''
last_dont_index = -1
for do_index in do_matches:
    for dont_index in dont_matches:
        if dont_index > do_index and do_index > last_dont_index:
            # print(do_index, dont_index)
            corrected_memory += memory[do_index:dont_index]
            # print(memory[do_index:dont_index])
            last_dont_index = dont_index
            break

    if do_index > dont_matches[-1]:
        corrected_memory += memory[do_index:]
        break


# print(len(memory))
# print(len(corrected_memory))

func_calls = re.findall(pattern, corrected_memory)

num_pattern = r'(\d{1,3})'
total_sum = 0
for func_call in func_calls:
    num1, num2 = re.findall(num_pattern, func_call)

    total_sum += int(num1) * int(num2)
    # print(num1, num2)

print(total_sum)
