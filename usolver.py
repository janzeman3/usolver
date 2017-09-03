## main script

print

# parse arguments
print("Parsing arguments...")

from common.ArgumentsParser import CArgumentsParser

Arguments = CArgumentsParser()

print("Arguments parsed:")
print("- Solver name:       " + Arguments.Solver)
print("- Solver parameters: " + str(Arguments.InputVariables))
print

# load solver list
print("Loading list of solvers...")

from common.SolverListLoader import CSolverListLoader

SolverListLoader = CSolverListLoader()
SolverList = SolverListLoader.SolverList
del SolverListLoader

print("Solver list loaded:")
print(SolverList.keys())

print("\n")