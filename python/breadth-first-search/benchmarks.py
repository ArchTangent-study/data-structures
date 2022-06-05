# Breadth-First Search (BFS) benchmarking.
import breadth_first_search_1, breadth_first_search_2 ,breadth_first_search_3
import timeit

from typing import Any, Dict, Optional
from collections import deque

def bench_bfs_1(suite):
    for graph, source, target in suite:
        bfs = breadth_first_search_1.breadth_first_search(graph, source, target)

def bench_bfs_2(suite):
    for graph, source, target in suite:
        bfs = breadth_first_search_2.breadth_first_search(graph, source, target)

def bench_bfs_3(suite):
    for graph, source, target in suite:
        bfs = breadth_first_search_3.breadth_first_search(graph, source, target)

if __name__ == "__main__":
    suite = [
        ({'A': ['B']}, 'A', 'B'),
        ({'A': ['B']}, 'C', 'B'),
        ({'A': ['B','C'],'C': ['D']}, 'A', 'D'),
        ({'A': ['B','C'],'C': ['D']}, 'A', 'E'),
        ({'A': ['B','C'],'C': ['D']}, 'B', 'D'),
        ({'A': ['B','D'],'B': ['C','J'],'D': ['G','H'],'E': ['C'],'H': ['E']}, 'A', 'C'),
        ({'A': ['B','D'],'B': ['C','J'],'D': ['G','H'],'E': ['C'],'H': ['E']}, 'D', 'C'),
    ]

    bfs_2 = timeit.timeit(
        'bench_bfs_2(suite)',
        setup='from __main__ import bench_bfs_2, suite'
    )

    bfs_3 = timeit.timeit(
        'bench_bfs_3(suite)',
        setup='from __main__ import bench_bfs_3, suite'
    )

    # Since BFS1 mutates the graph in-place, test it last
    bfs_1 = timeit.timeit(
        'bench_bfs_1(suite)',
        setup='from __main__ import bench_bfs_1, suite'
    )

    print("BFS 1 (Recursive, Mut)")
    print(f"  time: {bfs_1}")

    print("BFS 2 (Recursive, Imm)")
    print(f"  time: {bfs_2}")

    print("BFS 3 (Queue)")
    print(f"  time: {bfs_3}")
