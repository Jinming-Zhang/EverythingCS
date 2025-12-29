# Jinming Zhang
1. Q5 is the most difficult question because unlike other questions which are about implementing search algorithm, Q5 requires structuring the problem so that it can be solved using a search algorithm.
	It needs a completely different point of view and helped a lot on understanding the role of searching-AI.
2. Q1 and Q2 are the easiest question because it's really simple to implement and the implementation for Queue and Stack are already provided.
3. h(n) = the manhattan distance from the pacman's current position to the furthest unvisited corner
	1. Addmissible: It's the minumium distance for pacman to go to the corner without walls so it's guarenteed less than the actual path cost in the maze.
	2. Consistency: Since each step cost 1, the heuristic is consistent if $$h(n) \le 1+h(n')$$
		- If the available move is 1 step closer to the furthest corner, $h(n) = 1 + h(n')$
		- If the available move is 1 step further to the furthest corner, $h(n)<1+h(n')$
		Therefore this heuristic is consistent.
	1. The heuristic is the sum of all the distance of all the foods divide by 2.
	- Strength:
	- Weakness: