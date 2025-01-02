with open(r"D:\Projects\advent_of_code\2024\inputs\D1209", 'r') as f:
    disk_map = f.read()

blocks = []
file_meta = {}
free_space_meta = {}
for i, char in enumerate(disk_map):
    if i%2 == 0:
        file_meta[int(i/2)] = (len(blocks), int(char))
        blocks += [int(i/2)] * int(char)
    else:
        free_space_meta[len(blocks)] = int(char)
        blocks += [None]*int(char)

# print(len(blocks))
# print(file_meta)
sorted_file_list = list(file_meta.keys())
sorted_file_list.sort(reverse=True)
print(len(sorted_file_list))

for file in sorted_file_list:
    # print('****************')
    # print(file)
    file_loc, length = file_meta[file]
    # print(file_loc, length)
    free_space_locations = list(free_space_meta.keys())
    free_space_locations.sort()
    for free_space_loc in free_space_locations:
        # print(free_space_meta)
        if free_space_meta[free_space_loc] >= length and free_space_loc < file_loc:
            free_space_length = free_space_meta[free_space_loc]
            # print(free_space_loc, free_space_length)
            blocks = (blocks[:free_space_loc] + [file]*length + [None]*(free_space_length-length)
                      + blocks[free_space_loc+free_space_length:])
            # print(blocks)
            blocks = blocks[:file_loc] + [None]*length + blocks[file_loc+length:]
            # print(blocks)
            free_space_meta.pop(free_space_loc, None)
            free_space_meta[free_space_loc+length] = free_space_length-length
            # print(free_space_meta)
            break
    # print(file_name, length)

# print('**********')
# print(blocks)

# Problem 1
# for i, block in enumerate(blocks):
#     if block is None:
#         for j, last_block in enumerate(blocks[::-1]):
#             if last_block is not None and (len(blocks)-j-1)>i:
#                 blocks[i] = last_block
#                 blocks[len(blocks)-j-1] = None
#                 break
# print(blocks)

# Problem 2



check_sum = 0

for i, block in enumerate(blocks):
    if block is not None:
        check_sum += block*i

print(check_sum)
