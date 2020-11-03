#include <cs50.h>
#include <stdlib.h>
#include <stdio.h>
#include <time.h>

#define MAX 5

int main(int argc, string argv[])
{
    // declare array storage for Pokemon
    char *pokemons[MAX] = {0};
    // collect and store Pokemon
    for (int i = 0; i < MAX; i++)
    {
        printf("Give me a Pokemon: ");
        pokemons[i] = get_string();
    }
    // choose and print out random Pokemon
    srand(time(NULL));
    int r = rand() % (4 + 1 - 1) + 1;
    printf("I choose you, %s!\n", pokemons[r]);
}