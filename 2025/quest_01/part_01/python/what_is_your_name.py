from os import path
import sys

workdir = path.abspath(path.dirname(__file__))
sys.path.insert(1, path.join(workdir, "../../python"))
import utils

fname = path.join(workdir, "../everybody_codes_e2025_q01_p1.txt")

input_as_map = utils.prepare_data_from_file(fname)

name_len = len(input_as_map[utils.NAME_KEY])

current_name_pos = 1

for command in input_as_map[utils.COMMAND_KEY]:
    direction   = command[:1]
    shift_count = int(command[1:])
    match direction:
        case "R":
            current_name_pos = min(current_name_pos + shift_count, name_len)
        case "L":
            current_name_pos = max(current_name_pos - shift_count, 1)

print(input_as_map[utils.NAME_KEY][current_name_pos-1])