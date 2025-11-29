from os import path
import sys

workdir = path.abspath(path.dirname(__file__))
sys.path.insert(1, path.join(workdir, "../../python"))
import utils

fname = path.join(workdir, "../everybody_codes_e2025_q01_p3.txt")

input_as_map = utils.prepare_data_from_file(fname)

def get_normalized_shift_count(shift_count, name_len): return shift_count - (shift_count // name_len) * name_len

def swap_names(name_list, old_pos, new_pos): name_list[old_pos-1], name_list[new_pos-1] = name_list[new_pos-1], name_list[old_pos-1]

def r_operation(current_name_pos, shift_count, name_len, name_list):
    """
    """
    normalized_shift_count = get_normalized_shift_count(shift_count, name_len)
    if normalized_shift_count > 0:
        # Call the target shift operation
        new_pos = utils.r_circle_operation(current_name_pos, normalized_shift_count, name_len, name_list)
        swap_names(name_list, current_name_pos, new_pos)
    return 1

def l_operation(current_name_pos, shift_count, name_len, name_list):
    """
    """
    normalized_shift_count = get_normalized_shift_count(shift_count, name_len)
    if normalized_shift_count > 0:
        # Call the target shift operation
        new_pos = utils.l_circle_operation(current_name_pos, normalized_shift_count, name_len, name_list)
        swap_names(name_list, current_name_pos, new_pos)
    return 1

# Organize the operations in a map with the oparation's shortcut as key.
operations_map = {
    "R": r_operation,
    "L": l_operation
}

# Answer for: What is the name of your second parent?
print(utils.get_name(input_as_map, operations_map))