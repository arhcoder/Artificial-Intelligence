import numpy as np
from read import read_matrix

# Función para obtener eigenvalores de una matriz
# por el método de la potencia:
def eigen(matrix):

    '''
        Recibe una matriz de numpy;

        Calcula los eigenvalores y eigenvectores
        mediante el método de las potencias;

        Retorna dos valores:
        eigenvalues, eigenvectors;
    '''

    # Valores del modelo:
    iterations = 1000
    max_error = 0.001

    # Inicialización:
    rows = matrix.shape[0]
    x0 = np.array([1] * rows)

    # Iteraciones;
    # Hasta "iterations" o converger con "max_error":
    for iteration in range(iterations):

        # Se encuentra el vector como producto de la matriz
        # y el vector inicial x0:
        y = np.dot(matrix, x0)

        # Se calculan los valores propios:
        # xk = y / || y ||
        xk = y / np.linalg.norm(y)

        # Convergencia:
        eigenvalue = np.dot(xk, np.dot(matrix, xk))

        # Si ya se hizo por lo menos una iteración, se puede
        # hacer una prueba de convergencia con base en la
        # diferencia entre el valor propio calculado en la
        # iteración anterior y en la actual:
        if iteration > 0 and abs(eigenvalue - past_eigenvalue) < max_error:
            break
        
        # Se actualizan los datos para una nueva iteración:
        x0 = xk
        past_eigenvalue = eigenvalue
    
    # Se retornan los mejores valores calculados;
    # Eigenvalor y eigenvector:
    return eigenvalue, xk


# IMPLEMENTACIÓN:
matrix = read_matrix()
eigenvalue, eigenvector = eigen(matrix)

print("\nPARA LA MATRIZ:")
for row in matrix:
    for data in row:
        print(f"[{data}]", end="")
    print()

print(f"\n * Eigenvalor: {eigenvalue}")
print(f" * Eigenvector: {eigenvector}\n")