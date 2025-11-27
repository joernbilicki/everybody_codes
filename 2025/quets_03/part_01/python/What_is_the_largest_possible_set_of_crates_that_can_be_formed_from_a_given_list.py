from os import path

# Make the functionality of a custom file available to import
workdir = path.abspath(path.dirname(__file__))

# Create the absolute path to the given data file
fname = path.join(workdir, "../everybody_codes_e2025_q03_p1.txt")

def prepare_data_from_file(fname):
    """
    reads the given file and creates a list of numbers (type: string)
    
    :param fname: Name of the file to read the numbers from.
    :return: List of numbers (type: string).
    """
    with open(fname) as file:
        input_line = file.readline()
        return input_line.split(",")

crate_sizes = prepare_data_from_file(fname)

crate_set = set(crate_sizes)

largest_set = 0

for i in crate_set:
    largest_set += int(i)

print(largest_set)

