#include <cs50.h>
#include <stdio.h>

double accumulate_interest(double balance, double rate);

int main(void)
{
    printf("Starting balance: ");
    double start = get_double();
    printf("Annual interest rate: ");
    double interest = get_double();
    double updated = accumulate_interest(start, interest);
    printf("Updated balance: %.2f\n", updated);
}

double accumulate_interest(double balance, double rate)
{
    int sum = balance * (1 + rate);
    return sum;
}