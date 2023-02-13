#include <stdio.h>
#include <stdlib.h>

#define max 20

// DESARROLLADORES:

//		RAMOS HERRERA IVAN ALEJANDRO | @arhcoder.
//  	HERNANDEZ MAGALLANES JORGE ANTONIO.

// DESCRIPCIÓN:

//		Programa que calcula la matriz de adyacencia de un grafo,
//      a partir de sus datos ingresados. El algoritmo solicita la
//      cantidad de nodos del grafo, si es un grafo DIRIGIDO, además
//      de si es un MULTIGRAFO. En caso de ser un grafo NO dirigido,
//      pide al usuario sólo los datos del triángulo superiror.

//      Además de calcular la matriz de adyacencia del grafo, utiliza
//      el algoritmo de Warshall para obtener sus componentes conexos,
//      además de que imprime la sucesión de matrices booleanas
//      generadas en el proceso de "avance".


int Matrix[max][max];
int PathMatrix[max][max];
int nodes, edges, directionated, multi;
int startIndex, row, column;
int election, index;

// Imprime una matriz //
void showMatrix(int matrix[max][max], int nodes)
{
    /// Recibe la matriz de un grafo.
    /// Dependiendo de la cantidad de nodos, imprime la matriz.
    for (int row = 0; row < nodes; row++)
    {
        for (int column = 0; column < nodes; column++)
        {
            printf("[%i]", matrix[row][column]);
        }
        printf("\n");
    }
}

int main()
{
    system("cls");

    printf("\n| INTRODUZA LOS DATOS DEL GRAFO |\n");
    printf("________________________________________________________________\n\n");

    // Pregunta si el grafo es direccionado, mientras el resultado sea 1 o 0.
    do
    {
        printf("* %cEl Grafo es dirigido?\n  [S%c = 1 | No = 0]: ", 168, 161);
        scanf("%i", &directionated);
    }
    while(directionated != 1 && directionated != 0);

    do
    {
        printf("\n* %cEl Grafo tiene bucles?\n  [S%c = 1 | No = 0]: ", 168, 161);
        scanf("%i", &multi);
    }
    while(multi != 1 && multi != 0);

    // Pregunta por la cantidad de nodos a representar.
    do
    {
        printf("\n* Cantidad de nodos: ");
        scanf("%i", &nodes);
    }
    while (nodes <= 0);
    printf("________________________________________________________________\n\n");
    
    // Recorre las filas de la matriz para rellenarla.
    for (row = 0; row < nodes; row++) // Filas.
    {
        // StartIndex controla la columna por la que se quiere preguntar.
        if(directionated == 0 && multi == 0) // Sin dirección y SÍ es multigrafo.
        {
            startIndex = row + 1; // Preguntará sólo por el triángulo superior de la matriz.
        }
        else if(directionated == 0 && multi == 1) // Sin dirección y SÍ es multigrafo.
        {
            startIndex = row + 0;
        }
        else // Con dirección.
        {
            startIndex = 0; // Preguntará por toda la matriz.
        }

        // Recorre las columnas de la matriz para rellenarlas.
        for (column = startIndex; column < nodes; column++) // Columnas.
        {
            // Si está en la diagonal.
            if(row == column)
            {
                // Si SÍ es multigrafo.
                if(multi == 1)
                {
                    printf("\n|||||||| Cantidad de bucles del nodo %i: ", row+1);
                    scanf("%i", &edges);
                    Matrix[row][column] = edges * 2;
                }

                // Si NO es multigrafo.
                else
                {
                    Matrix[row][column] = 0;
                }
            }
            // Si el grafo es direccionado.
            else if(directionated == 1)
            {
                printf("\nCantidad de aristas de %i %c %i: ", row+1, 175, column+1);
                scanf("%i", &Matrix[row][column]);
            }
            else
            {
                printf("\nCantidad de aristas entre los nodos %i y %i: ", row+1, column+1);
                scanf("%i", &edges);
                Matrix[row][column] = edges;
                Matrix[column][row] = edges;
            }     
        }       
    }
    system("cls");

    // Imprime la matriz de adyacencia.
    printf("\n________________________________________________________________\n\n");
    printf("| MATRIZ DE ADYACENCIA |\n________________________________________________________________\n\n");
    showMatrix(Matrix, nodes);
    printf("________________________________________________________________\n\n");

    // Despliega el "menú" //
    do
    {
        printf("* %cDesea calcular los componentes conexos del grafo?\n  [S%c = 1 | Salir = 0]: ", 168, 161);
        scanf("%i", &election);
    }
    while(election != 1 && election != 0);

    // Calcula los componentes conexos del grafo.
    printf("\n________________________________________________________________\n");
    if(election == 1)
    {
        // Se copia la matriz de adyacencia en la matriz de camino.
        for(row = 0; row < nodes; row++)
        {
            for(column = 0; column < nodes; column++)
            {
                PathMatrix[row][column] = Matrix[row][column];
            }
        }

        // Se inicia el algoritmo de Warshall.
        for(index = 0; index < nodes; index++)
        {
            // Se recorren filas.
            for(row = 0; row < nodes; row++)
            {
                // Se recorren columnas.
                for(column = 0; column < nodes; column++)
                {
                    // Condicional de avance //
                    PathMatrix[row][column] =
                    (PathMatrix[row][column] || (PathMatrix[row][index] &&
                    PathMatrix[index][column]));
                }
            }

            // Se imprime la matriz booleana //
            if(index != nodes - 1)
            {
                printf("\n\n* Iteraci%cn %i:\n\n", 162, index + 1);
                showMatrix(PathMatrix, nodes);
            }
        }
        printf("\n________________________________________________________________\n\n");
        
        // Imprime la matriz resultado //
        printf("| MATRIZ RESULTADO |\n________________________________________________________________\n\n");
        showMatrix(PathMatrix, nodes);
    }

    printf("\n________________________________________________________________\n\n");
    system("pause");
}