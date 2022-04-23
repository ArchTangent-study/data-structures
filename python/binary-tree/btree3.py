# Binary Tree - 3nd Version with built-in sorting.

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __lte___(self, other):
        return self.val <= other.val
    
    def __gt__(self, other):
        return self.val > other.val

    def __repr__(self) -> str:
        return f"Node {self.val}: ({self.left},{self.right})"

class BTree:
    def __init__(self):
        self.nodes = []
        self.current = 0

    def add_node(self, val):
        node = Node(val)
        self.nodes.append(node)
        if self.current > 0:
            self.place_node(node)
        self.current += 1

    def place_node(self, n):
        """Finds the Node that has has Node `n` as its child"""
        next = 0
        while next is not None:
            n2 = self.nodes[next]
            if n > n2:
                if n2.right is None:
                    n2.right = self.current
                    next = None
                else:
                    next = n2.right
            else:
                if n2.left is None:
                    n2.left = self.current
                    next = None
                else:
                    next = n2.left

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
    print("--- BTREE (2) ---")

    vals = [4, 8, 5, 7, 6, 2, 4, 9, 5, 1]
    tree = BTree()
    for val in vals:
        tree.add_node(val)
    print(f"Tree:\n{tree}")
    print(f"Sort: {sorted(vals)}")

