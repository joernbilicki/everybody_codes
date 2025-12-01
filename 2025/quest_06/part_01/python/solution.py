from os import path
import sys

# Make the functionality of a custom file available to import
workdir = path.abspath(path.dirname(__file__))
sys.path.insert(1, path.join(workdir, "../../python"))
import utils

# Create the absolute path to the given data file
fname = path.join(workdir, "../everybody_codes_e2025_q06_p1.txt")
training_plan = utils.prepare_data_from_file(fname)

def add_mentor(mentor_dict:dict, category:str):
    if category not in mentor_dict: mentor_dict[category] = 0
    mentor_dict[category] += 1

def add_mentors_for_novice(novice_dict:dict, mentor_dict, category:str):
    if category not in novice_dict: novice_dict[category] = 0
    novice_dict[category] += mentor_dict[category.capitalize()]

mentors = "ABC"
novices = "abc"

mentor_dict = {}
novice_dict = {}

for category in training_plan:
    if category in mentors: add_mentor(mentor_dict, category)
    if category in novices: add_mentors_for_novice(novice_dict, mentor_dict, category)

novice_mentor_count = 0

for novice in novice_dict:
    print(novice)

# What is the total number of possible novice-mentor pairs?
print(novice_mentor_count)
