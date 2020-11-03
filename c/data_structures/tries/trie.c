#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>
#include <ctype.h>


#define ALPHABET_SIZE 27


typedef struct trie_node
{
    //marker for end of word
    bool is_word;

    //pointers to other nodes
    struct trie_node *children[ALPHABET_SIZE];
}
trie_node;

trie_node *construct_node(void)
{
    trie_node *new = malloc(sizeof(trie_node));
    if (new == NULL)
    {
        printf("Couldn't allocate space\n");
        return false;
    }
    new->is_word = false;
    for (int i = 0; i < ALPHABET_SIZE; i++)
    {
        new->children[i] = NULL;
    }
    return new;
}


void insert_node(trie_node *root, const char *key)
{
    int level;
    int length = strlen(key);
    int index;
    trie_node *new = root;

    for (level = 0; level < length; level++)
    {
        //convert each char to location in alphabet
        index = toupper(key[level]) - 'A';
        //check alphabet array at current letter location
        //if empty, create new node at current letter location
        if (new->children[index] == NULL)
        {
            new->children[index] = construct_node();
        }
        //link previous alphabet array with next alphabet array at current letter location
        new = new->children[index];
    }
    // end of word
    new->is_word = true;
}

bool search_word(trie_node *root, const char *key)
{
    int level;
    int length = strlen(key);
    int index;

    trie_node *new = root;

    for (level = 0; level < length; level++)
    {
        //convert each char to location in alphabet
        index = toupper(key[level]) - 'A';
        //check alphabet array at current letter location
        //if empty, return false
        if (new->children[index] == NULL)
        {
            return false;
        }
        //if next letter in alphabet array at the location exists, go to it
        new = new->children[index];
    }
    return true;
}

void delete_trie(trie_node *root)
{
    for (int i = 0; i < ALPHABET_SIZE; i++)
    {
        if(root->children[i] != NULL)
        {
            delete_trie(root->children[i]);
        }
    }
    free(root);
}


int main(void)
{
    const char *keys[] = {"a", "ab", "abc", "then", "now", "however", "okay", "sure", "tries", "multiword"};
    char *result[] = {"Not in trie", "In trie"};

    trie_node *root = construct_node();
    for (int i = 0; i < sizeof(keys)/sizeof(keys[0]); i++)
    {
        insert_node(root, keys[i]);
    }

    for (int i = 0; i < sizeof(keys)/sizeof(keys[0]); i++)
    {
        printf("%s --- %s\n", keys[i], result[search_word(root, keys[i])] );
    }

    delete_trie(root);

    return 0;
}