import regex as re
manifest = open("inputs/19_01_input.txt", 'r').read().strip()

workflows, parts = manifest.split('\n\n')

workflows = workflows.split('\n')
parts = parts.split('\n')

formatted_workflows = {}
for workflow in workflows:
    rules = []
    for rule in workflow.split('{')[1].replace('}','').split(','):
        rules.append(rule.split(':'))
    formatted_workflows[workflow.split('{')[0]] = rules

# for key, values in formatted_workflows.items():
#     print(key, values)
# print('\n'.join(formatted_workflows))


formatted_parts = []
pattern = r'([0-9]+)'
for part in parts:
    formatted_parts.append(re.findall(pattern, part))
    # print(re.findall(pattern, part))

# print(formatted_parts)

start_workflow = 'in'
total = 0

for part in formatted_parts:
    x , m, a, s = part
    # print(x, m, a, s)

    next_workflow = 'in'
    while next_workflow not in ['A','R']:
        workflow_rules = formatted_workflows[next_workflow]
        # print(workflow_rules)

        for rule in workflow_rules:
            if len(rule) > 1:
                category = rule[0][0]
                limit = int(re.findall(pattern, rule[0])[0])
                operator = rule[0][1]
                rule_workflow = rule[1]
                # print(category, operator, limit, rule_workflow)
            elif len(rule) == 1:
                category = ''
                limit = ''
                operator = ''
                rule_workflow = rule[0]
                # print(category, operator, limit, rule_workflow)

            # print(category, operator, limit, rule_workflow)
            if operator == '<' and category == 'x':
                if int(x) < limit:
                    next_workflow = rule_workflow
                    break
            elif operator == '>' and category == 'x':
                if int(x) > limit:
                    next_workflow = rule_workflow
                    break
            elif operator == '<' and category == 'm':
                if int(m) < limit:
                    next_workflow = rule_workflow
                    break
            elif operator == '>' and category == 'm':
                if int(m) > limit:
                    next_workflow = rule_workflow
                    break
            elif operator == '<' and category == 'a':
                if int(a) < limit:
                    next_workflow = rule_workflow
                    break
            elif operator == '>' and category == 'a':
                if int(a) > limit:
                    next_workflow = rule_workflow
                    break
            elif operator == '<' and category == 's':
                if int(s) < limit:
                    next_workflow = rule_workflow
                    break
            elif operator == '>' and category == 's':
                # print('here')
                if int(s) > limit:
                    # print('here 1')
                    next_workflow = rule_workflow
                    break
            elif operator == '' and category == '':
                next_workflow = rule_workflow
                break

        # print(next_workflow)
        # print(workflow_rules)
        # next_workflow = 'A'

    if next_workflow == 'A':
        total = total + int(x) + int(m) + int(a) + int(s)

print(total)