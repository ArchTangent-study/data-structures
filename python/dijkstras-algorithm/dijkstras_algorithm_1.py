# Dijkstra's Algorithm - Version 1
from typing import Dict, List, Optional
from heapq import heappop, heappush


def dijkstra(graph: Dict, source, target) -> Optional[List]:
    """Returns shortest path in (node, cost) form from `source` to `target`.
    
    `graph` is a { node: [ (edge, cost), (edge, cost), ... ] } dict, and all 
    nodes are represented as strings (e.g `A`, `B`, `C`, ...).
    """
    # Table of {node: (parent, running_cost)} used to build the path
    cost_table = { source: ( source, 0 ) }
    # Min heap stores closest (running_cost, node) for *all* nodes in grahph
    closest_costs = [ (0, source) ]

    while len(closest_costs) > 0:
        (closest_cost, closest_node) = heappop(closest_costs)

        # Update cost table with *lower* (parent, running_cost)
        for (edge, cost) in graph[closest_node]:
            new_cost = closest_cost + cost
            if edge not in cost_table or new_cost < cost_table[edge][1]:
                cost_table[edge] = (closest_node, new_cost)

            heappush(closest_costs, (new_cost, edge))

    # No valid path found
    if target not in cost_table:
        return None

    # Construct final path from source -> target
    path = []
    to_node, from_node = target, cost_table[target][0]
    while to_node != source:
        # Cost from parent to child is (cost_to_child - cost_to_parent)
        edge_cost = cost_table[to_node][1] - cost_table[from_node][1]
        path.append((to_node, edge_cost))
        to_node, from_node = from_node, cost_table[from_node][0]
    # Reverse to get source -> target order        
    path.reverse()

    return path
    

def test_dijkstra():
    graph =  {
        'A': [('B', 3), ('C', 5)],
        'B': [('F', 2), ('E', 8)],
        'C': [('D', 2)],
        'D': [('E', 2)],
        'E': [],
        'F': [('E', 5)],
    }
    suite = [
        ('A', 'A', 0),
        ('A', 'B', 3),
        ('A', 'C', 5),
        ('A', 'D', 7),
        ('A', 'E', 9),
        ('A', 'F', 5),
        ('A', 'J', None),        
    ]

    for source, target, expected in suite:
        path = dijkstra(graph, source, target)
        if path is not None:
            cost = sum((pair[1] for pair in path))
        else:
            cost = None

        assert cost == expected
