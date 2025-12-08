from os import path
import sys

# Make the functionality of a custom file available to import
workdir = path.abspath(path.dirname(__file__))
sys.path.insert(1, path.join(workdir, "../../python"))
import utils

# Create the absolute path to the given data file
fname = path.join(workdir, "../everybody_codes_e2025_q07_p2.txt")

# Prepare a managable structure from the data file
input_as_dict:dict = utils.prepare_data_from_file(fname)

result:int = 0

names:list = input_as_dict[utils.NAMES]
rules:dict = input_as_dict[utils.RULES]

for i in range(len(names)):
    name = names[i]
    if utils.check_name(name, rules) != None:
        result += (i + 1)

# Find all the names that comply with the rules and calculate the sum of their indices.
print(result)
