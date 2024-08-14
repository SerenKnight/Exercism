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


# print(card_average([5, 6, 7]))


def approx_average_is_average(hand):
    actual_average = sum(hand) / len(hand)
    first_strategy = (hand[0] + hand[-1]) / 2
    second_strategy = hand[int(len(hand) / 2)]

    if first_strategy == actual_average or second_strategy == actual_average:
        return True
    else:
        return False


# print(approx_average_is_average([1, 2, 3]))
# print(approx_average_is_average([2, 3, 4, 8, 8]))
# print(approx_average_is_average([1, 2, 3, 5, 9]))


def average_even_is_average_odd(hand):
    evens = hand[1::2]
    odds = hand[::2]
    average_evens = sum(evens) / len(evens)
    average_odds = sum(odds) / len(odds)
    if average_evens == average_odds:
        return True
    else:
        return False


print(average_even_is_average_odd([1, 2, 3]))
print(average_even_is_average_odd([1, 2, 3, 4]))
