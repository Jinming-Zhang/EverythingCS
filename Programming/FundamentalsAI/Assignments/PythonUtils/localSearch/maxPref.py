from openpyxl import *
from random import shuffle
from typing import List

# utility function


def deep_clone_primitive_list(original):
    return [x for x in original]


def swap_elements(original, i, j):
    cp = deep_clone_primitive_list(original)
    tmp = cp[j]
    cp[j] = cp[i]
    cp[i] = tmp
    return cp


# read data
file_dir = "/home/wolf/Desktop/NEU_Courses_Repo/FundamentalsAI/Assignments/Problemsets/Mid1/InputCourseSynthesis.xlsx"

wb = load_workbook(filename=file_dir)
ws = wb.active

# read data from excel
data = []
for row in ws.iter_rows(min_row=2, min_col=2, values_only=True):
    row_values = []
    for cell in row:
        row_values.append(cell)
    data.append(row_values)
n = len(data)


def lookup_score(r, c):
    return data[r][c]


def evaluate_state_score(people: List[int], days: List[int]):
    total = 0
    state = combine_people_day(people, days)
    for i in range(0, len(state), 2):
        step = lookup_score(state[i], state[i+1])
        total += step
    return total


def evaluate_state_score2(state):
    total = 0
    for i in range(0, len(state), 2):
        step = lookup_score(state[i], state[i+1])
        total += step
    return total


def combine_people_day(people, day):
    res = []
    for i in range(len(people)):
        res.append(people[i])
        res.append(day[i])
    return res


def get_random_initial_state(n):
    rand = list(range(0, n))
    shuffle(rand)
    return rand


def hill_climbing(n):
    initial_people = get_random_initial_state(n)
    initial_days = get_random_initial_state(n)

    # climbing
    current_people = deep_clone_primitive_list(initial_people)
    current_score = evaluate_state_score(current_people, initial_days)

    it_count = 0
    while (True):
        next_people_candidate = deep_clone_primitive_list(current_people)
        next_people_candidate_score = evaluate_state_score(
            next_people_candidate, initial_days)

        # swap people
        for i in range(len(current_people)-1):
            for j in range(i+1, len(current_people)):
                next_people = swap_elements(current_people, i, j)
                next_score = evaluate_state_score(next_people, initial_days)
                if (next_score > next_people_candidate_score):
                    next_people_candidate = deep_clone_primitive_list(
                        next_people)
                    next_people_candidate_score = next_score

        if (next_people_candidate_score > current_score):
            current_people = deep_clone_primitive_list(next_people_candidate)
            current_score = next_people_candidate_score
        else:
            break
    return combine_people_day(current_people, initial_days)


best_score = 0
best_pair = []
for i in range(0, 100):
    print("Iteration: " + str(i+1) + ". Current best score: " + str(best_score))

    result = hill_climbing(len(data))
    score = evaluate_state_score2(result)
    if (score > best_score):
        best_score = score
        best_pair = deep_clone_primitive_list(result)
print(best_score)
