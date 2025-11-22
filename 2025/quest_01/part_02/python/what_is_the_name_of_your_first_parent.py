from os import path
import sys

workdir = path.abspath(path.dirname(__file__))
sys.path.insert(1, path.join(workdir, "../../python"))
import utils

fname = path.join(workdir, "../everybody_codes_e2025_q01_p2.txt")

input_as_map = utils.prepare_data_from_file(fname)

name_len = len(input_as_map[utils.NAME_KEY])

current_name_pos = 1

for command in input_as_map[utils.COMMAND_KEY]:
    direction   = command[:1]
    shift_count = int(command[1:])
    match direction:
        case "R":
            current_name_pos = (current_name_pos + shift_count) % name_len
            if current_name_pos == 0:
                current_name_pos = name_len
        case "L":
            if current_name_pos == shift_count:
                current_name_pos = name_len
            else:
                current_name_pos = (current_name_pos - shift_count) % name_len

print(input_as_map[utils.NAME_KEY][current_name_pos-1])