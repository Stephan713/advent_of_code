with open(r"D:\Projects\advent_of_code\2024\inputs\D1205", 'r') as f:
    input_file = f.read()

def increasing(L):
    return all(x<y for x,y in zip(L, L[1:]))

def build_accumulated_rules(rules):
    accumulated_rules = []
    # print('@@@@@@@@@@')

    while rules:
        first_numbers =[]
        second_numbers = []
        for x, y in rules:
            first_numbers.append(x)
            second_numbers.append(y)

        # print(rules)
        # print(first_numbers)
        # print(second_numbers)

        start_numbers = [x for x in first_numbers if x not in second_numbers]

        start_numbers = set(start_numbers)

        accumulated_rules += list(start_numbers)

        # print(start_numbers)
        # print(rules)
        for x, y in [(x, y) for x, y in rules if x in start_numbers]:
            rules.remove((x, y))

        # print(rules)

    # print('@@@@@@@@@')

    # print(accumulated_rules)
    return accumulated_rules

# input_file = [line.strip() for line in input_file]
rules, updates = input_file.split('\n\n')

rules = rules.split()
updates = updates.split()

rules_list = []

for rule in rules:
    rules_list.append((int(rule.split('|')[0]), int(rule.split('|')[1])))

# updates = [update.split(',') for update in updates]
updates = [[int(num) for num in update.split(',')] for update in updates]

sum = 0
reject_sum = 0

for i, update in enumerate(updates):
    # if i ==3:
    valid_rules = []
    for x, y in rules_list:
        if x in update and y in update:
            valid_rules.append((x, y))

    if all(update.index(x) < update.index(y) for x,y in valid_rules):
        sum += update[int((len(update)-1)/2)]
    else:
        # print(update)
        sorted_rules = build_accumulated_rules(valid_rules)

        sorted_rules.extend(x for x in update if x not in sorted_rules)

        reject_sum += sorted_rules[int((len(update) - 1) / 2)]
        # print(sorted_rules)
        #
        # break
        # # print(update)
        # update.sort(key=lambda x: sorted_rules.index(x) if x in sorted_rules else float('inf'))
        #
        # reject_sum += update[int((len(update)-1)/2)]
        # if not all(update.index(x) < update.index(y) for x, y in valid_rules):
        #     print('********')
        #     print(update)
        #     print(valid_rules)
        #     print(sorted_rules)
        #     break




print(sum)
print(reject_sum)