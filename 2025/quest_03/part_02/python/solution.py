from os import path
import sys

# Make the functionality of a custom file available to import
workdir = path.abspath(path.dirname(__file__))
sys.path.insert(1, path.join(workdir, "../../python"))
import utils

# Create the absolute path to the given data file
fname = path.join(workdir, "../everybody_codes_e2025_q03_p2.txt")

crate_sizes = sorted(set(utils.prepare_data_from_file(fname)))

set_size = 0

for i in range(20):
    set_size += crate_sizes[i]

# Answer for: What is the smallest possible set of the crates that can be used for this purpose?
print(set_size)

