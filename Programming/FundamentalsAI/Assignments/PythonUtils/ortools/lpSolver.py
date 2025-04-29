from ortools.linear_solver import pywraplp

'''
Components of a LP Problem
1. Objective function that composed of variables
2. Constraints on the variables
'''

solver = pywraplp.Solver.CreateSolver('GLOP')

c11 = solver.IntVar(0, 1, "a")
c12 = solver.IntVar(0, 1, "a")
c13 = solver.IntVar(0, 1, "a")
c14 = solver.IntVar(0, 1, "a")
c15 = solver.IntVar(0, 1, "a")
c16 = solver.IntVar(0, 1, "a")
c17 = solver.IntVar(0, 1, "a")
c18 = solver.IntVar(0, 1, "a")
c19 = solver.IntVar(0, 1, "a")

c21 = solver.IntVar(0, 1, "a")
c22 = solver.IntVar(0, 1, "a")
c23 = solver.IntVar(0, 1, "a")
c24 = solver.IntVar(0, 1, "a")
c25 = solver.IntVar(0, 1, "a")
c26 = solver.IntVar(0, 1, "a")
c27 = solver.IntVar(0, 1, "a")
c28 = solver.IntVar(0, 1, "a")
c29 = solver.IntVar(0, 1, "a")

c31 = solver.IntVar(0, 1, "a")
c32 = solver.IntVar(0, 1, "a")
c33 = solver.IntVar(0, 1, "a")
c34 = solver.IntVar(0, 1, "a")
c35 = solver.IntVar(0, 1, "a")
c36 = solver.IntVar(0, 1, "a")
c37 = solver.IntVar(0, 1, "a")
c38 = solver.IntVar(0, 1, "a")
c39 = solver.IntVar(0, 1, "a")


c41 = solver.IntVar(0, 1, "a")
c42 = solver.IntVar(0, 1, "a")
c43 = solver.IntVar(0, 1, "a")
c44 = solver.IntVar(0, 1, "a")
c45 = solver.IntVar(0, 1, "a")
c46 = solver.IntVar(0, 1, "a")
c47 = solver.IntVar(0, 1, "a")
c48 = solver.IntVar(0, 1, "a")
c49 = solver.IntVar(0, 1, "a")

c51 = solver.IntVar(0, 1, "a")
c52 = solver.IntVar(0, 1, "a")
c53 = solver.IntVar(0, 1, "a")
c54 = solver.IntVar(0, 1, "a")
c55 = solver.IntVar(0, 1, "a")
c56 = solver.IntVar(0, 1, "a")
c57 = solver.IntVar(0, 1, "a")
c58 = solver.IntVar(0, 1, "a")
c59 = solver.IntVar(0, 1, "a")

c61 = solver.IntVar(0, 1, "a")
c62 = solver.IntVar(0, 1, "a")
c63 = solver.IntVar(0, 1, "a")
c64 = solver.IntVar(0, 1, "a")
c65 = solver.IntVar(0, 1, "a")
c66 = solver.IntVar(0, 1, "a")
c67 = solver.IntVar(0, 1, "a")
c68 = solver.IntVar(0, 1, "a")
c69 = solver.IntVar(0, 1, "a")

solver.Add(c11+c12+c13+c14+c15+c16+c17+c18+c19 == 3)
solver.Add(c21+c22+c23+c24+c25+c26+c27+c28+c29 == 3)
solver.Add(c31+c32+c33+c34+c35+c36+c37+c38+c39 == 3)
solver.Add(c41+c42+c43+c44+c45+c46+c47+c48+c49 == 3)
solver.Add(c51+c52+c53+c54+c55+c56+c57+c58+c59 == 3)
solver.Add(c61+c62+c63+c64+c65+c66+c67+c68+c69 == 3)


solver.Add(c11+c21+c31+c41+c51+c61 == 2)
solver.Add(c12+c22+c32+c42+c52+c62 == 2)
solver.Add(c13+c23+c33+c43+c53+c63 == 2)
solver.Add(c14+c24+c34+c44+c54+c64 == 2)
solver.Add(c15+c25+c35+c45+c55+c65 == 2)
solver.Add(c16+c26+c36+c46+c56+c66 == 2)
solver.Add(c17+c27+c37+c47+c57+c67 == 2)
solver.Add(c18+c28+c38+c48+c58+c68 == 2)
solver.Add(c19+c29+c39+c49+c59+c69 == 2)

solver.Maximize(2*c11+4*c12+1*c13+8*c14+6*c15+9*c16+3*c17+7*c18+5*c19 +
                7*c21+2*c22 + 3*c23 + 1*c24 + 9*c25 + 4*c26 + 5*c27 + 6*c28 + 8*c29 +
                1*c31 + 5*c32 + 2*c33 + 8*c34 + 6*c35 + 9*c36 + 7*c37 + 4*c38 + 3*c39 +
                6*c41 + 7*c42 + 3*c43 + 1*c44 + 8*c45 + 9*c46 + 2*c47 + 5*c48 + 4*c49 +
                7*c51 + 1*c52 + 6*c53 + 3*c54 + 9*c55 + 4*c56 + 8*c57 + 5*c58 + 2*c59 +
                3*c61 + 1*c62 + 6*c63 + 4*c64 + 8*c65 + 9*c66 + 2*c67 + 5*c68 + 7*c69)
# solver.Maximize(40*x + 30*y)


status = solver.Solve()
if status == pywraplp.Solver.OPTIMAL:
    print('Solution:')
    print('Objective value =', solver.Objective().Value())
    print(c11.solution_value())
    print(c12.solution_value())
    print(c13.solution_value())
    print(c14.solution_value())
    print(c15.solution_value())
    print(c16.solution_value())

else:
    print('The problem does not have an optimal solution.')
