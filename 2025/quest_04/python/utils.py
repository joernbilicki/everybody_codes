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
