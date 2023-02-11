#include "tsp.hpp"

using namespace std;

void ACOTSP::ShowRoads()
{
    /// Muestra en pantalla la matriz de ciudades:
    cout<<"\nMATRIZ DE CIUDADES:\n";
    for (int row = 0; row < cities; row++)
	{
		for(int column = 0; column < cities; column++)
		{
			cout<<"["<<roads[row][column]<<"]";
		}
		cout<<endl;
	}
}

void ACOTSP::ShowPheromones()
{
    /// Muestra en pantalla la matriz de feromonas:
    cout<<"\nMATRIZ DE FEROMONAS:\n";
    for (int row = 0; row < cities; row++)
	{
		for(int column = 0; column < cities; column++)
		{
			cout<<"["<<roadsPheromone[row][column]<<"]";
		}
		cout<<endl;
	}
}

void ACOTSP::ShowVisibilities()
{
    /// Muestra en pantalla la matriz de feromonas:
    cout<<"\nMATRIZ DE VISIBILIDADES:\n";
    for (int row = 0; row < cities; row++)
	{
		for(int column = 0; column < cities; column++)
		{
			cout<<"["<<visibilityRoads[row][column]<<"]";
		}
		cout<<endl;
	}
}

void ACOTSP::ShowPaths()
{
    for (int ant = 0; ant < antsAmount; ant++)
    {
        for (int city = 0; city < cities; city++)
        {
            cout<<"["<<paths[ant][city]<<"]";
        }
        cout<<endl;
    }
}

void ACOTSP::ShowBest()
{
	cout<<"\nMejor recorrido ["<<bestFitness<<"km]:"<<endl;
    for (int city = 0; city < cities; city++)
    {
        cout<<""<<bestPath[city]<<" => ";
    }
    cout<<""<<bestPath[0]<<";\n\n";
}