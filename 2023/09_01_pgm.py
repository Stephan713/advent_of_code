from typing import Union, List, Dict, Any

input_file = open("inputs/09_01_input.txt", 'r')
tot_sum = 0

history_readings = input_file.readlines()
# print(history_readings[0])

history_readings = [x.strip().split(' ') for x in history_readings]
# print(history_readings[0])

# history_readings = [['0', '3', '6', '9', '12', '15'],
#                     ['1', '3', '6', '10', '15', '21'],
#                     ['10', '13', '16', '21', '30', '45']]

for i, reading in enumerate(history_readings):

    # if i == 142:
    #     print(reading)
    diff_levels = []
    diff_zero = False
    current_list = reading
    while not diff_zero:
        diff_list = [int(y) - int(x) for x, y in zip(current_list, current_list[1:])]

        if i == 142:
            print('diff_list:', diff_list)

        if all (x == 0 for x in diff_list):
            diff_zero = True
        else:
            current_list = diff_list

        diff_levels.append(diff_list)

    # if i == 142:
    #     print('diff_levels:', diff_levels)

    inc_number = 0
    next_num = 0
    for level in diff_levels[::-1]:
        # print('level', level)
        inc_number = level[0] - inc_number
        # if i == 142:
        # print('inc_number:', inc_number)

    # print('inc_number:',inc_number)
    next_num = int(reading[0])-inc_number

    # print('next_num:', next_num)

    tot_sum = tot_sum + next_num

    # if i == 142:
    #     print(tot_sum)
    # if i == 1:
    #     break

    # print(i)

print(tot_sum)
