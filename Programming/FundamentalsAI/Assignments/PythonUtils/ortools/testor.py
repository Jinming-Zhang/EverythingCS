
from ortools.linear_solver import pywraplp

solver = pywraplp.Solver('Timetabling Problem',
                         pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

v1 = solver.IntVar(0, 5, 't1')
v2 = solver.IntVar(0, 7, 't2')
solver.Add(v1 <= 2 or v1 >= 3)
cstraints = solver.constraints()
solver.Maximize(v1+v2)
solver.Solve()
print(v1.solution_value())
print(v2.solution_value())
