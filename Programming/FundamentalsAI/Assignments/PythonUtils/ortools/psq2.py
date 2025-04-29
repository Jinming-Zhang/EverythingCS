#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
from ortools.linear_solver import pywraplp

solver = pywraplp.Solver('Timetabling Problem',
                         pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)


h1, h2, h3, h4, h5 = range(5)
allHouses = range(5)
houseDic = {}
houseDic[0] = "h1"
houseDic[1] = "h2"
houseDic[2] = "h3"
houseDic[3] = "h4"
houseDic[4] = "h5"
billy, david,  sommer, jinhao, xiaof = range(5)
allStudents = range(5)
studentDic = {}
studentDic[0] = "billy"
studentDic[1] = "david"
studentDic[2] = "sommer"
studentDic[3] = "jinhao"
studentDic[4] = "xiaofeng"
pink, orange, blue, red, purple = range(5)
allColors = range(5)
colorDic = {}
colorDic[0] = 'pink'
colorDic[1] = 'orange'
colorDic[2] = 'blue'
colorDic[3] = 'red'
colorDic[4] = 'purple'
steak, sushi, samosa, salad, sandwitch = range(5)
allFoods = range(5)
foodDic = {}
foodDic[0] = 'steak'
foodDic[1] = 'sushi'
foodDic[2] = 'samosa'
foodDic[3] = 'salad'
foodDic[4] = 'sandwitch'
basketball, vollayball, baseball, soccor, hockey = range(5)
allSports = range(5)
sportDic = {}
sportDic[0] = 'basketball'
sportDic[1] = 'vollayball'
sportDic[2] = 'baseball'
sportDic[3] = 'soccor'
sportDic[4] = 'hockey'
kettyperry, jz, jb, kw, ts = range(5)
allSingers = range(5)
singerDic = {}
singerDic[0] = 'kp'
singerDic[1] = 'jz'
singerDic[2] = 'jb'
singerDic[3] = 'kw'
singerDic[4] = 'ts'

X = {}
for h in allHouses:
    for c in allColors:
        for s in allStudents:
            for f in allFoods:
                for sp in allSports:
                    for sing in allSingers:
                        X[h, c, s, f, sp, sing] = solver.BoolVar(
                            'X[%s %s %s %s %s %s]' % (houseDic[h], colorDic[c], studentDic[s], foodDic[f], sportDic[sp], singerDic[sing]))

# each house has one solution
for h in allHouses:
    solver.Add(solver.Sum([X[h, c, s, f, sp, sing]
               for c in allColors for s in allStudents for f in allFoods for sp in allSports for sing in allSingers]) == 1)

for c in allColors:
    solver.Add(solver.Sum([X[h, c, s, f, sp, sing]
               for h in allHouses for s in allStudents for f in allFoods for sp in allSports for sing in allSingers]) == 1)
for s in allStudents:
    solver.Add(solver.Sum([X[h, c, s, f, sp, sing]
               for h in allHouses for c in allColors for f in allFoods for sp in allSports for sing in allSingers]) == 1)
for f in allFoods:
    solver.Add(solver.Sum([X[h, c, s, f, sp, sing]
               for h in allHouses for c in allColors for s in allStudents for sp in allSports for sing in allSingers]) == 1)
for sp in allSports:
    solver.Add(solver.Sum([X[h, c, s, f, sp, sing]
               for h in allHouses for c in allColors for s in allStudents for f in allFoods for sing in allSingers]) == 1)
for sing in allSingers:
    solver.Add(solver.Sum([X[h, c, s, f, sp, sing]
               for h in allHouses for c in allColors for s in allStudents for f in allFoods for sp in allSports]) == 1)
# billy lives in house 1
# vars = []
# vars = [X[h1, c, billy, f, sp, sing]
#         for c in allColors for f in allFoods for sp in allSports for sing in allSingers]
# vars2 = [x for x in vars]
# solver.Add(solver.Sum(vars2) == 1)

solver.Add(solver.Sum([X[h1, c, billy, f, sp, sing]
           for c in allColors for f in allFoods for sp in allSports for sing in allSingers]) == 1)

# pink house is left of red house

# student play basketball has a neighbour eats steak for lunch
solver.Add(solver.Sum([X[h, c, s, steak, basketball, sing]
           for h in allHouses for c in allColors for s in allStudents for sing in allSingers]) == 0)
# vars = []
# for h in range(1, 4):
#     bbs = [X[h, c, s, f, basketball, sing]
#            for c in allColors for s in allStudents for f in allFoods for sing in allSingers]
#     left = [X[h-1, c, s, steak, sp, sing]
#             for c in allColors for s in allStudents for sp in allSports for sing in allSingers]
#     right = [X[h+1, c, s, steak, sp, sing]
#              for c in allColors for s in allStudents for sp in allSports for sing in allSingers]
#     for x in bbs:
#         vars.append(x)
#     for x in left:
#         vars.append(x)
#     for x in right:
#         vars.append(x)
#     solver.Add(solver.Sum(vars) == 2)
# katy perry is a students favourite singer
solver.Add(solver.Sum([X[h, c, s, f, sp, kettyperry]
           for h in allHouses for c in allColors for s in allStudents for f in allFoods for sp in allSports]) == 1)
# david's finger is jz
solver.Add(solver.Sum([X[h, c, david, f, sp, jz]
           for h in allHouses for c in allColors for f in allFoods for sp in allSports]) == 1)
# billy lives next to orange house
solver.Add(solver.Sum([X[h2, orange, s, f, sp, sing]
           for s in allStudents for f in allFoods for sp in allSports for sing in allSingers]) == 1)
# house 3 eats sushi
solver.Add(solver.Sum(X[h3, c, s, sushi, sp, sing]
           for c in allColors for s in allStudents for sp in allSports for sing in allSingers) == 1)
# purple house play volleyball
solver.Add(solver.Sum([X[h, purple, s, f, vollayball, sing]
           for h in allHouses for s in allStudents for f in allFoods for sing in allSingers]) == 1)
# basketball lives next to tylor swift
solver.Add(solver.Sum([X[h, c, s, f, basketball, ts]
           for h in allHouses for c in allColors for s in allStudents for f in allFoods]) == 0)

# if in basketball in h1
solver.Add(solver.Sum([X[h1, c, s, f, basketball, sing]for c in allColors for s in allStudents for f in allFoods for sing in allSingers] +
                      [X[h3, c, s, f, sp, ts]for c in allColors for s in allStudents for f in allFoods for sp in allSports]) <= 1)
# basketball x ts
solver.Add(solver.Sum([X[h1, c, s, f, basketball, sing]for c in allColors for s in allStudents for f in allFoods for sing in allSingers] +
                      [X[h4, c, s, f, sp, ts]for c in allColors for s in allStudents for f in allFoods for sp in allSports]) <= 1)

solver.Add(solver.Sum([X[h1, c, s, f, basketball, sing]for c in allColors for s in allStudents for f in allFoods for sing in allSingers] +
                      [X[h5, c, s, f, sp, ts]for c in allColors for s in allStudents for f in allFoods for sp in allSports]) <= 1)

# basketball x steak
solver.Add(solver.Sum([X[h1, c, s, f, basketball, sing]for c in allColors for s in allStudents for f in allFoods for sing in allSingers] +
                      [X[h3, c, s, steak, sp, sing]for c in allColors for s in allStudents for sing in allSingers for sp in allSports]) <= 1)

solver.Add(solver.Sum([X[h1, c, s, f, basketball, sing]for c in allColors for s in allStudents for f in allFoods for sing in allSingers] +
                      [X[h4, c, s, steak, sp, sing]for c in allColors for s in allStudents for sing in allSingers for sp in allSports]) <= 1)
solver.Add(solver.Sum([X[h1, c, s, f, basketball, sing]for c in allColors for s in allStudents for f in allFoods for sing in allSingers] +
                      [X[h5, c, s, steak, sp, sing]for c in allColors for s in allStudents for sing in allSingers for sp in allSports]) <= 1)
# if basketball in h2

solver.Add(solver.Sum([X[h2, c, s, f, basketball, sing]for c in allColors for s in allStudents for f in allFoods for sing in allSingers] +
                      [X[h4, c, s, f, sp, ts]for c in allColors for s in allStudents for f in allFoods for sp in allSports]) <= 1)

solver.Add(solver.Sum([X[h2, c, s, f, basketball, sing]for c in allColors for s in allStudents for f in allFoods for sing in allSingers] +
                      [X[h5, c, s, f, sp, ts]for c in allColors for s in allStudents for f in allFoods for sp in allSports]) <= 1)
# ts
solver.Add(solver.Sum([X[h2, c, s, f, basketball, sing]for c in allColors for s in allStudents for f in allFoods for sing in allSingers] +
                      [X[h4, c, s, steak, sp, sing]for c in allColors for s in allStudents for sing in allSingers for sp in allSports]) <= 1)
solver.Add(solver.Sum([X[h2, c, s, f, basketball, sing]for c in allColors for s in allStudents for f in allFoods for sing in allSingers] +
                      [X[h5, c, s, steak, sp, sing]for c in allColors for s in allStudents for sing in allSingers for sp in allSports]) <= 1)
# if basket ball in h3
solver.Add(solver.Sum([X[h3, c, s, f, basketball, sing]for c in allColors for s in allStudents for f in allFoods for sing in allSingers] +
                      [X[h1, c, s, f, sp, ts]for c in allColors for s in allStudents for f in allFoods for sp in allSports]) <= 1)
solver.Add(solver.Sum([X[h3, c, s, f, basketball, sing]for c in allColors for s in allStudents for f in allFoods for sing in allSingers] +
                      [X[h5, c, s, f, sp, ts]for c in allColors for s in allStudents for f in allFoods for sp in allSports]) <= 1)
# ts
solver.Add(solver.Sum([X[h3, c, s, f, basketball, sing]for c in allColors for s in allStudents for f in allFoods for sing in allSingers] +
                      [X[h1, c, s, steak, sp, sing]for c in allColors for s in allStudents for sing in allSingers for sp in allSports]) <= 1)
solver.Add(solver.Sum([X[h3, c, s, f, basketball, sing]for c in allColors for s in allStudents for f in allFoods for sing in allSingers] +
                      [X[h5, c, s, steak, sp, sing]for c in allColors for s in allStudents for sing in allSingers for sp in allSports]) <= 1)
# if basketball in h4
solver.Add(solver.Sum([X[h4, c, s, f, basketball, sing]for c in allColors for s in allStudents for f in allFoods for sing in allSingers] +
                      [X[h1, c, s, f, sp, ts]for c in allColors for s in allStudents for f in allFoods for sp in allSports]) <= 1)
solver.Add(solver.Sum([X[h4, c, s, f, basketball, sing]for c in allColors for s in allStudents for f in allFoods for sing in allSingers] +
                      [X[h2, c, s, f, sp, ts]for c in allColors for s in allStudents for f in allFoods for sp in allSports]) <= 1)

# ts
solver.Add(solver.Sum([X[h4, c, s, f, basketball, sing]for c in allColors for s in allStudents for f in allFoods for sing in allSingers] +
                      [X[h1, c, s, steak, sp, sing]for c in allColors for s in allStudents for sing in allSingers for sp in allSports]) <= 1)
solver.Add(solver.Sum([X[h4, c, s, f, basketball, sing]for c in allColors for s in allStudents for f in allFoods for sing in allSingers] +
                      [X[h2, c, s, steak, sp, sing]for c in allColors for s in allStudents for sing in allSingers for sp in allSports]) <= 1)
# if basketball in h5
solver.Add(solver.Sum([X[h5, c, s, f, basketball, sing]for c in allColors for s in allStudents for f in allFoods for sing in allSingers] +
                      [X[h1, c, s, f, sp, ts]for c in allColors for s in allStudents for f in allFoods for sp in allSports]) <= 1)
solver.Add(solver.Sum([X[h5, c, s, f, basketball, sing]for c in allColors for s in allStudents for f in allFoods for sing in allSingers] +
                      [X[h2, c, s, f, sp, ts]for c in allColors for s in allStudents for f in allFoods for sp in allSports]) <= 1)
solver.Add(solver.Sum([X[h5, c, s, f, basketball, sing]for c in allColors for s in allStudents for f in allFoods for sing in allSingers] +
                      [X[h3, c, s, f, sp, ts]for c in allColors for s in allStudents for f in allFoods for sp in allSports]) <= 1)

# steak
solver.Add(solver.Sum([X[h5, c, s, f, basketball, sing]for c in allColors for s in allStudents for f in allFoods for sing in allSingers] +
                      [X[h1, c, s, steak, sp, sing]for c in allColors for s in allStudents for sing in allSingers for sp in allSports]) <= 1)
solver.Add(solver.Sum([X[h5, c, s, f, basketball, sing]for c in allColors for s in allStudents for f in allFoods for sing in allSingers] +
                      [X[h2, c, s, steak, sp, sing]for c in allColors for s in allStudents for sing in allSingers for sp in allSports]) <= 1)
solver.Add(solver.Sum([X[h5, c, s, f, basketball, sing]for c in allColors for s in allStudents for f in allFoods for sing in allSingers] +
                      [X[h3, c, s, steak, sp, sing]for c in allColors for s in allStudents for sing in allSingers for sp in allSports]) <= 1)

# kw x volly
solver.Add(solver.Sum([X[h1, c, s, f, sp, kw]for c in allColors for s in allStudents for f in allFoods for sp in allSports] +
                      [X[h3, c, s, f, vollayball, sing]for c in allColors for s in allStudents for sing in allSingers for f in allFoods]) <= 1)
solver.Add(solver.Sum([X[h1, c, s, f, sp, kw]for c in allColors for s in allStudents for f in allFoods for sp in allSports] +
                      [X[h4, c, s, f, vollayball, sing]for c in allColors for s in allStudents for sing in allSingers for f in allFoods]) <= 1)
solver.Add(solver.Sum([X[h1, c, s, f, sp, kw]for c in allColors for s in allStudents for f in allFoods for sp in allSports] +
                      [X[h5, c, s, f, vollayball, sing]for c in allColors for s in allStudents for sing in allSingers for f in allFoods]) <= 1)
solver.Add(solver.Sum([X[h2, c, s, f, sp, kw]for c in allColors for s in allStudents for f in allFoods for sp in allSports] +
                      [X[h4, c, s, f, vollayball, sing]for c in allColors for s in allStudents for sing in allSingers for f in allFoods]) <= 1)
solver.Add(solver.Sum([X[h2, c, s, f, sp, kw]for c in allColors for s in allStudents for f in allFoods for sp in allSports] +
                      [X[h5, c, s, f, vollayball, sing]for c in allColors for s in allStudents for sing in allSingers for f in allFoods]) <= 1)

# 3
solver.Add(solver.Sum([X[h3, c, s, f, sp, kw]for c in allColors for s in allStudents for f in allFoods for sp in allSports] +
                      [X[h1, c, s, f, vollayball, sing]for c in allColors for s in allStudents for sing in allSingers for f in allFoods]) <= 1)

solver.Add(solver.Sum([X[h3, c, s, f, sp, kw]for c in allColors for s in allStudents for f in allFoods for sp in allSports] +
                      [X[h5, c, s, f, vollayball, sing]for c in allColors for s in allStudents for sing in allSingers for f in allFoods]) <= 1)
# 4
solver.Add(solver.Sum([X[h4, c, s, f, sp, kw]for c in allColors for s in allStudents for f in allFoods for sp in allSports] +
                      [X[h1, c, s, f, vollayball, sing]for c in allColors for s in allStudents for sing in allSingers for f in allFoods]) <= 1)
solver.Add(solver.Sum([X[h4, c, s, f, sp, kw]for c in allColors for s in allStudents for f in allFoods for sp in allSports] +
                      [X[h2, c, s, f, vollayball, sing]for c in allColors for s in allStudents for sing in allSingers for f in allFoods]) <= 1)
# 5

solver.Add(solver.Sum([X[h5, c, s, f, sp, kw]for c in allColors for s in allStudents for f in allFoods for sp in allSports] +
                      [X[h1, c, s, f, vollayball, sing]for c in allColors for s in allStudents for sing in allSingers for f in allFoods]) <= 1)
solver.Add(solver.Sum([X[h5, c, s, f, sp, kw]for c in allColors for s in allStudents for f in allFoods for sp in allSports] +
                      [X[h2, c, s, f, vollayball, sing]for c in allColors for s in allStudents for sing in allSingers for f in allFoods]) <= 1)
solver.Add(solver.Sum([X[h5, c, s, f, sp, kw]for c in allColors for s in allStudents for f in allFoods for sp in allSports] +
                      [X[h3, c, s, f, vollayball, sing]for c in allColors for s in allStudents for sing in allSingers for f in allFoods]) <= 1)
# for h in range(1, 4):
#     liveHere = solver.BoolVar("")
#     isLeft = solver.BoolVar("")
#     isRight = solver.BoolVar("")
#     bbs = [X[h, c, s, f, basketball, sing]
#            for c in allColors for s in allStudents for f in allFoods for sing in allSingers]
#     left = [X[h-1, c, s, f, sp, ts]
#             for c in allColors for s in allStudents for f in allFoods for sp in allSports]
#     right = [X[h+1, c, s, f, sp, ts]
#              for c in allColors for s in allStudents for f in allFoods for sp in allSports]
#     liveHereLeft = bbs+left + [liveHere, isLeft]
#     liveHereRight = bbs+right + [liveHere, isRight]
#     # solver.Add(solver.Sum(liveHereLeft) == 4)
#     solver.Add(solver.Sum(liveHereRight) == 4)
# baseball eats samosa
solver.Add(solver.Sum([X[h, c, s, samosa, baseball, sing]
           for h in allHouses for c in allColors for s in allStudents for sing in allSingers]) == 1)
# sommoer play soccer
solver.Add(solver.Sum([X[h, c, sommer, f, soccor, sing]
           for h in allHouses for c in allColors for f in allFoods for sing in allSingers]) == 1)
# jinhao lives in blue
solver.Add(solver.Sum([X[h, blue, jinhao, f, sp, sing]
           for h in allHouses for f in allFoods for sp in allSports for sing in allSingers]) == 1)
# xiaofeng eats salad
solver.Add(solver.Sum([X[h, c, xiaof, salad, sp, sing]
           for h in allHouses for c in allColors for sp in allSports for sing in allSingers]) == 1)
# hockey like jb
solver.Add(solver.Sum([X[h, c, s, f, hockey, jb]
           for h in allHouses for c in allColors for s in allStudents for f in allFoods]) == 1)
# pink eat sandwitch
solver.Add(solver.Sum([X[h, pink, s, sandwitch, sp, sing]
           for h in allHouses for s in allStudents for sp in allSports for sing in allSingers]) == 1)
# vollay next to kw
solver.Add(solver.Sum([X[h, c, s, f, vollayball, kw]
           for h in allHouses for c in allColors for s in allStudents for f in allFoods]) == 0)

solver.Add(solver.Sum([X[h, c, s, f, sp, sing]
           for h in allHouses for c in allColors for s in allStudents for f in allFoods for sp in allSports for sing in allSingers]) == 5)


solver.Solve()
for vari in solver.variables():
    if vari.solution_value() == 1:
        print(vari.name())
# billy = solver.IntVar(1, 6, "billy")
# david = solver.IntVar(1, 6, "david")
# sommer = solver.IntVar(1, 6, "sommer")
# jinhao = solver.IntVar(1, 6, "jinhao")
# xiaof = solver.IntVar(1, 6, "xiaofeng")

# pink = solver.IntVar(1, 6, 'pink')
# orange = solver.IntVar(1, 6, 'orange')
# blue = solver.IntVar(1, 6, 'blue')
# red = solver.IntVar(1, 6, 'red')
# purple = solver.IntVar(1, 6, 'purple')

# steak = solver.IntVar(1, 6, 'steak')
# sushi = solver.IntVar(1, 6, 'sushi')
# samosa = solver.IntVar(1, 6, 'samosa')
# salad = solver.IntVar(1, 6, 'salad')
# sandwitch = solver.IntVar(1, 6, 'sandwitch')

# basketball = solver.IntVar(1, 6, 'basketball')
# vollayball = solver.IntVar(1, 6, 'vollayball')
# baseball = solver.IntVar(1, 6, 'baseball')
# soccor = solver.IntVar(1, 6, 'soccor')
# hockey = solver.IntVar(1, 6, 'hockey')

# kettyperry = solver.IntVar(1, 6, 'kettyperry')
# jz = solver.IntVar(1, 6, 'jz')
# jb = solver.IntVar(1, 6, 'jb')
# kw = solver.IntVar(1, 6, 'kw')
# ts = solver.IntVar(1, 6, 'ts')

# solver.Add(billy == 1)
# solver.Add(pink <= red)
# solver.Add(basketball == steak+1 or basketball == steak - 1)
# # 5
# solver.Add(david == jz)
# # 6
# # solver.Add(billy == orange + 1 or billy == orange-1)
# # 7
# solver.Add(sushi == 3)
# # 8
# solver.Add(purple == vollayball)
# # 9
# # solver.Add(basketball == ts+1 or basketball == ts-1)
# # 10
# solver.Add(baseball == samosa)
# # 11
# solver.Add(sommer == soccor)
# # 12
# solver.Add(jinhao == blue)
# # 13
# solver.Add(xiaof == salad)
# # 14
# solver.Add(jb == hockey)
# # 15
# solver.Add(pink == sandwitch)
# # 16
# # solver.Add(kw == vollayball+1 or kw == vollayball-1)

# solver.Solve()
# for vari in solver.variables():
#     print(vari.name(), '->', vari.solution_value())
# In[2]:
# allStudents = range(5)
# allHouses = range(5)
# allColors = range(5)
# allFoods = range(5)
# allArtists = range(5)
# allSports = range(5)


# start_time = time.time()

# # Define our binary variables for the students and teachers
# X = {}
# for s in allStudents:
#     for h in allHouses:
#         for sp in allSports:
#             for f in allFoods:
#                 for a in allArtists:
#                     X[s, h, sp, f, a] = solver.BoolVar(
#                         'X[%i %i %i %i %i]' % (s, h, sp, f, a))

# H = {}
# for h in allHouses:
#     for c in allColors:
#         H[h, c] = solver.BoolVar('H[%i %i]' % (h, c))
# # Define our objective function
# solver.Maximize(solver.Sum(
#     X[s, c, d] for s in allStudents for c in allCourses for d in allDays if StudentCourseData[c][s] == 'Y'))


# # Each student must take one course on each day
# for s in allStudents:
#     for d in allDays:
#         solver.Add(solver.Sum([X[s, c, d] for c in allCourses]) == 1)


# # Student can't take courses no one teaching
# for s in allStudents:
#     for c in allCourses:
#         for d in allDays:
#             solver.Add(X[s, c, d] <= solver.Sum([Y[t, c, d]
#                        for t in allTeachers]))


# current_time = time.time()
# reading_time = current_time - start_time
# sol = solver.Solve()
# solving_time = time.time() - current_time

# print('Optimization Complete with Total Happiness Score of',
#       round(solver.Objective().Value()))
# print("")
# print('Our program needed', round(solving_time, 3),
#       'seconds to determine the optimal solution')


# # In[6]:


# # Print Output for Students

# # for s in allStudents:
# #     for c in allCourses:
# #         for d in allDays:
# #             if X[s, c, d].solution_value() == 1:
# #                 print("Student", StudentList[s], "is taking Course", CourseList[c],
# #                       "on Day", DayList[d])
# #     print("")
