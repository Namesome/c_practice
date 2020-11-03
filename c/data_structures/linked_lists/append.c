#include<stdio.h>
#include<stdlib.h>

#define SIZE 10

typedef struct node
{
    // the value to store in this node
    int n;

    // the link to the next node in the list
    struct node* next;
}
node;

node* head = NULL;

void append(int i)
{
    // build new node
    node *new = malloc(sizeof(node));
    if (new == NULL)
    {
        printf("Couldn't allocate memory\n");
        exit(1);
    }

    // initialize new node
    new->n = i;
    new->next = NULL;
    // traverse list with two pointers // not sure what the 2nd one is for?
    node *current = head;
    //node *previous = NULL;

    // if the list is empty, prepend
    if (head == NULL)
    {
        head = new;
    }
    // else add new node to end of list
    else
    {
        while (current->next != NULL)
        {
            current = current->next;
        }
        //previous = current;
        current->next = new;
    }
}

int main(int argc, char* argv[])
{
    // creating list
    printf("Appending ints 0-%i onto the list...\n", SIZE - 1);
    for (int i = 0; i < SIZE; i++)
    {
        append(i);
    }
    printf("done!\n");

    // printing out list
    printf("Your list contains ");
    for (node*  ptr = head; ptr != NULL; ptr = ptr->next)
    {
        printf("%i ", ptr->n);
    }
    printf("\n");

    return 0;
}