# Breadth-First Search (BFS)

Breadth-First Search implementations in Python, with unit testing available via `pytest`.

These versions of BFS return the `depth` of the first Node found, or `None` if not found.

Edge Cases:
- Source Node == Target Node
- Invalid Source/Target Node
- Cyclical graphs

## Method 1: Recursive (Mutating)

Big Picture:
1. Use a `Dict(Node, List[Node])` as the graph, where all `Node`s are of the same type.
2. Check all `edges` of `source` (starting Node) to see if they equal `target`
    - if so, return the current `depth`
3. If none of the `edge`s match `target`:
    - gather `edges` in a separate list
    - delete current `source` node from the graph (to avoid cycling)
    - recursively perform `breadth_first_search()` for each of the missed edges

Caveats:
- this version mutates the graph in-place which may not be desired.

## Method 2: Recursive (Non-Mutating)

Big Picture:
1. Use a `Dict(Node, List[Node])` as the graph, where all `Node`s are of the same type.
2. Check all `edges` of `source` (starting Node) to see if they equal `target`
    - if so, return the current `depth`
3. If none of the `edge`s match `target`:
    - gather `edges` in a separate list
    - add current `source` to a set of `searched` Nodes (to avoid cycling)
    - recursively perform `breadth_first_search()` for each of the missed edges

## Method 3: Queue

Uses a queue (from `collections.deque`) for fast insertion and deletion from either end of the queue.

Big Picture:
1. Store a `set` of `searched` nodes.
2. Store a queue of `(node, depth)` pairs (`to_search`), starting with `(edge, 1)` for each edge connected to the `source` Node.
3. Repeat steps `4` to `6` while queue is not empty:  
4. Pop the first `(node, depth)` pair from the front of the queue.
5. If the `node` is the `target`: return the `depth`.
6. If `node` is *not* the `target` *and* is *not* in `searched`:
    - add its `edge`s to the end of the queue
    - add the `node` to `searched` (to avoid cycling)
7. If queue is emptied before `target` is found, return `None`.

## Testing

Ensure that `pytest` is installed, then run one of the following:
- `pytest breadth_first_search_1.py`
- `pytest breadth_first_search_2.py`
- `pytest breadth_first_search_3.py`

## Benchmarks

Winner: **Recursive (Mutating)**

Benched using `timeit` in `benchmarks.py`:
1. Recursive (Mutating): `1.385 seconds`
2. Recursive (Non-Mutating): `5.312 seconds`
3. Queue: `8.977 seconds`
