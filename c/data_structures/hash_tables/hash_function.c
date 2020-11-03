#include <cs50.h>
#include <ctype.h>
#include <stdio.h>

int hash_function(char* key, int size)
{
    // sum ascii values
    int hash = 0;
    while(*key != '\0')
    {
        hash += toupper(*key) - 'A';
        key++;
    }
    // mod by size to stay w/in bound of table
    return hash % size;
}

int main(int argc, char* argv[])
{
    // get hash table size
    printf("Hash table size: ");
    int size = get_int();

    // get key
    printf("Key: ");
    char* key = get_string();

    // calculate and print index
    printf("The string '%s' is mapped to index %i\n", key,
    hash_function(key, size));

    return 0;
}