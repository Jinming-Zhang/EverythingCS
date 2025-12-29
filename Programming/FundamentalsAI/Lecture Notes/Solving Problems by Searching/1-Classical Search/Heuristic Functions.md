# Heuristic functions
The purpose of a heuristic function $h(n)$ is to estimate the cost (to solve the problem) of a **solution** beginning from the state and node n (initial state becomes starting at node n). 

## Heuristic Function Properties
$h(n)=$ The estimated cost of the cheapest path from the state at node $n$ to a goals state.
#### Admissible (可容的) Heuristic
A `admissible heuristic` function is a heuristic function that **never overestimates** the cost to reach the goal.
#### Consistency Heuristic
A `consistent heuristic` function is a heuristic function has the property for each successors of n, n':
$$h(n) \le g(n') + h(n')$$
(There shouldn't be a child state we can , such that the cost of getting their AND the estimated cost of getting to goal from there is more optimal the the current estimated cost to goal. 
If there is such a child, then our heuristic won't make sense, because it doesn't guide us towards the optimal solution).

# How to generate good heuristic functions
### Relaxed Problem
An alternative version of the problem that has fewer restrictions on actions.

- Any optimal solution to the original problem, is also a solution in the relaxed problem

> The cost of an optimal solution to a relaxed problem is an admissible heuristic for the original problem.