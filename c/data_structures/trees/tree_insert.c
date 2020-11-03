#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int n;
    struct node* left;
    struct node* right;
}
node;

node* root;

bool insert(int val)
{
    // search for insertion point
        // return false if val is already in tree
    node *current = root;
    node *previous = NULL;
    while (current != NULL)
    {
        if (val == current->n)
        {
            return false;
        }
        else if (val > current->n)
        {
            previous = current;
            current = current->right;
        }
        else
        {
            previous = current;
            current = current->left;
        }
    }
    // build new node
    node *new = malloc(sizeof(node));
    if (new == NULL)
    {
        printf("Couldn't allocate memory for node\n");
        return false;
    }
    new->n = val;
    new->left = NULL;
    new->right = NULL;
    // insert new node at insertion point
    if (val > previous->n)
    {
        previous->right = new;
    }
    else
    {
        previous->left = new;
    }
    // return true
    return true;
}

bool search(node* root, int val)
{
    // if root is NULL
    if (root == NULL)
    {
        // return false
        return false;
    }
    // if root->n is val
    if (root->n == val)
    {
        // return true
        return true;
    }
    // if val is less than root->n
    else if (val < root->n)
    {
        // search left child
        return search(root->left, val);
        }
    // if val is greater than root->n
    else
    {
        // search right child
        return search(root->right, val);
    }
}

int main(void)
{
    // create root node
    root = malloc(sizeof(node));
    if (root == NULL)
    {
        printf("Out of memory!\n");
        return 1;
    }
    root->n = 7;
    root->left = NULL;
    root->right = NULL;

    // create more nodes
    node* three = malloc(sizeof(node));
    if (three == NULL)
    {
        printf("Out of memory!\n");
        return 1;
    }
    three->n = 3;
    three->left = NULL;
    three->right = NULL;

    node* six = malloc(sizeof(node));
    if (six == NULL)
    {
        printf("Out of memory!\n");
        return 1;
    }
    six->n = 6;
    six->left = NULL;
    six->right = NULL;

    node* nine = malloc(sizeof(node));
    if (nine == NULL)
    {
        printf("Out of memory!\n");
        return 1;
    }
    nine->n = 9;
    nine->left = NULL;
    nine->right = NULL;

    // link together nodes
    root->left = three;
    root->right = nine;
    three->right = six;

    // testing insert
    for(int i = 0; i < 10; i++)
    {
        printf("Inserting %i ...%s!\n", i, insert(i)? "success" : "fail");
    }
    for(int i = 0; i < 10; i++)
    {
        printf("Tree contains %i? %s\n", i, search(root, i)? "true" : "false");
    }

    return 0;
}