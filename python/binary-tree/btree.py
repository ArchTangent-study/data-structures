# Binary Tree structure (list-based) for study purposes.
#
# Assumes a *complete* binary tree. Children are allowed to be null (None).

from collections import deque
from typing import Optional
from enum import Enum

class Side(Enum):
    LEFT = 0
    RIGHT = 1
    def toggle(self):
        if self == self.LEFT:
            self = self.RIGHT
        else:
            self = self.LEFT

class Node:
    # def __init__(self, val: int|None, left: int|None=None, right: int|None=None) -> None:
    def __init__(self, val: Optional[int], left: Optional[int]=None, right:Optional[int]=None) -> None:
        self.val = val
        self.left = left    # index of value that is <= self
        self.right = right  # index of value that is > self
    def __repr__(self) -> str:
        return f"Node {self.val}: ({self.left},{self.right})"

class BTree:
    """Standard list-based BTree structure."""
    def __init__(self) -> None:
        self.nodes = []
        self.next = 0

    def add_node(self, node):
        if self.nodes.__len__() == 0:
            self.nodes.append(node)
            self.next += 1
        else:
            for child in self.nodes:
                if self.compare(node, child):
                    break

    def compare(self, n1, n2) -> bool:
        """Compares two Nodes and returns true if a valid place is found"""
        if n1.val <= n2.val:
            if n2.left is None:
                n2.left = self.next
                self.nodes.append(n1)
                self.next += 1
                return True
            else:
                self.compare(n1, self.nodes[n2.left])
        elif n1.val > n2.val:
            if n2.right is None:
                n2.right = self.next
                self.nodes.append(n1)
                self.next += 1
                return True
            else:
                self.compare(n1, self.nodes[n2.right])
        return True

    def __repr__(self) -> str:
        """String representation of the Node and L/R child Node **values**"""
        result = []
        for node in self.nodes:
            v = node.val
            c1 = (None if node.left is None else self.nodes[node.left].val)
            c2 = (None if node.right is None else self.nodes[node.right].val)
            result.append(f"    Node {v}: ({c1}, {c2})")
        return '\n'.join(result)


if __name__ == "__main__":
    print("--- BTREE ---")

    vals = [4, 8, 5, 7, 6, 2, 4, 9, 5, 1]
    tree = BTree()
    for val in vals:
        tree.add_node(Node(val))
    print(f"Tree:\n{tree}")
    print(f"Sort: {sorted(vals)}")
  
