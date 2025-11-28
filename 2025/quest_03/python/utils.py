def prepare_data_from_file(fname):
    """
    reads the given file and creates a sorted list of numbers.
    
    :param fname: Name of the file to read the numbers from.
    :return: Sorted list of numbers.
    """
    with open(fname) as file:
        input_line = file.readline()
        return sorted(list(map(int, input_line.split(","))))
