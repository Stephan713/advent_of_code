patterns = open("inputs/13_01_input.txt", 'r').read().strip()

patterns = patterns.split('\n\n')

patterns = [pattern.split('\n') for pattern in patterns]

# print(patterns)



def get_sum(pattern):
# for pattern in patterns:
    # print(pattern)
    reflection_found = False
    tot_sum = 0
    for i in range(len(pattern)-1):
        if len(pattern[:i+1]) > len(pattern[:i:-1]):
            if sum(sum(0 if a==b else 1 for a,b in zip(x, y)) for x, y in zip(pattern[:i+1][len(pattern[:i+1]) - len(pattern[:i:-1]):], pattern[:i:-1])) == 1:
                tot_sum = tot_sum + (i+1)*100
                reflection_found = True
                # print(i)
                break
        elif len(pattern[:i+1]) < len(pattern[:i:-1]):
            if sum(sum(0 if a==b else 1 for a, b in zip(x,y)) for x,y in zip(pattern[:i+1], pattern[:i:-1][len(pattern[:i:-1])-len(pattern[:i+1]):])) == 1:
                tot_sum = tot_sum + (i + 1) * 100
                # print(i)
                reflection_found = True
                break


    print(pattern)
    print(tot_sum)
    if reflection_found:
        return tot_sum, reflection_found
    transpose_pattern = list(map("".join, zip(*pattern)))

    for i in range(len(transpose_pattern)-1):
        if len(transpose_pattern[:i + 1]) > len(transpose_pattern[:i:-1]):
            if sum(sum(0 if a==b else 1 for a,b in zip(x, y)) for x, y in zip(transpose_pattern[:i + 1][len(transpose_pattern[:i + 1]) - len(transpose_pattern[:i:-1]):], transpose_pattern[:i:-1])) == 1:
                tot_sum = tot_sum + (i + 1)
                reflection_found = True
                # print(i)
                break
        elif len(transpose_pattern[:i + 1]) < len(transpose_pattern[:i:-1]):
            if sum(sum(0 if a==b else 1 for a,b in zip(x, y)) for x, y in zip(transpose_pattern[:i + 1], transpose_pattern[:i:-1][len(transpose_pattern[:i:-1]) - len(transpose_pattern[:i + 1]):])) == 1:
                tot_sum = tot_sum + (i + 1)
                reflection_found = True
                # print(i)
                break
    print(pattern)
    print(tot_sum)
    return tot_sum, reflection_found

# print(tot_sum)

new_sum = 0

for i, pattern in enumerate(patterns):
    sum_1, reflection_found = get_sum(pattern)
    new_sum = new_sum + sum_1


print(new_sum)