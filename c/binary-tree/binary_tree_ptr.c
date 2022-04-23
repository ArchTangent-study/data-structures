// Binary Tree with pointers, done as an exercise.
// Nodes only take integers, for simplicity.
#include <stdio.h>

struct TreeNode {
    int data;
    struct TreeNode *left;
    struct TreeNode *right;
};

void printNode(struct TreeNode *n) {
    if(!n) {
        printf("Node: Null");
    }
    printf("Node: %d", n->data);
}

int main() {
    struct TreeNode root = {0, 0, 0};
    printNode(&root);

    return 0;
}
