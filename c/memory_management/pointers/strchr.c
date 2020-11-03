#include <stdio.h>
#include <cs50.h>

char* my_strchr(char* str, char c)
{
    while(*str != '\0')
    {
        if(c == *str)
        {
            return "FOUND";
        }
        str++;
    }
    return NULL;
}

int main(void)
{
    printf("String: ");
    char* str = get_string();
    printf("Character: ");
    char c = get_char();
    printf("Looking for substring...\n");
    char* result = my_strchr(str, c);
    if (result == NULL)
    {
        printf("Couldn't find %c.\n", c);
    }
    else
    {
        printf("Substring: %s \n", result);
    }
}