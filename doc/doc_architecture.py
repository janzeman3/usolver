## @page Architecture Architecture
#  description of basics architecture
#
#  @section archDecisions Decisions
#
#  @subsection archDecPython Python
#  Accroding to \ref R3 requirement, python will be used.
#
#  @subsection archDecStructure Structure and add-ons
#  According to \ref R1 requirement, the add-ons will be realized by copying the files.
#
#  According to \ref R2 requirement, each solver will have its own directory,
#  which brings possibility of many source files by each solber, see \ref archSolverDirectory.
#
#  @section archScheme Scheme/diagram
#
#  USolver has following class structures:
#   - solver list loader
#   - input processing:
#      - input structure loader
#      - input loader
#   - solver run
#   - output processing:
#      - ouput structure loader
#      - output creator
#
#  @section archInterfaces Interfaces
#
#  @subsection archSolverListStructure Solver list structure
#
#  Solver list is dictionary in form:
#   {uniqueSolverName: pathToSolver}
#
#  @section archSolverDirectory Solver directory
#
#  @subsection archSolverDirectoryPath Path to solver directory
#
#  @subsection archSolverDirectoryStructure Structure of solver directory
#
#  @subsection archSolverList Solver list update and maintanence
#
