import regex as re

input_file = open("02_01_input.txt", 'r')
id_sum = 0

max_limits = {
    'red' : 12,
    'green' : 13,
    'blue' : 14
}

for i,line in enumerate(input_file.readlines()):
    game_id, game_outcomes = line.split(':')[0], line.split(':')[1]
    cube_sets = game_outcomes.split(';')
    # print(game_id)
    # print(cube_sets)
    include = True
    for cube_set in cube_sets:
        # print(cube_set)
        for cube in cube_set.split(','):
            count, color = cube.strip().split(' ')[0], cube.strip().split(' ')[1]
            # print(count)
            # print(color)

            if int(count) > max_limits[color]:
                include = False
                break

        if not include:
            break

    if include:
        id_sum = id_sum + int(game_id.split(' ')[1])
        # print(int(game_id.split(' ')[1]))

    # if i == 10:
    #     break

print(id_sum)


input_file = open("02_01_input.txt", 'r')
power_sum = 0

for i,line in enumerate(input_file.readlines()):
    game_id, game_outcomes = line.split(':')[0], line.split(':')[1]
    cube_counts = game_outcomes.replace(';', ',')
    # print(cube_counts)
    cube_counts = cube_counts.split(',')
    cube_counts = [cube_set.strip() for cube_set in cube_counts]
    print(cube_counts)

    min_counts = {
        'red':0,
        'blue':0,
        'green':0
    }

    for cube_count in cube_counts:
        count, color = cube_count.split(' ')[0], cube_count.split(' ')[1]

        if int(count) > min_counts[color]:
            min_counts[color] = int(count)

    print(min_counts)
    prod = 1
    for keys, value in min_counts.items():
        if value != 'inf':
            prod = prod * value

    print(prod)
    power_sum = power_sum + prod
    # print(power_sum)

    # if i == 2:
    #     break

print(power_sum)