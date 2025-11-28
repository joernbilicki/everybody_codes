def prepare_data_from_file(fname):
    """
    Creates a list of numbers reresenting the given file data.

    :param fname: Namev of the data file.
    :return: List of numbers.
    """
    gear_list = []
    with open(fname, 'r') as file:
        for line in file:
            gear_list.append(int(line))

    return gear_list


def get_gear_ratio(gear_list):
    """
    Calculates the overall gear ratio for a given gear list.

    :param gear_list: The list of gears to calculate with.
    :return gear_ratio: The calculated gear ratio.
    """
    gear_ratio = 1.0
    first_gear = gear_list[0]

    for i in range(1, len(gear_list)):
        second_gear = gear_list[i]
        gear_ratio = gear_ratio * (first_gear / second_gear)
        first_gear = second_gear

    return gear_ratio