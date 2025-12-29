import time
from ortools.linear_solver import pywraplp
from ortools.sat.python import cp_model

model = cp_model.CpModel()


allLetters = range(26)
f = model.NewIntVar(0, 9, 'f')
o = model.NewIntVar(0, 9, 'o')
r = model.NewIntVar(0, 9, 'r')
t = model.NewIntVar(0, 9, 't')
y = model.NewIntVar(0, 9, 'y')
e = model.NewIntVar(0, 9, 'e')
s = model.NewIntVar(0, 9, 's')
i = model.NewIntVar(0, 9, 'i')
x = model.NewIntVar(0, 9, 'x')
n = model.NewIntVar(0, 9, 'n')


letters = [f, o, r, t, y, e, s, i, x, n]
model.AddAllDifferent(letters)
model.Add(10000*f+1000*o+100*r+10*t+y+100*t+10*e+n +
          100*t+10*e+n == 10000*s+1000*i+100*x+10*t+y)
solver = cp_model.CpSolver()
status = solver.Solve(model)

for x in letters:
    print(x, solver.Value(x))
