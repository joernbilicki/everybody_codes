NAMES:str = "names"
RULES:str = "rules"


def prepare_names(data_dict:dict, line:str) -> None:
    """
    The first line of the input data is a comma separated list of names.
    This function creates a "real list from -this input and adds it
    under the key NAMES in the given dictionary.
    
    :param data_dict: Holds the name list under the key NAMES. Empty at start.
    :type data_dict: dict
    :param line: Comma-separated list of names
    :type line: str
    """
    data_dict[NAMES] = [x.rstrip() for x in line.split(",")]


def prepare_rule(data_dict:dict, line:str) -> None:
    """
    Adds the content of a line (formatted as rule) under the key RULES to the 
    given dictionary.
    
    :param data_dict: Holds the rules as dictionary under the key RULES.
    :type data_dict: dict
    :param line: Rule.
    :type line: str
    """
    rule:str = [x.rstrip() for x in line.split(">")]
    if RULES in data_dict:
        data_dict[RULES][rule[0]] = rule[1].replace(",", "")
    else: 
        data_dict[RULES] = {rule[0]: rule[1].replace(",", "")}


def add_rules_for_leafletters(rules_dict:dict) -> None:
    """
    There may be letter on the right hand side of everey rule, that represents a leaf in
    the given "grammar". That is: there is no left hand side with such a letter. 
    To simplify the rule evaluation logic, this function adds such leafletters as empty rules
    to the rules dictionary.
    
    :param data_dict: Dictionary of rules.
    :type data_dict: dict
    """
    leafletters:str = ""
    
    for rule in rules_dict:
        rhs:str = rules_dict[rule]
        for letter in rhs:
            if letter not in rules_dict: leafletters += letter
    
    for letter in leafletters:
        rules_dict[letter] = ""


prepare_ops:list = [prepare_names, prepare_rule]


def prepare_data_from_file(fname:str) -> dict:
    """
    Prepares the input data as dictionary of
    - a list of names (key: NAMES)
    - and a dictionary of rules (key: RULES).
    
    :param fname: Filename of the input data.
    """
    with open(fname) as file:
        ops_index:int = 0
        data_dict:dict = {}
        for line in file:
            if len(line.strip()) > 0:
                prepare_ops[ops_index](data_dict, line)
            ops_index = 1
    
    add_rules_for_leafletters(data_dict[RULES])

    return data_dict


def check_name(name:str, rules:dict) -> dict:
    """
    Checks the given name accordiung to the given rules.
    
    :param name: Name to check.
    :type name: str
    :param rules: Rules to check the given name.
    :type rules: dict
    :return: The last matching rule, if the name matches the rules, None otherwise.
    :rtype: dict
    """
    last_rule:dict = None
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
                last_rule = rules[name[i]]
                next_letters = last_rule
            else:
                # The name doesn't match the grammar
                last_rule = None
                break

        return last_rule
