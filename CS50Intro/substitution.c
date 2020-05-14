#include <cs50.h>
#include <stdio.h>
#include <math.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>


int main(int argc, string argv[])
{
    int i;
    int j;
    int n;

    if (argc != 2)
    {
        printf("Usage: %s Key\n", argv[0]);//check if key does exist. In case of error outputs help message with usage
        return 1;
    }

    
    for (i = 0, n = strlen(argv[1]); i < n; i++)
    {
        if (!isalpha(argv[1][i]))
        {
            printf("Key can contain only aplphabetical letters\n");//checking for numbers and other symbols that cannot be in key
            return 1;
        }
    }

    
    int strl = strlen(argv[1]);
    if (strl < 26)
    {
        printf("Only 26-letters-long keys are accepted\n"); // no check that key got 26 chars in it
        return 1;
    }

    
    int counter = 0;
    int cnt = 0;
    for (i = 0; i < strl; i++)
    {
        for (j = 0; argv[1][j] != '\0'; j++)
        {
            cnt++;
            if (argv[1][j] == argv[1][i])
            {
                counter++;
            }
        }
    }

    if (counter != strl)
    {
        printf("Key cannot contain repeated symbols\n");//Check for repeated characters and return error in case
        return 1;
    }

    
    string plaintext = get_string("plaintext: "); // getting the plain text
    printf("ciphertext: ");

    //Encryption
    int textinput = strlen(plaintext);
    for (i = 0; i < textinput; i+=1)
    {
        for (j = 0; j < 26; j+=1)
        {
            if (plaintext[i] == 'a' + j)
            {
                
                if (argv[1][j] >= 'a' && argv[1][j] <= 'i')
                {
                    printf("%c", argv[1][j]);
                }
                else
                {
                    char let1 = argv[1][j] + 32;
                    printf("%c", let1);
                }
            }
            else if (plaintext[i] == 'A' + j)
            {
                
                if (argv[1][j] >= 'a' && argv[1][j] <= 'i')
                {
                    char let2 = argv[1][j] - 32;
                    printf("%c", let2);
                }
                else
                {
                    printf("%c", argv[1][j]);
                }
            }
        }

        //Print non-alphabetical 
        if (!isalpha(plaintext[i]))
        {
            printf("%c", plaintext[i]);
        }

    }

    
    printf("\n");
}
