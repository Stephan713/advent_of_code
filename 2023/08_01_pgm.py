import regex as re
from math import lcm

input_file = open("inputs/08_01_input.txt", 'r')
tot_steps = 0

data = input_file.read()

directions, nodes = data.split('\n\n')

nodes_dict = {}

for i, node in enumerate(nodes.split('\n')):
    nodes_dict[node.split(' = ')[0]] = node.split(' = ')[1].strip('(').strip(')').split(', ')
    # print(node.split(' = ')[0])
    # print(node.split(' = ')[1].strip('(').strip(')').split(', '))
    # if i==2:
    #     break

# print(nodes_dict)

start_node = 'AAA'
end_node = 'ZZZ'
# steps = 1
current_node = start_node

# nodes_dict={
#     'AAA' : ['BBB','BBB'],
#     'BBB' : ['AAA','ZZZ'],
#     'ZZZ' : ['ZZZ','ZZZ']
# }
# directions='LLR'
# start_node = 'AAA'
# current_node = start_node



def get_steps(current_node):
    steps = 1
    destination = False
    while not destination:

        for i, direction in enumerate(directions):
            # print(current_node)
            # print(direction)
            if direction == 'L':
                next_node = nodes_dict[current_node][0]
            elif direction == 'R':
                next_node = nodes_dict[current_node][1]

            if next_node[2] == 'Z':
                destination = True
                break
            else:
                steps = steps + 1
                current_node = next_node

    return steps

        # print(next_node)
    # print(steps)

        # if i == 3:
        #     destination = True
        #     break

# print(steps)

########################################################

# nodes_dict={
#     '11A' : ['11B','XXX'],
#     '11B' : ['XXX','11Z'],
#     '11Z' : ['11B','XXX'],
#     '22A' : ['22B','XXX'],
#     '22B' : ['22C','22C'],
#     '22C' : ['22Z','22Z'],
#     '22Z' : ['22B','22B'],
#     'XXX' : ['XXX','XXX']
# }
# directions='LR'
# start_node = 'AAA'
# current_node = start_node

starting_nodes = [key for key in nodes_dict.keys() if key[2]=='A']
# destination = False
current_nodes = starting_nodes
steps = 1

steps_list = []
for node in starting_nodes:
    print(node)
    steps_list.append(get_steps(node))

print(steps_list)

print(lcm(14893, 19951, 22199, 16579, 17141, 12083))