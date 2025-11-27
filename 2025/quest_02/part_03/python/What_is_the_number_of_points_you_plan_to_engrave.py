from os import path
import sys

workdir = path.abspath(path.dirname(__file__))
sys.path.insert(1, path.join(workdir, "../../part_02/python"))
import solver

print(solver.solve(1001))