#include <iostream>
#include <fstream>
#include "tsp.hpp"
#include "reader.cpp"
#include "show.cpp"
#include "parameters.cpp"
#include "algorithm.cpp"
#include "tsp.cpp"

using namespace std;

int main(int argc, char const *argv[])
{
    // Ejecuta la instancia de TSP de 29 ciudades:
    ACOTSP TSP29(29, "instances/tsp29.csv");
    TSP29.SetParameters();
    TSP29.InstanceTSP();
    // TSP29.ShowRoads();
    // TSP29.ShowPheromones();
    // TSP29.ShowVisibilities();
    // TSP29.ShowPaths();
    TSP29.Simulate();
    TSP29.ShowBest();
    system("pause");
    system("cls");

    
    // Ejecuta la instancia de TSP de 127 ciudades:
    ACOTSP TSP127(127, "instances/tsp127.csv");
    TSP127.SetParameters();
    TSP127.InstanceTSP();
    // TSP127.ShowRoads();
    // TSP127.ShowPheromones();
    // TSP127.ShowVisibilities();
    // TSP127.ShowPaths();
    TSP127.Simulate();
    TSP127.ShowBest();
    system("pause");
    system("cls");

    return 0;
}