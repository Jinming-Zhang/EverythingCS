# Definitions for Problems
- Initial State: The state that the agent starts with.
- Actions: The actions available to the agent at each state.
- Transition Model: The description of what each action does. Or a function that returns the result state for each action at given state.
	**Successors** of a state is the states that are reachable from that state by doing certain action.
- State Space: The set of all states that are reachable from the initial state (by any sequence of actions).
- Path of a state space is a sequence of states connected by a sequence of actions.
- Goal test: Test that determines if a given state is a goal state (can be more than one goal state in a state space).
- Path cost function: Assigns a numerical cost to each path.
- Step cost: The numerical cost for each action in a given state.

## Node Generation
Adding nodes into the queue that will be evaluated later.
## Expand a Node
Expand a node means the node is selected to be deciding next action. (evaluate its children).