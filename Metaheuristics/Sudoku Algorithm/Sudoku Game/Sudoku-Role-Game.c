#include <stdio.h>
#include <stdlib.h>
#include <time.h>

//////////////////////////////////////////////////////////////////////////////////

// DESARROLLADORES:

//		RAMOS HERRERA IVAN ALEJANDRO | @arhcoder.

// DESCRIPCIÓN:
	/*
		JUEGO DE ROL DE SUDOKU, EN DONDE EL USUARIO COMPITE
        CONTRA LA PC EN TURNOS ALTERNADOS. AMBOS JUGADORES
        DEBEN COMPLETAR UN TABLERO DE SUDOKU DADO, CON
        POSIBILIDAD DE SALTAR TURNOS, AQUEL QUE COLOQUE EL
        ÚLTIMO NÚMERO DEL TABLERO, SERÁ EL GANADOR.
	*/
//		
//////////////////////////////////////////////////////////////////////////////////

// Tamaño del sudoku;
#define n 9

// Error programado para la máquina.
// Un 34% de las veces, la máquina fallará / saltará
// su turno, para equilibrar la competitividad.
#define machineError 34

// Tiempo de espera de la máquina mientras responde; en segundos.
#define machineDramaThinkingTimeInSeconds 2

// FUNCIONES PARA CONTROLAR EL DISEÑO EN PANTALLA //
void instructions()
{
    // Limpia la pantalla //
    system("cls");

    // Despliega las instrucciones del juego.
    printf("\n______________________________________________________________________________\n");
    printf("\n\n\t\t\t| SUDOKU ROLE GAME |\n\n");
    printf("\n______________________________________________________________________________\n");
    printf("\nInstrucciones:\n");
    printf("\n* Se siguen las mismas reglas de un tablero de Sudoku.");
    printf("\n* El juego se lleva a cabo por turnos entre el usuario (tú) y la PC.");
    printf("\n* Cuando sea tu turno, decide si colocar un número, o saltar el turno.");
    printf("\n* Si decides colocar un número, especifica las coordenadas y el número.");
    printf("\n* Si el número ingresado es incorrecto, tu turno se perderá.");
    printf("\n* La computadora puede acertar, fallar y saltar turnos según le convenga.");
    printf("\n\n* El jugador que coloque el ÚLTIMO NÚMERO del Sudoku, GANARÁ.");
    printf("\n\n______________________________________________________________________________\n");
    printf("\n¿Estás listo para jugar?\n\n");
    system("pause");
    system("cls");
}
void print(int sudoku[n][n])
{
    printf("\n_____________________________________\n");
    printf("\n\t    | SUDOKU |\n\n");
    printf("😎   (1)(2)(3)  (4)(5)(6)  (7)(8)(9)\n\n");
	for (int row = 0; row < n; row++)
	{
        // Números que indican el número de fila.
        printf("(%i)  ", row + 1);
		for (int column = 0; column < n; column++)
        {
            // Imprime las casillas vacías.
            if (sudoku[row][column] == 0) printf("[ ]");
            // Imprime las casillas con datos.
            else printf("[%i]", sudoku[row][column]);

            // Separación de bloques de 3 x 3.
            // Imprime un salto de línea extra cada tres filas.
            if ((row + 1) % 3 == 0 && column == n - 1) printf("\n");
            // Imprime un espacio extra cada tres columnas.
            if ((column + 1) % 3 == 0) printf("  ");
        }
		printf("\n");
	}
    printf("_____________________________________\n");
}

// FUNCIONES PARA SOLUCIONAR EL SUDOKU //
int canPut(int sudoku[n][n], int row, int col, int number)
{
    /// Recibe la matriz del sudoku, un par de coordenadas y un número.
    /// Regresa 1 si el número se puede colocar el las coordenadas.

	// Si ya se colocó el número en la fila.
	for (int x = 0; x <= 8; x++)
    {
        if (sudoku[row][x] == number) return 0;
    }

    // Si ya se colocó el número en la fila.
	for (int x = 0; x <= 8; x++)
    {
        if (sudoku[x][col] == number) return 0;
    }

	// Si ya se colocó el número en la la matriz 3 x 3.
	int startRow = row - row % 3;
    int startCol = col - col % 3;

	for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            if (sudoku[i + startRow][j + startCol] == number) return 0;
        }
    }
	return 1;
}
int solve(int sudoku[n][n], int row, int col)
{
    /// Recibe una matriz de sudoku y las coordenadas
    /// donde empieza a resolver.
    /// Regresa 1 si el sudoku tiene solución.
    /// Regresa 0 si el sudoku no tiene solución.

    // Condicional de detención recursiva.
	if (row == n - 1 && col == n)
    {
        return 1;
    }

    // Se avanza a la siguiente columna.
	if (col == n)
	{
		row++;
		col = 0;
	}

    // Si la casilla ya contiene un número que no sea 0.
	if (sudoku[row][col] > 0)
    {
        return solve(sudoku, row, col + 1);
    }

    // Intenta agregar números del 1 al 9.
	for (int num = 1; num <= n; num++)
	{
        // Verifica si es posible poner el número del 1 al 9.
		if (canPut(sudoku, row, col, num)==1)
		{
            // Coloca el número.
			sudoku[row][col] = num;

            // Validando con la siguiente columna, verifica que
            // el número colocado sea válido.
			if (solve(sudoku, row, col + 1) == 1)
            {
                return 1;
            }
		}

        // Hace retroceso eliminando el número colocado.
        // Paso de Backtracking para recorrer el árbol de soluciones.
		sudoku[row][col] = 0;
	}
	return 0;
}

// FUNCIONES PARA MANEJAR LOS TURNOS DE JUEGO //
void userPutANumber(int sudoku[n][n], int solution[n][n])
{
    /// Recibe la matriz del tablero de sudoku actual y la solución.
    /// Pide al usuario hacer su turno en el tablero actual.

    // Limpia la consola y muestra el estado actual del sudoku.
    system("cls");
    print(sudoku);

    int row, column, number, skipnt;
    printf("\n\n| SU TURNO |\n");

    // Pregunta si desea colocar un número o saltar el turno.
    do
    {
        printf("\n¿Desea colocar un número?\n[1 = Sí][0 = Saltar turno]:\n");
        scanf("%i", &skipnt);
    }
    while (skipnt != 0 && skipnt != 1);

    if (skipnt == 1)
    {
        // Pregunta el número de fila.
        do
        {
            printf("\nNÚMERO DE FILA: ");
            scanf("%i", &row);
        }
        while (row < 1 || row > n);

        // Pregunta el número de columna.
        do
        {
            printf("\nNÚMERO DE COLUMNA: ");
            scanf("%i", &column);
        }
        while (column < 1 || column > n);

        // Pregunta el número a ingresar.
        do
        {
            printf("\nNÚMERO A COLOCAR: ");
            scanf("%i", &number);
        }
        while (number < 1 || number > n);

        // Si el número es correcto según la solución,
        // lo inserta, sino, pasa de largo.
        if(solution[row - 1][column - 1] == number)
        {
            sudoku[row - 1][column - 1] = number;
            printf("\n * %i colocado en [%i][%i] correctamente...\n\n", number, row, column);
        }
        else
        {
            printf("\n * Número incorrecto...\n\n");
        }
    }
    else
    {
        printf("\n * Usted saltó turno...\n\n");
    }

    system("pause");
    system("cls");
}
void machinePutANumber(int sudoku[n][n], int solution[n][n])
{
    /// Recibe la matriz del tablero de sudoku actual y la solución.
    /// Genera un número aleatorio, que servirá para definir
    /// si la máquina falla, salta turno o tira correctamente.
    /// Desición con respecto a la constante "machineError".

    // Limpia la consola y muestra el estado actual del sudoku.
    system("cls");
    print(sudoku);

    // Espera 2 segundos para darle drama.
    printf("\n\n| TURNO DE LA PC |\n");
    printf("\nPensando...\n");
    sleep(machineDramaThinkingTimeInSeconds);

    // Número aleatorio entre 1 y 100.
    srand(time(NULL));
    int random = (rand() % (100 - 1 + 1)) + 1;

    // Si la máquina acierta.
    if (random > machineError)
    {
        // Encuentra un par de coordenadas vacías.

        // Primero elige una coordenada aleatoriamente.
        srand(time(NULL));
        int row = (rand() % (n - 1));
        int col = (rand() % (n - 1));

        // La PC escaneará todas las casillas desde ese
        // punto ([row][col]), buscando una vacía, si
        // llega hasta el final sin encontrar nada, va
        // al principio y repite el proceso.

        int voidSpaceLocated = 0;
        while (voidSpaceLocated == 0)
        {
            if (sudoku[row][col] == 0)
            {
                // Hace un tiro acertado.
                sudoku[row][col] = solution[row][col];
                printf("\n * La PC colocó %i en [%i][%i] correctamente...\n\n", solution[row][col], row + 1, col + 1);
                voidSpaceLocated = 1;
            }
            else
            {
                // Si ya llegó al final del tablero.
                if (row == n - 1 && col == n - 1)
                {
                    row = 0;
                    col = 0;
                }
                // Si llegó al final de la fila.
                else if (col == n - 1)
                {
                    col = 0;
                    row++;
                }
                else
                {
                    col++;
                }
            }  
        }
    }
    // La máquina falla.
    else
    {
        // En la mitad de los casos, fallará.
        if (random % 2 == 0)
        {
            printf("\n * La PC falló su turno...\n\n");
        }
        // En la otra mitad de casos, saltará el turno.
        else
        {
            printf("\n * La PC saltó su turno...\n\n");
        }
    }

    system("pause");
    system("cls");
}
int isTheGameOver(int sudoku[n][n], int solution[n][n])
{
    /// Recibe la matriz del tablero de sudoku actual y la solución.
    /// Compara ambas soluciones para saber si el juego terminó.
    /// Si ambas matrices son iguales, el resultado es 1, sino; 0.

    for (int row = 0; row < n; row++)
    {
        for (int col = 0; col < n; col++)
        {
            if (sudoku[row][col] != solution[row][col])
            {
                return 0;
            }
        }
    }
    return 1;
}

// FUNCIÓN DE EJECUCIÓN //
int main()
{
    // Activa tildes en consola de Windows.
    system("chcp 65001");
    system("cls");

    // Muestra las instrucciones //
    instructions();

    // Sudoku inicial //
    int sudoku[n][n] =
    {
        { 0, 6, 0, 1, 0, 4, 0, 5, 0 },
        { 0, 0, 8, 3, 0, 5, 6, 0, 0 },
        { 2, 0, 0, 0, 0, 0, 0, 0, 1 },
        { 8, 0, 0, 4, 0, 7, 0, 0, 6 },
        { 0, 0, 6, 0, 0, 0, 3, 0, 0 }, 
        { 7, 0, 0, 9, 0, 1, 0, 0, 4 },
        { 5, 0, 0, 0, 0, 0, 0, 0, 2 },
        { 0, 0, 7, 2, 0, 6, 9, 0, 0 },
        { 0, 4, 0, 5, 0, 8, 0, 7, 0 },
    };
    print(sudoku);

    // Sudoku de solución //
    int solution[n][n];

    // Se copia el contenido de la matriz inicial del sudoku
    // en la matriz "solution", y en esta se va a colocar la solución.
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            solution[i][j] = sudoku[i][j];
        }
    }

    // Se calcula la solución del sudoku.
    solve(solution, 0, 0);

    // Interacción con el usuario //
    int turn = 0;
    int gameOver = 0;

    // Se entra en el ciclo de juego por turnos.
    while (gameOver == 0)
    {
        // Si turno = 0 tira el usuario.
        if (turn == 0)
        {
            // Se efectúa el turno.
            userPutANumber(sudoku, solution);

            // Si el usuario terminó el juego.
            if (isTheGameOver(sudoku, solution) == 1)
            {
                print(sudoku);
                printf("\n\n* ¡FELICIDADES, GANASTE EL JUEGO!\n\n");
                gameOver = 1;
            }
        }
        // Si turno = 1 tira la máquina.
        else
        {
            // Se efectúa el turno.
            machinePutANumber(sudoku, solution);

            // Si la máquina terminó el juego.
            if (isTheGameOver(sudoku, solution) == 1)
            {
                print(sudoku);
                printf("\n\n* ¡LÁSTIMA, LA PC GANÓ EL JUEGO!\n\n");
                gameOver = 1;
            }
        }

        // Cambia de turno.
        if  (turn == 0) turn = 1;
        else turn = 0;
    }

    printf("\n\n");
    system("pause");
    system("cls");
}