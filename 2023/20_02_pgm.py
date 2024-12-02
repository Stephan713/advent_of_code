import math
from collections import deque
from math import lcm
module_configuration = open("inputs/20_01_input.txt", 'r').read().strip().splitlines()

# module - name, type, memory, target

modules = {}

for config in module_configuration:
    source, target = config.split(" -> ")
    if source == 'broadcaster':
        module = 'broadcaster'
        modules[source] = {
            'type': 'broadcaster',
            'memory': [],
            'target': target.split(", ")
        }
    else:
        module = source[1:]
        modules[source[1:]] = {
            'type' : source[:1],
            'memory' : [],
            'target' : target.split(", ")
        }

    if modules[module]['type'] == '%':
        modules[module]['memory'] = 'off'
    elif modules[module]['type'] == '&':
        modules[module]['memory'] = {}

# print(modules)
for module, props  in modules.items():
    for target in props['target']:
        if target != 'rx' and modules[target]['type'] == '&':
            modules[target]['memory'][module] = 'lo'

rx_input = 'bb'
seen = { name: 0 for name, module in modules.items() if rx_input in module['target']}
cycle_lengths={}
presses = 0
while True:
    presses+=1

    # origin, target, pulse
    q = deque([(modules['broadcaster']['type'], x, 'lo') for x in modules['broadcaster']['target']])

    while q:
        origin, target, pulse = q.popleft()
        # print(origin, target, pulse)

        if target not in modules.keys():
            continue

        module = modules[target]

        if target == rx_input and pulse == 'hi':
            seen[origin] += 1
            if origin not in cycle_lengths:
                cycle_lengths[origin] = presses
            else:
                assert presses == seen[origin] * cycle_lengths[origin]

            if all(seen.values()):
                x = 1
                for cycle_length in cycle_lengths.values():
                    x = lcm(x, cycle_length)

                print(x)
                exit(0)

        # print(module)
        if module['type'] == '%':
            if pulse == 'lo':
                module['memory'] = 'on' if module['memory'] == 'off' else 'off'
                # print(modules[target])
                out_pulse = 'hi' if module['memory'] == 'on' else 'lo'

                for x in module['target']:
                    # print(target, x, out_pulse)
                    q.append((target, x, out_pulse))

        else:
            module['memory'][origin] = pulse
            # print(modules[target])
            out_pulse = 'lo' if all(x == 'hi' for x in module['memory'].values()) else 'hi'

            for x in module['target']:
                # print(target, x, out_pulse)
                q.append((target, x, out_pulse))

print(cycle_lengths)