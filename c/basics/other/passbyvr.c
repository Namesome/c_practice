#include <stdio.h>

void decrement_passed_by_value(int a)
{
    a--;
}
void decrement_passed_by_reference(int* a)
{
    (*a)--;
}

int main(void)
{
    int a = 4;
    decrement_passed_by_value(a);
    printf("%d\n", a);
    decrement_passed_by_reference(&a);
    printf("%d\n", a);
}