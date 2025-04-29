### a)
330
Solved by ortools:
```py
data = [
    [60, 80, 90, 70],
    [80, 90, 100, 80],
    [60, 50, 90, 50],
    [70, 60, 50, 80],
]

alldays = range(4)
allPeople = range(4)
X = {}
for v in allPeople:
    for d in alldays:
        X[v, d] = solver.BoolVar("%d in day %d" % (v, d))
for v in allPeople:
    solver.Add(solver.Sum([X[v, d]for d in alldays]) == 1)
for d in alldays:
    solver.Add(solver.Sum([X[v, d]for v in allPeople]) == 1)

solver.Maximize(solver.Sum([X[v, d]*data[v][d]
                for v in allPeople for d in alldays]))

solver.Solve()
print(solver.Objective().Value())
for v in solver.variables():
    if(v.solution_value() == 1):
        print(v.name())
```

### b)
##### Random Restart Hill-Climbing
1. Initial State:
	- List of (Player, Day) pairs that satisfies the constraints: each player only works in one day, each day only have one player.
2. At each iteration:
	1. For each random two pairs, swap the players in those two pairs, if the score increases, keep the swapped list of pairs as new solution.
3. Until no swap can improve the score anymore, let the current list of pairs be the final solution.

Repeat the process for N random initial states and use the result with the highest score.

##### Apply to given initial state
(bill, 1), (xiaofeng, 2), (paul, 3), (satya, 4), score 270
1. iteration 1:
	1. (xiaofeng, 1),(bill, 2),(paul, 3),(satya, 4), score: 300
	1. (paul, 1),(xiaofeng, 2),(bill, 3),(satya, 4), score: 280
	1. (satya, 1),(xiaofeng, 2),(paul, 3),(bill, 4), score: 290
	1. (bill, 1),(paul, 2),(xiaofeng, 3),(satya, 4), score: 250
	1. (bill, 1),(satya, 2),(paul, 3),(xiaofeng, 4), score: 290
	1. (bill, 1),(xiaofeng, 2),(satya, 3),(paul, 4), score: 290
2. iteration 2: start with a), since it has highest score
	1. (bill, 1),(xiaofeng, 2),(paul, 3),(satya, 4), score: 270
	1. (paul, 1),(bill, 2),(xiaofeng, 3),(satya, 4), score: 260
	1. (satya, 1),(bill, 2),(paul, 3),(xiaofeng, 4), score: 320
	1. (xiaofeng, 1),(paul, 2),(bill, 3),(satya, 4), score: 300
	1. (xiaofeng, 1),(satya, 2),(paul, 3),(bill, 4), score: 290
	1. (xiaofeng, 1),(bill, 2),(satya, 3),(paul, 4), score: 320
2. iteration 3: pick c), since it has the highest score
	1. (bill, 1),(satya, 2),(paul, 3),(xiaofeng, 4), score: 290
	1. (paul, 1),(bill, 2),(satya, 3),(xiaofeng, 4), score: 330
	1. (xiaofeng, 1),(bill, 2),(paul, 3),(satya, 4), score: 300
	1. (satya, 1),(paul, 2),(bill, 3),(xiaofeng, 4), score: 320
	1. (satya, 1),(xiaofeng, 2),(paul, 3),(bill, 4), score: 290
	1. (satya, 1),(bill, 2),(xiaofeng, 3),(paul, 4), score: 270	
2. iteration 3: pick b), since it has the highest score
	1. (bill, 1),(paul, 2),(satya, 3),(xiaofeng, 4), score: 320
	1. (satya, 1),(bill, 2),(paul, 3),(xiaofeng, 4), score: 320
	1. (xiaofeng, 1),(bill, 2),(satya, 3),(paul, 4), score: 320
	1. (paul, 1),(satya, 2),(bill, 3),(xiaofeng, 4), score: 300
	1. (paul, 1),(xiaofeng, 2),(satya, 3),(bill, 4), score: 300
	1. (paul, 1),(bill, 2),(xiaofeng, 3),(satya, 4), score: 260
	
Since we can not get a higher score since iterate 3-b, the final solution for local search is 
>  (paul, 1),(bill, 2),(satya, 3),(xiaofeng, 4), score: 330

and it is optimal solution.
### c)
Score using local search from 100 iterations:
9725