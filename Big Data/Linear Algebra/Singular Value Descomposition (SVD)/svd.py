import numpy as np
from read import read_matrix
# from eigen import eigen

# Función para la descomposición de una
# matriz por SVD:
def svd(matrix):

    '''
        Recibe una matriz de numpy;

        Calcula los componentes de la matriz SVD;

        Retorna U, Sigma, V;
        Considerando "matrix" como "A";
        Donde:
            * U: Matriz ortogonal de vectores
            singulares izquierdos.

            * Sigma: Matriz diagonal con valores
            singulares de A.

            * V: transpuesta de la matriz ortogonal
            de vectores singulares derechos.
    '''

    # Obtiene A * A^T:
    A_AT = np.dot(matrix, matrix.T)

    # Obtiene los eigen valores y vectores:
    # eigenvalues, eigenvectors = eigen(A_AT)
    eigenvalues, eigenvectors = np.linalg.eig(A_AT)

    # Calcula los valores singulares SIGMA:
    sigma = np.sqrt(eigenvalues)
    U = eigenvectors

    # Se obtiene V:
    V = np.dot(matrix.T, U) / sigma

    return U, sigma, V

# IMPLEMENTACIÓN:
matrix = read_matrix()
U, S, V = svd(matrix)

print("\nPARA LA MATRIZ:")
for row in matrix:
    for data in row:
        print(f"[{data}]", end="")
    print()

print(f"\n * Eigenvalores: {S ** 2}")
print(f" * Eigenvectores:\n{U}\n")
print(f" * Derechos:\n{V}")