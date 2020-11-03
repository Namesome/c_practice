#include <assert.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

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

int length(void)
{
    // traverse list
    // count nodes
    int count = 0;
    node *current = head;
    while (current != NULL)
    {
        current = current->next;
        count++;
    }
    // return length
    return count;
}

void free_memory(void)
{
    node *current = head;
    while (head != NULL)
    {
        current = head;
        head = head->next;
        free(current);
    }
}

int main(int argc, char* argv[])
{
    // create linked list
    for (int i = 0; i < SIZE; i++)
    {
        node* new = malloc(sizeof(node));

        if (new == NULL)
        {
            exit(1);
        }
        //printf("%p\n", &head);
        new->n = i;
        //printf("%p\n", new->next);
        new->next = head;
        //printf("%p\n", new->next);
        //printf("%p\n", head);
        head = new;
        //printf("%p\n", head);
        //printf("%i\n", head->n);
        //printf("%p\n", head->next);
    }

    printf("Making sure that list length is indeed %i...\n", SIZE);

    // test length function
    assert(length() == SIZE);
    printf("good!\n");

    free_memory();

    return 0;
}