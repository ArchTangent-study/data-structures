// Binary Tree structure in C.

#include <stdio.h>

// Each Child can have 0, 1, or 2 child indexes.
struct Child {
    char name[20];
    int  ix;
    int  child1;
    int  child2;
};

struct BTree {
    struct  Child vals[10];
    int     count;
    int     size;
};

// BTree default constructor.
struct BTree newBTree() {
    struct BTree t1;
    t1.size = 10;
    return t1;
}

void printChild(struct Child c) {
    printf("Child [%d] '%s': %d, %d\n", c.ix, c.name, c.child1, c.child2);
}

void printTree(struct BTree t) {
    printf("BTree:\n");
    int i;
    for (i = 0; i < t.count; i++) {
        printChild(t.vals[i]);
    }
}

int main()
{
    struct Child c0 = {"1st", 0, -1, -1};
    struct BTree t1 = newBTree();

    printChild(c0);
    printTree(t1);

    return 0;
}
