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

print(data[0][1])  # row 0 col 1


def lookup_pair_score(r, c):
    if (r < c):
        return data[r][c]
    else:
        return data[c][r]


def evaluate_state_score(state: List[int]):
    total = 0
    for i in range(0, len(state), 2):
        step = lookup_pair_score(state[i], state[i+1])
        total += step
    return total


def get_random_initial_state(n):
    random_state = list(range(0, n))
    shuffle(random_state)
    return random_state


def hill_climbing(n):
    initial_state = get_random_initial_state(n)

    # climbing
    current_state = deep_clone_primitive_list(initial_state)
    current_score = evaluate_state_score(current_state)

    while (True):
        next_state_candidate = deep_clone_primitive_list(current_state)
        next_state_candidate_score = evaluate_state_score(next_state_candidate)
        for i in range(0, len(current_state)-1):
            for j in range(i+1, len(current_state)):
                next_state = swap_elements(current_state, i, j)
                next_score = evaluate_state_score(next_state)
                if (next_score > next_state_candidate_score):
                    next_state_candidate = deep_clone_primitive_list(
                        next_state)
                    next_state_candidate_score = next_score

        if (next_state_candidate_score > current_score):
            current_state = deep_clone_primitive_list(next_state_candidate)
            current_score = next_state_candidate_score
        else:
            break
    return current_state


best_score = 0
best_pair = []
for i in range(0, 100):
    print("Iteration: " + str(i+1) + ". Current best score: " + str(best_score))

    result = hill_climbing(len(data))
    score = evaluate_state_score(result)
    if (score > best_score):
        best_score = score
        best_pair = deep_clone_primitive_list(result)
print(best_score)
print(best_pair)
