#include <vector>
#include <random>
#include <time.h>
#include <math.h>
#include <algorithm>

#include "tsp.hpp"

using namespace std;

void printLine()
{
    cout<<"\n\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n";
}

void ACOTSP::ANTS()
{
    // Crea un vector de vectores para guardar los caminos de las hormigas;
    // Cada vector de este vector corresponder a una hormiga y su ruta:
    int ant, step, city, i, j;
    // vector<double> pathsProbability = {};
    srand(time(NULL));
    int firstCity;
    for (i = 1; i <= antsAmount; i++)
    {
        // Coloca la hormiga en una ciudad aleatoria:
        firstCity = rand() % (cities);
        vector<int> path = {};
        path.push_back(firstCity);
        for (int x = 0; x < cities; x++)
            path.push_back(-1);
        paths.push_back(path);
    }

    // Para cada hormiga, se sigue el camino:
    vector<double> fitness;
    for (ant = 0; ant < antsAmount; ant++)
    {
        fitness.push_back(0);
    }
    for (ant = 0; ant < antsAmount; ant++)
    {
        // cout<<"HORMIGA "<<ant+1<<endl;
        // pathsProbability.clear();
        // Da un paso para cada hormiga:
        vector<int> transitedCities = {};
        transitedCities.clear();
        transitedCities.push_back(firstCity);

        // Crea una lista con los caminos disponibles,
        // para ignorarlos al tratar de caminar sobre ellos:
        vector<int> disponibles = {};
        disponibles.clear();
        for (city = 0; city < cities; city++)
        {
            disponibles.push_back(city);
        }

        srand(time(NULL));
        for (step = 0; step < cities-1; step++)
        {
            // cout<<"PASO "<<step+1<<endl;
            // Se encuentran las probabilidades para todos los
            // los caminos que puede tomar:
            //* Calcula la sumatoria de probabilidades del denominador
            //* de la fórmula de probabilidad de algoritmo de hormigas:
            //* <INSERTE FÓRMULA AQUÍ>;
            // Encuentra el cociente con todos los caminos:
            double sum = 0;
            double pheromone, visibility, numerator, probability;
            int actualCity = paths[ant][step];
            disponibles.erase(remove(disponibles.begin(), disponibles.end(), actualCity), disponibles.end());
            transitedCities.push_back(actualCity);
            // cout<<"Actual: "<<actualCity<<endl;
            vector<double> pathsProbability = {};
            pathsProbability.clear();
            for (city = 0; city < cities; city++)
            {
                if (std::find(transitedCities.begin(), transitedCities.end(), city) == transitedCities.end())
                {
                    // a++;
                    pheromone = roadsPheromone[actualCity][city];
                    visibility = visibilityRoads[actualCity][city];
                    sum += (pow(pheromone, pheromoneImportance)*(pow(visibility, visibilityImportance)));
                    // cout<<"a";
                }
                // cout<<"a: "<<a<<endl;
            }
            // cout<<sum<<endl;
            
            // Encuentra la probabilidad para cada camino:
            for (int path = 0; path < cities; path++)
            {
                if (std::find(transitedCities.begin(), transitedCities.end(), path) == transitedCities.end())
                {
                    // cout<<"a";
                    pheromone = roadsPheromone[path][actualCity];
                    visibility = visibilityRoads[path][actualCity];
                    numerator = (pow(pheromone, pheromoneImportance)*(pow(visibility, visibilityImportance)));
                    probability = numerator / sum;
                    pathsProbability.push_back(probability);
                }
            }
            // cout<<"Actual:"<<actualCity<<"; Incial: "<<firstCity<<"; ";
            // cout<<probability<<"Con "<<disponibles.size()<<endl;
            double suma = 0;
            for (int ix = 0; ix < pathsProbability.size(); ix++)
            {
                // cout<<"["<<pathsProbability[ix]<<"]";
                suma += pathsProbability[ix];
            }

            if (suma == 0 || pathsProbability.size() == 0)
            {
                break;
            }

            // cout<<"SUMA:"<<suma<<endl;

            // Decide qué camino tomar:
            // Calcula un aleatorio entre 0 y 1; y en base a la sumatoria
            // de caminos con base en la probabilidad de cada uno; se queda
            // con uno de estos caminos (que suman 1 de probabilidad):
            double random = ((double) rand() / (RAND_MAX));
            // cout<<endl<<random<<endl;
            sum = 0;
            int nextCity = actualCity;
            // Se asegura de que la siguiente ciudad no sea la actual:
            // vector<int> availableCities = {};
            /*for (city = 0; city < cities; city++)
            {
                // Si la ciudad ya fue transitada, no la toma:
                if (std::find(transitedCities.begin(), transitedCities.end(), city) == transitedCities.end())
                {
                    availableCities.push_back(city);
                    // cout<<city<<" -> ";
                }
            }*/
            // cout<<endl;

            double nextPoint = 0;
            while (nextCity == actualCity)
            {
                sum = 0;
                for (city = 0; city < disponibles.size(); city++)
                {
                    // Si tiene que pasar por una ciudad por la que no ha transitado:
                    // if (std::find(transitedCities.begin(), transitedCities.end(), city) != transitedCities.end())
                    // {
                    //     break;
                    // }
                    // Si el aleatorio está en el rango permitido de este camino:
                    nextPoint = sum + pathsProbability[city];
                    // cout<<"if "<<random<<"    >=    ("<<sum<<")    &&    "<<random<<"    <    ("<<nextPoint<<")"<<endl;
                    if (double(random) >= double(sum) && double(random) < double(sum + pathsProbability[city]))
                    {
                        // Encontró el próximo camino:
                        // cout<<"Próxima ciudad: "<<availableCities[city]<<endl;
                        nextCity = disponibles[city];

                        // Agrega la ciudad a la lista de las transitadas:
                        transitedCities.push_back(nextCity);
                        break;
                    }
                    // Probabilidad acumulada de los caminos:
                    sum += pathsProbability[city];
                }
            }
            
            paths[ant][step+1] = nextCity;
            fitness[ant] += roads[actualCity][nextCity];
            // cout<<"["<<paths[ant][step+1]<<"]";
            // pathsProbability.clear();*/

            // When is the last step, it complete the road going to the starting city:
            if (step == cities-2)
            {
                // cout<<nextCity<<";"<<endl;
                fitness[ant] += roads[nextCity][firstCity];
            }
        }
        // cout<<"\n";
        // pathsProbability.clear();
    }

    // Encuentra la mejor solución y la respalda:
    bestPath = {};
    bestPath.clear();
    /* if (bestFitness == null)
    {
        bestFitness = fitness[0];
    }*/
    int bestAnt = 0;
    for (ant = 0; ant < antsAmount; ant++)
    {
        // cout<<"if ("<<fitness[ant]<<" < "<<bestFitness<<")"<<endl;
        if (fitness[ant] < bestFitness)
        {
            bestFitness = fitness[ant];
            bestAnt = ant;
        }
    }
    for (city = 0; city < cities; city++)
    {
        bestPath.push_back(paths[bestAnt][city]);
    }

    for (ant = 0; ant < antsAmount; ant++)
    {
        cout<<"\nHormiga "<<ant+1<<" ["<<fitness[ant]<<"km]:"<<endl;
        for (city = 0; city < cities; city++)
        {
            cout<<""<<paths[ant][city]<<" => ";
        }
        cout<<""<<paths[ant][0]<<";"<<endl;
    }
    printLine();
    cout<<"Mejor camino ["<<bestFitness<<"km]:"<<endl;
    for (city = 0; city < cities; city++)
    {
        cout<<""<<bestPath[city]<<" => ";
    }
    cout<<""<<bestPath[0]<<";";
    printLine();

    // Actualiza la feromona:
    //* Para cada tramo recorrido, se agrega la feromona correspondiente
    //* al camino de las hormigas, basados en la fórmula:
    //? <INSERTE FÓRMULA AQUÍ>:
    // Evapora la feromona:
    for (i = 0; i < cities; i++)
    {
        for (j = 0; j < cities; j++)
        {
            roadsPheromone[i][j] *= (1 - pheromoneEvaporation);
        }
    }
    // Deposita la feromona:
    double pheromona = 0;
    // cout<<"a";
    for (ant = 0; ant < antsAmount; ant++)
    {
        // Feromona depositada:
        pheromona = double(double(pheromoneStep) / double(fitness[ant]));
        // cout<<"b";
        // cout<<"\n";
        for (city = 0; city < cities; city++)
        {
            // cout<<"c";
            // El último tramo:
            if (city == cities - 1)
            {
                // cout<<"d";
                // cout<<"Hormiga "<<ant<<"; ["<<paths[ant][city]<<"]-["<<paths[ant][0]<<"] += "<<pheromona<<endl;
                roadsPheromone[paths[ant][city]][paths[ant][0]] += pheromona;
                roadsPheromone[paths[ant][0]][paths[ant][city]] += pheromona;
            }
            else
            {
                // cout<<"e";
                // cout<<"Hormiga "<<ant<<"; ["<<paths[ant][city]<<"]-["<<paths[ant][city+1]<<"] += "<<pheromona<<endl;
                roadsPheromone[paths[ant][city]][paths[ant][city+1]] += pheromona;
                roadsPheromone[paths[ant][city+1]][paths[ant][city]] += pheromona;
            }
        }
    }
    // ShowPheromones();
}

void ACOTSP::Simulate()
{
    srand(time(NULL));
    bestFitness = 1000000000;
    for (int iteration = 1; iteration <= iterations; iteration++)
    {
        printLine();
        cout<<"INTERACION "<<iteration<<" DE "<<iterations;
        printLine();
        srand(time(NULL));
        ACOTSP::ANTS();
        // ACOTSP::ShowPheromones();
    }
}