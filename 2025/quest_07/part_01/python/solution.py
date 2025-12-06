from os import path
import sys

# Make the functionality of a custom file available to import
workdir = path.abspath(path.dirname(__file__))
sys.path.insert(1, path.join(workdir, "../../python"))
import utils

# Create the absolute path to the given data file
fname = path.join(workdir, "../everybody_codes_e2025_q07_p1.txt")

# Prepare a managable structure from the data file
input_as_dict:dict = utils.prepare_data_from_file(fname)

result:str = "NOT_FOUND"

rules:dict = input_as_dict[utils.RULES]

for name in input_as_dict[utils.NAMES]:
    if utils.check_name(name, rules):
        result = name
        break

# Which name from the list can be created while following the rules?
print(result)
