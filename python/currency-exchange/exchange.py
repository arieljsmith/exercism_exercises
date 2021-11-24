# from _pytest.mark.structures import _XfailMarkDecorator


def exchange_money(budget, exchange_rate):
    """

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """

    value = budget / exchange_rate

    return value


def get_change(budget, exchanging_value):
    """

    :param budget: float - amount of money you own.
    :param exchanging_value: int - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """

    leftover_money = budget - exchanging_value

    return leftover_money


def get_value_of_bills(denomination, number_of_bills):
    """

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.
    """

    total_value = denomination * number_of_bills

    return total_value


def get_number_of_bills(budget, denomination):
    """

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """

    total_bills = budget / denomination

    return int(total_bills)


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """

    actual_exchange_rate = exchange_rate + exchange_rate * (spread / 100)

    max_value = denomination * get_number_of_bills(exchange_money(budget, \
        actual_exchange_rate), denomination)

    return int(max_value)


def non_exchangeable_value(budget, exchange_rate, spread, denomination):
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int non-exchangeable value.
    """
    actual_exchange_rate = exchange_rate + exchange_rate * (spread / 100)

    not_exchangeable = exchange_money(budget, actual_exchange_rate) - \
        exchangeable_value(budget, exchange_rate, spread, denomination)
    # 106.041666666667
    # 80
    return int(not_exchangeable)

# cant_be_exchanged = exchange_money(budget, exchange_rate) - exchangeable_value(budget, exchange_rate, spread, denomination)

# cant_be_exchanged = budget (int(budget / denomination))

# say you have a budget of $28.20. You want to get as much as possible
# in $5 bills. You could get $25 out of this, or 5 $5 bills. The
# unexchangeable portion would be $3.20. How do you get this?
# budget - (int(budget/denomination))
