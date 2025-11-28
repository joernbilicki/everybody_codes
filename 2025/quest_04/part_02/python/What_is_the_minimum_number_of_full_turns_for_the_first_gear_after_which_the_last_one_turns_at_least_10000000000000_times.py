from os import path
from math import ceil
import sys

# Make the functionality of a custom file available to import
workdir = path.abspath(path.dirname(__file__))
sys.path.insert(1, path.join(workdir, "../../python"))
import utils

# Create the absolute path to the given data file
fname = path.join(workdir, "../everybody_codes_e2025_q04_p2.txt")

gear_list = utils.prepare_data_from_file(fname)

gear_ratio = utils.get_gear_ratio(gear_list)

minimum_turns = 10000000000000

print(ceil((1/gear_ratio)*minimum_turns))