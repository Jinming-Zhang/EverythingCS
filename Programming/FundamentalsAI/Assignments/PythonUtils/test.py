from typing import List
from structures.node import node
from graphAlgorithms import minimiumSpanningTree

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


def evaluate_cost(path):
    '''
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


def print_path(path: List[node]):
    for n in path:
        print(n.id + " -> ", end="")
    print("")


def copy_path(path: List[node]):
    copyed_path = []
    for p in path:
        copyed_path.append(p)
    return copyed_path


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


def get_next_in_frontier(frontier: List[List[node]]):
    fn = 999999
    expand = None
    for candidate in frontier:
        gn = evaluate_cost(candidate)
        # heuristic = smart_hn(candidate)
        heuristic = dumb_hn(candidate)
        if gn+heuristic < fn:
            fn = gn+heuristic
            expand = candidate
    frontier.remove(expand)
    return expand


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


# edges = minimiumSpanningTree.find_minimium_spanning_tree([a, b, d, f])
find_min_path()
# print((evaluate_cost([a, f, b, d, e, c, a])))
# print((evaluate_cost([a, b, f, d, e, c, a])))
# print((evaluate_cost([a, d, b, f, e, c, a])))
# print((evaluate_cost([a, e, b, d, f, c, a])))


def evaluate_string_path(string_p):
    actual_path = []
    for p in string_p:
        if p == 'A':
            actual_path.append(a)
        if p == 'B':
            actual_path.append(b)
        if p == 'C':
            actual_path.append(c)
        if p == 'D':
            actual_path.append(d)
        if p == 'E':
            actual_path.append(e)
        if p == 'F':
            actual_path.append(f)
    return evaluate_cost(actual_path)


# al = [
#     "ACDFEBA",
#     "AFCDEBA",
#     "AECFDBA",
#     "ABCEFDA",
#     "ADFCEBA",
#     "ADEFCBA",
#     "ADBFECA",
#     "ADCEFBA",
#     "ADCBEFA",
#     "ADCFBEA",
# ]
# for alala in al:
    # print(evaluate_string_path(alala))
# a star
# print_path([a, b, e, d, c, f])
# print((evaluate_cost([a, d, c, f, e, b, a])))
# print((evaluate_cost([a, e, c, f, d, b, a])))
# print((evaluate_cost([a, b, c, d, e, f, a])))
# print(is_goal_state([a, b, c, d, e, f, a]))
# print(is_goal_state([a, b, c, d, e, f, f, a]))
# print(is_goal_state([]))
# print(is_goal_state([a, b, c, d, e, f, f]))
# print(is_goal_state([c, b, d, e, f, a]))
# print(is_goal_state([a, b, c, b, d, e, f, a]))
# print(is_goal_state([a, e, c, d, f, b, a]))
