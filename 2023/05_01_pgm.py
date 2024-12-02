import regex as re

input_file = open("inputs/05_01_input.txt", 'r')

sd_maps = input_file.readlines()

# print(sd_maps)

number_pattern = r'([0-9]+)'
seeds = re.findall(number_pattern, sd_maps[0].split(':')[1])
# print(seeds)

seed_to_soil = soil_to_fertilizer = fertilizer_to_water = water_to_light = light_to_temperature \
    = temperature_to_humidity = humidity_to_location = {}

for i, line in enumerate(sd_maps):
    if re.search('seed-to-soil', line):
        seed_to_soil_index = i
    elif re.search('soil-to-fertilizer', line):
        soil_to_fertilizer_index = i
    elif re.search('fertilizer-to-water', line):
        fertilizer_to_water_index = i
    elif re.search('water-to-light', line):
        water_to_light_index = i
    elif re.search('light-to-temperature', line):
        light_to_temperature_index = i
    elif re.search('temperature-to-humidity', line):
        temperature_to_humidity_index = i
    elif re.search('humidity-to-location', line):
        humidity_to_location_index = i

# print('seed_to_soil')
# print(sd_maps[seed_to_soil_index+1:soil_to_fertilizer_index-1])
#
# print('soil_to_fertilizer')
# print(sd_maps[soil_to_fertilizer_index+1:fertilizer_to_water_index-1])
#
# print('fertilizer_to_water')
# print(sd_maps[fertilizer_to_water_index+1:water_to_light_index-1])
#
# print('water_to_light')
# print(sd_maps[water_to_light_index+1:light_to_temperature_index-1])
#
# print('light_to_temperature')
# print(sd_maps[light_to_temperature_index+1:temperature_to_humidity_index-1])
#
# print('temperature_to_humidity')
# print(sd_maps[temperature_to_humidity_index+1:humidity_to_location_index-1])
#
# print('humidity_to_location')
# print(sd_maps[humidity_to_location_index+1:len(sd_maps)])

def get_source_dest_mapping(data, start_index, end_index, source):
    mapping = {}
    destination = None
    for maps in data[start_index:end_index]:
        sd_list = re.findall(number_pattern, maps)

        if int(sd_list[1]) <= int(source) < int(sd_list[1]) + int(sd_list[2]):
            destination = int(sd_list[0]) + (int(source) - int(sd_list[1]))
    # print(source , ":", destination)
    # print('source:', source)
    # print('destination:', destination)
    return destination

# seed_to_soil = get_source_dest_mapping(sd_maps, seed_to_soil_index+1, soil_to_fertilizer_index-1)
# soil_to_fertilizer = get_source_dest_mapping(sd_maps, soil_to_fertilizer_index+1, fertilizer_to_water_index-1)
# fertilizer_to_water = get_source_dest_mapping(sd_maps, fertilizer_to_water_index+1, water_to_light_index-1)
# water_to_light = get_source_dest_mapping(sd_maps, water_to_light_index+1, light_to_temperature_index-1)
# light_to_temperature = get_source_dest_mapping(sd_maps, light_to_temperature_index+1, temperature_to_humidity_index-1)
# temperature_to_humidity = get_source_dest_mapping(sd_maps, temperature_to_humidity_index+1, humidity_to_location_index-1)
# humidity_to_location = get_source_dest_mapping(sd_maps, humidity_to_location_index+1, len(sd_maps))

# print(seed_to_soil)
# print(soil_to_fertilizer)
# print(fertilizer_to_water)
# print(water_to_light)
# print(light_to_temperature)
# print(temperature_to_humidity)
# print(humidity_to_location)

def get_location(seed):
    soil = get_source_dest_mapping(sd_maps, seed_to_soil_index + 1, soil_to_fertilizer_index - 1, seed) or seed
    fertilizer = get_source_dest_mapping(sd_maps, soil_to_fertilizer_index + 1, fertilizer_to_water_index - 1, soil) or soil
    water = get_source_dest_mapping(sd_maps, fertilizer_to_water_index + 1, water_to_light_index - 1, fertilizer) or fertilizer
    light = get_source_dest_mapping(sd_maps, water_to_light_index + 1, light_to_temperature_index - 1, water) or water
    temperature = get_source_dest_mapping(sd_maps, light_to_temperature_index + 1, temperature_to_humidity_index - 1, light) or light
    humidity = get_source_dest_mapping(sd_maps, temperature_to_humidity_index + 1, humidity_to_location_index - 1, temperature) or temperature
    location = get_source_dest_mapping(sd_maps, humidity_to_location_index + 1, len(sd_maps), humidity) or humidity
    # print(seed, ":", soil, ":", fertilizer, ":", water, ":", light, ":", temperature, ":", humidity, ":", location)
    return int(location)

seed_location = {}

for seed in seeds:
    soil = get_source_dest_mapping(sd_maps, seed_to_soil_index + 1, soil_to_fertilizer_index - 1, seed) or seed
    fertilizer = get_source_dest_mapping (sd_maps, soil_to_fertilizer_index+1, fertilizer_to_water_index-1, soil) or soil
    water = get_source_dest_mapping(sd_maps, fertilizer_to_water_index+1, water_to_light_index-1, fertilizer) or fertilizer
    light = get_source_dest_mapping(sd_maps, water_to_light_index+1, light_to_temperature_index-1, water) or water
    temperature = get_source_dest_mapping(sd_maps, light_to_temperature_index+1, temperature_to_humidity_index-1, light) or light
    humidity = get_source_dest_mapping(sd_maps, temperature_to_humidity_index+1, humidity_to_location_index-1, temperature) or temperature
    location = get_source_dest_mapping(sd_maps, humidity_to_location_index+1, len(sd_maps), humidity) or humidity

    seed_location[seed] = location
    # print(seed, ":", soil, ":", fertilizer, ":",water, ":", light, ":", temperature, ":", humidity, ":", location)

# print(min(list(seed_location.values())))


###################################################################
seeds = re.findall(number_pattern, sd_maps[0].split(':')[1])
seed_ranges = [[int(seeds[i]), int(seeds[i]) + int(seeds[i+1]) -1] for i in range(0,len(seeds), 2)]

print(seed_ranges)
def get_valid_ranges(pre_ranges, cur_maps):
    valid_ranges = []

    for valid_start_range, valid_end_range in pre_ranges:
        # print('valid_start_range:', valid_start_range)
        # print('valid_end_range:', valid_end_range)
        for dest, src, sz in cur_maps:
            # print(dest, src, sz)
            dest = int(dest)
            src = int(src)
            sz = int(sz)
            # print(dest, src, sz)

            src_end = src + sz -1
            diff = dest - src
            # print('src_end:',src_end)
            # print('diff:', diff)

            # no overlap
            if valid_start_range > src_end or valid_end_range < src:
                # print('no overlap')
                continue

            # inside
            if src<=valid_start_range<=src_end and src<=valid_end_range<=src_end:
                # print('here')
                valid_ranges.append([valid_start_range+diff, valid_end_range+diff])
                break

            # left
            if src <= valid_end_range <= src_end:
                valid_ranges.append([src+diff, valid_end_range+diff])
                pre_ranges.append([valid_start_range, src - 1])
                break

            # right
            if src <= valid_start_range <= src_end:
                # print('right')
                valid_ranges.append([valid_start_range+diff, src_end+diff])
                pre_ranges.append([src_end+1, valid_end_range])
                break

            # both sides
            if valid_start_range < src and valid_end_range > src_end:
                valid_ranges.append([src+diff, src_end+diff])
                pre_ranges.append([valid_start_range, src - 1])
                pre_ranges.append([src_end + 1, valid_end_range])
                break
        else:
            # print('herhe')
            valid_ranges.append([valid_start_range,valid_end_range])

            # print(valid_ranges)


    return valid_ranges


levels = []
seed_to_soil_maps = []
for i, line in enumerate(sd_maps[seed_to_soil_index+1:soil_to_fertilizer_index-1]):
    seed_to_soil_maps.append(line.strip().split(' '))

levels.append(seed_to_soil_maps)

valid_soil_ranges = get_valid_ranges(seed_ranges, seed_to_soil_maps)

# print(seed_ranges)
# print(valid_soil_ranges)

soil_to_fertilizer_maps = []
for i, line in enumerate(sd_maps[soil_to_fertilizer_index+1:fertilizer_to_water_index-1]):
    soil_to_fertilizer_maps.append(line.strip().split(' '))

# print(soil_to_fertilizer_maps)
valid_fertilizer_ranges = get_valid_ranges(valid_soil_ranges, soil_to_fertilizer_maps)

# print(valid_fertilizer_ranges)
levels.append(soil_to_fertilizer_maps)

fertilizer_to_water_maps = []
for i, line in enumerate(sd_maps[fertilizer_to_water_index+1:water_to_light_index-1]):
    fertilizer_to_water_maps.append(line.strip().split(' '))

# print('fertilizer_to_water_maps:',fertilizer_to_water_maps)
valid_water_ranges = get_valid_ranges(valid_fertilizer_ranges, fertilizer_to_water_maps)

# print(valid_water_ranges)
levels.append(fertilizer_to_water_maps)

water_to_light_maps = []
for i, line in enumerate(sd_maps[water_to_light_index+1:light_to_temperature_index-1]):
    water_to_light_maps.append(line.strip().split(' '))

valid_light_ranges = get_valid_ranges(valid_water_ranges, water_to_light_maps)

levels.append(water_to_light_maps)

light_to_temperature_maps = []
for i, line in enumerate(sd_maps[light_to_temperature_index+1:temperature_to_humidity_index-1]):
    light_to_temperature_maps.append(line.strip().split(' '))

valid_temperature_ranges = get_valid_ranges(valid_light_ranges, light_to_temperature_maps)

levels.append(light_to_temperature_maps)

temperature_to_humidity_maps = []
for i, line in enumerate(sd_maps[temperature_to_humidity_index+1:humidity_to_location_index-1]):
    temperature_to_humidity_maps.append(line.strip().split(' '))

valid_humidity_ranges = get_valid_ranges(valid_temperature_ranges, temperature_to_humidity_maps)

levels.append(temperature_to_humidity_maps)

humidity_to_location_maps = []
for i, line in enumerate(sd_maps[humidity_to_location_index+1:len(sd_maps)]):
    humidity_to_location_maps.append(line.strip().split(' '))

valid_location_ranges = get_valid_ranges(valid_humidity_ranges, humidity_to_location_maps)

levels.append(humidity_to_location_maps)

for location_range in valid_location_ranges:
    print(location_range)

