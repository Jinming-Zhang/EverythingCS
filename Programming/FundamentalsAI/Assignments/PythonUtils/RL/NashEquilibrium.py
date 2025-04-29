from ortools.linear_solver import pywraplp
# equilibrium for bill
solver = pywraplp.Solver(
    'Solver', pywraplp.Solver.CLP_LINEAR_PROGRAMMING)
a = solver.NumVar(0, 1, 'a')
b = solver.NumVar(0, 1, 'b')
c = solver.NumVar(0, 1, 'c')
d = solver.NumVar(0, 1, 'd')
e = solver.NumVar(0, 1, 'e')

solver.Add(a+b+c+d+e == 1)
solver.Add(4*a+b-2*c-d == 2*a+3*b+2*c+e)
solver.Add(2*a+3*b+2*c+e == a+2*c+3*d+2*e)
solver.Add(a+2*c+3*d+2*e == -b-2*c+d+4*e)
solver.Solve()
for v in solver.variables():
    print(v.name(), ': ', v.solution_value())

a = a.solution_value()
b = b.solution_value()
c = c.solution_value()
d = d.solution_value()
e = e.solution_value()


def printBillyPayoff(p, q, r, s):
    bpayoffCol1 = 4*a*p+1*b*p-2*c*p-1*d*p+0*e*p
    bpayoffCol2 = 2*a*q+3*b*q+2*c*q+0*d*q+1*e*q
    bpayoffCol3 = 1*a*r+0*b*r+2*c*r+3*d*r+2*e*r
    bpayoffCol4 = 0*a*s-1*b*s-2*c*s+1*d*s+4*e*s

    bpayoff = bpayoffCol1 + bpayoffCol2 + bpayoffCol3 + bpayoffCol4
    print(bpayoff)


printBillyPayoff(1,  0,  0,  0)
printBillyPayoff(0,  1,  0,  0)
printBillyPayoff(0,  0,  1,  0)
printBillyPayoff(0,  0,  0,  1)
printBillyPayoff(.2,  .3,  .1,  .4)
printBillyPayoff(.1,  .2,  .3,  .4)
printBillyPayoff(.5,  0,  .2,  .3)

# solver2 = pywraplp.Solver(
#     'Solver', pywraplp.Solver.CLP_LINEAR_PROGRAMMING)
# p = solver2.NumVar(0, 1, 'p')
# q = solver2.NumVar(0, 1, 'q')
# r = solver2.NumVar(0, 1, 'r')
# s = solver2.NumVar(0, 1, 's')

# solver2.Add(p+q+r+s == 1)
# solver2.Add(-4*p-2*q-r == -p-3*q-s)
# solver2.Add(-p-3*q-s == 2*p-2*q-2*r+2*s)
# solver2.Add(2*p-2*q-2*r+2*s == p-3*r-s)
# solver2.Add(p-3*r-s == -q-2*r-4*s)
# solver2.Solve()
# for v in solver2.variables():
#     print(v.name(), ': ', v.solution_value())

p =1.0/18
q = 4.0/9
r = q
s = p


def printSommerPayoff(a, b, c, d, e):
    sPayoffCol1 = -(4*a*p+1*b*p-2*c*p-1*d*p+0*e*p)
    sPayoffCol2 = -(2*a*q+3*b*q+2*c*q+0*d*q+1*e*q)
    sPayoffCol3 = -(1*a*r+0*b*r+2*c*r+3*d*r+2*e*r)
    sPayoffCol4 = -(0*a*s-1*b*s-2*c*s+1*d*s+4*e*s)

    sPayoff = sPayoffCol1 + sPayoffCol2+sPayoffCol3+sPayoffCol4
    print(sPayoff)


print("sommer payoff")
printSommerPayoff(.4, 0, .3, 0, .3)
printSommerPayoff(.7, 0, .1, 0, .2)
printSommerPayoff(1, 0, 0, 0, 0)
printSommerPayoff(0, 0, 1, 0, 0)
printSommerPayoff(0, 0, 0, 0, 1)


# def pn(n):
#     res = 0
#     for i in range(1, n):
#         if i == n-1:
#             res += pow(-0.5, i) * 0.5
#         else:
#             res += pow(-0.5, i)
#     res += 1
#     return res


# print(pn(2))
# print(pn(3))
# print(pn(4))
# print(pn(5))
# print(pn(6))
# print(pn(7))
# print(pn(8))
# print(pn(1000000000))
