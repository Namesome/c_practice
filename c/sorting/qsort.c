/* qsort example */
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef struct {
    int winner;
    int loser;
} pair;
pair list[6];


int compare (const void * a, const void * b)
{

  pair *pairA = (pair *)a;
  pair *pairB = (pair *)b;

  return ( (pairB->winner - pairB->loser) - (pairA->winner - pairA->loser) );
}

int main ()
{
    srand ( time(NULL) );

    printf("Before sorting\n");
    for(int i = 0; i < 6; i++){
        list[i].winner = rand()%10;
        list[i].loser = i;
        printf ("Winner = %d Loser = %d Strength = %d\n", list[i].winner, list[i].loser, list[i].winner - list[i].loser);
    }
    printf("AFTER sorting\n");
    qsort (list, 6, sizeof(pair), compare);
    for (int n = 0; n < 6; n++)
         printf ("Winner = %d Loser = %d Strength = %d\n", list[n].winner, list[n].loser, list[n].winner - list[n].loser);
    return 0;
}