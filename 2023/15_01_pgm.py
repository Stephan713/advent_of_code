import re
from collections import deque
i_seq = open("inputs/15_01_input.txt", 'r').read().strip().splitlines()


i_seq = [seq.replace('\n','').split(',') for seq in i_seq]
i_seq = i_seq[0]

i_seq = [re.split(r'[=-]', seq) for seq in i_seq]

# print(i_seq)

boxes = [[] for _ in range(256)]

# i_seq = ['pc']
hash_value = 0
for step in i_seq:
    current_hash_value = 0
    for letter in step[0]:
        current_hash_value = ((current_hash_value + ord(letter)) * 17) % 256

    if current_hash_value ==2:
        print(step)
    # print(current_hash_value)

    if len(boxes[current_hash_value]) == 0 and step[1] != '':
        boxes[current_hash_value].append(step)
    else:
        match = False
        for lens in boxes[current_hash_value]:
            if step[1] == '' and lens[0] == step[0]:
                boxes[current_hash_value].remove(lens)
                match = True
                break
            elif step[1] == '':
                match = True
                continue
            elif lens[0] == step[0]:
                lens[1] = step[1]
                match = True
                break
            # else:
            #     boxes[current_hash_value].append(step)
            #     break
        if not match and step[1] != '':
            boxes[current_hash_value].append(step)

    if current_hash_value == 2:
        print('boxx: ',boxes[2])

# print(boxes[2])
power = 0
for i, box in enumerate(boxes):
    for j, lens in enumerate(box):
        power = power + ((i+1) * (j+1) * int(lens[1]))

print(power)

