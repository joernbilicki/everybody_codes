from os import path
import sys

# Make the functionality of a custom file available to import
workdir = path.abspath(path.dirname(__file__))
sys.path.insert(1, path.join(workdir, "../../python"))
import utils

# Create the absolute path to the given data file
fname = path.join(workdir, "../everybody_codes_e2025_q01_p1.txt")

# Prepare a managable structure from the data file
input_as_map = utils.prepare_data_from_file(fname)

def r_operation(current_name_pos, shift_count, name_len, name_list): 
    """
    Returns for the "right shift operation" the new position
    in the name list. (ignores the parameter name_list)
    """
    return min(current_name_pos + shift_count, name_len)

def l_operation(current_name_pos, shift_count, name_len, name_list):
    """
    Returns for the "left shift operation" the new position
    in the name list. (ignores the parameters name_len and name_list)
    """
    return max(current_name_pos - shift_count, 1)

# Organize the operations in a map with the oparation's shortcut as key.
operations_map = {
    "R": r_operation,
    "L": l_operation
}

# Answer for: what is your name? 
print(utils.get_name(input_as_map, operations_map))
