#include <stdio.h>
#include <stdlib.h>

// DESARROLLADORES:

//		RAMOS HERRERA IVAN ALEJANDRO | @arhcoder.
//  	HERNANDEZ MAGALLANES JORGE ANTONIO.

// DESCRIPCIÓN:
/*
	ALGORITMO QUE POR MEDIO DEL INGRESO DE UNA MATRIZ DE ADYACENCIA DE PESO, PROPORCIONADA POR EL USUARIO, MUESTRA LA MATRIZ DE PESO INGRESADA
	ASI COMO COSTO PARA RECORRER TODOS LOS NODOS DEL GRAFO  Y EL COSTO MINIMO TOTAL QUE SERIA NECESARIO PARA REALIZAR LA TAREA, ASI COMO MOSTRAR EL CAMINO
	QUE SEGUIRIA PARA RECORRER LOS NODOS.
*/

#define nodes 9
#define infinity 9999

// Para fines prácticos del ejercicio, la matriz se declarará directamente en el código.
int matrix[nodes][nodes] =
{
    {0,  6,  0,  10, 0,  0,  8,  0,  0},
    {6,  0,  11, 0,  15, 0,  0,  13, 0},
    {0,  11, 0,  0,  0,  0,  0,  4,  0},
    {10, 0,  0,  0,  6,  0,  0,  0,  0},
    {0,  15, 0,  6,  0,  2,  0,  0,  0},
    {0,  0,  0,  0,  2,  0,  4,  0,  6},
    {8,  0,  0,  0,  0,  4,  0,  0,  5},
    {0,  13, 4,  0,  0,  0,  5,  0,  7},
    {0,  0,  0,  0,  0,  6,  5,  7,  0},
};

int i, j, first, second, nodex1, nodex2, currentNode = 1;
int lower, final, condition;
int parent[nodes];

int find(int i)
{
	while(parent[i])
    {
        i = parent[i];
    }
	return i;
}
int same(int i, int j)
{
	if(i != j)
	{
		parent[j] = i;
		return 1;
	}
	return 0;
}
void kruskal(int xnodes)
{
    printf("\n\n| Camino a recorrer |\n");
    printf("________________________________________\n\n");
    while(currentNode < xnodes)
    {
        for(i = 0, lower = infinity; i < xnodes; i++)
        {
            for(j = 0; j < xnodes; j++)
            {
                if(matrix[i][j] < lower)
                {
                    lower = matrix[i][j];
                    first = nodex1 = i;
                    second = nodex2 = j;
                }
            }
        }

        nodex1 = find(nodex1);
        nodex2 = find(nodex2);

        if (same(nodex1, nodex2))
        {
            // Para imprimir los nodos como texto, se usará ascii //
            // A partir del ascii 65 comienzan las letras mayúsculas //
            printf("* %i: Peso entre (%c) -> (%c) = %i\n", currentNode++, 65 + first, 65 + second, lower);
            final += lower;
        }
        matrix[first][second] = matrix[second][first] = infinity;
    }
    printf("\n * Expansi%cn m%cnima: %i\n", 162, 161, final);
    printf("________________________________________");
}

int main()
{
    system("cls");

    // Variables de uso general //
    int election, row, column, final = 0;

    // Imprime la matriz //
    printf("\n| MATRIZ DE PESO DEL GRAFO |\n");
    printf("________________________________________\n\n");
    for (row = 0; row < nodes; row++)
    {
        for (column = 0; column < nodes; column++)
        {
            printf("[%2i]", matrix[row][column]);
        }
        printf("\n");
    }
    printf("\n________________________________________\n\n");

    // Confirma si se desea realizar el cálculo del algoritmo de Kruskal //
    do
    {
        printf("* %cDesea calcular el %crbol de expansi%cn m%cnima del grafo?\n  [S%c = 1 | Salir = 0]: ", 168, 160, 162, 161, 161);
        scanf("%i", &election);
    }
    while (election != 1 && election != 0);

    // Efectúa el cálculo //
    if (election == 1)
    {
        // Se eliminan los ceros de la matriz //
        for (row = 0; row < nodes; row++)
        {
            for (column = 0; column < nodes; column++)
            {
                if (matrix[column][row] == 0)
                {
                    matrix[column][row] = infinity;
                }
            }
        }

        // Aplica el algoritmo de Kruskal a la matriz de pesos //
        kruskal(nodes);

        // Imprime la matriz resultante //
        printf("\n\n| MATRIZ DE PESO RESULTANTE |\n");
        printf("________________________________________\n\n");
        for (row = 0; row < nodes; row++)
        {
            for (column = 0; column < nodes; column++)
            {
                if (matrix[row][column] == infinity)
                    printf("[ x]");
                else
                    printf("[%2i]", matrix[row][column]);
            }
            printf("\n");
        }
        printf("\n________________________________________\n\n");
    }
    else
    {
        system("cls");
        printf("\nAdiós...\n\n");
    }
    
    system("pause");
    return 0;
}