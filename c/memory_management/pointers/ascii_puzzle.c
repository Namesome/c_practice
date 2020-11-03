#include <stdio.h>

int main(void)
{
    int s = 65;
    int* t = &s;

    char c = 'I';
    char N = s + 'P' - 'A';
    char B = *t - s + N + 2;
    char E = &s - t + 78;
    char J = *t + 19;
    char I = N + 'A' - s - 1;
    char O = 347/5;

    printf("%c%c%c%c%c%c%c\n", N, I, c, E, J, O, B);
}