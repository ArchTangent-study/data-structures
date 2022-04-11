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

int main()
{
    struct Child c0 = {"1st", 0, -1, -1};
    printf("Child 1: %s %d %d, %d\n", c0.name, c0.ix, c0.child1, c0.child2);

    return 0;
}
