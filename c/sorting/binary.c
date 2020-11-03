#include <cs50.h>
#include <stdio.h>

#define SIZE 8

bool search(int needle, int haystack[], int size)
{
    int upper = size - 1;
    int lower = 0;
    
    while (upper >= lower)
    {
        int middle = (upper + lower) / 2;
        
        if (needle == haystack[middle])
        {
            return true;
        }
        else if (needle < haystack[middle])
        {
            upper = middle - 1;
        }
        else
        {
            lower = middle + 1;
        }
    }
    return false;
    
    // define upper and lower bounds

    // halve array until bounds overlap

        // define middle

        // if needle is at middle
            // return true

        // if needle is left of middle
            // reset upper bound

        // if needle is right of middle
            // reset lower bound

    // return false
}

int main(void)
{
    int numbers[SIZE] = { 4, 8, 15, 16, 23, 42, 50, 108 };
    printf("> ");
    int n = GetInt();
    if (search(n, numbers, SIZE))
    {
        printf("YES\n");
    }
    else
    {
        printf("NO\n");
    }
}