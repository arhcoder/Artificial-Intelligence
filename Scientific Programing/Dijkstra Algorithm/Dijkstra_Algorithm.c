#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <stdbool.h>

#define n 8

// DESARROLLADORES:

//		RAMOS HERRERA IVAN ALEJANDRO | @arhcoder.
//  	HERNANDEZ MAGALLANES JORGE ANTONIO.

// DESCRIPCIÓN:

//		PROGRAMA QUE ENCUENTRA EL CAMINO MÁS CORTO ENTRE LOS NODOS DE 
//		UN GRAFO, ATRAVEZ DEL ALGORITMO DE dijkstra Y MUESTRA LA SUMA DEL PESO
//		GENERADO EN EL RECOCORRIDO DEL GRAFO, ADEMÁS DE INDICAR SI EXISTE UN CAMINO EN
//		ESPECIFICO.

// Matriz del grafo //
int matrix[n][n] =
{
	{ 0, 3, 1, 0, 0, 0, 0, 0 },
	{ 3, 0, 0, 1, 0, 0, 5, 0 },
	{ 1, 0, 0, 2, 0, 5, 0, 0 },
	{ 0, 1, 2, 0, 4, 2, 0, 0 },
	{ 0, 0, 0, 4, 0, 0, 2, 1 },
	{ 0, 0, 5, 2, 0, 0, 0, 3 },
	{ 0, 5, 0, 0, 2, 0, 0, 0 },
	{ 0, 0, 0, 0, 1, 3, 0, 0 },
};
char nodes[n] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'};

int minNode(int costs[], int doneNodes[])
{
    int minCost = INT_MAX;
	int minNode;

    for (int index = 0; index < n; index++)
	{
        if (doneNodes[index] == false && costs[index] <= minCost)
		{
			minCost = costs[index], minNode = index;
		}
	}
    return minNode;
}

void dijkstra()
{
    int costs[n];
	int doneNodes[n] = {0};

    for (int index = 0; index < n; index++)
	{
        costs[index] = INT_MAX;
	}
    costs[0] = 0;

    for (int i = 0; i < n - 1; i++)
	{
		int min = minNode(costs, doneNodes);
        doneNodes[min] = 1;

		int j;
		for (j = 0; j < n; j++)
		{
			if (!doneNodes[j] && matrix[min][j] && costs[min] != INT_MAX && costs[min] + matrix[min][j] < costs[j])
			{
				costs[j] = costs[min] + matrix[min][j];
			}
		}

		if(costs[j] > i)
		{
			printf("=> %c ", nodes[i + 1]);
		}
    }
	printf("\n\n* Costo:  %i ", costs[n] - 1);
}

int main()
{
	// Se activa la librería de Windows para los acentos //
	system("chcp65001");
	system("cls");

	int i, j, ini, fin;
	int opc;

	// Imprime la matriz //
	printf("\n_____________________________________________\n");
    printf("\n| MATRIZ DE PESOS DEL GRAFO |");
	printf("\n_____________________________________________\n\n");
	for (int column = 0; column < n; column++)
	{
		for (int row = 0; row < n; row++)
		{
			printf("[%i]", matrix[column][row]);
		}
		printf("\n");
	}
	printf("_____________________________________________\n");

	// Menú de consulta para el usuario //
	int election;
    do
    {
        printf("\n* ¿Desea calcular la distancia entre A y H?\n  [Sí = 1 | Salir = 0]: ");
        scanf("%i", &election);
    }
    while(election != 1 && election != 0);

	if (election == 1)
	{	
		printf("\n_____________________________________________\n");
		printf("\n| RECORRIDO MÁS CORTO ENTRE A => H |");
		printf("\n_____________________________________________\n\nA ");

		dijkstra();

		printf("\n_____________________________________________\n\n");
		system("pause");
	}
	else
	{
		system("cls");
		system("pause");
	}
}