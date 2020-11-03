#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int n = 0;

    do
    {
       printf("Please enter a positive integer: ");
       n = get_int();
    }
    while (n <= 0);
}