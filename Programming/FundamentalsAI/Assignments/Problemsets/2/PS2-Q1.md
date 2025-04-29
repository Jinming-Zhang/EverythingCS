# JInming Zhang
## Problem #1
### a)
Optimal partition for the 6 students into 3 pairs:
(Billy + Jinhao) = 96
(David + Xinchang) = 80
(Niranjan + Szeka) = 10
of score 186.

### b)
#### Brute Force Approach:
Try all possible cases of the m pairs and find the one with highest score.
There are total of 
$$\frac{100!}{2^{50}} \approx 8.289\times 10^{142}$$ 
cases.

The brute force approach is guarenteed to find the optimal solution, but it's very slow.
With the help of all the RTX 3090ti on and off the market the we should be able to get a solution within our life time.

#### Hill-Climbing Approach:
Define the problem as follows:
- Initial State:
	- A list of randomly ordered number for 1-n, without duplication
	- Example for n = 6, some valid initial states are as follows
		1. \[1,4,3,6,5,2\]
		1. \[1,3,5,6,4,2\]
		1. \[3,5,1,2,6,4\]

- State Transitions:
	- Pick any two element in the list and swap their position, there are total of $\binom{n}{2}$ possible actions at every state.

- Evaluation Function:
	- From left to right of the list, count each consecutive elements as a pair, sum the score of all the pairs based on the given information.

A Hill-Climbing algorithm that finds a solution for this problem will be:

- Starting at a random initial state
- At each iteration, try all the possible actions and pick the one that has the highest score
- Loop until non of the possible actions has a higher score than the currect state.
- Return the current state as the solution.

This Hill-Climbing algorithm can generate a solution really fast, but it's not guarenteed to be the optimal solution.

#### Local Beam Approach
Define the problem same as Hill-Climbing approach, with same initial state, state transition and evaluation function.

Define a positive number k,

- At each iteration, we pick the top k results that have the highest score.
- For the top k result, evaluate all the possible states each result can reach, then pick the top k result again with the highest score.
- Keep looping until there is no better result can be reached from the top k result set.
- Return the highest score in the top k result set as a solution.

Similar to Hill-Climbing, Local Beam Approach can generate a solution real quick, but it's not guarenteed to be the optimal solution.


### c)
By using random-restart hill-climbing algorithm with iteration 100, the best score it can find is:
$$4894$$


Python script snippet:
```py
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


# read data, please don't hack my machine
file_dir = "/home/wolf/Desktop/NEU_Courses_Repo/FundamentalsAI/Assignments/Problemsets/2/Problem Set 2 - Compatibility Scores.xlsx"

wb = load_workbook(filename=file_dir)
ws = wb.active

# read data from excel
data = []
for row in ws.iter_rows(min_row=2, min_col=2, values_only=True):
    row_values = []
    for cell in row:
        row_values.append(cell)
    data.append(row_values)
# print(data)
n = len(data)


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
for i in range(0, len(data)):
    print("Iteration: " + str(i+1) + ". Current best score: " + str(best_score))

    result = hill_climbing(len(data))
    score = evaluate_state_score(result)
    if (score > best_score):
        best_score = score
        best_pair = deep_clone_primitive_list(result)
print(best_score)

```