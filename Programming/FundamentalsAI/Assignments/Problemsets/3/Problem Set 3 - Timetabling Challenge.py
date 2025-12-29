#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import pandas as pd
from ortools.linear_solver import pywraplp


# In[2]:


AllData = pd.ExcelFile("Input Data.xlsx")
StudentCourseData = pd.read_excel(AllData, 'StudentCourse')
TeacherCourseData = pd.read_excel(AllData, 'TeacherCourse')
TeacherBlockData = pd.read_excel(AllData, 'TeacherDay')
CourseBlockData = pd.read_excel(AllData, 'CourseDay')

print(StudentCourseData)
print("")

print(TeacherCourseData)
print("")

print(TeacherBlockData)
print("")

print(CourseBlockData)


# In[3]:


# StudentCourseData[8][3] ='Y' means that Student S3 wants to take Course C8
print(StudentCourseData[8][3])

# TeacherCourseData[9][5] ='Y' means that Course C5 can be taught by Teacher T9
print(TeacherCourseData[9][5])

# TeacherDayData[1][5] ='N' means that Day D1 cannot be assigned to Teacher T5
print(TeacherBlockData[1][5])

# CourseDayData[3][0] ='N' means that Day D3 cannot be assigned to Course C0
print(CourseBlockData[3][0])


# In[4]:


numStudents = 8
numTeachers = 6
numCourses = 12
numDays = 4

allStudents = range(numStudents)
allTeachers = range(numTeachers)
allCourses = range(numCourses)
allDays = range(numDays)

StudentList = ['S0', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7']
TeacherList = ['T0', 'T1', 'T2', 'T3', 'T4', 'T5']
CourseList = ['C0', 'C1', 'C2', 'C3', 'C4',
              'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'C11']
DayList = ['D0', 'D1', 'D2', 'D3']


# In[5]:


solver = pywraplp.Solver('Timetabling Problem',
                         pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

start_time = time.time()

# Define our binary variables for the students and teachers
X = {}
for s in allStudents:
    for c in allCourses:
        for d in allDays:
            X[s, c, d] = solver.BoolVar('X[%i,%i,%i]' % (s, c, d))

Y = {}
for t in allTeachers:
    for c in allCourses:
        for d in allDays:
            Y[t, c, d] = solver.BoolVar('Y[%i,%i,%i]' % (t, c, d))

# Define our objective function
solver.Maximize(solver.Sum(
    X[s, c, d] for s in allStudents for c in allCourses for d in allDays if StudentCourseData[c][s] == 'Y'))


# Each student must take one course on each day
for s in allStudents:
    for d in allDays:
        solver.Add(solver.Sum([X[s, c, d] for c in allCourses]) == 1)

# Each course is taught on exactly one of the four days
for c in allCourses:
    solver.Add(solver.Sum([Y[t, c, d]
               for d in allDays for t in allTeachers]) == 1)

# Exactly three courses are taught each day
for d in allDays:
    solver.Add(solver.Sum([Y[t, c, d]
               for c in allCourses for t in allTeachers]) == 3)

# Each course is assigned to one teacher
for c in allCourses:
    solver.Add(solver.Sum([Y[t, c, d]
               for t in allTeachers for d in allDays]) == 1)

# Each teacher teaches exactly two courses
for t in allTeachers:
    solver.Add(solver.Sum([Y[t, c, d]
               for c in allCourses for d in allDays]) == 2)

# No teacher may teach more than one course per day
for t in allTeachers:
    for d in allDays:
        solver.Add(solver.Sum([Y[t, c, d] for c in allCourses]) <= 1)

# Set of courses can be taught by each teacher
for c in allCourses:
    for t in allTeachers:
        if (TeacherCourseData[c][t] != 'Y'):
            solver.Add(solver.Sum([Y[t, c, d] for d in allDays]) == 0)

# Set of days each teacher is unavailable to work
for d in allDays:
    for t in allTeachers:
        if TeacherBlockData[d][t] == 'N':
            solver.Add(solver.Sum(Y[t, c, d] for c in allCourses) == 0)

# Set of days which courses cannot be offered
for d in allDays:
    for c in allCourses:
        if CourseBlockData[d][c] == 'N':
            solver.Add(solver.Sum([Y[t, c, d]for t in allTeachers]) == 0)

# Student can't take courses no one teaching
for s in allStudents:
    for c in allCourses:
        for d in allDays:
            solver.Add(X[s, c, d] <= solver.Sum([Y[t, c, d]
                       for t in allTeachers]))


current_time = time.time()
reading_time = current_time - start_time
sol = solver.Solve()
solving_time = time.time() - current_time

print('Optimization Complete with Total Happiness Score of',
      round(solver.Objective().Value()))
print("")
print('Our program needed', round(solving_time, 3),
      'seconds to determine the optimal solution')


# In[6]:


# Print Output for Students

for s in allStudents:
    for c in allCourses:
        for d in allDays:
            if X[s, c, d].solution_value() == 1:
                print("Student", StudentList[s], "is taking Course", CourseList[c],
                      "on Day", DayList[d])
    print("")


# In[7]:


for t in allTeachers:
    for c in allCourses:
        for d in allDays:
            if Y[t, c, d].solution_value() == 1:
                print("Teacher", TeacherList[t], "is teaching Course", CourseList[c],
                      "on Day", DayList[d])
    print("")
