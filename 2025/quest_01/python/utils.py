NAME_KEY    = 0 # Key to the name list in the resulting map
COMMAND_KEY = 1 # Key to the command list in the resulting map

def prepare_data_from_file(fname):
    """
    This function takes the filename to create a map of two
    lists based on the data in the given file. The lists can be accessed 
    with the following keys:
    - Key == NAME_KEY: Retrieves the list of names to search in.
    - Key == COMMAND_KEY: Retrieves the list of search commands.
    
    :param fname: Name of the input file (string).
    :return: A new map as described in the summary.
    """

    # The resulting map
    input_as_map = {}

    # We expect the first "useful" row contains the comma separated list of names.
    current_key = NAME_KEY

    # Read the file line by line
    with open(fname, 'r') as file:
        for line in file:
            # If the row contains "useful" data...
            if len(line.strip()) > 0:
                # ...convert the line to a list and put it with the current key in the map.
                input_as_map[current_key] = line.strip().split(',')
                current_key += 1

    return input_as_map


def get_name(input_as_map, operations_map):
    """
    Returns from the input map the name according to the given operations in this map.
    Every operation in this map will be mapped to a function in the operations_map.

    :param input_as map: Map, that contains a name list and a operations list.
    :param operations_map: Map that contains a function to be executed for va given operation.
    :return: The name found in the name list.
    """
    name_len = len(input_as_map[NAME_KEY])
    current_name_pos = 1

    for command in input_as_map[COMMAND_KEY]:
        direction   = command[:1]
        shift_count = int(command[1:])
        current_name_pos = operations_map[direction](current_name_pos, shift_count, name_len)

    return input_as_map[NAME_KEY][current_name_pos-1]