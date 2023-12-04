import regex as re

input_file = open("04_01_input.txt", 'r')
tot_winnings = 0
winnings = 0

for i,line in enumerate(input_file.readlines()):
    card_no = line.split(':')[0]
    winning_num = line.split(':')[1].split('|')[0].strip().split(' ')
    my_num = line.split(':')[1].split('|')[1].strip().split(' ')

    # print(card_no)
    # print(winning_num)
    # print(my_num)

    winning_num = [num for num in winning_num if len(num) > 0]
    my_num = [num for num in my_num if len(num) > 0]

    # print(winning_num)
    # print(my_num)

    winnings = 0

    for num in my_num:
        if num in winning_num and winnings == 0:
            winnings = 1
            # print(num)
            # print('winnings1: ', winnings)
        elif num in winning_num:
            winnings = winnings * 2
            # print(num)
            # print('winnings1: ', winnings)

    # print('winnings: ', winnings)
    tot_winnings = tot_winnings + winnings
    # if i == 2:
    #     break

# print('tot_winnings: ', tot_winnings)


#################################################################

input_file = open("04_01_input.txt", 'r')
initial_scratch_cards = input_file.readlines()
# print(initial_scratch_cards)

def get_win_numbers(winning_numbers, my_numbers):
    win_numbers = 0
    for num in my_numbers:
        if num in winning_numbers:
            win_numbers = win_numbers + 1

    return win_numbers

card_counts = {}
for i,scratch_card in enumerate(initial_scratch_cards):
    card_no = scratch_card.split(':')[0]
    card_counts[card_no] = 1

for i,scratch_card in enumerate(initial_scratch_cards):

    card_no = scratch_card.split(':')[0]
    winning_num = scratch_card.split(':')[1].split('|')[0].strip().split(' ')
    my_num = scratch_card.split(':')[1].split('|')[1].strip().split(' ')

    winning_num = [num for num in winning_num if len(num) > 0]
    my_num = [num for num in my_num if len(num) > 0]

    cards_won = get_win_numbers(winning_num, my_num)
    card_num = card_no.split(' ')[-1].strip()

    print('processing card_no: ',card_no)
    print('cards won: ', cards_won)

    num_scrathc_cards = card_counts[card_no]
    for j, keys in enumerate(card_counts.keys()):
        if j >= int(card_num) and j < (int(card_num) + int(cards_won)):
            print(keys)
            card_counts[keys] = card_counts[keys] + num_scrathc_cards

    # if i == 2:
    #     break

print(card_counts)
tot_num_cards = 0
for keys, values in card_counts.items():
    tot_num_cards = tot_num_cards + values

print(tot_num_cards)
