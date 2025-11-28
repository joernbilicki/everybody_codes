from os import path
import sys

# Make the functionality of a custom file available to import
workdir = path.abspath(path.dirname(__file__))
sys.path.insert(1, path.join(workdir, "../../python"))
import utils

# Create the absolute path to the given data file
fname = path.join(workdir, "../everybody_codes_e2025_q03_p1.txt")

crate_sizes = utils.prepare_data_from_file(fname)

largest_set = 0

for crate in crate_sizes:
    largest_set += crate

print(largest_set)

