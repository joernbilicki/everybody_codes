NAME_KEY    = 0
COMMAND_KEY = 1

def prepare_data_from_file(fname):

    input_as_map = {}

    current_key = NAME_KEY

    with open(fname, 'r') as file:
        for line in file:
            if len(line.strip()) > 0:
                input_as_map[current_key] = line.strip().split(',')
                current_key += 1

    return input_as_map