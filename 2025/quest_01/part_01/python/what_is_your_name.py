from os import path

workdir = path.abspath(path.dirname(__file__))
filepath = path.join(workdir, "../everybody_codes_e2025_q01_p1.txt")

NAME_KEY    = 0
COMMAND_KEY = 1

input_as_map = {}

current_key = NAME_KEY

with open(filepath, 'r') as file:
    for line in file:
        if len(line.strip()) > 0:
            input_as_map[current_key] = line.strip().split(',')
            current_key += 1

name_len = len(input_as_map[NAME_KEY])

current_name_pos = 1

for command in input_as_map[COMMAND_KEY]:
    direction   = command[:1]
    shift_count = int(command[1:])
    match direction:
        case "R":
            current_name_pos = min(current_name_pos + shift_count, name_len)
        case "L":
            current_name_pos = max(current_name_pos - shift_count, 1)

print(input_as_map[NAME_KEY][current_name_pos-1])