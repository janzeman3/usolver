## @page Requirements Requirements
#  user requirements on system
#
#  @section MainAim Main aim
#  Main aim of the sowtware is provide universal solver of many problems.
#
#  @section Requiremnts Requirements
#
#  @subsection R1 Easy extensions
#  Addition of new problem must be easy and done by user. While the list of problems is maintened by programmer.
#
#  @subsection R2 Complex problems
#  Each problem can be of bigger complexity.
#
#  @subsection R3 GNU/GPL
#  SW will be distributed under GNU/GPL licence. Most of SW will be free, but some parts can be customized and payed.
#
#  @subsection R4 Input to solver - command line
#  Each solver requires input information. The information will be entered using command line:
#  - option A (command line only): usolver.py solver=NameOfProblem inputVariable1=value1 inputVariable2=value2...
#  - option B1 (ini-file only): usolver.py -i NameOfIniFile
#  - option B2 (ini-file only): usolver.py --ini NameOfIniFile
#  - option C (combination): usolver.py --ini NameOfIniFile solver=NameOfProblem inputVariable1=value1 inputVariable2=value2...
#
#  If option C is used and a variable is definde twice (i.e. in commnad line and also in ini-file)
#  value from commnad line overrides the ini-file value.
#
#  The overriding is feature: user can set solver in ini file and then change only a few parameters, when executes the solver.
