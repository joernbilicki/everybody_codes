from os import path
import sys

# Make the functionality of a custom file available to import
workdir = path.abspath(path.dirname(__file__))
sys.path.insert(1, path.join(workdir, "../../python"))
import utils

# Create the absolute path to the given data file
fname = path.join(workdir, "../everybody_codes_e2025_q03_p3.txt")

crate_sizes = utils.prepare_data_from_file(fname)

set_count = 0

while len(crate_sizes) > 0:
    set_count += 1
    crate_set = set(crate_sizes)
    for crate in crate_set:
        crate_sizes.remove(crate)

print(set_count)