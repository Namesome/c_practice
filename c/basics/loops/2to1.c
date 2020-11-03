#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // iterate from 0 through 25

        // use division and mod to print combos of numbers

    /*for (int i = 0; i < 5; i++)
        for (int j = 0; j < 5; j++)
            printf("i = %d, j = %d\n", i, j);*/

    for (int i = 0; i < 25; i++)
    {
        printf("i = %i, j = %i\n", i / 5, i % 5);
    }
}