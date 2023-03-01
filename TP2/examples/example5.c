int main()
{
    float a_number;
    float another_number;
    bool boolean;
    a_number = 5;
    another_number = 3;
    boolean = true;

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