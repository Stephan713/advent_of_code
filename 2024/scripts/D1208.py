with open(r"D:\Projects\advent_of_code\2024\inputs\D1208", 'r') as f:
    grid = f.readlines()

grid = [[char for char in line.strip()] for line in grid]

freq_dict = {}

for i, row in enumerate(grid):
    for j, col in enumerate(row):
        if grid[i][j] != '.':
            if grid[i][j] in freq_dict.keys():
                # print(freq_dict[grid[i][j]])
                freq_dict[grid[i][j]].add((i, j))
            else:
                # freq_dict[grid[i][j]] = set()
                freq_dict[grid[i][j]] = {(i, j)}

            # print(freq_dict)
anti_nodes = set()

for key, values in freq_dict.items():
    for i, (x,y) in enumerate(list(values)):
        for j, (p,q) in enumerate(list(values)[i+1:]):
            x_distance = abs(x-p)
            y_distance = abs(y-q)

            # print(f"{x}:{y}->{p}:{q}")
            # x,y anti_node
            if x <= p and y <= q:
                # print(x-x_distance, y-y_distance)
                # print(p+x_distance, q+y_distance)
                i=0
                while True:
                    if (x-i*x_distance) < 0 or (x-i*x_distance) > len(grid)-1 or (y-i*y_distance) < 0 or (y-i*y_distance) > len(grid[0])-1:
                        break
                    else:
                        anti_nodes.add((x-i*x_distance, y-i*y_distance))
                        i+=1

                i=0
                while True:
                    if (p+i*x_distance) < 0 or (p+i*x_distance) > len(grid)-1 or (q+i*y_distance) < 0 or (q+i*y_distance) > len(grid[0])-1:
                        break
                    else:
                        anti_nodes.add((p+i*x_distance, q+i*y_distance))
                        i+=1

            elif x >= p and y <= q:
                i=0
                while True:
                    if (x+i*x_distance) < 0 or (x+i*x_distance) > len(grid)-1 or (y-i*y_distance) < 0 or (y-i*y_distance) > len(grid[0])-1:
                        break
                    else:
                        anti_nodes.add((x + i * x_distance, y - i * y_distance))
                        i+=1

                i=0
                while True:
                    if (p-i*x_distance) < 0 or (p-i*x_distance) > len(grid)-1 or (q+i*y_distance) < 0 or (q+i*y_distance) > len(grid[0])-1:
                        break
                    else:
                        anti_nodes.add((p - i * x_distance, q + i * y_distance))
                        i+=1
                # print(x+x_distance, y-y_distance)
                # print(p-x_distance, q+y_distance)


            elif x <= p and y >= q:
                i = 0
                while True:
                    if (x-i*x_distance) < 0 or (x-i*x_distance) > len(grid) - 1 or (y+i*y_distance) < 0 or (
                            y+i*y_distance) > len(grid[0]) - 1:
                        break
                    else:
                        anti_nodes.add((x-i*x_distance, y+i*y_distance))
                        i += 1

                i = 0
                while True:
                    if (p+i*x_distance) < 0 or (p+i*x_distance) > len(grid) - 1 or (q-i*y_distance) < 0 or (
                            q-i*y_distance) > len(grid[0]) - 1:
                        break
                    else:
                        anti_nodes.add((p+i*x_distance, q-i*y_distance))
                        i += 1
                # print(x-x_distance, y+y_distance)
                # print(p+x_distance, q-y_distance)


            elif x >= p and y >= q:
                i = 0
                while True:
                    if (x+i*x_distance) < 0 or (x+i*x_distance) > len(grid) - 1 or (y+i*y_distance) < 0 or (
                            y+i*y_distance) > len(grid[0]) - 1:
                        break
                    else:
                        anti_nodes.add((x+i*x_distance, y+i*y_distance))
                        i += 1

                i = 0
                while True:
                    if (p-i*x_distance) < 0 or (p-i*x_distance) > len(grid) - 1 or (q-i*y_distance) < 0 or (
                            q-i*y_distance) > len(grid[0]) - 1:
                        break
                    else:
                        anti_nodes.add((p-i*x_distance, q-i*y_distance))
                        i += 1

                # print(x+x_distance, y+y_distance)
                # print(p+x_distance, q-y_distance)



count = 0
for x,y in anti_nodes:
    if x < 0 or y < 0 or x > len(grid)-1 or y > len(grid[0])-1:
        continue
    else:
        # print(x,y)
        count += 1

print(len(anti_nodes))
# print(anti_nodes)
print(count)