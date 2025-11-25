import re

def prepare_data_from_file(fname):
    with open(fname) as file:
        cn_in_file = file.readline()
        cn_input = [int(item) for item in re.findall("-?\\d+", cn_in_file)]

    return cn_input

def multiply (cn1, cn2):
    return [cn1[0] * cn2[0] - cn1[1] * cn2[1], 
            cn1[0] * cn2[1] + cn1[1] * cn2[0]]

def divide (cn1, cn2):
    return [cn1[0] // cn2[0], 
            cn1[1] // cn2[1]]

def add (cn1, cn2):
    return [cn1[0] + cn2[0], 
            cn1[1] + cn2[1]]
