#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <math.h>

int sum(int x, int y);

int main(void)
{
    int input, input2;
    input = get_int();
    input2 = get_int();
    printf("%i\n", sum(input, input2));
}

int sum(int x, int y)
{
    return x + y;
}