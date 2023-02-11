#include "tsp.hpp"

using namespace std;

void ACOTSP::SetParameters()
{
    // Pide al usuario los parámetros para
    // ejecutar el algoritmo:
	system("cls");
    cout<<"\n\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n";
	cout<<" ALGORITMO DE COLONIA DE HORMIGAS";
	cout<<"\n Para resolucion de TSP";
    cout<<"\n\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n";
	cout<<" Para la instancia actual con "<<cities<<" ciudades";
    cout<<"\n\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n";
	cout<<endl;
	cout<<"\n* Cantidad de hormigas: ";
	cin>>antsAmount;
	cout<<"* Influencia de la fermona: ";	
	cin>>pheromoneImportance;
	cout<<"* Influencia de las visibilidad: ";
	cin>>visibilityImportance;
    cout<<"* Valor inicial de fermona: ";
	cin>>defaultPheromone;
	cout<<"* Evaporacion de fermona: ";
	cin>>pheromoneEvaporation;
	cout<<"* Rastro de feromona: ";
	cin>>pheromoneStep;
	cout<<"* Cantidad de iteraciones: ";
	cin>>iterations;
    cout<<"\n";
}