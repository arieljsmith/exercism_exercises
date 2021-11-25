def get_coordinate(record):
    """

    :param record: tuple - a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """

    return record[1]


def convert_coordinate(coordinate):
    """

    :param coordinate: str - a string map coordinate
    :return:  tuple - the string coordinate seperated into its individual components.
    """

    coordinate_tuple = tuple(list(coordinate))

    return coordinate_tuple


def compare_records(azara_record, rui_record):
    """

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: bool - True if coordinates match, False otherwise.
    """

    converted_azara = convert_coordinate(azara_record[1])

    if converted_azara == rui_record[1]:
        return True

    return False


def create_record(azara_record, rui_record):
    """

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return:  tuple - combined record, or "not a match" if the records are incompatible.
    """

    if compare_records(azara_record, rui_record) is True:
        info_list = list(azara_record)
        for element in rui_record:
            info_list.append(element)
        info_tuple = tuple(info_list)
        return info_tuple

    return "not a match"


def clean_up(combined_record_group):
    """

    :param combined_record_group: tuple of tuples - everything from both participants.
    :return: string of tuples separated by newlines - everything "cleaned". Excess coordinates and information removed.
    """
    tuple_list = []

    for outer_element in combined_record_group:
        temp_list = list(outer_element)
        del temp_list[1]
        tuple_list.append(tuple(temp_list))

    formatted_data = ""

    for element in tuple_list:
        formatted_data += f"""{element}\n"""

    return formatted_data
