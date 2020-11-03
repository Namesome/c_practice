#include <cs50.h>
#include <stdio.h>

int main(int argc, string argv[])
{
    // array storage for ints
    int arr[5] = {0};
    // collect and store ints
    for(int i = 0; i < 5; i++)
    {
        arr[i] = get_int();
    }
    // calculate mean
    float sum = 0;
    for(int i = 0; i < 5; i++)
    {
        sum += arr[i];
    }
    // print mean
    printf("Mean is: %.2f\n", sum/5);
}