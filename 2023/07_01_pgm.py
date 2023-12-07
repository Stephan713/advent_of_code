import regex as re

input_file = open("inputs/07_01_input.txt", 'r')

all_hands = input_file.readlines()

all_hands = [x.strip() for x in all_hands]

cards = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
card_ranks = ['A','B','C','D','E','F','G','H','I','J','Q','K','L']
card_ranks={}

def get_type(hand):
    rank = 0
    # print(hand)
    cards_in_hand = list(hand.replace('J',''))
    # print(cards_in_hand)
    unique_cards = set(cards_in_hand)
    num_J = len([m.start() for m in re.finditer('J', hand)])
    # print(hand)
    # print(num_J)

    if len(unique_cards) == 1 or len(unique_cards) == 0:
        #five of a kind
        rank = 7
    elif len(unique_cards) == 2:
        # possible four of a kind or full house
        prev_rank = 0
        for card in unique_cards:
            if len([m.start() for m in re.finditer(card, hand)]) + num_J == 4:
                # four of a kind
                rank = 6
            if len([m.start() for m in re.finditer(card, hand)]) + num_J == 3:
                # full house
                rank = 5

            if rank > prev_rank:
                prev_rank = rank

        rank = prev_rank

    elif len(unique_cards) == 3:
        # possible three of a kind or two pair
        prev_rank = 0
        for card in unique_cards:
            if len([m.start() for m in re.finditer(card, hand)]) + num_J== 3:
                # three of a kind
                rank = 4
            if len([m.start() for m in re.finditer(card, hand)]) + num_J== 2:
                # two pair
                rank = 3

            if rank > prev_rank:
                prev_rank = rank

        rank = prev_rank

    elif len(unique_cards) == 4:
        rank = 2
    elif len(unique_cards) == 5:
        rank = 1

    # print(rank)
    return rank

total_hands_types = {
    'five_of_a_kind': [],
    'four_of_a_kind': [],
    'full_house': [],
    'three_of_a_kind': [],
    'two_pair': [],
    'one_pair': [],
    'high_card': []
}

for i, hand in enumerate(all_hands):
    hand_type = get_type(hand.split(' ')[0])
    if hand_type == 7:
        total_hands_types['five_of_a_kind'].append(hand)
    elif hand_type == 6:
        # print(hand)
        total_hands_types['four_of_a_kind'].append(hand)
    elif hand_type == 5:
        total_hands_types['full_house'].append(hand)
    elif hand_type == 4:
        total_hands_types['three_of_a_kind'].append(hand)
    elif hand_type == 3:
        total_hands_types['two_pair'].append(hand)
    elif hand_type == 2:
        total_hands_types['one_pair'].append(hand)
    elif hand_type == 1:
        total_hands_types['high_card'].append(hand)

    # if i == 32:
    #     break

# print('********')
# print(total_hands_types)

# cards =       ['A','K','Q','T','9','8','7','6','5','4','3','2','J']
#               ['M','L','K','J','I','H','G','F','E','D','C','B','A']
def rep_func(hand_prize):
    hand = hand_prize.split(' ')[0]
    return hand.replace('A','M').replace('K','L').replace('Q','K').replace('9','I').replace('8','H').\
        replace('7','G').replace('6','F').replace('5','E').replace('4','D').replace('3','C').replace('2','B').\
        replace('J','A').replace('T','J')

sorted_list = []
for key, values in total_hands_types.items():
    print(len(values))
    sorted_values = values
    sorted_values.sort(reverse=True, key=rep_func)
    print('######')
    print(sorted_values)
    sorted_list = sorted_list + sorted_values
    # sorted_list.append(sorted_values)
    # print(sorted_values)

print('********')
# print(sorted_list)

total_prize = 0
for i, hand_prize in enumerate(sorted_list):

    total_prize = total_prize + (int(hand_prize.split(' ')[1]) * (1000 - i))

print(total_prize)