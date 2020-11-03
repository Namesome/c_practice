#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <cs50.h>

int main(void)
{
    printf("Message: ");
    char *string = get_string();
    int len = strlen(string);
    int alpha_num = 0;

    for (int i = 0; i < len; i++)
    {
        if (!(isalpha(string[i])) && string[i] != ' ')
        {
            printf("Invalid input\n");
            return 1;
        }
    }

    for (int i = 0; i < len; i++)
    {
        if (isalpha(string[i]))
        {
            if (alpha_num % 2 == 0)
            {
                string[i] = toupper(string[i]);
                alpha_num++;
            }
            else
            {
                string[i] = tolower(string[i]);
                alpha_num++;
            }
        }
        else if (string[i] == ' ')
        {
            printf(" ");
        }
        printf("%c", string[i]);
    }

    printf("\n");

    return 0;
}