from os import path
from math import floor

# Make the functionality of a custom file available to import
workdir = path.abspath(path.dirname(__file__))

# Create the absolute path to the given data file
fname = path.join(workdir, "../everybody_codes_e2025_q04_p1.txt")

gear_list = []
with open(fname, 'r') as file:
    for line in file:
       gear_list.append(int(line))

factor = 1.0

first_gear = gear_list[0]

for i in range(1, len(gear_list)):
    second_gear = gear_list[i]
    factor = factor * (first_gear / second_gear)
    first_gear = second_gear

print(floor(2025*factor))