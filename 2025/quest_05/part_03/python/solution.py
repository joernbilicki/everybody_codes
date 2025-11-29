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

# Create a fishbone list. Format:
# - Index 0: Number of the sword
# - Index 1: Fishbone (list)
# - Index 2: Quality of the fishbone in index 1
# Additionally calculate the max length of all fishbones
fishbone_list = []
fishbone_max_len = 0
for sword in sword_quality:
    fishbone = utils.create_fishbone(sword_quality[sword])
    fishbone_list.append([sword, fishbone, int(utils.get_quality_of(fishbone))])
    fishbone_len = len(fishbone)
    if fishbone_len > fishbone_max_len: 
        fishbone_max_len = fishbone_len

# Normalize all fishbones to the same length for easier calculation (add trailing "zero" spines)
for fishbone_data in fishbone_list:
    fishbone = fishbone_data[1]
    fishbone_len = len(fishbone)
    while fishbone_len < fishbone_max_len:
        utils.add_new_spine(0, fishbone)
        fishbone_len += 1

# Create a new list, where each entry has the following structure:
# - Index 0: Number of the sword with leading zeros, if required (makes sorting easier)
# - Index 1: Sword value as a concatenated string of all level numbers (each lebvel number has leading zeros if required)
# - Index 2: Quality of a sword as integer
sword_values = []
filler = "000"

for fishbone_data in fishbone_list:
    sword = filler[len(fishbone_data[0]):] + fishbone_data[0]
    fishbone_value = ""
    for spine in fishbone_data[1]:
        spine_value = ""
        for i in spine:
            if i != utils.NaN:
                spine_value += str(i)
        spine_value = filler[len(spine_value):] + spine_value
        fishbone_value += spine_value
    sword_values.append([sword, fishbone_value, fishbone_data[2]])

# Sort the sword values in reversed order:
# 1. The better quality (x[2]) wins
# 2. The better levwel number (x[1]) wins
# 3. The better sword number (x[0]) wins
sorted_sword_values = sorted(sword_values, key=lambda x: (x[2], x[1], x[0]), reverse=True)

# Calculate the checksum
checksum = 0
position = 1
for sword_value in sorted_sword_values:
    checksum += position * int(sword_value[0])
    position += 1

# Answer for: What is the checksum of the sorted list?
print(checksum)