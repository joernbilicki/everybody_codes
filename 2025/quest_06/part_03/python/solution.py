from os import path
import sys

# Make the functionality of a custom file available to import
workdir = path.abspath(path.dirname(__file__))
sys.path.insert(1, path.join(workdir, "../../python"))
import utils

# Create the absolute path to the given data file
fname = path.join(workdir, "../everybody_codes_e2025_q06_p3.txt")
training_plan = utils.prepare_data_from_file(fname)


def count_mentors(working_plan:str, 
                  pos:int, 
                  training_plan_total_len:int,
                  novice_mentor_distance) -> int:
    """
    Counts the mentors for a novice at a given position in the total training plan within a maximal distance.
    
    :param working_plan: The total training plan based on the given data and the repetition factor.
    :type working_plan: str
    :param pos: The position of the given novice in the working_plan.
    :type pos: int
    :param training_plan_total_len: The total length of the working_plan to check the boundary to the right hand side..
    :type training_plan_total_len: int
    :param novice_mentor_distance: The maximal distance to find mentors for a given novice (based on its position in the
    working_plan).
    :return: The count of mentors found around a novice within the given distance.
    :rtype: int
    """
    count = 0

    left_end  = pos - novice_mentor_distance
    right_end = pos + novice_mentor_distance + 1

    if left_end < 0:
        left_end = 0
    if right_end > training_plan_total_len:
        right_end = training_plan_total_len

    count = working_plan[left_end:right_end].count(working_plan[pos].upper())
    return count

novices = "abc"
training_plan_count = 1000
novice_mentor_distance = 1000

working_plan = training_plan * training_plan_count
training_plan_total_len = len(working_plan)

novice_mentor_count = 0

for i in range(training_plan_total_len):
    if working_plan[i] in novices:
        novice_mentor_count += count_mentors(working_plan, i, training_plan_total_len, novice_mentor_distance)

# What is the total number of possible novice-mentor pairs?
print(novice_mentor_count)
