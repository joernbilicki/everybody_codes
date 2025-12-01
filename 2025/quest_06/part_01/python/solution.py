from os import path
import sys

# Make the functionality of a custom file available to import
workdir = path.abspath(path.dirname(__file__))
sys.path.insert(1, path.join(workdir, "../../python"))
import utils

# Create the absolute path to the given data file
fname = path.join(workdir, "../everybody_codes_e2025_q06_p1.txt")
training_plan = utils.prepare_data_from_file(fname)

mentors = "A"
novice_mentor_count = utils.get_count(training_plan, mentors)

# What is the total number of possible novice-mentor pairs in the sword fighting category?
print(novice_mentor_count)
