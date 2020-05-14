#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n;
    do
    n=get_int("Please input the height of the Mario pyramid: \n");
    while (n<1 || n>8);
    
    for (int i=0;i<n;i+=1) // first loop for lines
    {
        for (int s=(n-1)-i; s>0;s-=1) //Here we are making spaces in reverse to hashes
        {
            printf(" ");   

        }
        for (int j=0; j<=i;j+=1) //This and next for loop are for hashes
        {
            printf("#");   

        }
        printf("  ");
        for (int j=0; j<=i;j+=1)
        {
            printf("#");   

        }
        printf("\n");
    }
}
