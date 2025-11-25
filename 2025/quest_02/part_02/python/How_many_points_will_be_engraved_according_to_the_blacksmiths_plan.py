from os import path
import sys

workdir = path.abspath(path.dirname(__file__))
sys.path.insert(1, path.join(workdir, "../../python"))
import utils

# Create the absolute path to the given data file
fname = path.join(workdir, "../everybody_codes_e2025_q02_p2.txt")

def is_in_range(cn):
    return (-1000000 <= cn[0] <= 1000000) and (-1000000 <= cn[1] <= 1000000)

cn_input = utils.prepare_data_from_file(fname)

cn_input = [35300,-64910]

offset = 1000
cn_offset = [offset, offset]
cn_bottom_right = utils.add(cn_input, cn_offset)

cn_grid = []

grid_size = 101
distance = offset // (grid_size-1) # 10 according to the task

for y in range(grid_size):
    for x in range(grid_size):
        cn_grid.append([cn_input[0] + x * distance, 
                        cn_input[1] + y * distance])
        
print(cn_grid)
print(len(cn_grid))

count_result = len(cn_grid)

for cn in cn_grid:
    cn_result = cn
    for i in range(99):
        cn_result = utils.multiply(cn_result, cn_result)
        cn_result = utils.divide(cn_result, [100000,100000])
        cn_result = utils.add(cn_result, cn)
        if not is_in_range(cn_result):
            count_result -= 1
            break

print(count_result)