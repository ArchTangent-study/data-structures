// Binary Tree structure in C for practice purposes.
// Notes:
// - be mindful of pass by value (copy) vs by reference (pointer).

#include <stdio.h>
#include <assert.h>

// Each Child can have 0, 1, or 2 child indexes.
struct Child {
    char name[16];
    int  ix;
    int  left;
    int  right;
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
    printf("Child [%d] '%s': %d, %d\n", c.ix, c.name, c.left, c.right);
}

void printTree(struct BTree *t) {
    assert(t->count >= 0);

    printf("BTree: ");
    if (t->count == 0) {
        printf("empty\n");
        return;
    }
    printf("\n");
    int i;
    for (i = t->count; i > 0; i--) {
        printf(" - ");
        printChild(t->vals[i - 1]);
    }
}

// Adds a Child to the BTree if not full.
void pushChild(struct BTree *t, struct Child c) {
    printf("[pushChild] c address: %p\n", &c);
    printf("[pushChild] t address: %p\n", &t);

    printf("[pushChild] Child [%d] '%s': %d, %d\n", c.ix, c.name, c.left, c.right);

    printf("pushing child...\n");
    if (t->count < t->size) {
        t->vals[t->count] = c;
        t->count++;
        printf("[pushChild] t.count is %d\n", t->count);
    } else {
        printf("BTree of size %d is full!\n", t->size);
    }
}

int main()
{
    struct Child c0 = {"1st", 0, -1, -1};
    struct BTree t0 = newBTree();

    printf("[main] c0 address: %p\n", &c0);
    printf("[main] t0 address: %p\n", &t0);

    pushChild(&t0, c0);
    printChild(c0);
    printTree(&t0);
    printf("count: %d", t0.count);

    return 0;
}
