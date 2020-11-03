#include <stdio.h>
#include <ctype.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Correct usage: ./bitcap <lowercase letter>\n");
        return 1;
    }
    if (argv[1][1] != 0)
    {
        printf("Only one letter allowed\n");
        return 2;
    }
    
    if (islower(argv[1][0]))
    {
        printf("Capitalized: %c\n", argv[1][0] & 0b11011111);
    }
    else if(isupper(argv[1][0]))
    printf("Uppercase letter!\n");
    else
    printf("Not a letter\n");

    return 0;
}