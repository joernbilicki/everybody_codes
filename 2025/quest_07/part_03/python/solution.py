from os import path
import sys

# Make the functionality of a custom file available to import
workdir = path.abspath(path.dirname(__file__))
sys.path.insert(1, path.join(workdir, "../../python"))
import utils

# Create the absolute path to the given data file
fname = path.join(workdir, "../everybody_codes_e2025_q07_p3_1.txt")

# Prepare a managable structure from the data file
input_as_dict:dict = utils.prepare_data_from_file(fname)


prefixes:list = input_as_dict[utils.NAMES]
rules:dict    = input_as_dict[utils.RULES]

unique_names:set = {}

for prefix in prefixes:
    final_rule:dict = utils.check_name(prefix, rules)
    if final_rule != None:
        # Todo
        break

# How many unique names can be created based on the given prefixes and rules?
print(len(unique_names))
