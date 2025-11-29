from math import floor
from os import path

# Make the functionality of a custom file available to import
workdir = path.abspath(path.dirname(__file__))

# Create the absolute path to the given data file
fname = path.join(workdir, "../everybody_codes_e2025_q04_p3.txt")

gear_list = []

with open(fname, 'r') as file:
    for line in file:
        gears = list(map(int, line.split("|")))
        gear_list.append(gears)

gear_ratio = 1.0
first_gear = gear_list[0][0]
gear_list[len(gear_list)-1].append(-1) # Append dummy value to the last list entry to make the loop work

for i in range(1, len(gear_list)):
    second_gear = gear_list[i][0]
    gear_ratio = gear_ratio * (first_gear / second_gear)
    first_gear = gear_list[i][1]

# Answer for: How many full turns will the last gear make if the first one turns exactly 100 times?
print(floor(100*gear_ratio))