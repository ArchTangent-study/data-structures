// Binary Tree structure in C for practice purposes.
// Note: errors seem to be due to copy mechanics (passing as value)

#include <stdio.h>
#include <assert.h>

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
    t1.count = 0;
    t1.size = 10;
    return t1;
}

void printChild(struct Child c) {
    printf("Child [%d] '%s': %d, %d\n", c.ix, c.name, c.child1, c.child2);
}

void printTree(struct BTree t) {
    assert(t.count >= 0);

    printf("BTree: ");
    if (t.count == 0) {
        printf("empty\n");
        return;
    }
    printf("\n");
    int i;
    for (i = t.count; i > 0; i--) {
        printf(" - ");
        printChild(t.vals[i - 1]);
    }
}

// Adds a Child to the BTree if not full.
void pushChild(struct BTree t, struct Child c) {
    printf("pushing child...\n");
    if (t.count < t.size) {
        t.vals[t.count + 1] = c;
        t.count++;
    } else {
        printf("BTree of size %d is full!\n", t.size);
    }
}

int main()
{
    struct Child c0 = {"1st", 0, -1, -1};
    struct BTree t0 = newBTree();

    pushChild(t0, c0);
    printChild(c0);
    printTree(t0);
    printf("count: %d", t0.count);

    return 0;
}
