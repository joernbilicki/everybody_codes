from os import path
import sys

workdir = path.abspath(path.dirname(__file__))
sys.path.insert(1, path.join(workdir, "../../python"))
import utils

fname = path.join(workdir, "../everybody_codes_e2025_q01_p2.txt")

input_as_map = utils.prepare_data_from_file(fname)

# Organize the operations in a map with the oparation's shortcut as key.
operations_map = {
    "R": utils.r_circle_operation,
    "L": utils.l_circle_operation
}

# Answer for: What is the name of your first parent?
print(utils.get_name(input_as_map, operations_map))