# Jinming Zhang
# Question #1
Uniform Cost Search.
Lowest cost path from A to G with path cost of 23:
> A->B->E->G

# Question #2
1
 For every input graph, Uniform Cost Search (UCS) is a special case of A* Search
# Question #3
2
A* returns optimal solution when the heuristic function is admissible (for tree search).
# Question #4
1
Every consistent heuristic is also admissible

# Question #5

```cs
BFS(startNode, goalTest){
	// fifo queue for nodes to be expanded
	queue = new Queue()
	queue.add(startNode)

	// a list of nodes that have already been expanded	
	expandHistory = new List<LOCATION>(); 

	// a dictionary that stores the optimal moves to each node
	pathToNodes = new Dictionary<LOCATION, List<Direction>>();

	// initialize the path to the startNode as an empty moves list
	pathToNodes.add(startNode, [])

	while queue is not empty {
		node = queue.Dequeue()
		get path to the node from pathToNodes dictionary
		// add to expand history so we don't expand it again
		expandHistory.add(node)

		for each [DIRECTION, LOCATION] in Neighbours(node) {
			// extend the path to the new LOCATION
			newPath = path.add(DIRECTION)
			if(LOCATION passed goalTest) {
				return newPath as result
			}
		    else {
				if(LOCATION not in expandHistory) {
					// store the path to the location
					pathToNodes.add(LOCATION, newPath)
					// and add it to the queue to be expanded later
					queue.add(LOCATION)
				}
			}
		}
	}
    return non-solution
}
```


