#include <cs50.h>
#include <stdio.h>

int main(void)
{
    printf("Give me a number between 1 and 23: ");
    int n = get_int();

    if (n < 1 || n > 23)
    {
        printf("Input not in range\n");
        return 1;
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = n; j > 0; j--)
        {
            printf("#");
        }
        printf("\n");
    }

    return 0;
}