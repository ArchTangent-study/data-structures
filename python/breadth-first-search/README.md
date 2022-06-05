# Breadth-First Search

Breadth-First Search implementations in Python, with unit testing available via `pytest`.

Edge Cases:
- Source Node == Target Node
- Cyclical graphs
- Invalid Source/Target Node

## Method 1: Recursive (Mutating)

Big Picture:
1. Use a `Dict(Node, List[Node])` as the graph, where all `Node`s are of the same type.
2. Check all `connections` of `source` (starting Node) to see if they equal `target`
    - if so, return the current `depth`
3. If none of the `connection`s match `target`:
    - gather `connections` in a separate list
    - delete current `source` node from the graph (to avoid cycling)
    - recursively perform `breadth_first_search()` for each of the missed connections

Caveats:
- this version mutates the graph in-place which may not be desired.
- this version doesn't work if `source == target`

## Testing

Ensure that `pytest` is installed, then run one of the following:
- `pytest breadth_first_search_1.py`
