## \brief Parses arguments from command line and encapsulates them
class CArgumentsParser:
  ## \brief Parses arguments from command line
  def __init__(self):
    ## String containgn Solver ID, is used for search in \ref archSolverListStructure "SolverList"
    self.Solver = ""
    ## Dictionary of loaded variables - see archInputVariablesStructure
    self.InputVariables = {}

    self._ParseCommandLine()

  def _ParseCommandLine(self):
    import argparse

    parser = argparse.ArgumentParser(description = "uSolver")
    parser.add_argument("-i", "--ini", help = "ini-file with list of variables")
    parser.add_argument("variables", nargs="*", help = "variables and values for solver")

    ParsedArguments = parser.parse_args()

    if ParsedArguments.ini:
      self._ParseCommandIniFile(ParsedArguments)

    self._ParseCommandLineVariables(ParsedArguments)

  def _ParseCommandLineVariables(self, ParsedArguments):
    for arg in ParsedArguments.variables:
      splitArg = arg.split("=")
      if len(splitArg) == 2:
        key = splitArg[0]
        value = splitArg[1]

        self.InputVariables[key] = value

        if key == "solver":
          self.Solver = value

  def _ParseCommandIniFile(self, ParsedArguments):
    iniFileName = ParsedArguments.ini
    print("Warning: Parsing of ini-files is not supported yet.")
