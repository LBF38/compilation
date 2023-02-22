int main()
{
    float a_number = 5.0;
    float another_number = 3.0;
    bool boolean = false;

    while (boolean == true)
    {
        if (a_number > another_number)
        {
            a_number = a_number - another_number;
        }
        else
        {
            another_number = another_number - a_number;
        }
    }
}