from collections import deque
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

# print(modules)

lo = hi = 0

# print(modules.keys())
#
# exit(0)
rx_input = 'bb'
cycle_lengths = { name: None for name, module in modules.items() if rx_input in module['target']}

for _ in range(1000):
    lo+=1

    # origin, target, pulse
    q = deque([(modules['broadcaster']['type'], x, 'lo') for x in modules['broadcaster']['target']])

    while q:
        origin, target, pulse = q.popleft()
        # print(origin, target, pulse)
        if pulse == 'lo':
            lo+=1
        else:
            hi+=1

        if target not in modules.keys():
            continue

        module = modules[target]

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

print(lo*hi)
# print(hi)

