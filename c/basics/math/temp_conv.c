#include <stdio.h>
#include <cs50.h>

int main(void)
{
    printf("Temperature in F: ");
    float f = get_float();
    float c = (f - 32) * 5/9;
    printf("Temperature in C: %.2f\n", c);
    return 0;
}