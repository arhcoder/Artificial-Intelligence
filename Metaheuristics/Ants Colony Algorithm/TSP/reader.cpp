#include <string>
#include "tsp.hpp"

using namespace std;

void ACOTSP::InstanceTSP()
{
    // Abre el archivo de TSP:	
    ifstream file;
    file.open(citiesFilePath);
    
    // Separa casilla por casilla:
    string box = "";
    int row = 0;
    int column = 0;
    int data;
    while(file.good())
    {
        // Obtiene el dato y lo guarda en la matriz
        getline(file, box, ',');
        
        if (column == cities)
        {
            column = 0;
            row++;
        }

        // Guarda en la posición correspondiente a la matriz:
        // cout<<stoi(box)<<" ";
        data = stoi(box);
        roads[row][column] = data;
        if (data != 0)
            visibilityRoads[row][column] = (1 / double(data));
        else
            visibilityRoads[row][column] = 0;
        column++;

        if (row == cities-1 && column == cities-1)
        {
            roads[cities-1][cities-1] = 0;
            visibilityRoads[cities-1][cities-1] = 0;
            break;
        }
    }

    // Inicializa todos los datos de feromonas:
    for (row = 0; row < cities; row++)
	{
		for(column = 0; column < cities; column++)
		{
			roadsPheromone[row][column] = defaultPheromone;
		}
	}
}