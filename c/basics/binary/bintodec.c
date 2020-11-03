#include <stdio.h>
#include <math.h>

int main(void)
{
    //whole thing can be done with 1 strol call (base 2), but that's no fun
    //if input is int, can also convert via %10 /10

    //initialize array for binary storage
    char binary[] = {1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1};
    printf("Size of array in bytes: %lu\n", sizeof(binary));

    //find out array length (sizeof divison - in case of char 1/1, int maybe 4/1, etc)
    short int array_length = sizeof(binary)/sizeof(binary[0]);
    printf("Array length (string of numbers): %hi\n", array_length);

    if(array_length > 64)
    {
        printf("Input number too large\n");
        return 1;
    }

    //loop to print out binary input
    printf("Binary sequence to be converted: ");
    for (int i = 0; i < array_length; i++)
    {
        printf("%i", binary[i]);
    }
    printf("\n");

    //prepare array to store decimal equivalent numbers in
    unsigned long long int decimal[array_length];

    //loop iterates through each binary number (from char array), checks if it is 0 or 1
    //then according to its position calculates decimal equivalent via power of 2
    for (int i = 0; i < array_length; i++)
    {
        if (binary[i] == 1)
        {
            decimal[i] = pow(2, array_length - 1 - i);
        }
        else if (binary[i] == 0)
        {
            decimal[i] = 0;
        }
        else
        {
            printf("Invalid input detected\n");
            return 2;
        }
    }

    //variable to store the sum of decimals (the final number)
    unsigned long long int sum = 0;

    //loop for summing decimals from array into the final number
    for (int i = 0; i < array_length; i++)
    {
        sum += decimal[i];
    }
    printf("Decimal equivalent: %llu\n", sum);
    return 0;
}