### a)
A consistent heuristic has the following property:
$$h(n) \leq g(n') + h(n')\text{ for each successor $n'$ of n}$$

##### Case 1: n' is goal state
If $n'$ is goal state, then $h(n')=0$, and we have $h(n) \leq g(n')$.
Since $g(n')$ is the actual cost from initial state to goal state, so $h(n)$ has to be admissible.

##### Case 2: n' is not goal state
Since for each successor, $h(n)$ will not greater than the actual cost to that successor and the hueristic from that successor to goal state. The inequality can be expanded for each successor until it reaches goal state.
1. $h(n)\leq g(n') + h(n')$
1. $h(n') \leq g(n'') + h(n'') \implies h(n)\leq  g(n') + (g(n'') + h(n''))$
3. etc... for each successor of n, n', ..., untial goal state reached if it exists

Based on the transitive property of inequality, we can ensure that $h(n)\leq C^*(n)$


### b)
In each step, we can only move 1 block,  the Manhattan distance represents the minimum moves we need to move the blocks to their goal position. So it is admissible.

### c)
h(n) is not admissible.
Because each score represents a disordered pair, however, it's possible to change 2 score in one move, so the score is not guarenteed to be less than the number of moved required to reach goal state.
Example initial state:
$$
  \left[\begin{array}{|rrr|}
    1 & 2 & 3 \\
    4 & 5 & 口 \\ 
    7 & 8 & 6 \\
  \end{array}\right]
$$
In the above board we have a score of 2: (7,6), (8,6)
But we can actually reach goal state in 1 step (moving 6 to the top).