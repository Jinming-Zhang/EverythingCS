import math
from ortools.linear_solver import pywraplp

bs = range(10)
ss = range(8)

# billyPayoffTable[2][3] payoff at col3, row4
billyPayoffTable = []

for s in ss:
    colPayoff = []
    for b in bs:
        billyX = b
        billyY = len(bs)-b-1
        sommerX = s
        sommerY = len(ss)-s-1

        res = 0
        if billyY > sommerY:
            res += sommerY+1
        if billyY < sommerY:
            res += -1-billyY
        if billyX > sommerX:
            res += 1+sommerX
        if billyX < sommerX:
            res += -1-billyX
        colPayoff.append(res)
    billyPayoffTable.append(colPayoff)
print("payoff table for billy")
for b in bs:
    for s in ss:
        print(billyPayoffTable[s][b], '\t', end="")
    print('')


def getBillyPayoff(bvars, svars):
    res = 0
    for s in range(len(svars)):
        for b in range(len(bvars)):
            res += bvars[b] * svars[s] * billyPayoffTable[s][b]
    return res


# solve Nash equilibrium for billy
solver = pywraplp.Solver(
    'Solver', pywraplp.Solver.CLP_LINEAR_PROGRAMMING)

billyvars = []
for b in bs:
    billyvars.append(solver.NumVar(0, 1, 'billy%d' % (b)))

solver.Add(solver.Sum(billyvars) == 1)

for s in range(len(ss)-1):
    solver.Add(solver.Sum([billyPayoffTable[s][b] * billyvars[b] for b in bs])
               == solver.Sum([billyPayoffTable[s+1][b] * billyvars[b] for b in bs]))
solver.Solve()
sum = 0
bvars = []
for v in solver.variables():
    print(v.name(), ':', v.solution_value())
    bvars.append(v.solution_value())
    sum += v.solution_value()
# verify solution...
print(sum)
print(getBillyPayoff(bvars, [1, 0, 0, 0, 0, 0, 0]))
print(getBillyPayoff(bvars, [0, 1, 0, 0, 0, 0, 0]))
print(getBillyPayoff(bvars, [0, 0, 1, 0, 0, 0, 0]))
print(getBillyPayoff(bvars, [0, 0, 0, 1, 0, 0, 0]))
print(getBillyPayoff(bvars, [0, 0, 0, 0, 1, 0, 0]))
print(getBillyPayoff(bvars, [0, 0, 0, 0, 0, 1, 0]))
print(getBillyPayoff(bvars, [0, 0, 0, 0, 0, 0, 1]))

print(getBillyPayoff(bvars, [.1, .1, .1, .1, .1, .1, .4]))
print(getBillyPayoff(bvars, [.5, .3, .1, .1, 0, 0, 0]))
print(getBillyPayoff(bvars, [.1, .25, .15, .1, .1, .1, .2]))


# solve Nash equilibrium for Sommer
solver = pywraplp.Solver(
    'Solver', pywraplp.Solver.CLP_LINEAR_PROGRAMMING)

sommarvars = []
for s in ss:
    sommarvars.append(solver.NumVar(0, 1, 'sommer%d' % (s)))

solver.Add(solver.Sum(sommarvars) == 1)


# exclude options with 0 value from billy's result
billyOptions = [0, 2, 4, 5]  # 5, 7, 9]
solver.Add(solver.Sum([billyPayoffTable[s][0] * sommarvars[s] for s in ss])
           == solver.Sum([billyPayoffTable[s][2] * sommarvars[s] for s in ss]))
solver.Add(solver.Sum([billyPayoffTable[s][7] * sommarvars[s] for s in ss])
           == solver.Sum([billyPayoffTable[s][9] * sommarvars[s] for s in ss]))

solver.Add(solver.Sum([billyPayoffTable[s][0] * sommarvars[s] for s in ss])
           == solver.Sum([billyPayoffTable[s][4] * sommarvars[s] for s in ss]))
# solver.Add(solver.Sum([billyPayoffTable[s][7] * sommarvars[s] for s in ss])
#            == solver.Sum([billyPayoffTable[s][9] * sommarvars[s] for s in ss]))
solver.Solve()
sum = 0
svars = []
for v in solver.variables():
    print(v.name(), ':', v.solution_value())
    sum += v.solution_value()
    svars.append(v.solution_value())
# svars.append(0.011235955056179782/2)
# svars.append(0)
# svars.append(0.6853932584269663/2)
# svars.append(0.3033707865168539/2)
# svars.append(0.3033707865168539/2)
# svars.append(0.6853932584269663/2)
# svars.append(0)
# svars.append(0.011235955056179782/2)

# verify solution...
print(sum)
print(-getBillyPayoff([1, 0, 0, 0, 0, 0, 0, 0, 0, 0], svars))
print(-getBillyPayoff([0, 0, 1, 0, 0, 0, 0, 0, 0, 0], svars))
print(-getBillyPayoff([0, 0, 0, 0, 1, 0, 0, 0, 0, 0], svars))
print(-getBillyPayoff([0, 0, 0, 0, 0, 1, 0, 0, 0, 0], svars))
print(-getBillyPayoff([0, 0, 0, 0, 0, 0, 0, 1, 0, 0], svars))
print(-getBillyPayoff([0, 0, 0, 0, 0, 0, 0, 0, 0, 1], svars))
