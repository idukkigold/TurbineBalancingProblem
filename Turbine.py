from __future__ import print_function
from ortools.constraint_solver import pywrapcp

def main():
  """Entry point of the program"""
  solver = pywrapcp.Solver('ConstraintExample')

  # Create the variables.
  num_vals = 3
  x = solver.IntVar(0, num_vals - 1, 'x')
  y = solver.IntVar(0, num_vals - 1, 'y')
  z = solver.IntVar(0, num_vals - 1, 'z')

  # Constraint 0: x != y.
  solver.Add(x != y)

  print('Number of constraints =', solver.Constraints())

  # Call the solver.
  decision_builder = solver.Phase([x, y, z], solver.CHOOSE_FIRST_UNBOUND, solver.ASSIGN_MIN_VALUE)
  solver.NewSearch(decision_builder)
  while solver.NextSolution():
    solution = 'Solution:'
    for var in [x, y, z]:
      solution += ' {} = {};'.format(var.Name(), var.Value())
    print(solution)
  solver.EndSearch()
  print("Number of solutions found:", solver.Solutions())
  print('')
  print('Advanced usage:')
  print('Problem solved in ', solver.WallTime(), ' milliseconds')
  print('Memory usage: ', pywrapcp.Solver.MemoryUsage(), ' bytes')

if __name__ == "__main__":
  main()