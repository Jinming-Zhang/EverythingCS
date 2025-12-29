## Q4
### a)
 For any value of n, the solution will have n+1 nodes, with starting point at both the beginning and the ending of the path.
 So there will be n-1 nodes in the middle that compose the path.

#### Hill Climbing  Strategy is as Follows:
1. Randomly construct a initial solution, with starting point at both the beginning and the ending, all other locations in the middle with random order without duplication.
2. For each iteration, try swap the position of 2 out of the n-1 nodes and evaluate the new path cost
	1. There are total of $\binom{n-1}{2}$ possible cases to test at each iteration.
	2. Pick the one that reduce the path cost the most as the updated solution.
3. Repeat  the iteration until no better solution can be found.

#### Steps for Solving Initial Solution: AFBDECA
At each step, choose 2 out of 5 locations in the middle and swap their position, which means there there are $\binom{5}{2}=10$ possible actions at each iteration.

- Iteration 1:
	1. AFBDECA,   <- initial state, path cost = 600
	2. ABFDECA, path cost = 453
	3. ADBFECA, path cost = 214
	4. AEBDFCA, path cost = 316
	5. ACBDEFA, path cost = 512
	6. AFDBECA, path cost = 457
	7. AFEDBCA, path cost = 512
	8. AFCDEBA, path cost = 424
	9. AFBEDCA, path cost = 512
	10. AFBCEDA, path cost = 510
	11. AFBDCEA, path cost = 455

Since ADBFECA has lowest path cost of 214, chose this for this iteration.
- Iteration 2:
	1. ABDFECA, path cost = 261
	2. AFBDECA, path cost = 600
	1. AEBFDCA, path cost = 312
	1. ACBFEDA, path cost = 318
   1. ADFBECA, path cost = 263
   2. ADEFBCA, path cost = 318
   3. ADCFEBA, path cost = 38
   4. ADBEFCA, path cost = 130
   5. ADBCEFA, path cost = 318
   6. ADBFCEA, path cost = 265

Since ADCFEBA has lowest path cost of 38, chose this for this iteration.
- Iteration 3:
    1. ACDFEBA, path cost = 173
    1. AFCDEBA, path cost = 424
    1. AECFDBA, path cost = 312
    1. ABCEFDA, path cost = 171
    1. ADFCEBA, path cost = 175
    1. ADEFCBA, path cost = 230
    1. ADBFECA, path cost = 214
    1. ADCEFBA, path cost = 122
    1. ADCBEFA, path cost = 230
    1. ADCFBEA, path cost = 177

Since there is no more optimal solution can be reached from this state, we chose ADCFEBA as our final solution with path cost 38.

It is a optimal solution because it's the same as the solution found by A\* in the below sections.

### b)
#### Search Problem Definition
For any value of n, define a problem as follows:
- State:
	- State of the problem will be a list representing a path that is currently travelled, with the starting location appended at the end to calculate the returning cost.
	So that the second last element will be the current location
	- For example, assume starting point is A, here are some valid states:
		- \[A, B, C, A\], path is A->B->C, currently at location C, returning cost to A is included.
		- \[A, E, F, B, A\], path is A->E->F->B, currently at location B
- Initial State: 
	- A list contains only the starting location: \[StartingLocation\]
- Goal State:
	- A list of nodes with starting location at both the beginning and the end, and all other locations at the middle in any order without duplicates.
	- Examples of valid goal state:
		- \[A, B, E, C, F, D, A\]
		- \[A, D, E, B, F, C, A\]
- Transition Model:
	- All the available paths from current location towars another unvisited location
- Cost:
	- Sum of the path cost until current location *plus* the path cost from current location to the starting location

#### Heuristic Function
For each state of the problem, define the heuristic as follows:

> h(n) = sum of all the edges' weight of the minimium spanning tree that is consist of the starting point and all the locations that haven't been visited yet.

For example, at state \[A, C, E\], unvisited locations are \[B, D, F\].
First we construct a minimum spanning tree of graph \[A, B, D, F\], which contains following edges:
- (a-b), cost 3
- (a-d), cost 6
- (b-f), cost 50

The the heuristic for state \[A, C, E\] will be the sum of all edges in the minimum spanning tree consisted of \[A, B, D, F\]: $3+6+50=59$.

##### Admissible:
This heuristic is admissible because it's guarenteed to be less than the optimal solution.


- The optimal solution at current state needs to visit all the remaining nodes.
- In the minimium spanning tree that consist of all the remaining nodes, the sum of the edges is the minimum cost that connects all the locations.

As MST tree’s largest cost is that all nodes are linked all in left or right child and make tree like LinkedList, in this case, the cost of MST is equal to TSP but in other cases, as it is less than TSP. Therefore, this heuristic function is admissible.

##### Good Enough Estimate:
For the given example, using uniform-cost-search will expand 49 nodes to find the optimal solution, whereas using A\* with above heuristic expands 25 nodes. 
Also the optimal solution has a path cost of 38, and the sum of all the edges of MST is 27.
So it's a good enough estimate.

#### c)
Starting wtih node A, the initial state is \[A\]. 
The A\* algorithm using the above heuristic expands nodes in the following order:
1. A B A
2. A D A
3. A D C A
4. A C A
5. A C D A
6. A B D A
7. A D B A
8. A D C B A
9. A B E A
10. A B C A
11. A B C D A
12. A C B A
13. A D C E A
14. A C D B A
15. A B D C A
16. A B E C A
17. A D B C A
18. A E A
19. A E B A
20. A D B E A
21. A E B D A
22. A B E F A
23. A B E F C A
24. A B E F C D A

The final solution is ABEFCDA with path cost 38.


##### py script snippet
```py
from typing import List
class node:
    def __init__(self, id=None, value=None, neighbours=None)   None:
        self.id = id
        self.value = value
        self.neighbours: List[Tuple[node, float]] = neighbours

# Define the graph
a = node("a", neighbours=[])
b = node("b", neighbours=[])
c = node("c", neighbours=[])
d = node("d", neighbours=[])
e = node("e", neighbours=[])
f = node("f", neighbours=[])

a.neighbours.append((b, 3))
a.neighbours.append((c, 50))
a.neighbours.append((d, 6))
a.neighbours.append((e, 100))
a.neighbours.append((f, 200))


b.neighbours.append((a, 3))
b.neighbours.append((c, 4))
b.neighbours.append((d, 50))
b.neighbours.append((e, 7))
b.neighbours.append((f, 50))


c.neighbours.append((a, 50))
c.neighbours.append((b, 4))
c.neighbours.append((d, 5))
c.neighbours.append((e, 50))
c.neighbours.append((f, 9))


d.neighbours.append((a, 6))
d.neighbours.append((b, 50))
d.neighbours.append((c, 5))
d.neighbours.append((e, 200))
d.neighbours.append((f, 100))


e.neighbours.append((a, 100))
e.neighbours.append((b, 7))
e.neighbours.append((c, 50))
e.neighbours.append((d, 200))
e.neighbours.append((f, 8))


f.neighbours.append((a, 200))
f.neighbours.append((b, 50))
f.neighbours.append((c, 9))
f.neighbours.append((d, 100))
f.neighbours.append((e, 8))

def print_path(path: List[node]):
    for n in path:
        print(n.id + "   ", end="")
    print("")

# Calculating MSP
def get_next_edge(edge_q: List[Tuple[node, float]]):
    lowest_cost = 999999
    candidate = None
    for edge in edge_q:
        successor, step_cost = edge
        if(step_cost < lowest_cost):
            lowest_cost = step_cost
            candidate = edge
    return candidate


def find_minimium_spanning_tree(graph: List[node]):
    if(len(graph) == 1):
        return []
    result_edges = []
    visited_locations = set()
    edge_q = []

    current_node = graph[0]
    visited_locations.add(current_node)

    for edge in current_node.neighbours:
        if(edge[0] in graph):
            edge_q.append(edge)

    while(len(visited_locations) != len(graph)):
        next_edge = get_next_edge(edge_q)
        edge_q.remove(next_edge)
        successor, step_cost = next_edge
        if(successor not in visited_locations):
            visited_locations.add(successor)
            result_edges.append(next_edge)

            for new_edge in successor.neighbours:
                new_successor, new_step_cost = new_edge
                if(new_successor in graph and 
	               new_successor not in visited_locations):
                    edge_q.append(new_edge)
    return result_edges


# utility functions for A* search
def evaluate_cost(path):
    '''
	calculates g(n)
    path = [a, ..., a]
    '''
    cost = 0
    start: node = path[0]
    for i in range(1, len(path)):
        next = path[i]
        for neighbour in start.neighbours:
            if neighbour[0].id == next.id:
                cost += neighbour[1]
                start = next
                continue
    return cost


def is_goal_state(travel_history: List[node]):
    if(len(travel_history) != 7):
        return False
    if(travel_history[0].id != 'a' or travel_history[-1].id != 'a'):
        return False
    path = travel_history[1:6]
    check = ['b', 'c', 'd', 'e', 'f']
    for p in path:
        if(p.id in check):
            check.remove(p.id)
    return len(check) == 0


def copy_path(path: List[node]):
    copyed_path = []
    for p in path:
        copyed_path.append(p)
    return copyed_path


# two heuristic functions
def dumb_hn(state: List[node]):
    return 0


def smart_hn(state: List[node]):
    if(is_goal_state(state)):
        return 0
    all = [b, c, d, e, f]
    for s in state:
        if s in all:
            all.remove(s)
    all.append(a)
    minspan_edges = minimiumSpanningTree.find_minimium_spanning_tree(all)
    total = 0
    for edge in minspan_edges:
        total += edge[1]
    return total

# slow implementation of priority queue
def get_next_in_frontier(frontier: List[List[node]]):
    fn = 999999
    expand = None
    for candidate in frontier:
        gn = evaluate_cost(candidate)
        heuristic = smart_hn(candidate)
        # heuristic = dumb_hn(candidate)
        if gn+heuristic < fn:
            fn = gn+heuristic
            expand = candidate
    frontier.remove(expand)
    return expand

####################### this is the A* function ##################
def find_min_path():
    # state is the path until current node
    # i.e. [a,b,e], current node is e.
    start_state: List[node] = [a]
    frontier: List[List[node]] = []
    for successor in start_state[-1].neighbours:
        path_to_neighbour = [a, successor[0], a]
        frontier.append(path_to_neighbour)
    expanded_node = []

    solution = None

    while(len(frontier) > 0):
        current_path = get_next_in_frontier(frontier)
        expanded_node.append(current_path)
        if(is_goal_state(current_path)):
            solution = current_path
            break
        # need to add a to the last manually
        current_node = current_path[-2]
        for successor_tuple in current_node.neighbours:
            successor, step_cost = successor_tuple
            if(successor not in current_path):
                new_path = copy_path(current_path)
                new_path.insert(len(new_path)-1, successor)
                frontier.append(new_path)

    if(solution is None):
        print("no solution")
    else:
        print_path(solution)
        print("Nodes expanded: " + str(len(expanded_node)))
        for sub_path in expanded_node:
            for n in sub_path:
                print(n.id+" ", end="")
            print("")
        print("Cost: " + str(evaluate_cost(solution)))

# get the optimal solution and print the path
find_min_path()
```
