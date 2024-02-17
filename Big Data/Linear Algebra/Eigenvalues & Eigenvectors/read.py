import numpy as np

# Función para leer y construir una matriz desde consola:
def read_matrix():

    # Define el tamaño de la matriz:
    print("\nTamaño de la matriz")
    columns = int(input("* Columnas: "))
    rows = int(input("* Filas: "))

    # Recolecta los datos de la matriz:
    matrix = []
    for row in range(rows):
        print(f"\nFila {row+1}")
        data = []
        for column in range(columns):
            data.append(float(input(f"  * Dato {column+1}: ")))
        matrix.append(data)
    
    # Retorna una matrix de numpy: 
    return np.array(matrix)