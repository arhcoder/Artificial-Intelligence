#include "tsp.hpp"

using namespace std;

/// CONSTRUCTOR ///
ACOTSP::ACOTSP(int ncities, string instanceFile)
{
    /// @brief Instancia de una una resolución de
    /// Algoritmo de Colonia de hormigas para la
    /// resolución de TSP.

    /// @param ncities contiene la cantidad de
    /// ciudades de la instancia TSP.

    /// @param instanceFile contiene la ruta
    /// del archivo csv del que se extraerá la
    /// matriz de adyacencia del grafo de ciudades.

    // Guarda los datos para instanciar el objeto:
    cities = ncities;
    citiesFilePath = instanceFile;

    // Crea la matriz de ciudades:
    /* int i;
    roads = new int *[cities];
    for (i = 0; i < cities; i++)
        roads[i] = new int[cities];*/
}