#include <stdio.h>
#include <stdlib.h>

#define SIZE 5

typedef struct node
{
    // the value to store in this node
    int n;

    // the link to the next node in the list
    struct node* next;
}
node;

node* head = NULL;

void insert_sorted(int i)
{
    // build new node
    node *new = malloc(sizeof(node));
    // initialize new node
    new->n = i;
    new->next = NULL;
    // traverse list with two pointers
    // break if we find a value larger than i
    node *current = head;
    // if new belongs at head, prepend
    if (head == NULL)
    {
        head = new;
    }
    else if (head->n > new->n)
    {
        new->next = head;
        head = new;
    }

    // else insert in middle or end
    else
    {
        while ((current->next != NULL) && (current->next->n < i))
        {
            current = current->next;
        }
        new->next = current->next;
        current->next = new;
    }
}

int main(int argc, char* argv[])
{
    printf("Inserting %i random ints to the list...\n", SIZE);
    for (int i = 0; i < SIZE; i++)
    {
        insert_sorted(rand() % SIZE);
    }
    printf("done!\n");

    // printing out list
    printf("Your list now contains ");
    for (node*  ptr = head; ptr != NULL; ptr = ptr->next)
    {
        printf("%i ", ptr->n);
    }
    printf("\n");

    return 0;
}