from collections import defaultdict

with open(r"D:\Projects\advent_of_code\2024\inputs\D1211", 'r') as f:
    stones = f.read()

stones = stones.split(' ')
# print(stones)

freq = defaultdict(int)
for stone in stones:
    freq[stone] += 1

blinks = 75


for i in range(blinks):
    split_stones = defaultdict(int)
    for stone in freq:
        if stone == '0':
            split_stones['1'] += freq[stone]
        elif len(stone) % 2 == 0:
            l = stone[:int(len(stone)/2)].lstrip('0') if stone[:int(len(stone)/2)].lstrip('0') else '0'
            r = stone[int(len(stone)/2):].lstrip('0') if stone[int(len(stone)/2):].lstrip('0') else '0'
            split_stones[l] += freq[stone]
            split_stones[r] += freq[stone]
        else:
            split_stones[str(int(stone)*2024)] += freq[stone]

    freq = split_stones

sum = 0
for stone, count in freq.items():
    sum += count

print(sum)
print(len(freq))
exit()
#########################################3333
for i in range(blinks):
    split_stones = []
    for stone in stones:
        if stone == '0':
            split_stones.append('1')
        elif len(stone) % 2 == 0:
            split_stones.append(stone[:int(len(stone)/2)].lstrip('0') if stone[:int(len(stone)/2)].lstrip('0') else '0')
            split_stones.append(stone[int(len(stone)/2):].lstrip('0') if stone[int(len(stone)/2):].lstrip('0') else '0')
        else:
            split_stones.append(str(int(stone)*2024))
            # print(stone)
            # print(split_stones)

    # print(split_stones)
    stones = split_stones

print(len(stones))

