from os import path
from math import floor
import sys

# Make the functionality of a custom file available to import
workdir = path.abspath(path.dirname(__file__))
sys.path.insert(1, path.join(workdir, "../../python"))
import utils

# Create the absolute path to the given data file
fname = path.join(workdir, "../everybody_codes_e2025_q04_p1.txt")

gear_list = utils.prepare_data_from_file(fname)

gear_ratio = utils.get_gear_ratio(gear_list)

# Answer for: How many full turns will the last gear make if the first one turns exactly 2025 times?
print(floor(2025*gear_ratio))