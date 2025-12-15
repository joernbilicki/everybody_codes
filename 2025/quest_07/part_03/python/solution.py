from os import path
import sys

# Make the functionality of a custom file available to import
workdir = path.abspath(path.dirname(__file__))
sys.path.insert(1, path.join(workdir, "../../python"))
import utils


def add_name(name:str, names:set, current_rule_rhs:str, rules:dict) -> None:
    """
    Adds a name to a list of unique names. Each name has at least 7 and at most 11 letters.
    This method walks recursive through a list of letters (based on the rules dictionary) and
    adds them to the given name.
    
    :param name: The name to add to the set of unique names.
    :type name: str
    :param names: The resulting set of unique names.
    :type names: set
    :param current_rule_rhs: The letters of the righrt hand side of the current rule.
    :type current_rule_rhs: str
    :param rules: The rules dictionary.
    :type rules: dict
    """
    if len(name) <= 11: 
        if 7 <= len(name): 
            names.add(name)
        for letter in current_rule_rhs:
            add_name((name + letter).strip(), names, rules[letter], rules)


# Create the absolute path to the given data file
fname = path.join(workdir, "../everybody_codes_e2025_q07_p3.txt")

# Prepare a managable structure from the data file
input_as_dict:dict = utils.prepare_data_from_file(fname)

prefixes:list = input_as_dict[utils.NAMES]
rules:dict    = input_as_dict[utils.RULES]

unique_names:set = set()

for prefix in prefixes:
    final_rule_rhs:dict = utils.check_name(prefix, rules)
    if final_rule_rhs != None:
        add_name(prefix, unique_names, final_rule_rhs, rules)

# How many unique names can be created based on the given prefixes and rules?
print(len(unique_names))