input_file = open(r"D:\Projects\advent_of_code\2024\inputs\D1201", 'r')

group1 = []
group2 = []

for i,line in enumerate(input_file.readlines()):
    group1.append(int(line.split()[0]))
    group2.append(int(line.split()[1]))

group1.sort()
group2.sort()

sim_score = 0

for i in group1:
    if i in group2:
        sim_score += i * group2.count(i)

print(sim_score)
print(group1)
print(group2)
