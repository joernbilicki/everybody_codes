from os import path
from math import ceil
import sys

# Make the functionality of a custom file available to import
workdir = path.abspath(path.dirname(__file__))
sys.path.insert(1, path.join(workdir, "../../python"))
import utils

# Create the absolute path to the given data file
fname = path.join(workdir, "../everybody_codes_e2025_q05_p1.txt")

sword_quality = utils.prepare_data_from_file(fname)
# There is just one entry in the dictionary. Retrieve it.
value = iter(sword_quality).__next__()
quality_data = sword_quality[value]

fishbone = utils.create_fishbone(quality_data)

quality = utils.get_quality_of(fishbone)

# Answer for: What is the quality of the sword currently being recorded by the armourer?
print(quality)