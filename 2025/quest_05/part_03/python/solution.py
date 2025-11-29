from os import path
from math import ceil
import sys

# Make the functionality of a custom file available to import
workdir = path.abspath(path.dirname(__file__))
sys.path.insert(1, path.join(workdir, "../../python"))
import utils

# Create the absolute path to the given data file
fname = path.join(workdir, "../everybody_codes_e2025_q05_p3.txt")

sword_quality = utils.prepare_data_from_file(fname)

fishbone_list = []
fishbone_max_len = 0
for sword in sword_quality:
    fishbone = utils.create_fishbone(sword_quality[sword])
    fishbone_list.append([sword, fishbone, int(utils.get_quality_of(fishbone))])
    fishbone_len = len(fishbone)
    if fishbone_len > fishbone_max_len: 
        fishbone_max_len = fishbone_len

# Format of fishbone_list
# - Index 0: Number of the sword
# - Index 1: Fishbone (list)
# - Index 2: Quality of the fishbone in index 1

# Normalize all fishbones to the same length for easier calculation
for fishbone_data in fishbone_list:
    fishbone = fishbone_data[1]
    fishbone_len = len(fishbone)
    while fishbone_len < fishbone_max_len:
        utils.add_new_spine(0, fishbone)
        fishbone_len += 1

# Create a new list, where each entry has the following structure:
# - Index 0: Number of the sword
# - Index 1: Sword value
sword_values = []
sword_filler = "000"

for fishbone_data in fishbone_list:
    sword = sword_filler[len(fishbone_data[0]):] + fishbone_data[0]
    value = ""
    for spine in fishbone_data[1]:
        for i in spine:
            if i == utils.NaN:
                value += "0"
            else:
                value += str(i)

    sword_values.append([sword, value, fishbone_data[2]])

sorted_sword_values = sorted(sword_values, key=lambda x: (x[2], x[1], x[0]), reverse=True)

checksum = 0
position = 1
for sword_value in sorted_sword_values:
    checksum += position * int(sword_value[0])
    position += 1
# Answer for: What is the checksum of the sorted list?
print(checksum)