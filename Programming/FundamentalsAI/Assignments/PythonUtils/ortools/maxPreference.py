from ortools.linear_solver import pywraplp
import pandas

solver = pywraplp.Solver('Max Preference',
                         pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

filePath = "D:\\Projects\\ObsidianNotes\\NEU_Courses_Repo\\FundamentalsAI\\Assignments\\Problemsets\\Mid1\\InputCourseSynthesis.xlsx"
sheetName = "Data"
data = pandas.read_excel(filePath, sheet_name=sheetName, header=None)
# print(data[0][0])
print(data[1][1])
print(data[2][4])
allVolunteers = range(100)
allDays = range(100)
X = {}
for v in allVolunteers:
    for d in allDays:
        X[v, d] = solver.BoolVar("%d in day %d" % (v, d))

for v in allVolunteers:
    solver.Add(solver.Sum([X[v, d]for d in allDays]) == 1)

for d in allDays:
    solver.Add(solver.Sum([X[v, d]for v in allVolunteers]) == 1)

# for v in allVolunteers:
#     for d in allDays:
#         solver.Add(X[v, d] == X[d, v])

solver.Maximize(solver.Sum([X[v, d]*data[v+1][d+1]
                for v in allVolunteers for d in allDays]))

solver.Solve()
print(solver.Objective().Value())

# data = [
#     [60, 80, 90, 70],
#     [80, 90, 100, 80],
#     [60, 50, 90, 50],
#     [70, 60, 50, 80],
# ]

# alldays = range(4)
# allPeople = range(4)
# X = {}
# for v in allPeople:
#     for d in alldays:
#         X[v, d] = solver.BoolVar("%d in day %d" % (v, d))
# for v in allPeople:
#     solver.Add(solver.Sum([X[v, d]for d in alldays]) == 1)
# for d in alldays:
#     solver.Add(solver.Sum([X[v, d]for v in allPeople]) == 1)

# solver.Maximize(solver.Sum([X[v, d]*data[v][d]
#                 for v in allPeople for d in alldays]))

# solver.Solve()
# print(solver.Objective().Value())
# for v in solver.variables():
#     if(v.solution_value() == 1):
#         print(v.name())
