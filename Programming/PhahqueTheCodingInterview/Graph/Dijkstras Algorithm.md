# Dijkstra's Algorithm

Finding shortest path between any nodes in a graph.

Variation: Finding shortest path between a **given node** and all other nodes in the graph.

## Pseudocode
- Mark all nodes unvisited, keep a set of unvisited nodes
- For each node, keep track of it's tentative value (试验的), shortest path cost from initial node to that node, initialise with $+\infty$
- Set initial node as *current* node
- For *current* node, check all the **unvisited** neighbours and update their tentative value.
- After updated all unvisited neighbours if the *current* node, mark *current* node as visited, remove it from unvisited set and
- From unvisited set, select the one with smallest tentative value and expand on that.
- Stop when the smallest tentative distance among the unvisited nodes is $+\infty$