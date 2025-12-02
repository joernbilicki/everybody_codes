from os import path
import sys

# Make the functionality of a custom file available to import
workdir = path.abspath(path.dirname(__file__))
sys.path.insert(1, path.join(workdir, "../../python"))
import utils

# Create the absolute path to the given data file
fname = path.join(workdir, "../everybody_codes_e2025_q06_p3.txt")
training_plan = utils.prepare_data_from_file(fname)

training_plan = "AABCBABCABCabcabcABCCBAACBCa"



def count_mentors(working_plan:str, 
                  pos:int, 
                  training_plan_start_len:int,
                  training_plan_count:int, 
                  current_training_plan:int,
                  novice_mentor_distance) -> int:
    count = 0

    left_end  = pos - novice_mentor_distance
    right_end = pos + novice_mentor_distance + 1

    if current_training_plan == 1: # The position is int the first pattern block
        if left_end < 0:
            left_end = 0
    if current_training_plan == training_plan_count: # The position is in the last pattern block
        if right_end > training_plan_start_len:
            right_end = training_plan_start_len

    count = working_plan[left_end+training_plan_start_len:right_end+training_plan_start_len].count(working_plan[pos].upper())
    return count


working_plan = training_plan * 3 # Only working with the middle part. Avoiding overflow to the left / righ hand side.

novice_mentor_distance = 10
training_plan_count = 2
current_training_plan = 1

novices = "abc"

training_plan_start_len = len(training_plan)
training_plan_total_len = training_plan_start_len * training_plan_count
novice_mentor_count = 0

for i in range(training_plan_total_len):
    logical_pos = i % training_plan_start_len 
    if i > 0 and logical_pos == 0:
        current_training_plan += 1
    if training_plan[logical_pos] in novices:
        novice_mentor_count += count_mentors(working_plan, i, training_plan_start_len, training_plan_count, current_training_plan, novice_mentor_distance)

# What is the total number of possible novice-mentor pairs?
print(novice_mentor_count)
