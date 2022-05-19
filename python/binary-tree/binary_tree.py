# Binary Tree (LeetCode version)
#
# Specifically designed for practicing LeetCode problems.

from typing import List, Optional

class Side:
    LEFT = 1
    RIGHT = 2


class Node:
    def __init__(self, val):
        self.value = val
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

    def left_value(self) -> Optional[int]:
        return self.left.value if self.left else None
    
    def right_value(self) -> Optional[int]:
        return self.right.value if self.right else None

    def __lte___(self, other):
        return self.value <= other.val
    
    def __gt__(self, other):
        return self.value > other.val

    def __repr__(self) -> str:
        return f"Node {self.value}: ({self.left},{self.right})"


class BinaryTree:
    """Binary tree meant to be used with LeetCode.
    
    Representation of LeetCode Trees:
    - represented using an array
    - values in array stores in Pre-Order fashion (root, left, right)
    - null nodes (None) are stored *unless* at end of the array
    - every two nodes added (after 1st), increment `parent_ix` by 1
    - child nodes are filled from left to right

    Example:
    - [3,9,20,null,null,15,7] (both 15 and 7 have null children, but aren't shown)
    """
    def __init__(self, nodes: List[Optional[int]]):
        self.nodes: List[Node] = []
        self.current_ix: int = -1
        self.parent_ix: int = -1
        self.parent_side = Side.RIGHT

        for node in nodes:
            self.add_node(node)

    def add_node(self, val):
        node = Node(val)
        self.nodes.append(node)
        self.current_ix += 1
        side = Side.LEFT if self.current_ix % 2 == 1 else Side.RIGHT

        # If there's a parent node in the tree, assign incoming Node to it
        if self.parent_ix > -1:
            self.assign_child(self.current_ix, self.parent_ix, side)

        if side == Side.RIGHT:
            self.set_next_parent_index()

    def assign_child(self, child_ix, parent_ix, parent_side):
        """Assigns index (pointer) of child node to parent node at given index"""
        parent = self.nodes[parent_ix]
        if parent_side == Side.LEFT:
            parent.left = self.nodes[child_ix]
        else:
            parent.right = self.nodes[child_ix]

    def set_next_parent_index(self):
        """Set parent index to the next non-null Node in the tree."""
        p_index = self.parent_ix + 1
        for new_ix, node in enumerate(self.nodes[p_index:], start=p_index):
            if node.value is not None:
                self.parent_ix = new_ix

    def __len__(self) -> int:
        return len(self.nodes)

    def __repr__(self) -> str:
        """String representation of the Tree as an array"""
        return f"{[n.value for n in self.nodes]}"

    def display(self):
        """Pretty string representation of the Node and L/R child Node **values**"""
        result = ["Tree:"]
        for node in self.nodes:
            if node.value is not None:
                v = node.value
                c1 = (None if node.left is None else node.left.value)
                c2 = (None if node.right is None else node.right.value)
                result.append(f"  Node {v:2}: ({c1}, {c2})")
        print('\n'.join(result))

# ----------------------------- #
# ---------- TESTING ---------- #
# ----------------------------- #

def test_binary_tree():
    suite = [
        (
            [3, 9, 20, None, None, 15, 7], 
            [3, 9, 20, None, None, 15, 7], 
            [9, None, 15, None, None, None, None], 
            [20, None, 7, None, None, None, None], 
            "[3, 9, 20, None, None, 15, 7]",
            7
        ),
        (
            [1, 2, None, 3, None, 4], 
            [1, 2, None, 3, None, 4], 
            [2, 3, None, 4, None, None], 
            [None, None, None, None, None, None], 
            "[1, 2, None, 3, None, 4]",
            6
        ),
        (
            [1, None, 2, None, 3, None, 4], 
            [1, None, 2, None, 3, None, 4], 
            [None, None, None, None, None, None, None], 
            [2, None, 3, None, 4, None, None], 
            "[1, None, 2, None, 3, None, 4]",
            7
        ),
        (
            [1], 
            [1], 
            [None], 
            [None], 
            "[1]",
            1
        ),
        (
            [], 
            [], 
            [], 
            [], 
            "[]",
            0
        ),        
    ]
    for test_data, values, lefts, rights, string, length in suite:
        tree = BinaryTree(test_data)
        assert [node.value for node in tree.nodes] == values
        assert [node.left_value() for node in tree.nodes] == lefts
        assert [node.right_value() for node in tree.nodes] == rights
        assert f"{tree}" == string
        assert len(tree) == length
        