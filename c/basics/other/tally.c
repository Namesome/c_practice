#include <stdio.h>
#include <string.h>

int main (int argc, char *argv[])
{
    if (argc != 1)
    {
        int len = 0;
        for (int i = 0; i < argc - 1; i++)
        {
            len += strlen(argv[i + 1]);
        }
        printf("%i\n", len);
    }
    else
    {
        printf("Invalid input\n");
    }
}