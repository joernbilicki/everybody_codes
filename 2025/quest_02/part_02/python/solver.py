from os import path
import sys

workdir = path.abspath(path.dirname(__file__))
sys.path.insert(1, path.join(workdir, "../../python"))
import utils


def is_in_range(cn):
    """
    Checks a given complex number, whether every part is in the range
    -1000000 <= part <= 1000000.
    
    :param cn: The complex number to check
    :return: true, if all parts are within the range, false otherwise.
    """
    return (-1000000 <= cn[0] <= 1000000) and (-1000000 <= cn[1] <= 1000000)


def do_cycles(cn):
    """
    Implementation of the required 100 calculation cycles.
    Exits prematurely, if the resulting complex number is
    out of range, or exits after all cycles.
    
    :param cn: A complex number in the grid to perfrom the 
    calculation for.
    :return: 1, if the calculation exeeds the range, 0 otherwise.
    """
    cn_div = [100000,100000]
    cn_result = cn
    for i in range(99):
        cn_result = utils.multiply(cn_result, cn_result)
        cn_result = utils.divide(cn_result, cn_div)
        cn_result = utils.add(cn_result, cn)
        if not is_in_range(cn_result):
            return 1
    return 0


def solve(grid_size):
    """
    Solves the quest's part.
    
    :param grid_size: BeschreibungSize of the grid for the
    calculation.
    :return: Count of complex numbers, that don't exeed the range.
    """
    # Create the absolute path to the given data file
    fname = path.join(workdir, "everybody_codes_e2025_q02_p2.txt")
    cn_input = utils.prepare_data_from_file(fname)

    offset = 1000
    cn_offset = [offset, offset]

    # Calculation of the lower right corner is just for information
    cn_bottom_right = utils.add(cn_input, cn_offset)

    # Create the grid
    distance = offset // (grid_size-1) # 10 according to the task
    cn_grid = []
    for y in range(grid_size):
        for x in range(grid_size):
            cn_grid.append([cn_input[0] + x * distance, 
                            cn_input[1] + y * distance])
    
    # Output just for information
    print(cn_grid)
    print(len(cn_grid))

    # Assumption: At the beginning no complex number in the grid exeeds the range
    count_result = len(cn_grid)

    for cn in cn_grid:
        # Reduce the count, if a given complex number in the grid exeeds the range
        count_result -= do_cycles(cn)

    # return the remaining count
    return count_result