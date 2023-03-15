#include <stdio.h>

typedef struct complex
{
    float real;
    float imag;
} complex;

complex add(complex n1, complex n2)
{
    complex temp;
    temp.real = n1.real + n2.real;
    temp.imag = n1.imag + n2.imag;
    return temp;
}

int main()
{
    complex n1 = {.float = 1, .imag = 3};
    complex n2 = {.float = 2, .imag = 4};
    complex result;
    result = add(n1, n2);
    printf("Sum = %.1f + %.1fi", result.real, result.imag);
    return 0;
}