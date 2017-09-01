## Loads list of available solvers
class CSolverListLoader:

  ## \brief List of available solvers
  #
  # Dictionary - structure see in \ref archSolverListStructure
  SolverList = {}

  ## \brief constructor - fills SolverList
  #
  #  \todo make the list loading dynamic
  def __init__(self):
    self.SolverList = {"square": "square", "rectangle": "rectangle"}