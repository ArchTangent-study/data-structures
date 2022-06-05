# Breadth-First-Search (BFS) - Recursive, w/mutable {Node:List[Node]} graph.
from typing import Any, Dict, Optional, Set
from copy import copy

def breadth_first_search(graph: Dict, source, target) -> Optional[Any]:
    """Returns depth where target is first found, or None if not found."""
    if source == target:
        return 0
    if source in graph:
        searched = set()
        return bfs_inner(graph, source, target, 1, searched)
                
    # Target was not found
    return None

def bfs_inner(graph: Dict, source, target, depth: int, searched: Set): 
    to_check = []   

    if source in graph and source not in searched:
        for edge in graph[source]:
            if edge == target:
                return depth
            else:
                to_check.append(edge)
        # If target wasn't found at this depth:
        # - remove current node from graph (avoids cycles)
        # - perform BFS on next depth
        del graph[source]
        for new_source in to_check:
            new_bfs = bfs_inner(graph, new_source, target, depth + 1, searched)
            if new_bfs is not None:
                return new_bfs 
    
    # Target was not found
    return None


def test_bfs():
    suite = [
        ({'A': ['B']}, 'A', 'B', 1),
        ({'A': ['B']}, 'C', 'B', None),
        ({'A': ['B','C'],'C': ['D']}, 'A', 'D', 2),
        ({'A': ['B','C'],'C': ['D']}, 'A', 'E', None),
        ({'A': ['B','C'],'C': ['D']}, 'B', 'D', None),
        ({'A': ['B','D'],'B': ['C','J'],'D': ['G','H'],'E': ['C'],'H': ['E']}, 'A', 'C', 2),
        ({'A': ['B','D'],'B': ['C','J'],'D': ['G','H'],'E': ['C'],'H': ['E']}, 'D', 'C', 3),
    ]
    for graph, source, target, expected in suite:
        # Make copy of each graph, since this BFS mutates the graph
        graph = copy(graph)
        assert breadth_first_search(graph, source, target) == expected
