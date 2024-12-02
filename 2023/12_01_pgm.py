input_file = open("inputs/12_01_input.txt", 'r')

records = input_file.readlines()

records = [[x.strip().split(' ')[0],x.strip().split(' ')[1]] for x in records]

print(records)