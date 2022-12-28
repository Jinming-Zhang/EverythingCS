Dynamic programming applies when the subproblems overlap (when subproblems share subproblems).
Dynamic programming solves each subproblem just once and then saves/cache the result in a table, thereby avoiding duplicated calculations.

## Optimal Substructure
The types of problems that the optimal solution to the problem incorporate optimal solutions to related subproblems, which we may solve independently.

## Steps for developing dynamic programming algorithm
1. Characterize the structure of an optimal solution
2. Recursively define the value of an optimal solution
3. Compute the value of an optimal solution, typically in a bottom-up fashion
4. Construct an optimal solution from computed information