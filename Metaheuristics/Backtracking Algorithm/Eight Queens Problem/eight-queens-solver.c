#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define n 8
int solutions = 0;

/// Algoritmo de Backtracking que calcula todas
/// las soluciones del problema de las n reinas.

/// El algoritmo es especial para 8 reinas.

/// Para la representación de soluciones del
/// problema, se utilizará únicamente un vector
/// de n espacios. Puesto que la naturaleza del
/// ejercicio sigue las reglas de: 1. Cada columna
/// contiene sólo un número; 2. Cada fila contiene
/// sólo un número; utilizar una matriz de n x n
/// que simbolice todo el tablero, sería desperdiciar
/// espacio en memoria, puesto que por cada fila y
/// por cada columna se inocuparían n - 1 espacios.

/// De este modo, EL ÍNDICE DEL VECTOR REPRESENTA
/// EL NÚMERO DE FILA en la que está colocada la
/// reina, y EL NÚMERO DENTRO DEL VECTOR REPRESENTA
/// EL NÚMERO DE COLUMNA donde la reina se encuentra.

/// Reinas[2] = 2:
/// Reina en FILA 2 COLUMNA 4; (2, 4);

/// Los resultados del ejercicio -representados en
/// una matriz de n x n como ya se especificó-, se
/// plasmarán en un archivo .json, que se colocará
/// en internet y se le dará uso de API, para que
/// la aplicación "EIGHT QUEENS GAME ONLINE",
/// desarrollada igualmente por @arhcoder, alojada en:
/// "https://github.com/arhcoder/eight-queens-game/",
/// acceda a esta, y plasme sobre pantalla alguna de
/// las soluciones obtenidas, aleatoriamente.

/// NOTA: La API guardará todas las soluciones del
/// vector, como una lista.

/// FUNCIONES SOLUCIONADORAS ///
int canPut(int queens[], int position)
{
    /// Recibe el vector de una solución, y el índice
    /// en el que se plantea colocar una nueva reina;
    /// Si es posible colocarla, resulta 1; sino, 0.

    // NOTA: Un axioma del ajedrez indica que; si
    // teniendo el par de coordenadas de un par de
    // piezas, se calcula la diferencia entre sus
    // números de fila, y la diferencia entre sus
    // números de columna; el resultado será igual
    // siempre que estén ambas piezas en la misma
    // diagonal; derecha o izquierda.

    for (int i = 0; i < position; i++)
    {
        if
        (
            // Si la columna ya está ocupada.
            queens[i] == queens[position] ||
            // Si las diagonales ya están ocupadas.
            abs(position - i) == abs(queens[position] - queens[i])
        )
        return 0;
    }
    return 1;
}
void solve(int solution[], int queens)
{
    /// Función recursiva que recibe un vector
    /// de soluciones, y la cantidad de reinas
    /// que ya se han colocado. Se llama a así
    /// mismo validando cada que la solución
    /// siga siendo óptima. Y termina por
    /// rellenar el vector con las coordenadas
    /// correctas.

    /// Al algoritmo es de tipo "backracking",
    /// este aprovecha la función llamada
    /// "canPut()", para comprobar todo el
    /// tiempo, si la colocación secuencial de
    /// reinas es correcta; es decir, coloca
    /// una a una las reinas en órden, mientras
    /// se puedan colocar, y cuando encuentra
    /// un punto en donde no puede colocar más,
    /// regresa en el camino secuencialmente,
    /// en forma de árbol de desición que recorre
    /// por profundidad cada posible solución,
    /// mejorando el camino cada que se estanca. 

    // Si ya se colocaron todas las reinas.
    if (queens == n)
    {
        // El algortimo recursivo ha terminado.
        // Imprime la solución [solution].
        solutions++;
        printf("%2i. [ ", solutions);
        for (int i = 0; i < n; i++)
        {
            printf("%i ", solution[i] + 1);
        }
        printf("]\n");

        // Escribe en el archivo json de la API, la solución.
        writeASolutionIntoTheJSONFile(solution);
    }
    else
    {
        // Se expande el árbol de soluciones en profundidad.
        // Este ciclo sigue la secuencia de colocar reinas.
        for (solution[queens] = 0; solution[queens] < n; solution[queens]++)
        {
            // Comprueba si es posible colocar una reina en la posición actual.
            if (canPut(solution, queens))
            {
                solve(solution, queens + 1);
            }
        }
    }
}

/// FUNCIONES DE CREACIÓN DE API ///
void createJSONTemplate()
{
    /// Esta función crea la base del archivo .json
    /// en el que se guardarán las soluciones del
    /// algoritmo para posteriormente ser consumidas
    /// a modo de API.

    // Crea el archivo de texto vacío en el directirio
    // en que se ejecuta el ejecutable; como archivo de
    // atributo escribible "w".
    FILE* file = fopen("eight-queens-solutions.json", "w");

    // Escribe en el archivo la estructura de la api json.
    fprintf(file, "{\"solutions\":[");

    // Saca de RAM y pasa al disco duro el archivo editado.
    fclose(file);
}
void writeASolutionIntoTheJSONFile(int solution[])
{
    /// Recibe una solución en vector de enteros, y
    /// la escribe dentro del template del archivo json.

    // Abre el puntero de archivo en memoria.
    // Usa la propiedad "a", para sólo añadir "append"
    // texto extra al archivo abierto.
    FILE* file = fopen("eight-queens-solutions.json", "a");

    // Convierte la solución de parámetro en una lista json.
    char textSolution[36] = "[";
    int startByte = 1;

    // Concatena cada entero.
    for (int i = 0; i < n; i++)
    {
        startByte += sprintf(&textSolution[startByte], "\"%i\"", solution[i]);
        if (i < n - 1)
        {
            startByte += sprintf(&textSolution[startByte], "%c", 44);
        }
    }
    strcat(textSolution, "]");

    if (solutions < 92) strcat(textSolution, ",");
    if (solutions == 92) strcat(textSolution, "]}");

    // Agrega al archivo, la nueva solución.
    fprintf(file, textSolution);
    fclose(file);
}

int main()
{
    // Limpia la consola en que se ejecuta.
    system("cls");

    // Arreglo principal de soluciones.
    int Queens[n];

    // Se rellena el arreglo con -1 (espacios vacíos).
    for (int i = 0; i < n; i++)
    {
        Queens[i] = -1;
    }

    // Crea el nuevo archivo json de la API.
    createJSONTemplate();

    // Ejecuta el algoritmo.
    printf("\n| SOLUCIONES CON N = %i |\n\n", n);
    solve(Queens, 0);

    printf("\n");
    system("pause");
    return 0;
}