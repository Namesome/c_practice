#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <errno.h>
#include <limits.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./dectobin value\n");
        return 1;
    }

    //store input string into variable
    char *string = argv[1];

    //prepare variables for strtoll use - errno for error handling, char * for leftover string
    errno = 0;
    char *leftover;

    //extract integer + leftover string from console input (argv[1])
    long long int value = strtoll(string, &leftover, 10);

    //error handling
    if (errno != 0)
    {
        if (value == LLONG_MAX)
        {
            printf("Overflow\n");
            return 1;
        }
        else if (value == LLONG_MIN)
        {
            printf("Underflow\n");
            return 2;
        }
        else
        {
            printf("Not actually possible?");
            return 3;
        }
    }
    else if (errno == 0)
    {
        if (leftover == string)
        {
            printf("String does not begin with number\n");
            return 4;
        }
        else if (value <= 0)
        {
            printf("Only non-zero whole numbers (positive integers) allowed\n");
            return 5;
        }
        else if (*leftover != '\0')
        {
            printf("Converted numbers: %lli; leftover string: %s\n", value, leftover);
        }
    }

    // create array to store binary digits
    unsigned int array[100];

    //create variable to store binary length
    int j = 0;

    // calculate binary digits by repeatedly modulo (then dividing) by 2
    // store binary digits in array
    for (int i = 0; value > 0; i++)
    {
        array[i] = value % 2;
        value = value / 2;
        j++;
    }

    // print out array in reverse
    printf("Binary representation: ");
    for (int i = 0; i < j; i++)
    {
        printf("%i", array[j - i - 1]);
    }
    printf("\nLength of binary: %i\n", j);

    return 0;
}