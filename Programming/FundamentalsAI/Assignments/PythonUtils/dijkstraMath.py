from typing import *


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


if __name__ == "__main__":
    unvisited = set()
    pass
