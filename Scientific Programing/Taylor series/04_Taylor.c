#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define x 10

// Escrito por Alejandro Ramos | @arhcoder.

unsigned long factorial(int number)
{
    unsigned long factorial = 1;    
    for (int i = 1; i <= number; i++)
    {
        factorial = factorial * i;
    }
    return factorial;
}

int main()
{
    float currentTerm = 0;
    float previousTerm = -1;
    float sum = 0;
    int i = 0;

    system("chcp 65001");
    system("cls");
    printf("____________________________________________\n\n");
    printf("|  SERIE DE MCLOUREN PARA: e^x con x = %i  |\n", x);
    printf("____________________________________________\n\n");
    printf("| i |\t  | TÉRMINO |\t     | SUMA |\n");
    printf("____________________________________________\n\n");

    while (previousTerm != currentTerm)
    {
        previousTerm = currentTerm;
        currentTerm = (exp(0) / factorial(i)) * pow(x, i);
        sum += currentTerm;

        printf("  %i\t   %f\t      %f\n", i, currentTerm, sum);
        i++;
    }

    printf("____________________________________________\n\n");
    printf(" * Valor real:\t\t%f\n * Valor obtenido:\t%f\n", exp(x), sum);
    printf("____________________________________________\n\n");
    system("pause");
}