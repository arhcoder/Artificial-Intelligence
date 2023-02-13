#include <stdio.h>
#include <stdlib.h>

// DESARROLLADORES:

//		RAMOS HERRERA IVAN ALEJANDRO | @arhcoder.
//  	HERNANDEZ MAGALLANES JORGE ANTONIO.

// DESCRIPCIÓN:

//		Programa que construye un árbol binario e introduce
//      números que ordena bajo un esquema de (menores hacia
//      la izquierda, mayores hacia la derecha), y que muestra
//      en PREORDEN, INORDEN y POSTORDEN.

// Estructura de un nodo binario //
struct Binode
{
    int *data;
    struct Binode *first;
    struct Binode *second;
};

// FUNCIONES //
struct Binode *newBinode()
{
    /// Crea un espacio dinámico de memeria de un nuevo nodo binario.
    /// Regresa ese un puntero con ese mismo espacio de memoria.

    struct Binode *node;
    node = (struct Binode*) malloc(sizeof(struct Binode));
    node -> data = (int*) malloc(sizeof(int) * 2);

    // Data inicial //
    node -> data[0] = 0;

    // Dat de control //
    node -> data[1] = -1;

    node -> first = NULL;
    node -> second = NULL;

    return node;
}

void bintreeAppend(struct Binode *node, int data)
{
    /// Inserta un nodo con un núemero entero, dentro un árbol binario.
    /// Recibe la ubicación del árbol y el dato entero.

    if ((node != NULL) && (node -> first == NULL) && (node -> second == NULL))
    {
       node -> data[0] = data; 
       node -> data[1] = 0;

       // Hijo izquierdo//
       node -> first = newBinode();

       // Hijo derecho //
       node -> second = newBinode();
    }
    if (data < node -> data[0]) bintreeAppend(node -> first, data);
    else
    {
        if (data > node -> data[0]) bintreeAppend(node -> second, data);
    }
}


void showBintreePreorder(struct Binode *node)
{
    /// Imprime el árbol con preorden.

    if (node!=NULL)
    {
        if (node -> data[1] != -1)
        {
            printf("%i | ", node -> data[0]);
            showBintreePreorder(node -> first);
            showBintreePreorder(node -> second);
        }
    }
}


void showBintreeInorder(struct Binode *node)
{
    /// Imprime el árbol con inorden.

    if (node!=NULL)
    {
        if (node -> data[1] != -1)
        {
            showBintreeInorder(node -> first);
            printf("%i | ", node -> data[0]);
            showBintreeInorder(node -> second);
        }
    }
}

void showBintreePostorder(struct Binode *node)
{
    /// Imprime el árbol con postorden.

    if (node!=NULL)
    {
        if (node -> data[1] != -1)
        {
            showBintreePostorder(node -> first);
            showBintreePostorder(node -> second);
            printf("%i | ", node -> data[0]);
        }
    }
}

// Punto de ejecución //
int main ()
{
    // Activa la librería número 65001 de Windows para //
    // permitir el uso de caracteres especiales del //
    // código ASCII. SÓLO PARA WINDOWS //
    system("chcp 65001");
    system("cls");

    // Se crea un árbol binario vacío //
    struct Binode *Bintree;
    Bintree = newBinode();

    // Se imprime una descripción del programa //
    printf("\n| ÁRBOLES BINARIOS |\n____________________________\n\n");
    printf("* Descripción: Programa que inserta números enteros\ndentro de un árbol binario e imprime dicho árbol en\ndistintos órdenes.\n\n");
    system("pause");
    system("cls");

    /* TEST
    bintreeAppend(Bintree, 12);
    bintreeAppend(Bintree, 33);
    bintreeAppend(Bintree, 34);
    bintreeAppend(Bintree, 88);
    bintreeAppend(Bintree, 22);
    bintreeAppend(Bintree, 14);
    bintreeAppend(Bintree, 10);
    bintreeAppend(Bintree, 8);
    bintreeAppend(Bintree, 4);
    bintreeAppend(Bintree, 2);
    */

    // MENÚ //
    int election, data;
    do
    {
        printf("\n| ÁRBOLES BINARIOS |\n____________________________\n\n");
        printf("[1]: Agregar un número.\n[2]: Mostrar con Preorden.\n[3]: Mostrar con Inorden.\n[4]: Mostrar con Postorden.\n[5]: Salir.");
        printf("\n\nElige una opción: ");
        scanf("%i", &election);

        system("cls");
        switch (election)
        {
            case 1:
                printf("\n| Número: ");
                scanf("%i", &data);
                bintreeAppend(Bintree, data);
                printf("\n* %i agregado...\n\n", data);
            break;

            case 2:
                printf("\n| ");
                showBintreePreorder(Bintree);
                printf("\n\n");
            break;

            case 3:
                printf("\n| ");
                showBintreeInorder(Bintree);
                printf("\n\n");
            break;

            case 4:
                printf("\n| ");
                showBintreePostorder(Bintree);
                printf("\n\n");
            break;

            case 5:
                printf("\n* Adiós...\n\n");
            break;

            default:
                printf("\n * Opción equivocada...\n\n");
            break;
        }
        
        system("pause");
        system("cls");
    }
    while (election != 5);

    // Imprime el árbol antes de terminar //
    printf("\n| ÁRBOL EN PREORDEN |\n\n| ");
    showBintreePreorder(Bintree);
    printf("\n\n");
    system("pause");
    system("cls");

    printf("\n| ÁRBOL EN INORDEN |\n\n| ");
    showBintreeInorder(Bintree);
    printf("\n\n");
    system("pause");
    system("cls");

    printf("\n| ÁRBOL EN POSTORDEN |\n\n| ");
    showBintreePostorder(Bintree);
    printf("\n\n");
    system("pause");
    system("cls");

    printf("\n\n");
    system("pause");

    return 0;
}