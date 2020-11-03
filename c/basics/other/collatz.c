#include <cs50.h>
#include <stdio.h>

long long int collatz(long long int x);

int main(void)
{
    printf("Number: ");
    long long int num = get_long_long();
    if (num < 1)
    {
        printf("Positive numbers only\n");
        return 1;
    }
    printf("%lli steps\n", collatz(num));
    return 0;
}

long long int collatz (long long int n)
{
    if (n == 1)
        return 0;
    else if (n % 2 == 0)
        return 1 + collatz (n / 2);
    else
        return 1 + collatz (3 * n + 1);
}