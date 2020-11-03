#include <stdio.h>
#include <cs50.h>

int main(void)
{
    printf("non-negative numerator: ");
    double numerator = get_double();
    if (numerator < 0)
    {
        printf("Invalid input\n");
        return 1;
    }

    printf("positive denominator: ");
    double denominator = get_double();
    if (denominator < 0.1)
    {
        printf("Invalid input\n");
        return 2;
    }

    printf("%.2lf%%\n", numerator/denominator*100);

    return 0;
}