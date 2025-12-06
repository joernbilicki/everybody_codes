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
    # Assume the name will be found through the given rules ("grammar")
    name_found:bool = True
    name_len:int = len(name)

    if name[0] in rules:
        # Enter the grammar and retrieve the next possible letters from that rule 
        # that starts with the first letter of the given name
        next_letters:str = rules[name[0]]
        for i in range(1, name_len):
            # if the next letter of the given name is in the letters of the current rule
            if name[i] in next_letters:
                # Fetch the the rule for this letter and retrieve the next possible letters 
                # for this rule
                next_letters = rules[name[i]]
            else:
                # The name doesn't match the grammar
                name_found = False
                break
        # If the name matches the grammar
        if name_found:
            result = name
            break

print(result)
