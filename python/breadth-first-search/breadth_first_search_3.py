# Breadth-First-Search (BFS) - Queue, using a {Node:List[Node]} graph.
from typing import Any, Dict, Optional
from collections import deque

def breadth_first_search(graph: Dict, source, target) -> Optional[Any]:
    """Returns depth where target is first found, or None if not found."""
    if source == target:
        return 0
    # Queue of (node, depth) pairs
    to_search = deque([(edge, 1) for edge in graph.get(source, ())])
    searched = {source}

    # Remove & search first node in queue, and add edges to back (FIFO)
    while to_search:
        node, depth = to_search.popleft()
        if node == target:
            return depth
        if node in searched:
            continue
        # Get edges of current node and add node to searched (avoid cycling)
        to_search.extend([(edge, depth+1) for edge in graph.get(node, ())]) # type: ignore
        searched.add(node)

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
        assert breadth_first_search(graph, source, target) == expected
