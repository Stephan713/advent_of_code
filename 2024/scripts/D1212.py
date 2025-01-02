from collections import deque

with open(r"D:\Projects\advent_of_code\2024\inputs\D1212", 'r') as f:
    garden = f.readlines()

garden = [[crop for crop in row.strip()] for row in garden]

regions = []
rows = len(garden)
cols = len(garden[0])

seen = set()

cost = 0

for row in range(rows):
    for col in range(cols):
        if (row,col) not in seen:
            curr_region = [(row,col)]
            region = deque([(row,col)])
            seen.add((row,col))
            crop = garden[row][col]
            area = 0
            perimeter = 0
            # print(crop)
            while region:
                # print(region)
                i,j = region.popleft()
                # print(i,j)
                # print(garden[i][j])
                area += 1
                for ni, nj in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
                    if 0 <= ni < rows and 0 <= nj < cols:
                        if (ni, nj) not in seen:
                            if garden[ni][nj] == crop:
                                seen.add((ni,nj))
                                region.append((ni,nj))
                                curr_region.append((ni,nj))
                    if ni < 0 or nj < 0 or ni == rows or nj == cols or garden[ni][nj] != crop:
                        perimeter += 1
                    # print(perimeter)

            # print(area)
            # print(perimeter)
            cost += (area * perimeter)
            regions.append(curr_region)


print(cost)

# print(len(regions))

cost = 0
for region in regions:
    crop = garden[region[0][0]][region[0][1]]
    # print('**************')
    # print(crop)
    # print(region)
    min_x, min_y, max_x, max_y = region[0][0], region[0][1], region[0][0], region[0][1]

    area = len(region)
    for x,y in region:
        min_x = x if x < min_x else min_x
        min_y = y if y < min_y else min_y
        max_x = x if x > max_x else max_x
        max_y = y if y > max_y else max_y

    # print(min_x, min_y, max_x, max_y)
    edges = 0
    for x in range(min_x-1, max_x+1):
        for y in range(min_y-1, max_y+1):
            # print(x,y)
            # a, b, c, d = garden[x][y], garden[x][y+1], garden[x+1][y], garden[x+1][y+1]
            sub_plot = [0 if x < 0 or y < 0 or x >= rows or y >= cols or (x,y) not in region else garden[x][y],
                     0 if x < 0 or y+1 < 0 or x >= rows or y+1 >= cols or (x,y+1) not in region else garden[x][y+1],
                     0 if x+1 < 0 or y < 0 or x+1 >= rows or y >= cols or (x+1,y) not in region else garden[x+1][y],
                     0 if x+1 < 0 or y+1 < 0 or x+1 >= rows or y+1 >= cols or (x+1,y+1) not in region else garden[x+1][y+1]]

            count = sub_plot.count(crop)

            if count == 1 or count == 3:
                edges += 1
            elif count == 2:
                # print(sub_plot)
                if ((sub_plot[0] == crop and sub_plot[3] == crop) or
                        (sub_plot[1] == crop and sub_plot[2] == crop)):
                    # print(sub_plot)
                    edges += 2



            # print(count, edges)

    # print(area, edges)
    # print(region)
    cost += area*edges

print(cost)

# print(garden)