#ifndef TSP_HPP
#define TSP_HPP

#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

/// CLASE ACOTSP ///
/*
    Funciona para resolver una instancia del
    problema TPS, teniendo un archivo .csv
    o cualquiera de texto plano en el que se
    tenga la matriz de adyacencia de ciudades
    DANDO POR HECHO QUE REPRESENTAN UN GRAFO
    TOTALMENTE CONEXO de ciudades.

    Está hecho para resolver implementaciones
    con el ALGORITMO DE COLONIA DE HORMIGAS.
*/
class ACOTSP
{
    //* ATRIBUTOS *//
    public:
        //* Para al instancia del TSP:
        int cities;
        string citiesFilePath;
        int roads[200][200];
        double visibilityRoads[200][200];
        int bestSolution[200];

        //* Para los parámetros del ACO:
        double roadsPheromone[200][200];
        int antsAmount;
        int pheromoneImportance;
        int visibilityImportance;
        double defaultPheromone;
        double pheromoneEvaporation;
        double pheromoneStep;
        int iterations;

        //* Variables del algoritmo:
        vector<vector<int>> paths;
        vector<int> bestPath;
        double bestFitness;
    
    //? MÉTODOS ?//
    public:
        ACOTSP(int ncities, string instanceFile);
        void InstanceTSP();
        void ShowRoads();
        void ShowPheromones();
        void ShowVisibilities();
        void ShowPaths();
        void SetParameters();
        void ANTS();
        void Simulate();
        void ShowBest();
};

#endif