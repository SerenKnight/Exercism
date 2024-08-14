def get_rounds(round_number):
    round_output = [round_number, round_number + 1, round_number + 2]
    return round_output


# print(get_rounds(27))


def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 + rounds_2


# print(concatenate_rounds([27, 28, 29], [35, 36]))


def list_contains_round(rounds, round_number):
    if round_number in rounds:
        return True
    else:
        return False


# print(list_contains_round([27, 28, 29, 35, 36], 29))
# print(list_contains_round([27, 28, 29, 35, 36], 30))


def card_average(hand):
    average = sum(hand) / len(hand)
    return average


print(card_average([5, 6, 7]))
