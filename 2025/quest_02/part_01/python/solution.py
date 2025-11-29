from os import path
import sys

workdir = path.abspath(path.dirname(__file__))
sys.path.insert(1, path.join(workdir, "../../python"))
import utils

# Create the absolute path to the given data file
fname = path.join(workdir, "../everybody_codes_e2025_q02_p1.txt")

cn_input = utils.prepare_data_from_file(fname)

cn_result = [0,0]
cn_div    = [10,10]

for i in range(3):
    cn_result = utils.multiply(cn_result, cn_result)
    cn_result = utils.divide(cn_result, cn_div)
    cn_result = utils.add(cn_result, cn_input)

result = "[" + ",".join(map(str, cn_result)) + "]"

# Answer for: what number will you get at the end of the process?
print(result)