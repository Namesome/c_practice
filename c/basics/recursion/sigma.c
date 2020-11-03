#include <cs50.h>
#include <stdio.h>

int sigma (int n);

int main(void)
{
    // ask user for a positive integer
    int n;
    do
    {
        printf("Enter a positive integer: ");
        n = get_int();
    }
    while (n < 1);

    // report answer
    printf("%i\n", sigma(n));
}

int sigma(int n)
{
    // base case when n is 0
    if (n == 0)
    {
        return 0;
    }
    // recursive case otherwise
    return n + sigma(n - 1);
}