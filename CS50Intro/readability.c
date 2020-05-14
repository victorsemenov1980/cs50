#include <cs50.h>
#include <stdio.h>
#include <math.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>



int main(void)
{
void trimTrailing(char * str);
int i;
int j;
int letters;
int sentences;
float index;
int x;
int L;
int S;
string text=get_string("Enter your text for evaluation:\n");
//I am making array of capital and smal alphabeth letters to count letter by comparison itiratevely. Thus I will exclude punctuation and spaces
char alphabeth[]={'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
int len = strlen(text);
trimTrailing(text);
//function to count words
int word;
word=0;
for(i=0;i<len;i+=1)
	{
		if((text[i]!=' ' && text[i+1]==' ' && text[i]!='.' && text[i]!='!' && text[i]!='?') ||(text[i]!=' ' && text[i+1]=='.')||(text[i]!=' ' && text[i+1]=='!')||(text[i]!=' ' && text[i+1]=='?'))
		{
			word=word+1;
		//	printf("I values %c\n",text[i]);

		}

	}
x=word;

// now we are counting letters and in the next loop sentences or actually the stopping punctuation
letters=0;
sentences=0;
j=0;

for (i = 0; i < len; i+=1)

{
    for (j=0;j<52;j+=1)
    {
        if (text[i]==alphabeth[j])
        {
            letters+=1;


        }
        else
        {
            letters+=0;

        }
    }
}
for (i = 0; i < len; i+=1)
{
    if (text[i]=='.' || text[i]=='!' || text[i]=='?')
    {
        sentences+=1;
    }
    else
    {
        sentences+=0;
    }
}

// now we are putting everything together
L=letters*100/x;
S=sentences*100/x;

index=0.0588 * L - 0.296 * S - 15.8;


//printf("Number of words: %i\n",x);

//printf("Number of letters in text: %i\n",letters);

//printf("Number of sentences: %i\n",sentences);

if (index<1)
    {
    printf("Before Grade 1\n");
    }
else if (index>16)
    {
    printf("Grade 16+\n");
    }
else
    {
    printf("Grade %0.0f\n",index);
    //printf("The reading Grade is: %f\n",index);
    }

}

void trimTrailing(char * str)
{
    int index, i;

    /* Set default index */
    index = -1;

    /* Find last index of non-white space character */
    i = 0;
    while(str[i] != '\0')
    {
        if(str[i] != ' ' && str[i] != '\t' && str[i] != '\n')
        {
            index= i;
        }

        i++;
    }

    /* Mark next character to last non-white space character as NULL */
    str[index + 1] = '\0';
}

