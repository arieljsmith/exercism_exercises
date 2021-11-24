import statistics


def first_last_average(hand):
    card_sum = hand[0] + hand[-1]
    card_avg = card_sum / 2
    return card_avg


def get_rounds(number):
    """

     :param number: int - current round number.
     :return: list - current round and the two that follow.
    """

    upcoming = [number, number + 1, number + 2]

    return upcoming


def concatenate_rounds(rounds_1, rounds_2):
    """

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    # NOTE TO SELF; HOW I WANT THIS TO WORK:
    # Create Variable all_rounds that starts as an empty list.
    # If rounds_1 isn't empty, add all items in rounds_1 into all_rounds.
    # Then, if rounds_2 isn't empty, do the same.
    # If rounds_1 IS empty, skip it and go to adding rounds_2.
    # If rounds_2 IS empty, skip it.
    # return all_rounds.
    # MUST BE ADDED FIRST TO LAST, so while i < len(rounds_x), run, then
    # increment i by 1.

    all_rounds = []
    i = 0

    while i < len(rounds_1):
        all_rounds.append(rounds_1[i])
        i += 1

    i = 0

    while i < len(rounds_2):
        all_rounds.append(rounds_2[i])
        i +=1

    return all_rounds

    # SECOND COMMENTED OUT
    # all_rounds = []

    # if rounds_1 != None:
    #     for round in rounds_1:
    #         all_rounds = all_rounds.append(round)
    #     if rounds_2 != None:
    #         for round in rounds_2:
    #             all_rounds = all_rounds.append(round)
    # elif rounds_2 != None:
    #     for round in rounds_2:
    #         all_rounds = all_rounds.append(round)

    # FIRST COMMENTED OUT
    # for round in rounds_2:
    #     all_rounds = all_rounds.append(round)


def list_contains_round(rounds, number):
    """

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return:  bool - was the round played?
    """

    verdict = False
    counter = len(rounds)

    while verdict is False and counter > 0:
        if rounds[counter - 1] == number:
            verdict = True
        else:
            counter -= 1

    return verdict


def card_average(hand):
    """

    :param hand: list - cards in hand.
    :return:  float - average value of the cards in the hand.
    """

    card_count = len(hand)
    card_sum = 0

    for card in hand:
        card_sum += card

    hand_average = card_sum / card_count

    return hand_average


def approx_average_is_average(hand):
    """

    :param hand: list - cards in hand.
    :return: bool - is approximate average the same as true average?
    """

    if first_last_average(hand) == card_average(hand) or \
        statistics.median(hand) == card_average(hand):
        verdict = True
    else:
        verdict = False

    return verdict


def average_even_is_average_odd(hand):
    """

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    even_list_length = len(hand)
    odd_list_length = len(hand) - 1
    even_sum = 0
    odd_sum = 0
    even_counter = 0
    odd_counter = 0

    # "even" average
    while even_list_length > 0:
        even_sum += hand[even_list_length - 1]
        even_list_length -= 2
        even_counter += 1

    even_average = even_sum / even_counter

    while odd_list_length > 0:
        odd_sum += hand[odd_list_length - 1]
        odd_list_length -= 2
        odd_counter += 1

    odd_average = odd_sum / odd_counter

    return bool(odd_average == even_average)


def maybe_double_last(hand):
    """

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    int_hand = []
    card = 0

    while card < len(hand):
        int_hand.append(int(hand[card]))
        card += 1

# ---===---

    # for card in hand:
    #     int_hand.append(int(hand[card]))
    new_hand = []

    if int_hand[-1] == 11:
        new_hand = int_hand[:-1]
        new_hand.append(22)
    else:
        new_hand = int_hand.copy()

    return new_hand


# # PERSONAL TESTS =========================
# input_1 = input("Enter some numbers: ")
# # input_2 = input("Enter more numbers: ")

# user_list_1 = input_1.split()
# # user_list_2 = input_2.split()

# print("You first entered: ", user_list_1)
# # print("You next entered: ", user_list_2)

# maybe_doubled = maybe_double_last(user_list_1)

# print("Possibly doubled list: ", maybe_doubled)

# # combined_list = concatenate_rounds(user_list_1, user_list_2)

# # print("Your concatenated list: ", combined_list)
