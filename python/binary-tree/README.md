# Binary Tree

[Binary Tree](https://en.wikipedia.org/wiki/Binary_tree) implementations in Python, with testing available via `pytest`.

## Traversal Types

Picture the following tree:
```
        1
       / \
      2   3
     / \
    4   5
```

Depth-First:
- Pre-Order: Root -> Left -> Right: `1, 2, 4, 5, 3`
- Post-Order: Left -> Right -> Root: `4, 5, 2, 3, 1`
- In-Order: Left -> Root -> Right: `4, 2, 5, 1, 3`

Breadth-First:
- Level-Order: lowest order (level) first: `1, 2, 3, 4, 5`

## Testing

Ensure that `pytest` is installed, then run one of the following:
- `pytest binary_tree.py`
