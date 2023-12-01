import regex as re

input_file = open("01_01_input.txt", 'r')
tot_sum = 0

for i,line in enumerate(input_file.readlines()):
    fd_regex = re.compile(r"[a-z]*(\d)")
    digits = fd_regex.match(line)
    for group in digits.groups():
        first_digit = group

    ld_regex = re.compile(r"[a-z 0-9]*(\d)")
    digits = ld_regex.match(line)
    for group in digits.groups():
        last_digit = group

    tot_sum = tot_sum + (int(first_digit)*10) + (int(last_digit))

    # if i == 10:
    #     break

print(tot_sum)

def get_num(digit=str):
    digit = digit.replace('one','1').replace('two','2').replace('three','3').replace('four','4').replace('five','5')\
        .replace('six','6').replace('seven','7').replace('eight','8').replace('nine','9').replace('zero','0')
    return digit


input_file = open("01_01_input.txt", 'r')
tot_sum = 0

for i,line in enumerate(input_file.readlines()):
    fd_regex = re.compile(r".*?(one|two|three|four|five|six|seven|eight|nine|zero|\d)[a-z 0-9]*")
    digits = fd_regex.match(line)
    for group in digits.groups():
        first_digit = group

    # print(first_digit)
    first_digit = get_num(first_digit)
    # print(first_digit)

    ld_regex = re.compile(r"[a-z 0-9]*(one|two|three|four|five|six|seven|eight|nine|zero|\d)")
    digits = ld_regex.match(line)
    for group in digits.groups():
        last_digit = group

    # print(last_digit)
    last_digit = get_num(last_digit)
    # print(last_digit)

    # print(line)
    # print("******")

    tot_sum = tot_sum + (int(first_digit)*10) + (int(last_digit))

    # if i == 10:
    #     break

print(tot_sum)
