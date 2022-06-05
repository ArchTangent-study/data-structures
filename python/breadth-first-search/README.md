# Breadth-First Search (BFS)

Breadth-First Search implementations in Python, with unit testing available via `pytest`.

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

## Testing

Ensure that `pytest` is installed, then run one of the following:
- `pytest breadth_first_search_1.py`
- `pytest breadth_first_search_2.py`
