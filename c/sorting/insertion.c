#include <stdio.h>

#define SIZE 8

void sort(int array[], int size)
{
    int temp;
    int j;
    
    for (int i = 1; i < size; i++)
    {
        j = i;
        while (j > 0 && (array[j] < array[j - 1]))
            {
                temp = array[j];
                array[j] = array[j - 1];
                array[j - 1] = temp;
                j--;
            }
    }
    printf("\n");
}
    // iterate through unsorted part of array from l->r

        // iterate through sorted part of array from r->l

            // figure out where in sorted portion element should go

            // shift sorted elements rightward

        // insert element into sorted portion of array

int main(void)
{
    int numbers[SIZE] = { 4, 3, 16, 50, 8, 23, 42, 108 };
    for (int i = 0; i < SIZE; i++)
    {
        printf("%i ", numbers[i]);
    }
    printf("\n");
    sort(numbers, SIZE);
    for (int i = 0; i < SIZE; i++)
    {
        printf("%i ", numbers[i]);
    }
    printf("\n");
}