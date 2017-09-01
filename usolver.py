## main script

from common.SolverListLoader import CSolverListLoader

SolverListLoader = CSolverListLoader()
SolverList = SolverListLoader.SolverList
del SolverListLoader

print("Solver list loaded:")
print(SolverList)
