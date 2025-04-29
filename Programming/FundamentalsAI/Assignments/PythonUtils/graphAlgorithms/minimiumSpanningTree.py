from typing import List, Tuple
from structures.node import node


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
                if(new_successor in graph and new_successor not in visited_locations):
                    edge_q.append(new_edge)
    return result_edges
