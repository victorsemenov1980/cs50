void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        if (width % 2 == 0)
        {
            for (int j = 0; j < width/2; j++)
            {
                RGBTRIPLE temp = image[i][j];
                image[i][j] = image[i][width - j];
                image[i][width - j] = temp;
            }
        }
        else if (width % 3 == 0)
        {
            for (int j = 0; j < (width - 1)/2; j++)
            {
                RGBTRIPLE temp = image[i][j];
                image[i][j] = image[i][width - j];
                image[i][width - j] = temp;
            }
        }
    }
    return;
}

//What is the value of width? Pay attention to that in 
//any case your code has undefined behavior. At least you have to use image[i][width - j -1]