#include <stdio.h>
#include <cs50.h>

bool valid_triangle(float a, float b, float c);

int main(void)
{
    float a = get_float();
    float b = get_float();
    float c = get_float();
    
    bool result = valid_triangle(a, b, c);
    if (result == 0)
    {
        printf("INVALID TRIANGLE\n");
    }
    else
    {
        printf("VALID TRIANGLE\n");
    }
}

bool valid_triangle(float a, float b, float c)
{
    if (a < 1 || b < 1 || c < 1)
    {
        return false;
    }
    if ((a + b <= c) || (a + c <= b) || (b + c <= a))
    {
        return false;
    }
        return true;       
}