# multiAgents.py
# --------------
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


from time import time
from util import manhattanDistance
from game import Directions
import random
import util

from game import Agent

from typing import *

# classes for calculating dijkstra


class StateWrapper:
    def __init__(self, state) -> None:
        self.state = state

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, StateWrapper) and __o.state == self.state

    def __hash__(self) -> int:
        return hash(self.state)

    def __str__(self) -> str:
        return str(self.state)


class DijkstraPathInfo:
    def __init__(self, stateWrapper) -> None:
        '''
        otherState: distination state
        cost: tentative value to otherState
        pathToDst: not implemented
        '''
        self.stateWrapper: StateWrapper = stateWrapper
        self.cost: float = float('inf')
        self.pathToDst: List[StateWrapper] = []

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DijkstraPathInfo) and __o.stateWrapper == self.stateWrapper

    def __hash__(self) -> int:
        return hash(self.stateWrapper)


class GameAdaptor:
    def __init__(self, gameState) -> None:
        self.gameState = gameState
        # -2 for walls on both sides
        self.mazeWidth = gameState.data.layout.width-2
        self.mazeHeight = gameState.data.layout.height-2
        self.allLocations: List[StateWrapper] = self.__getAllStates__()
        self.walls = gameState.getWalls()

    def getSuceessors(self, currentLocation: StateWrapper) -> List[StateWrapper]:
        '''
        return list of locations reachable from current location
        '''
        x, y = currentLocation.state
        successors = []
        # check north
        if (not self.walls[x][y+1]):
            successors.append(StateWrapper((x, y+1)))
        # check east
        if (not self.walls[x+1][y]):
            successors.append(StateWrapper((x+1, y)))
        # check south
        if (not self.walls[x][y-1]):
            successors.append(StateWrapper((x, y-1)))
        # check west
        if (not self.walls[x-1][y]):
            successors.append(StateWrapper((x-1, y)))
        return successors

    def __getAllStates__(self) -> List[StateWrapper]:
        '''
        Location = State in pacman
        format: (x,y)
        or : (col, row)
        with bottom-left be (1,1)
        '''
        locations: List[StateWrapper] = []
        for c in range(1, self.mazeWidth+1):
            [locations.append(StateWrapper((c, x)))
             for x in range(1, self.mazeHeight+1)]
        return locations


def allDijkstra(gameState: GameAdaptor) -> Dict[StateWrapper, List[DijkstraPathInfo]]:
    result: Dict[StateWrapper, List[DijkstraPathInfo]] = {}
    allLocations = gameState.allLocations
    for location in allLocations:
        result[location] = dijkstra(gameState, location)
    return result


def dijkstra(gameState: GameAdaptor, start: StateWrapper) -> List[DijkstraPathInfo]:
    '''
    given a gameState and a starting point
    find the shortest path cost from starting point to all game state
    return a list if DijkstraPathInfo
    each game state will have a corresponding DijkstraPathInfo that contains
    the shortest path cost from starting point to that game state, along with some
    other info
    '''
    result: List[DijkstraPathInfo] = []
    allLocations = gameState.allLocations

    unvisitedLocations: Set[DijkstraPathInfo] = set()
    current = None
    for location in allLocations:
        if location != start:
            nodeInfo = DijkstraPathInfo(location)
            unvisitedLocations.add(nodeInfo)
        else:
            current = DijkstraPathInfo(location)
            current.cost = 0
            unvisitedLocations.add(current)

    def getNextCandidate():
        candidate = None
        lowestCost = float('inf')
        for unvisited in unvisitedLocations:
            if unvisited.cost < lowestCost:
                candidate = unvisited
                lowestCost = unvisited.cost
        if (candidate != None):
            unvisitedLocations.remove(candidate)
        return candidate
    # dijkstra loop
    while (current != None):
        result.append(current)
        successors = gameState.getSuceessors(current.stateWrapper)
        # for each neighbour
        for successor in successors:
            # check if it's visited
            unvisitedMapping = None
            for unvisited in unvisitedLocations:
                if unvisited.stateWrapper == successor:
                    unvisitedMapping = unvisited
            # if it's not visited
            if unvisitedMapping != None:
                if unvisitedMapping.cost > current.cost+1:
                    unvisitedMapping.cost = current.cost + 1
                    unvisitedMapping.pathToDst = current

        # dijkstra with starting location is this location
        current = getNextCandidate()
    return result


def getDijkstraDistance(dst: StateWrapper, dijkstra: List[DijkstraPathInfo]):
    tarStates = [x.stateWrapper for x in dijkstra]
    if dst not in tarStates:
        return float('inf')
    return next(x.cost for x in dijkstra if x.stateWrapper == dst)


class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """

    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(
            gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(
            len(scores)) if scores[index] == bestScore]
        # Pick randomly among the best
        chosenIndex = random.choice(bestIndices)

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)

        oldFoodList = currentGameState.getFood().asList()
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [
            ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        if newPos in [s.configuration.pos for s in newGhostStates]:
            return float('-inf')
            # return successorGameState.getScore()
        if newPos in oldFoodList:
            return 100

        dist = float('inf')
        for foodPos in oldFoodList:
            manhattanDist = util.manhattanDistance(newPos, foodPos)
            if manhattanDist < dist:
                dist = manhattanDist
        # the closer to the food the better
        return 100-dist


def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()


class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn='scoreEvaluationFunction', depth='2'):
        self.index = 0  # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)


class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        bestAction, _ = self.minimax(gameState, 0, 1)
        return bestAction

    def minimax(self, gameState, agentIndex, depth):
        '''
        return (bestaction, score)
        '''
        agentsCount = gameState.getNumAgents()
        if gameState.isWin() or gameState.isLose() or depth > self.depth:
            score = [Directions.STOP, self.evaluationFunction(gameState)]
            return score

        # minimax
        isMax = agentIndex == 0
        optimalAction = None
        optimalScore = float('-inf')
        if not isMax:
            optimalScore = float('inf')

        actions = gameState.getLegalActions(agentIndex)
        for action in actions:
            newState = gameState.generateSuccessor(agentIndex, action)
            # get new score
            newScore = None
            if agentIndex == agentsCount - 1:
                _, newScore = self.minimax(newState, 0, depth+1)
            else:
                _, newScore = self.minimax(newState, agentIndex+1, depth)
            # update optimal move
            if (isMax):
                if newScore > optimalScore:
                    optimalScore = newScore
                    optimalAction = action
            else:
                if newScore < optimalScore:
                    optimalScore = newScore
                    optimalAction = action
        return [optimalAction, optimalScore]


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        bestAction, _, _, _ = self.minimax(
            gameState, 0, 1, float('-inf'), float('inf'))
        return bestAction

    def minimax(self, gameState, agentIndex, depth, maxi, mini):
        '''
        return (bestaction, score)
        '''
        agentsCount = gameState.getNumAgents()
        isMax = agentIndex == 0
        if gameState.isWin() or gameState.isLose() or depth > self.depth:
            score = self.evaluationFunction(gameState)
            if (isMax and score > maxi):
                maxi = score
            if (not isMax and score < mini):
                mini = score
            return [Directions.STOP, score, maxi, mini]

        # minimax
        optimalAction = None
        optimalScore = float('-inf')
        if not isMax:
            optimalScore = float('inf')

        actions = gameState.getLegalActions(agentIndex)
        for action in actions:
            # check prune condition
            if (mini < maxi):
                break

            # get new score
            newState = gameState.generateSuccessor(agentIndex, action)
            newScore = None
            if agentIndex == agentsCount - 1:
                _, newScore, _, _ = self.minimax(
                    newState, 0, depth+1, maxi, mini)
            else:
                _, newScore, _, _ = self.minimax(
                    newState, agentIndex+1, depth, maxi, mini)
            if (isMax):
                if newScore > optimalScore:
                    optimalScore = newScore
                    optimalAction = action
                if optimalScore > maxi:
                    maxi = optimalScore
            else:
                if newScore < optimalScore:
                    optimalScore = newScore
                    optimalAction = action
                if optimalScore < mini:
                    mini = optimalScore
        return [optimalAction, optimalScore, maxi, mini]


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        bestAction, _, _, _ = self.minimax(
            gameState, 0, 1, float('-inf'), float('inf'))
        return bestAction

    def minimax(self, gameState, agentIndex, depth, maxi, mini):
        '''
        return (bestaction, score)
        '''
        agentsCount = gameState.getNumAgents()
        isMax = agentIndex == 0
        if gameState.isWin() or gameState.isLose() or depth > self.depth:
            score = self.evaluationFunction(gameState)
            if (isMax and score > maxi):
                maxi = score
            if (not isMax and score < mini):
                mini = score
            return [Directions.STOP, score, maxi, mini]

        # minimax
        optimalAction = None
        optimalScore = float('-inf')
        expectiScore = 0

        if not isMax:
            optimalScore = float('inf')

        actions = gameState.getLegalActions(agentIndex)
        for action in actions:
            # check prune condition
            # if (mini < maxi):
            #     break

            # get new score
            newState = gameState.generateSuccessor(agentIndex, action)
            newScore = None
            if agentIndex == agentsCount - 1:
                _, newScore, _, _ = self.minimax(
                    newState, 0, depth+1, maxi, mini)
            else:
                _, newScore, _, _ = self.minimax(
                    newState, agentIndex+1, depth, maxi, mini)
            expectiScore += newScore * 1.0/len(actions)
            if (isMax):
                if newScore > optimalScore:
                    optimalScore = newScore
                    optimalAction = action
                if optimalScore > maxi:
                    maxi = optimalScore
            else:
                if newScore < optimalScore:
                    optimalScore = newScore
                    optimalAction = action
                if optimalScore < mini:
                    mini = optimalScore
        if isMax:
            return [optimalAction, optimalScore, maxi, mini]
        else:
            return [optimalAction, expectiScore, maxi, mini]


def hDistance(s, t, gameState):
    def updateDijkstra():
        print("calculating dijkstra")
        start = time()
        hDistance.mazeDijkstra = allDijkstra(
            wrapper)
        end = time()
        print("finished, time used: ", end="")
        print(end-start)
    # calculate dijkstra if not yet
    wrapper = GameAdaptor(gameState)
    if hDistance.mazeDijkstra == None:
        updateDijkstra()
    currentPosDijkstra = hDistance.mazeDijkstra[StateWrapper(s)]
    shortestCost = getDijkstraDistance(StateWrapper(t), currentPosDijkstra)
    # some time the state gives a position doesn't exist in the maze
    # i.e. (1.0, 1.5)
    if (shortestCost == float('inf')):
        return manhattanDistance(s, t)
    return shortestCost


hDistance.mazeDijkstra = None


def betterEvaluationFunction(gameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: 
    relevant features: 
    pacman position
    distance to closest food
    number of food left
    distance to closest ghost
    distance to closest capsule
    distance to closest food
    number of food left
    total scare time

    Ideal strategy:
    when pacman is 3 units away from the ghost, ignore ghost and focus on getting food, with preference of getting capsule first
    when pacman is 3 units within the ghost, if the ghost is scared, hunt the ghost, otherwise dodge the ghost

    Bugs:
    I think the state return by the function is sometimes funny because I can get a ghost position at (1.0, 1.5) which doesn't exist in the maze. But if I switch to use manhattan distance in such cases it will overweight other food distances and confuse my pacman.

    Also when the pacman can eat the ghost its not doing so even if the reward is high, I assume there is some implicit intermediate state exists that didn't get captured
    """
    "*** YOUR CODE HERE ***"
    # initialize data, whether useful or not
    pos = gameState.getPacmanPosition()
    availableActionsNo = len(gameState.getLegalActions())
    foods = gameState.getFood().asList()
    capsules = gameState.data.capsules
    ghostStates = gameState.getGhostStates()
    ghostPositions = [s.configuration.pos for s in ghostStates]
    ghostRespawnPositions = [s.start.pos for s in ghostStates]
    scaredTimes = [
        ghostState.scaredTimer for ghostState in ghostStates]
    gameScore = gameState.data.score

    # calculate state value
    if (gameState.isLose()):
        return float('-inf')
    if gameState.isWin() or foods == 0:
        print("winner is me!!")
        return 999999999+gameScore
    # features - ghost distances
    dstToClosestGhost = float('inf')
    dstToAllGhost = 0
    for ghostPos in ghostPositions:
        gDist = hDistance(pos, ghostPos, gameState)
        dstToAllGhost += gDist
        if (gDist < dstToClosestGhost):
            dstToClosestGhost = gDist
    # features - food distances
    dstToClosestFood = float('inf')
    dstToAllFood = 0
    for foodPos in foods:
        fDist = hDistance(pos, foodPos, gameState)
        dstToAllFood += fDist
        if (fDist < dstToClosestFood):
            dstToClosestFood = fDist
    foodsLeft = len(foods)
    # features - capsule distance
    dstToClosestCap = float('inf')
    dstToAllCap = 0
    for capPos in capsules:
        cDist = hDistance(pos, capPos, gameState)
        dstToAllCap += cDist
        if cDist < dstToClosestCap:
            dstToClosestCap = cDist
    # calculating score
    features = [dstToClosestGhost, dstToAllGhost, dstToClosestFood,
                dstToAllFood, foodsLeft, dstToClosestCap, dstToAllCap, availableActionsNo]

    result = 0
    # if dstToClosestGhost == float('inf'):
    #     print(ghostPositions)
    if dstToClosestGhost > 3:
        if dstToClosestCap != 0:
            result += 1.0/dstToClosestCap
            result += 5000/(len(capsules)+1)
        result += 1.0/dstToClosestFood
        result += 5000/(foodsLeft+1)
    else:
        if (sum(scaredTimes) <= 0):
            if (dstToClosestGhost != float('inf')):
                result += -500/dstToClosestGhost
            if availableActionsNo == 2:
                result -= 500
        else:
            result += 1.0/dstToClosestGhost
            result += 7000000/(len(ghostPositions)+1)
    result += gameScore
    return result


# Abbreviation
better = betterEvaluationFunction
