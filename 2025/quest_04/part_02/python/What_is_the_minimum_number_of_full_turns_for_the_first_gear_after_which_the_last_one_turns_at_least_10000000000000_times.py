from os import path
from math import floor
import sys

# Make the functionality of a custom file available to import
workdir = path.abspath(path.dirname(__file__))
sys.path.insert(1, path.join(workdir, "../../python"))
import utils

# Create the absolute path to the given data file
fname = path.join(workdir, "../everybody_codes_e2025_q04_p2.txt")

gear_list = utils.prepare_data_from_file(fname)

print(gear_list)

factor = 1.0

first_gear = gear_list[0]

for i in range(1, len(gear_list)):
    second_gear = gear_list[i]
    factor = factor * (first_gear / second_gear)
    first_gear = second_gear

print(floor(2025*factor))