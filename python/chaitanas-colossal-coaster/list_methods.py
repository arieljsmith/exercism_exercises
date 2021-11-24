def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    """
    If ticket_type == 1, append person_name to and return express_queue. else,
    append person_name to and return normal_queue.

    :param express_queue: list - names in the Fast-track queue.
    :param normal_queue:  list - names in the normal queue.
    :param ticket_type:  int - type of ticket. 1 = express, 0 = normal.
    :param person_name: str - name of person to add to a queue.
    :return: list - the (updated) queue the name was added to.
    """

    if ticket_type == 1:
        express_queue.append(person_name)
        returned_queue = express_queue.copy()
    else:
        normal_queue.append(person_name)
        returned_queue = normal_queue.copy()

    return returned_queue


def find_my_friend(queue, friend_name):
    """
    Initializes variable position and iterates through queue;
    if friend_name matches at any point during iteration, the
    position variable is set to that index, which is then returned.

    :param queue: list - names in the queue.
    :param friend_name: str - name of friend to find.
    :return: int - index at which the friends name was found.
    """

    position = None
    counter = 0

    for name in queue:
        if friend_name == name:
            position = counter
        counter += 1

    return position

# PERSONAL TEST =======

# queue_input = input("Enter some names: ")
# list_queue_input = queue_input.split()

# friend_name_input = input("Enter name to be found in previous list: ")

# print("Your friend is at position ", find_my_friend(list_queue_input, friend_name_input), ".")

# =======================


def add_me_with_my_friends(queue, index, person_name):
    """
    Adds person_name to queue at index.

    :param queue: list - names in the queue.
    :param index: int - the index at which to add the new name.
    :param person_name: str - the name to add.
    :return: list - queue updated with new name.
    """

    queue.insert(index, person_name)

    return queue


def remove_the_mean_person(queue, person_name):
    """
    Removes person_name from queue.

    :param queue: list - names in the queue.
    :param person_name: str - name of mean person.
    :return:  list - queue update with the mean persons name removed.
    """

    queue.remove(person_name)

    return queue


def how_many_namefellows(queue, person_name):
    """
    Returns number of occurrences of person_name in queue.

    :param queue: list - names in the queue.
    :param person_name: str - name you wish to count or track.
    :return:  int - the number of times the name appears in the queue.
    """

    counter = 0

    for name in queue:
        if person_name == name:
            counter += 1

    return counter


def remove_the_last_person(queue):
    """
    Removes last person in queue and returns their name.

    :param queue: list - names in the queue.
    :return: str - name that has been removed from the end of the queue.
    """
    owed_voucher = queue[-1]

    queue.remove(queue[-1])

    return owed_voucher


def sorted_names(queue):
    """

    :param queue: list - names in the queue.
    :return: list - copy of the queue in alphabetical order.
    """

    queue.sort()

    return queue
