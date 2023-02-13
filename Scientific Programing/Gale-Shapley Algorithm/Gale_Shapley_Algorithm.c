#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Hecho por Alejandro Ramos Herrera @arhcoder.

// Constantes adaptadas al ejercicio solicitado en la práctica.
#define n 3

// Lista de mujeres //
char *Ladies[] =
{
    "Ana",
    "Bea",
    "Clara"
};

// Lista de hombres //
char *Gentelman[] =
{
    "Jorge",
    "Luis",
    "Mario"
};

void showPeople()
{
    /// Se imprime una tabla con las personas del ejercicio.
    printf("\n_____________________________________\n");
    printf("\nPERSONAS DEL EJERCICIO\n_____________________________________\n");
    printf("\nPreferencia de hombres: \n\n");
    printf("| %6s: [%s] [%s] [%s]  | \n",
    Gentelman[0], Ladies[0], Ladies[1], Ladies[2]);
    printf("| %6s: [%s] [%s] [%s]  | \n",
    Gentelman[1], Ladies[1], Ladies[0], Ladies[2]);
    printf("| %6s: [%s] [%s] [%s]  | \n",
    Gentelman[2], Ladies[0], Ladies[1], Ladies[2]);
    
    printf("\n\nPreferencia de mujeres: \n\n");
    printf("| %6s: [%s] [%s] [%s]  | \n",
    Ladies[0], Gentelman[1], Gentelman[0], Gentelman[2]);
    printf("| %6s: [%s] [%s] [%s]  | \n",
    Ladies[1], Gentelman[0], Gentelman[1], Gentelman[2]);
    printf("| %6s: [%s] [%s] [%s]  | \n",
    Ladies[2], Gentelman[0], Gentelman[1], Gentelman[2]);
    printf("\n_____________________________________\n\n");
}

int shePrefers(int peopleMatrix[2 * n][n], int she, int firstMale, int secondMale)
{
    /// Para una mujer [she], con dos individuos como opción; [firstMale], [secondMale],
    /// regresa como resultado su preferencia, [1] para [firstMale]; [2] para [secondMale].
    /// El resultado se calcula con base en la matriz [peopleMatrix].

    for (int i = 0; i < n; i++)
    {
        return
        // Se prefiere al segundo individuo //
        (peopleMatrix[she][i] == secondMale)? 2:
        // Se prefiere al primer individuo //
        (peopleMatrix[she][i] == firstMale)? 1:
        // No se prefiere a ninguno //
        0;
    }
}

void creatingCouples(int peopleMatrix[2 * n][n])
{
    /// Se generan las parejas según la lista de personas.

    // Variables de uso //
    int couple[n];
    int singleMale[n];
    int singles = n;
    int firstMale;
 
    // Se vacían los vectores //
    memset(couple, -1, sizeof(couple));
    memset(singleMale, 0, sizeof(singleMale));

    while (singles > 0)
    {
        // Se escoge al primer hombre para pareja //
        for (firstMale = 0; firstMale < n; firstMale++)
        {
            if (singleMale[firstMale] == 0) break;
        }

        // Se validan las preferencias de mujeres a hombres //
        for (int i = 0; i < n && singleMale[firstMale] == 0; i++)
        {
            int she = peopleMatrix[firstMale][i];
 
 			// Se arman las parejas //
            if (couple[she - n] == -1)
            {
                couple[she - n] = firstMale;
                singleMale[firstMale] = 1;
                singles--;
            }
            else
            {
                int secondMale = couple[she - n];
 
 				// Se rompe una pareja antes formada y se cambia //
                if (shePrefers(peopleMatrix, she, firstMale, secondMale) == 0)
                {
                    couple[she - n] = firstMale;
                    singleMale[firstMale] = 1;
                    singleMale[secondMale] = 0;
                }
            }
        }
    }

    // Se imprimen las parejas por orden //
    system("cls");
    printf("\n_____________________________________\n\n");
    printf("PAREJAS\n_____________________________________\n\n");
    for (int index = 0; index < n; index++)
    {
        if (index + n == 3) printf("%s", Ladies[0]);
        if (index + n == 4) printf("%s", Ladies[1]);
        if (index + n == 5) printf("%s", Ladies[2]);
        if (couple[index] == 0) printf("\t%s\n", Gentelman[0]);
        if (couple[index] == 1) printf("\t%s\n", Gentelman[1]);
        if (couple[index] == 2) printf("\t%s\n", Gentelman[2]);
        printf("\t\t");
	}
}

int main()
{
    // Matriz de personas //
    // De 0 a 5 las personas de la tabla //
    int peopleMatrix[2 * n][n] =
    {
        // Mujeres //
        {3, 4, 5},
        {4, 3, 5},
        {3, 4, 5},

        // Hombres //
        {1, 0, 2},
        {0, 1, 2},
        {0, 1, 2},
    };

    // Se habilitan los acentos en consola de Windows //
    system("chcp 65001");
    system("cls");

    // Se muestra la lista de personas y sus preferencias //
    showPeople();
    system("pause");
    system("cls");

    // Se efectuan el algorítmo //
	creatingCouples(peopleMatrix);
    system("pause");
}