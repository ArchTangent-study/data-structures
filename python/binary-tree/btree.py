# Binary Tree in Python
# TODO: add testing

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.ix_less = None  # index of value that is <= self
        self.ix_more = None  # index of value that is > self
    def __repr__(self) -> str:
        return f"Node {self.val}: ({self.ix_less},{self.ix_more})"

class BTree:
    def __init__(self) -> None:
        self.nodes = []
        self.next = 0

    def add_node(self, node):
        print(f"Adding Node {node}...")
        if self.nodes.__len__() == 0:
            print(f"Tree is empty, adding to index 0")
            self.nodes.append(node)
            self.next += 1
        else:
            for child in self.nodes:
                if self.compare(node, child):
                    break

    def compare(self, n1, n2) -> bool:
        """Compares two Nodes and returns true if a valid place is found"""
        if n1.val <= n2.val:
            print(f"n1 ({n1.val}) is <= n2 ({n2.val})")
            if n2.ix_less is None:
                print("n2.ix_less is None")
                n2.ix_less = self.next
                self.nodes.append(n1)
                self.next += 1
                return True
            else:
                print("n2.ix_less is not None")
                self.compare(n1, self.nodes[n2.ix_less])
        elif n1.val > n2.val:
            print(f"n1 ({n1.val}) is > n2 ({n2.val})")
            if n2.ix_more is None:
                print("n2.ix_less is None")
                n2.ix_more = self.next
                self.nodes.append(n1)
                self.next += 1
                return True
            else:
                print("n2.ix_less is not None")
                self.compare(n1, self.nodes[n2.ix_more])
        return True

    def __repr__(self) -> str:
        """String representation of the Node and L/R child Node **values**"""
        result = []
        for node in self.nodes:
            v = node.val
            c1 = (None if node.ix_less is None else self.nodes[node.ix_less].val)
            c2 = (None if node.ix_more is None else self.nodes[node.ix_more].val)
            result.append(f"    Node {v}: ({c1}, {c2})")
        return '\n'.join(result)

if __name__ == "__main__":
    print("--- BTREE ---")
    vals = [4, 8, 5, 7, 6, 2, 4, 9, 5, 1]
    # vals = [4, 8, 5]
    tree = BTree()
    for val in vals:
        tree.add_node(Node(val))
    print(f"Tree:\n{tree}")
    print(f"Sort: {sorted(vals)}")
