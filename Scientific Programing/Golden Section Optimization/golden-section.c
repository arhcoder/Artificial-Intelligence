// LIBRERÍAS //
#include <stdio.h>
#include <math.h>

// f(x) que se pretende maximizar //
float f(float x)
{
    return 2 * sin(x) - ((x * x) / 10);
}

// Método de la razón dorada //
void goldMAX(float xl, float xu, int maxIterations, float maxError)
{
    // Variables de uso //
    float distance, x1, x2, fx1, fx2, xoptim, error = 0;

    // Se calcula la razón dorada //
    float GOLDEN = (sqrt(5) - 1) / 2;

    // Para la primer iteración se calculan... //
    distance = GOLDEN * (xu - xl);
    x1 = xl + distance;
    x2 = xu - distance;
    fx1 = f(x1);
    fx2 = f(x2);

    // Se imprimen los índices de la tabla de resultados...
    printf("\n\ni\t d\t xl\t xu\t x1\t x2\t fx1\t fx2\t %cptimo\t error\n", 162);

    // Se encuentra el primer óptimo //
    if (fx1 > fx2) xoptim = x1;
    else xoptim = x2;

    // Inicia las iteraciones //
    int i = 1; float xlo = xl, xup = xu;
    for (i = 1; i <= maxIterations; i++)
    {
        // Se calcula el error //
        if (xoptim != 0)
            error = ((GOLDEN - 1) * (-1 * (xu - xl) / xoptim)) * 100;
        
        // Se imprimen los resultados de la iteración //
        printf("%i\t %.4f\t %.4f\t %.4f\t %.4f\t %.4f\t %.4f\t %.4f\t %.4f\t %.2f%c\n", i, distance, xl, xu, x1, x2, fx1, fx2, xoptim, error, 37);

        // Se reevalúa la distancia //
        distance = GOLDEN * distance;

        // Se conserva el intervalo derecho //
        if (fx1 > fx2)
        {
            xoptim = x1;
            xl = x2;
            x2 = x1;
            x1 = xl + distance;
            fx2 = fx1;
            fx1 = f(x1);
        }
        // Se conserva el intervalo izquierdo //
        else
        {
            xoptim = x2;
            xu = x1;
            x1 = x2;
            x2 = xu - distance;
            fx1 = fx2;
            fx2 = f(x2);
        }
        
        // Se corta la ejecución si se encontró el error //
        if (error < maxError) break;
    }

    // Se imprime el óptimo encontrado //
    printf("\n\nPara:\n    f(x) = 2 Sen(x) - (x%c / 10):\n\nSecci%cn dorada:\n    Iteraciones: %i;\n    xInferior = %.1f;\n    xSuperior = %.1f;\n\nM%cximo:\n    f(%.4f) = %.4f;\n\nEs decir:\n    %cptimo: %.4f;\n    Con x = %.4f;\n    Error: %.4f%c;\n\n", 253, 162, i, xlo, xup, 160, xoptim, f(xoptim), 224, f(xoptim), xoptim, error, 37);
}


// PUNTO DE EJECUCIÓN //
int main(int argc, char const *argv[])
{
    // Variables de uso //
    int maxIterations;
    float xu, xl, maxError;
    system("cls");
    printf("\nM%cTODO DE SECCI%cN DORADA\n\n", 144, 224);

    // Se solicitan los parámetros para el método //
    printf("\n* L%cmite inferior: ", 161);
    scanf("%f", &xl);
    
    printf("* L%cmite superior: ", 161);
    scanf("%f", &xu);

    printf("* Iteraciones: ");
    scanf("%i", &maxIterations);

    printf("* M%cnimo error %c: ", 161, 37);
    scanf("%f", &maxError);

    // Ejecuta el método de la sección dorada //
    goldMAX(xl, xu, maxIterations, maxError);

    system("pause");
}