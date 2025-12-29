
from re import A
import time
from ortools.linear_solver import pywraplp
from ortools.sat.python import cp_model

model = cp_model.CpModel()

a = model.NewBoolVar('a')
b = model.NewBoolVar('b')
c = model.NewBoolVar('c')
d = model.NewBoolVar('d')
e = model.NewBoolVar('e')
f = model.NewBoolVar('f')


letters = [a, b, c, d, e, f]
model.Add(d+e == 1)
model.Add(f+e == 1)
model.Add(f+c == 1)
model.Add(b+c == 1)
model.Add(a+b+c == 1)
model.Add(a+b == 1)
model.Add(a+d == 1)
solver = cp_model.CpSolver()
status = solver.Solve(model)

for x in letters:
    print(x, solver.Value(x))
