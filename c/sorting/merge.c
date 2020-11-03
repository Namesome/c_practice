#include <stdio.h>

#define SIZE 8

int temp[SIZE] = {0};

//LOGIC FROM https://vinayakgarg.wordpress.com/2012/11/08/merge-sort-program-in-c/, still not sure how exactly it works...
//problems understanding recursion - parameters (array) passing and timing, can't seem to decipher it via debug50 either :/
//try implementing by myself if/when more advanced some day (and understand recursion hopefully) - read C book, solidify knowledge base
void merge (int array[], int start_1, int end_1, int start_2, int end_2)
{
    int index = 0;
    int s_1 = start_1;
    int s_2 = start_2;

    // While there are elements in both subarrays
    // Compare numbers at the start of the subarrays
    // Append smaller to merged array
    while (s_1 <= end_1 && s_2 <= end_2)
    {
        if (array[s_1] <= array[s_2])
        {
            temp[index] = array[s_1];
            index++;
            s_1++;
        }
        else
        {
            temp[index] = array[s_2];
            index++;
            s_2++;
        }
    }

    // While elements remain in subarray 1 (but not subarray 2)
    // Append element to merged array
    while (s_1 <= end_1)
    {
        temp[index] = array[s_1];
        s_1++;
        index++;
    }

    // While elements remain in subarray 2 (but not subarray 1)
    // Append element to merged array
    while (s_2 <= end_2)
    {
        temp[index] = array[s_2];
        s_2++;
        index++;
    }
    for (int i = 0; i < index; i++)
    {
        array[start_1 + i] = temp[i];
    }
}

void sort (int array[], int start, int end)
{
    if (end > start)
    {
        int middle = (start + end) / 2;

        // sort left half
        sort(array, start, middle);

        // sort right half
        sort(array, middle + 1, end);

        // merge the two halves
        merge(array, start, middle, middle + 1, end);
    }
}

int main(void)
{
    int numbers[SIZE] = { 1, 100, 999, 5, 8, 1000, 7, 108};
    for (int i = 0; i < SIZE; i++)
    {
        printf("%i ", numbers[i]);
    }
    printf("\n");
    sort(numbers, 0, SIZE - 1);

    for (int i = 0; i < SIZE; i++)
    {
        printf("%i ", numbers[i]);
    }
    printf("\n");
}