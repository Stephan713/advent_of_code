platform = tuple(open("inputs/14_01_input.txt", 'r').read().strip().splitlines())

# platform = list(map("".join, zip(*platform)))
# platform = ["#".join(["".join(sorted(list(group), reverse=True)) for group in row.split('#')]) for row in platform]
# platform = list(map("".join, zip(*platform)))
#
# print(sum(row.count('O') * (len(platform) - i) for i, row in enumerate(platform)))

def cycle():
    global platform
    for _ in range(4):
        platform = tuple(map("".join, zip(*platform)))
        platform = tuple("#".join(["".join(sorted(tuple(group), reverse=True)) for group in row.split('#')]) for row in
                    platform)
        platform = tuple(row[::-1] for row in platform)

seen = {platform}
array = [platform]
iter = 0
while True:
    iter += 1
    cycle()
    if platform in seen:
        break
    seen.add(platform)
    array.append(platform)

first = array.index(platform)

platform = array[(1000000000 - first) % (iter - first) + first]

print(iter, first)

print(sum(row.count('O') * (len(platform) - i) for i, row in enumerate(platform)))