
from ortools.linear_solver import pywraplp
solver = pywraplp.Solver('Max Preference',
                         pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
allVertices = [0, 1, 2, 3, 4, 5, 6]
allcolors = [0, 1, 2, 3]

X = {}
for v in allVertices:
    for c in allcolors:
        X[v, c] = solver.BoolVar('vertex %s colored %s' % (v, c))
Y = {}
for c in allcolors:
    Y[c] = solver.BoolVar("%s is used" % (c))

for v in allVertices:
    solver.Add(solver.Sum([X[v, c]for c in allcolors]) == 1)
# v0
for c in allcolors:
    solver.Add(solver.Sum([X[0, c], X[1, c]]) <= 1)
for c in allcolors:
    solver.Add(solver.Sum([X[0, c], X[3, c]]) <= 1)
for c in allcolors:
    solver.Add(solver.Sum([X[0, c], X[6, c]]) <= 1)

# v1
for c in allcolors:
    solver.Add(solver.Sum([X[1, c], X[0, c]]) <= 1)
for c in allcolors:
    solver.Add(solver.Sum([X[1, c], X[2, c]]) <= 1)
for c in allcolors:
    solver.Add(solver.Sum([X[1, c], X[3, c]]) <= 1)
for c in allcolors:
    solver.Add(solver.Sum([X[1, c], X[4, c]]) <= 1)

# v2
for c in allcolors:
    solver.Add(solver.Sum([X[2, c], X[1, c]]) <= 1)
for c in allcolors:
    solver.Add(solver.Sum([X[2, c], X[4, c]]) <= 1)
for c in allcolors:
    solver.Add(solver.Sum([X[2, c], X[6, c]]) <= 1)

# v3
for c in allcolors:
    solver.Add(solver.Sum([X[3, c], X[0, c]]) <= 1)
for c in allcolors:
    solver.Add(solver.Sum([X[3, c], X[1, c]]) <= 1)
for c in allcolors:
    solver.Add(solver.Sum([X[3, c], X[4, c]]) <= 1)
for c in allcolors:
    solver.Add(solver.Sum([X[3, c], X[5, c]]) <= 1)


# v4
for c in allcolors:
    solver.Add(solver.Sum([X[4, c], X[1, c]]) <= 1)
for c in allcolors:
    solver.Add(solver.Sum([X[4, c], X[2, c]]) <= 1)
for c in allcolors:
    solver.Add(solver.Sum([X[4, c], X[3, c]]) <= 1)
for c in allcolors:
    solver.Add(solver.Sum([X[4, c], X[5, c]]) <= 1)

# v5
for c in allcolors:
    solver.Add(solver.Sum([X[5, c], X[4, c]]) <= 1)
for c in allcolors:
    solver.Add(solver.Sum([X[5, c], X[3, c]]) <= 1)
for c in allcolors:
    solver.Add(solver.Sum([X[5, c], X[6, c]]) <= 1)

# v5
for c in allcolors:
    solver.Add(solver.Sum([X[6, c], X[0, c]]) <= 1)
for c in allcolors:
    solver.Add(solver.Sum([X[6, c], X[5, c]]) <= 1)
for c in allcolors:
    solver.Add(solver.Sum([X[6, c], X[2, c]]) <= 1)

for v in allVertices:
    for c in allcolors:
        solver.Add(X[v, c] <= Y[c])

solver.Minimize(solver.Sum([Y[c]for c in allcolors]))
solver.Solve()
print(solver.Objective().Value())
for v in solver.variables():
    if(v.solution_value() == 1):
        print(v.name())
