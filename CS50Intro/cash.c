#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    long int card;
    long int digits;
    card=get_long("Input you card number, please:\n"); // We are getting the number as long, because int is not long enough :-)
    if (card<0)
    {
        printf("Card number is not valid");
    }
    else
    {
        int counter = 0; // we can first check the length before going further
        digits=card;
        do
        {
            digits /= 10; //we are shifting the decimal point by dividing by 10 and when we come to zero the counter will tell us the length. As there is no length function in c for integers
            counter+=1; // each successful division when there is still something before zero gives us counting
        }
        while (digits > 0);
        if ((counter != 13) && (counter != 15) && (counter != 16)) // for input conditions of AMEX, Master and VISA, && is OR operator in C
        {
            printf("INVALID\n"); // as there are no option in the input conditions
        }

        int number[counter];
        for (int i = 0; i < counter; i+=1) // we have counter as the length of the number and we can loop therefore. We need to create a list out of card number digits
        {
            number[i] = card % 10; //by this we are flipping the number
            card = card / 10;
        }
        int typecheck[counter];
        for (int i = 1; i < counter; i+=1)
        {
            typecheck[i] = number[i];//we get the copy of flipped list without first digit. We need it to easily output the type of the card in case - valid
        }
        for (int i = 1; i < counter; i+=2) // we start at index 1 to get every other from second-to-last digit as now we are going along the flipped number, so i+1 will be the second-to-the-last in the original number
        {
            number[i] = number[i] * 2; // here we do the multiplication, step 1 of Luhn's algorithm
        }
        //having the unchanged (but flipped) card number saved as typecheck we can output the type of the card and we need to perform steps 2 and 3 of the algorythm
        int checksum = 0;//that is for further calculations, the trick is to split double digits and summ the number[i] list properly
        int tmp; //temporary summ storage
        if (counter == 13)
        {
        for (int i = 0; i < counter; i+=1)
        {
            tmp = (number[i] % 10) + (number[i]/10 % 10);
            checksum = checksum + tmp;
         }
        if (typecheck[12] == 4 && checksum % 10 == 0) // typecheck12 is the first number for 13 digit Visa
        {
            printf("VISA\n");
        }
        else
        {
            printf("INVALID\n");
        }
        }
        if (counter == 15)
        {
        for (int i = 0; i < counter; i++)
        {
            tmp = (number[i] % 10) + (number[i]/10 % 10);
            checksum = checksum + tmp;
        }
         if (typecheck[14] == 3 && checksum % 10 == 0 && (typecheck[13] == 4 || typecheck[13] == 7))//typecheck14 is the first number for 15 digit Amex
        {
            printf("AMEX\n");
        }
        else
        {
            printf("INVALID\n");
        }
        }
        if (counter == 16)
        {
        for (int i = 0; i < counter; i++)
        {
            tmp = (number[i] % 10) + (number[i]/10 % 10);
            checksum = checksum + tmp;
        }
        if (typecheck[15] == 4 && checksum % 10 == 0)//typecheck15 is the first digit of card number, which is in case of counter 16 shall be either Master or Visa. In case of 4 - this is Visa.
        {
            printf("VISA\n");
        }
        else if (typecheck[15] == 5 && checksum % 10 == 0 && (typecheck[14] == 1 || typecheck[14] == 2 || typecheck[14] == 3 || typecheck[14] == 4 || typecheck[14] == 5))// those are combinations for Master
            {
                printf("MASTERCARD\n");
            }
        else
        {
            printf("INVALID\n"); // as for 16 digits, there are no other options
        }
        }
        return 0;
    }
}    

