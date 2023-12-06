import regex as re
from functools import reduce
from operator import mul

input_file = open("inputs/03_01_input.txt", 'r')
tot_sum = 0

data = input_file.readlines()

number_of_lines = len(data)

for i,line in enumerate(data):
    line = line.strip()
    pattern = re.compile(r"([0-9]+)")
    # print(len(line))

    for j ,match in enumerate(pattern.finditer(line)):
        # print(match.group())
        # print(match.span())

        if match.span()[0] == 0:
            before_text = ''
        else:
            before_text = line.strip()[match.span()[0]-1]

        if match.span()[1] >= 139:
            after_text = ''
        else:
            after_text = line.strip()[match.span()[1]]

        if i == 0:
            above_text = ''
        elif match.span()[0] == 0:
            above_text = data[i - 1].strip()[match.span()[0]:match.span()[1] + 1]
        elif match.span()[1] == 140:
            above_text = data[i - 1].strip()[match.span()[0]-1:match.span()[1]]
        else:
            above_text = data[i-1].strip()[match.span()[0]-1:match.span()[1]+1]

        if i == len(data)-1:
            below_text = ''
        elif match.span()[0] == 0:
            below_text = data[i + 1].strip()[match.span()[0]:match.span()[1] + 1]
        elif match.span()[1] == 140:
            below_text = data[i + 1].strip()[match.span()[0]-1:match.span()[1]]
        else:
            below_text = data[i+1].strip()[match.span()[0]-1:match.span()[1]+1]

        boundaries = above_text + before_text + after_text + below_text

        # print(len(re.sub(r'[a-z0-9.]', '', boundaries)))

        # if match.group() in ['873']:
        #     print('Here')
        #     print(i)
        #     print(match.span())
        #     print('***')
        #     print(data[i-1].strip()[match.span()[0]-1:match.span()[1]+1])
        #     print('above_text: ', above_text)
        #     print('***')
        #     print('before_text: ', before_text)
        #     print('***')
        #     # print(line.strip()[match.span()[1]])
        #     print('after_text: ', after_text)
        #     print(below_text)

        if len(re.sub(r'[.]', '', boundaries)) > 0:
            # print(match.group())
            tot_sum = tot_sum + int(match.group())







    # if i == 11:
    #     break

# print(tot_sum)

####################################################

input_file = open("inputs/03_01_input.txt", 'r')
tot_sum = 0
product = 0

data = input_file.readlines()

number_of_lines = len(data)

for i,line in enumerate(data):
    gear_above = gear_below = gear_before = gear_after = 1
    line = line.strip()

    pattern = re.compile(r"(\*)")

    for j, match in enumerate(pattern.finditer(line)):

        if match.span()[0] == 0:
            before_text = ''
        else:
            before_text = line.strip()[match.span()[0] - 1]

        if match.span()[1] >= 139:
            after_text = ''
        else:
            after_text = line.strip()[match.span()[1]]

        if i == 0:
            above_text = ''
        elif match.span()[0] == 0:
            above_text = data[i - 1].strip()[match.span()[0]:match.span()[1] + 1]
        elif match.span()[1] == 140:
            above_text = data[i - 1].strip()[match.span()[0] - 1:match.span()[1]]
        else:
            above_text = data[i - 1].strip()[match.span()[0] - 1:match.span()[1] + 1]

        if i == len(data) - 1:
            below_text = ''
        elif match.span()[0] == 0:
            below_text = data[i + 1].strip()[match.span()[0]:match.span()[1] + 1]
        elif match.span()[1] == 140:
            below_text = data[i + 1].strip()[match.span()[0] - 1:match.span()[1]]
        else:
            below_text = data[i + 1].strip()[match.span()[0] - 1:match.span()[1] + 1]

        gear_set = {*range(match.span()[0]-1, match.span()[1]+1)}
        print('line no:', i)
        print('gear_set:', gear_set)
        gear_above = gear_below = gear_before = gear_after = 1

        gear_numbers = []
        if re.findall(r'[0-9]+', before_text):
            text = line[:match.span()[0]]
            gear_before = int(re.findall(r'([0-9]+)', text)[-1])
            gear_numbers.append(gear_before)

        if re.findall(r'[0-9]+', after_text):
            text = line[match.span()[1]:]
            gear_after= int(re.findall(r'([0-9]+)', text)[0])
            gear_numbers.append(gear_after)

        if re.findall(r'[0-9]+', above_text):
            # print('above_text')
            text = data[i-1]
            pattern = re.compile(r"([0-9]+)")
            for k, number in enumerate(pattern.finditer(text)):
                # print(number.group())
                # print(number.span())
                num_range = {*range(number.span()[0], number.span()[1])}
                # print(num_range)
                # print('inter:', gear_set.intersection(num_range))
                if list(gear_set.intersection(num_range)):
                    gear_above = int(number.group())
                    gear_numbers.append(gear_above)
                    # print('gear_above:', gear_above)

        if re.findall(r'[0-9]+', below_text):
            text = data[i + 1]
            pattern = re.compile(r"([0-9]+)")
            for k, number in enumerate(pattern.finditer(text)):
                num_range = {*range(number.span()[0], number.span()[1])}

                if list(gear_set.intersection(num_range)):
                    gear_below = int(number.group())
                    gear_numbers.append(gear_below)
                    # print('gear_below:', gear_below)



        if len(gear_numbers) > 1:
            product = reduce(mul, gear_numbers)
        else:
            product = 0
        print('product:', product)
        if product > 1:
            tot_sum = tot_sum + product

    # if i == 2:
    #     break

print(tot_sum)