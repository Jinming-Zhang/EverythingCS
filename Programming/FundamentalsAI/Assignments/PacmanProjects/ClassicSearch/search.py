# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

from enum import Enum
from typing import Dict, List, Set, Tuple
from game import Directions
import util

bottom = Directions.SOUTH
left = Directions.WEST
top = Directions.NORTH
right = Directions.EAST
stay = Directions.STOP


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self) -> None:
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state) -> bool:
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state) -> None:
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


'''
 class structs for organizing information
'''


class SearchStrategy(Enum):
    BFS = 1
    DFS = 2
    UCS = 3
    AS = 4


class State:
    def __init__(self, state: Tuple[int, int]) -> None:
        self.state = state


class StateInfo:
    def __init__(self, ancestor: State, direction: Directions, gn_value: float, fn_value: float) -> None:
        self.ancestor = ancestor
        self.direction = direction
        self.fn_value = fn_value
        self.gn_value = gn_value
        self.hn_value = 0


class EdgeInfo:
    def __init__(self, successor: State, direction: Directions, path_cost: float) -> None:
        self.successor = successor
        self.direction = direction
        self.path_cost = path_cost


def general_search(problem: SearchProblem, strategy: SearchStrategy, h=None):
    if (strategy is SearchStrategy.BFS):
        q = BFSQ(problem)
    elif (strategy is SearchStrategy.DFS):
        q = DFSQ(problem)
    elif (strategy is SearchStrategy.UCS):
        q = ASQ(problem)
    elif (strategy is SearchStrategy.AS):
        q = ASQ(problem, heuristic=h)

    # initialization
    visited = set()
    state_info_dict: Dict[Tuple[int, int], StateInfo] = {}

    # check if start state is the goal state
    start_state = problem.getStartState()
    if (problem.isGoalState(start_state)):
        return [Directions.STOP]

    goal_state = None

    hn = 0
    if h is not None:
        hn = h(start_state, problem)
    visited.add(start_state)
    state_info_dict[start_state] = StateInfo(
        State(start_state), Directions.STOP, 0, hn)
    # generating successors of start state to frontier
    for edge_info_tuple in problem.getSuccessors(start_state):
        edge_info = EdgeInfo(
            State(edge_info_tuple[0]), edge_info_tuple[1], edge_info_tuple[2])
        # visited list and state_info_dict will be updated in the try_push function when needed
        q.try_push(State(start_state), edge_info, state_info_dict, visited)

    while (not q.isEmpty()):
        current_state = q.pop()
        # goal check
        if problem.isGoalState(current_state):
            goal_state = current_state
            break

        # generating successors to frontier
        for edge_info_tuple in problem.getSuccessors(current_state):
            edge_info = EdgeInfo(
                State(edge_info_tuple[0]), edge_info_tuple[1], edge_info_tuple[2])

            q.try_push(State(current_state), edge_info,
                       state_info_dict, visited)
    if (goal_state is not None):
        return construct_path(state_info_dict, goal_state, problem)
    else:
        return []


def construct_path(state_info_dict: Dict[Tuple[int, int], StateInfo], goal_state: Tuple[int, int], problem: SearchProblem):
    '''
    state_info_dic: a dictionary that contains goal state and the ancestors to get to the goal state
    '''
    path = []
    current_state = goal_state
    while (problem.getStartState() != current_state):
        state_info: StateInfo = state_info_dict[current_state]
        path.append(state_info.direction)
        current_state = state_info.ancestor.state
    path.reverse()
    return path


def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    result = general_search(problem, SearchStrategy.DFS)
    print(result)
    return result


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    result = general_search(problem, SearchStrategy.BFS)
    return result


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    result = general_search(problem, SearchStrategy.UCS)
    print(result)
    return result


def nullHeuristic(state, problem: SearchProblem = None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    result = general_search(problem, SearchStrategy.AS, heuristic)
    return result


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch


class DFSQ():
    def __init__(self, problem: SearchProblem) -> None:
        self.problem = problem
        self.stack = util.Stack()

    def try_push(self, current_state: State, edge_info: EdgeInfo, state_info_dict: Dict[Tuple[int, int], StateInfo], visited: Set[Tuple[int, int]]):
        if edge_info.successor.state not in visited:
            self.stack.push(edge_info.successor.state)
            visited.add(current_state.state)
            state_info_dict[edge_info.successor.state] = StateInfo(
                current_state, edge_info.direction, 1, 1)

    def pop(self) -> Tuple[int, int]:
        return self.stack.pop()

    def isEmpty(self) -> bool:
        return self.stack.isEmpty()


class BFSQ():
    def __init__(self, problem: SearchProblem) -> None:
        self.problem = problem
        self.queue = util.Queue()

    def try_push(self, current_state: State, edge_info: EdgeInfo, state_info_dict: Dict[Tuple[int, int], StateInfo], visited: Set[Tuple[int, int]]):
        if edge_info.successor.state not in visited:
            self.queue.push(edge_info.successor.state)
            visited.add(edge_info.successor.state)
            state_info_dict[edge_info.successor.state] = StateInfo(
                current_state, edge_info.direction, 1, 1)

    def pop(self) -> Tuple[int, int]:
        return self.queue.pop()

    def isEmpty(self) -> bool:
        return self.queue.isEmpty()


class ASQ():
    def __init__(self, problem: SearchProblem, heuristic=None) -> None:
        self.problem = problem
        self.pq = util.PriorityQueue()
        self.heuristic = heuristic

    def try_push(self, current_state: State, edge_info: EdgeInfo, state_info_dict: Dict[Tuple[int, int], StateInfo], visited: Set[Tuple[int, int]]):
        current_state_cost = state_info_dict[current_state.state].gn_value
        hn = 0
        if self.heuristic is not None:
            hn = self.heuristic(edge_info.successor.state, self.problem)
        gn = current_state_cost + edge_info.path_cost

        if edge_info.successor.state not in visited:
            state_info_dict[edge_info.successor.state] = StateInfo(
                current_state, edge_info.direction, gn, gn+hn)
            self.pq.push(edge_info.successor.state, gn+hn)
        else:
            old_gn = state_info_dict[edge_info.successor.state].gn_value
            if old_gn > gn:
                state_info_dict[edge_info.successor.state] = StateInfo(
                    current_state, edge_info.direction, gn, gn+hn)
                self.pq.update(edge_info.successor.state, gn)
        visited.add(edge_info.successor.state)

    def pop(self) -> Tuple[int, int]:
        result = self.pq.pop()
        return result

    def isEmpty(self) -> bool:
        return self.pq.count <= 0
