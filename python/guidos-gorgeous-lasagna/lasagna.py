# TO DO: define the 'EXPECTED_BAKE_TIME' constant
EXPECTED_BAKE_TIME = 40
# TO DO: consider defining the 'PREPARATION_TIME' constant
#       equal to the time it takes to prepare a single layer
PREPARATION_TIME = 2


# TO DO: define the 'bake_time_remaining()' function
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int baking time already elapsed.
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


# TO DO: define the 'preparation_time_in_minutes()' function
#       and consider using 'PREPARATION_TIME' here
def preparation_time_in_minutes(num_layers):
    """Calculate how long preparation will take.

    :param num_layers: int number of layers user wants in lasagna.
    :return: int time needed for preparation derived from 'PREPARATION_TIME'.

    Function that takes the number of layers the user wants to have in their
    lasagna as an argument and returns how many minutes will be needed for
    preparation based on the `PREPARATION_TIME`.
    """

    return PREPARATION_TIME * num_layers


# TO DO: define the 'elapsed_time_in_minutes()' function
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate how much time has passed total.

    :param number_of_layers: int number of layers added to lasagna.
    :param elapsed_bake_time: int minutes lasagna has been baking in oven.
    :return:

    Function that takes the number of layers added to the lasagna and the
    amount of time in minutes the lasagna has been in the oven and returns
    how many total minutes have been spent cooking.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
