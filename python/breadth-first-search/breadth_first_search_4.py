"""Breadth-First-Search (BFS) - Double Buffer, using a {Node:List[Node]} graph."""
from typing import Dict, Optional


def breadth_first_search(graph: Dict, src, tgt) -> Optional[int]:
    """Returns depth where target is first found, or None if not found."""
    if src == tgt:
        return 0
    
    if src not in graph:
        return None

    qa = [edge for edge in graph[src]]
    qb = []

    seen = {src}
    depth = 1

    while qa or qb:
        while qa:
            node = qa.pop()

            if node == tgt:
                return depth
            if node in seen:
                continue

            seen.add(node)
            
            for edge in graph.get(node, ()):
                qb.append(edge)

        depth += 1
        qa, qb = qb, qa

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
