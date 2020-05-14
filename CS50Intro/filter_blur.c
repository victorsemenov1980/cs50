{
    for (int h = 0; h < height; h++)
    {
        for (int w = 0; w < width; w++)
        {
            int avgfordiv = 0;
            int neighvalgreen = 0;
            int neighvalblue = 0;
            int neighvalred = 0;

            for (int hh = -1; hh < 2; hh++)
            {
                for (int ww = -1; ww < 2; ww++)
                {
                    if ((h+hh) != height && (w+ww) != width && (h+hh) != -1 && (w+ww) != -1)
                    {
                        //sweep
                        avgfordiv++;//count up for division
                        neighvalgreen += image[h + hh][w + ww].rgbtGreen;
                        neighvalred += image[h + hh][w + ww].rgbtRed;
                        neighvalblue += image[h + hh][w + ww].rgbtBlue;
                    }
                }
            }
            //add values to pixels
             image[h][w].rgbtGreen = (int)(round((float)neighvalgreen / avgfordiv));
             image[h][w].rgbtBlue = (int)(round((float)neighvalblue / avgfordiv));
             image[h][w].rgbtRed = (int)(round((float)neighvalred / avgfordiv));

            //check cap
             if (image[h][w].rgbtGreen <= 255)
                {}
            else
                image[h][w].rgbtGreen %= 255;

            if (image[h][w].rgbtRed <= 255)
                {}
            else
                image[h][w].rgbtRed %= 255;

            if (image[h][w].rgbtBlue <= 255)
                {}
            else
                image[h][w].rgbtBlue %= 255;
        }
    }
    return;
}