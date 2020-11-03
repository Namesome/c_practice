#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // get multiple from user
    printf("Give me a number between 1 and 100: ");
    int n = get_int();
    if (n < 1 || n > 100)
    {
        printf("Invalid number\n");
        return 1;
    }

    int m = n;
    int n_max = 100/n;

    // iterate from multiple through 100
    // if not first, print comma and space - ... but also if not last
    // print number
    for (int i = 0; i < n_max; i++)
    {
        if (i < n_max - 1)
        {
            printf("%i", m);
            m = n + m;
            printf(", ");
        }
        else
        {
            printf("%i", m);
            m = n + m;
        }
    }
    printf("\n");

    return 0;
}