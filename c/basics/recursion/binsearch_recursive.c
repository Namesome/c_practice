#include <cs50.h>
#include <stdio.h>

#define SIZE 8

bool search(int n, int array[], int lower, int upper)
{
    // if n is not in array
    // return false
    if (lower > upper)
    return false;

    // define middle
    int middle = (lower + upper) / 2;

    // if n is at middle
    if (n == array[middle])
    {
        return true;
    }
    // if n is left of middle
        // search left half
    else if (n < array[middle])
    {
        return search(n, array, lower, middle - 1);
    }
    // if n is right of middle
        // search right half
    else
    {
        return search(n, array, middle + 1, upper);
    }
}

int main(void)
{
    int numbers[SIZE] = { 4, 8, 15, 16, 23, 42, 50, 108 };
    printf("> ");
    int n = get_int();
    if (search(n, numbers, 0, SIZE - 1))
    {
        printf("YES\n");
    }
    else
    {
        printf("NO\n");
    }
}