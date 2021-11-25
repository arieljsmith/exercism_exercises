def dict_creation():
    corn_dict = {}

    for space in range(1, 65):
        corn_dict[space] = 0

    corn_dict[1] = 1

    for space in range(2, 65):
        corn_dict[space] = corn_dict[space - 1] * 2

    return corn_dict


def square(number):
    corn_dict = dict_creation()

    if (number >= 1) and (number <= 64):
        return corn_dict[number]
    else:
        raise ValueError("square must be between 1 and 64")


def total():
    corn_dict = dict_creation()
    total = 0

    for space in corn_dict:
        total += corn_dict[space]

    return total

# ============================================
