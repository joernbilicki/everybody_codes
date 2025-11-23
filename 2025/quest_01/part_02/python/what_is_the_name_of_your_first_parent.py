from os import path
import sys

workdir = path.abspath(path.dirname(__file__))
sys.path.insert(1, path.join(workdir, "../../python"))
import utils

fname = path.join(workdir, "../everybody_codes_e2025_q01_p2.txt")

input_as_map = utils.prepare_data_from_file(fname)

def r_operation(current_name_pos, shift_count, name_len): 
    """
    Returns for the "right shift operation" the new position
    in the name list.
    """
    new_name_pos = (current_name_pos + shift_count) % name_len
    if new_name_pos == 0:
        new_name_pos = name_len
    return new_name_pos

def l_operation(current_name_pos, shift_count, name_len):
    """
    Returns for the "left shift operation" the new position
    in the name list.
    """
    if current_name_pos == shift_count:
        new_name_pos = name_len
    else:
        new_name_pos = (current_name_pos - shift_count) % name_len
    return new_name_pos

# Organize the operations in a map with the oparation's shortcut as key.
operations_map = {
    "R": r_operation,
    "L": l_operation
}

# Prints the resulting name 
print(utils.get_name(input_as_map, operations_map))