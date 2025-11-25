from os import path
import re

workdir = path.abspath(path.dirname(__file__))

# Create the absolute path to the given data file
fname = path.join(workdir, "../everybody_codes_e2025_q02_p1.txt")

def multiply (cn1, cn2):
    return [cn1[0] * cn2[0] - cn1[1] * cn2[1], 
            cn1[0] * cn2[1] + cn1[1] * cn2[0]]

def divide (cn1, cn2):
    return [cn1[0] // cn2[0], 
            cn1[1] // cn2[1]]

def add (cn1, cn2):
    return [cn1[0] + cn2[0], 
            cn1[1] + cn2[1]]

with open(fname) as file:
    cn_in_file = file.readline()
    cn_input = [int(item) for item in re.findall("\d+", cn_in_file)]

cn_result = [0,0]
cn_div    = [10,10]

for i in range(3):
    cn_result = multiply(cn_result, cn_result)
    cn_result = divide(cn_result, cn_div)
    cn_result = add(cn_result, cn_input)

result = "[" + ",".join(map(str, cn_result)) + "]"
print(result)