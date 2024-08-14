def get_rounds(round_number):
    round_output = [round_number, round_number + 1, round_number + 2]
    return round_output


# print(get_rounds(27))


def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 + rounds_2


print(concatenate_rounds([27, 28, 29], [35, 36]))
