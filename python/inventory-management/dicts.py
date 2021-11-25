def create_inventory(items):
    """

    :param items: list - list of items to create an inventory from.
    :return:  dict - the inventory dictionary.
    """
    item_dict = {}

    for element in items:
        item_dict[element] = 0

    for element in items:
        item_dict[element] += 1

    return item_dict


def add_items(inventory, items):
    """

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return:  dict - the inventory dictionary update with the new items.
    """

    for element in items:
        if element not in inventory:
            inventory[element] = 0

    for element in items:
        inventory[element] += 1

    return inventory


def decrement_items(inventory, items):
    """

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return:  dict - updated inventory dictionary with items decremented.
    """

    for element in items:
        if element in inventory and inventory[element] > 0:
            inventory[element] -= 1

    return inventory


def remove_item(inventory, item):
    """
    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return:  dict - updated inventory dictionary with item removed.
    """

    if item in inventory:
        del inventory[item]

    return inventory


def list_inventory(inventory):
    """

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    inventory_list = list(inventory.items())
    # inventory_list = [(k, v) for k, v in inventory.items()]

    counter = 0
    while counter < len(inventory_list):
        if inventory_list[counter][1] <= 0:
            del inventory_list[counter]
        counter += 1

    return inventory_list
