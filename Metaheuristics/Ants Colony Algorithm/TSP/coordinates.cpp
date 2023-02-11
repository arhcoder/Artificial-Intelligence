#include <iostream>
#include <fstream>
#include <cmath>
#include <cstdlib>
#include <string>

using namespace std;

void matrizAdyacencia(int tsp127[][2]);

int main()
{	
	// Abre el archivo de TSP:	
	ifstream archivo;
	archivo.open("bays127.tsp");
	
	// Variables necesarias:
	int tsp127[127][2];
	
	// Separa casilla por casilla:
	string casilla = "";
	int fila = 0;
	int columna = 0;
	
	while(archivo.good())
	{
		// Obtiene el dato y lo guarda en la matriz
		getline(archivo, casilla, ',');
		
		// Guarda en la posiciOn correspondiente a la matriz:
		//cout<<stoi(casilla)<<" ";
		tsp127[fila][columna] = stoi(casilla);
		
		columna++;
		
		if(columna==2){
			columna=0;
			fila++;
			
		}
		
		if(fila==127){
			break;
		}	
	}
	
	// Imprime la matriz:
	matrizAdyacencia(tsp127);
}


void matrizAdyacencia(int tsp127[][2])
{
	
	for (int row = 0; row < 127; row++)
	{
		for(int column = 0; column < 2; column++)
		{
			cout<<"["<<tsp127[row][column]<<"]";
		}
		cout<<endl;                         
	}
	
	printf("++++++++++++++++++++++++++++++++++\n");
	printf("++++++++++++++++++++++++++++++++++\n");
	printf("++++++++++++++++++++++++++++++++++\n");
	printf("++++++++++++++++++++++++++++++++++\n");
	
	double matrixAdy[127][127];
	double distance=0;
	
	for (int row = 0; row < 127; row++)
	{
		for(int cl1 = 0; cl1 < 127; cl1++)
		{
			distance=(sqrt((pow((tsp127[cl1][0]-tsp127[row][0]),2)+pow((tsp127[cl1][1]-tsp127[row][1]),2))));
			
			matrixAdy[row][cl1]=distance;
			matrixAdy[cl1][row]=distance;	
		}   
	}
	printf("++++++++++++++++++++++++++++++++++\n");
	printf("++++++++++++++++++++++++++++++++++\n");

	// Guarda el archivo como una matriz en un archivo nuevo .csv:
	ofstream miarchivo("tspx.csv");
	for(int row = 0; row < 127; row++)
	{
		for(int column = 0; column < 127; column++)
		{
			miarchivo<<matrixAdy[row][column]<<",";
		}
		miarchivo<<endl;
	}
	miarchivo.close();
}