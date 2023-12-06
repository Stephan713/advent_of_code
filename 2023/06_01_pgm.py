# prev_records = [[46,208], [85,1412], [75,1257], [82,1410]]
# prev_records = [[7,9], [15,40], [30,200]]
prev_records = [46857582, 208141212571410]

import math

total_ways_to_win = 1
# for time, distance in prev_records:
#     ways_to_win = 0
#     for i in range(1,time):
#         charging_time = speed = i
#         time_for_travel = time - charging_time
#         distance_travelled = time_for_travel * speed
#
#         if distance_travelled > distance:
#             ways_to_win = ways_to_win + 1
#
#         # print(i, speed, distance_travelled, distance)
#
#     # print(ways_to_win)
#     total_ways_to_win = total_ways_to_win * ways_to_win
#     # print(time, distance)
#
# print(total_ways_to_win)

###############################################
prev_records = [[46857582, 208141212571410]]

time = 46857582
distance = 208141212571410

for time, distance in prev_records:
    print(time, distance)


charging_time = speed = 41888667
time_for_travel = time - charging_time
distance_travelled = time_for_travel * speed
print(distance_travelled)

if distance_travelled > distance:
    print('True')
else:
    print('False')


print((-math.sqrt(time**2 - 4*distance) - time)/2)
print((math.sqrt(time**2 - 4*distance) - time)/2)

print(41888667-4968914)