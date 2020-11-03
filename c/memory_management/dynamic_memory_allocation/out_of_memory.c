#include <stdio.h>
#include <stdlib.h>

int *malloc_func()
{
    int *ptr = malloc(1);
    return ptr;
}


int main(void)
{
    int counter = 0;
    int *ptr = malloc(1);
    while (ptr != NULL)
    {
        counter++;
        malloc_func();
        printf("%i\n", counter);
    }
}