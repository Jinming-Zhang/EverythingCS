from ortools.sat.python import cp_model
import time

StartTime = time.process_time()
Happy = cp_model.CpModel()

# Define our variables: there are 15 students, 5 groups, 7 days
allStudents = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
allGroups = [1, 2, 3, 4, 5]
allDays = [1, 2, 3, 4, 5, 6, 7]
X = {}
for s in allStudents:
    for g in allGroups:
        for d in allDays:
            X[s, g, d] = Happy.NewIntVar(
                0, 1, "Student %d in group %d on day %d" % (s, g, d))

# on each day, every student is assigned to 1 group
for d in allDays:
    for s in allStudents:
        Happy.Add(sum([X[s, g, d]for g in allGroups]) == 1)

# on each day, every group contains exactly three students
for d in allDays:
    for g in allGroups:
        Happy.Add(sum([X[s, g, d]for s in allStudents]) == 3)

# student si and sj must be in the same group exactly once
for si in allStudents:
    for sj in allStudents:
        if si != sj:
            for dk in allDays:
                for dl in allDays:
                    if dk != dl:
                        for g in allGroups:
                            Happy.Add(
                                sum([X[si, g, dk], X[sj, g, dk], X[si, g, dl], X[sj, g, dl]]) != 4)

solver = cp_model.CpSolver()
status = solver.Solve(Happy)
totalTime = time.process_time() - StartTime
print("Total Time was", totalTime, "seconds")
print("")
for d in allDays:
    for g in allGroups:
        for s in allStudents:
            if solver.Value(X[s, g, d]) == 1:
                print("Day", d, "Group", g, "Student", s)
