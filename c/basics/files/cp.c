#include <stdio.h>

int main(int argc, char* argv[])
{
    if (argc != 3)
    {
        printf("Usage: cp source destination\n");
        return 1;
    }

    //copy the contents of argv[1] to argv[2]

    // open up the source file
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Invalid input file\n");
        return 2;
    }

    // now open up the destination file
    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        printf("Invalid output file\n");
        return 3;
    }

    // read the contents of the source file one char (int!) at a time

        // write the character to the destination file!

    int c;
    while ((c = fgetc(input)) != EOF)
    {
        fputc(c, output);
    }

    // you leak memory if you forget to close!
    fclose(input);
    fclose(output);

    return 0;
}
