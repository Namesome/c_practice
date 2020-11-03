#include <cs50.h>
#include <stdio.h>
#include <ctype.h>

int main (void)
{
    // Collect user input
    printf("Please enter an alphabetical character: ");
    char c = get_char();

    // If letter is uppercase
    //if (isupper(c))
    //if ((int) c >= 65 && (int) c <= 90)
    if (c >= 'A' && c <= 'Z')
        printf("Thank you for the uppercase letter!\n");

    // If the letter is lowercase
    else if (islower(c))
        printf("Thank you for the lowercase letter!\n");

    // If not an alphabetical character
    else
        printf("You did not enter an alphabetical character!\n");
}