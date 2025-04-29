# Uninformed Search

`Ununformed/Blind Search` means the algorithm can only separate **goal state** and **non-goal state**, and doesn't have any other information.

Uninformed search strategies are distinguished by the **order** of the nodes they expand (since they don't have any information).

> Algorithms that knows which non-goal state is more promising are classifed as [[Informed Search Strategies|Informed Search]].

## Uninformed Search Algorithms
Let `b` be the branching factor(how many branch each node expands) and `d` be the depth.
### BFS
Use a **queue** to expand nodes.
Goal-Test can be performed when
1. when selected for expansion.
2. when added to the queue.

Time Complexity: $O(b^d)$
Space Complexity: $O(b^d)$ 

>BFS needs to store all node's information before finds a path

### Uniform-Cost Search
Expand node with loweast path-cosst first (**priority queue**).

Nodes don't expanded by the order of depth, but by the summed edge cost.

The algorithm doesn't stop when a goal is found, it need to check all possible paths to find the optimal-cost path.

When a node is selected for expansion, the optimal-cost path must have been found to that node.

Time Complexity: $O(\mathrm{b}^{1+[C^*/\epsilon]})$, where **C*** is the optimal path's cost, $\epsilon$ is the cost for each path.

When all the paths have the same cost, BFS performs better than UCS. 
Because UCS nees to find all the paths to the Goal before it stops, whereas BFS stops immediately when it find the goal.

### DFS
Use a **stack** to expand nodes.

Time Complexity: $O(b^m)$, where $m$ is the maximum depth of any node, which can be larger than $d$, the depth of the shallowest solution.

Space Complexity: $O(bm)$ 
### Bidirectional BFS
Do BFS from initial state and goal state simultaneously. 
Time Complexity: $O(\mathrm{b}^{d/2})$
Space Complexity: $O(\mathrm{b}^{d/2})$ 
### BFS