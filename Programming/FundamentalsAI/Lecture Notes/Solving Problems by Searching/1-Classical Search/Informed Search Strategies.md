# Informed (Heuristic) Search Strategies
In informed search, usually a **evaluation function** $f(n)$ is provided as a cost estimate to guild the search algorithm on improving the order of node expansion.
- f(n) evaluation function: the function that determins which node to expand first at node n, is constructed as **cost-estimate** **from node n to the goal state**, node with **lowest** f(n), estimated cost, is expanded first.
- h(n) heuristic function: an estimated cost **from node n to the goal state**, it's a function that often used as part of a evaluation function at the predecessor of node n.
- g(n): the actual cost from **initial** state to node n.

## Greedy best-first search
Use heuristic function $h(n)$ and evaluation function and try to expand the node that's cloesest to the goal.
$$ f(n) = g(n)$$
- Can be incomplete when it can expand node that is already be expanded before
- Result may not be optimal because it can miss certain lower-cost paths that needs to go back a bit first.

## A* search
Use heuristic function **and** the step cost $f(n) = g(n) + h(n)$ as evaluation function, 
try to expand the node that has **lower coat to get to and cloesest to the goal**.

f(n)= the estimated cost of cheapest solution through.

It's different from *greedy best-first search* because it also take the step cost into consideration.
$$ f(n) = g(n) + h(n)$$
#### Note
- g(n) is the actual cost from **initial** state to **state n**, this value needs to be updated to the lowest cost whenever a state is visited
- f(n) is the estimated cost from **state n to goal state**, this is used to determine which node to expand
- For each node we visited, we need to *update g(n)* and *calculate f(n)*, these two steps are different!
#### Condition for A* search to yield optimal solution:
- The heuristic function it uses must be [[#Admissible Heuristic]].
- For graph search, the heuristic function must be [[#Consistency Heuristic]].

This can be proved be proving when a node is expanded by A* search, the optimal path to that node has already found.

#### Properties of A*
C\* is the the cost of optimal path.
f(n) is the estimated cost from n to goal.
1. A\* expands all nodes with $f(n) \lt C*$
	Because for each node A\* expands, an optimal path to that node is guarenteed found.  Also A\* **expands node in the order of non-decreasing $f(n)$**, so it can't expand a node with estimated path cost more than the actual optimal cost before the goal is expanded.
1. It's possible that for some of the nodes, f(n) = C\*, in such cases A\* might not expand the goal first.