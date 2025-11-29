from os import path
from math import ceil
import sys

# Make the functionality of a custom file available to import
workdir = path.abspath(path.dirname(__file__))
sys.path.insert(1, path.join(workdir, "../../python"))
import utils

# Create the absolute path to the given data file
fname = path.join(workdir, "../everybody_codes_e2025_q05_p2.txt")

sword_quality = utils.prepare_data_from_file(fname)

fishbone_list = []
for sword in sword_quality:
    fishbone_list.append(utils.create_fishbone(sword_quality[sword]))

min_quality = sys.maxsize
max_quality = utils.NaN

for fishbone in fishbone_list:
    current_quality = int(utils.get_quality_of(fishbone))
    if current_quality < min_quality:
        min_quality = current_quality
    if current_quality > max_quality:
        max_quality = current_quality

quality_difference = max_quality - min_quality
# Answer for: What is the quality difference between the best and the weakest sword on the given list?
print(quality_difference)