#include <iostream>
#include <MyBytesStack.h>
#include <MyBytesQueue.h>
using namespace std;

#define MAXDIGITS 10

/*
    ╔═════════════════════════════════════════════╗
    ║  CONVERSOR DE NÚMEROS; DE SISTEMA DECIMAL   ║
    ║  A CUALQUIERA SISTEMA DE BASE [2 a 9].      ║
    ╚═════════════════════════════════════════════╝
    ╔═════════════════════════════════════════════╗
    ║  Escrito por Alejandro Ramos @arhcoder.     ║
    ╚═════════════════════════════════════════════╝
    ╔═════════════════════════════════════════════╗
    ║  Fecha: Febrero 12, 2022.                   ║
    ╚═════════════════════════════════════════════╝
*/

void decimalToBase(double decimal, int base)
{
    /// Recibe un número en base decimal [double];
    /// Recibe una base numérica para convertir [int];
    /// Convierte el número decimal a la base numérica
    /// especificada y lo imprime en pantalla.

    /// NOTA: Actualmente la función sólo almacena e
    /// imprime el número convertido, sin embargo,
    /// sería conveniente retornarlo junto a la
    /// función, ya sea como string, o como double.

    // Convierte la parte entera //
    // Los digitos se almacenan en una PILA //
    BytesStack integerPart = BytesStack();
    int currentInt = (int) decimal;
    int digits = 0;

    // Divisiones sucesivas //
    while(currentInt != 0 && digits < MAXDIGITS)
    {
        // Dígito entero = Parte entera decimal / base;
        integerPart.add(currentInt % base);
        currentInt = (int) currentInt / base;
        digits++;
    }

    // Imprime la PILA de dígitos enteros recogidos.
    integerPart.show();


    // Punto medio //
    cout<<".";
    digits = 0;


    // Convierte la parte fraccionaria //
    // Los digitos se almacenan en una COLA //
    BytesQueue fractionalPart = BytesQueue();

    // Toma el número en decimal y le resta la parte entera.
    double currentFraction = decimal - (int) decimal;

    // Multiplicaciones sucesivas //
    while(currentFraction != 0 && digits < MAXDIGITS)
    {
        // Dígito fraccionario = Parte fraccionaria decimal * base;
        double product = currentFraction * base;
        fractionalPart.add((int) product);
        currentFraction = product - (int) product;
        digits++;
    }

    // Imprime la COLA de dígitos fraccionarios recogidos.
    fractionalPart.show();
}

int main()
{
    /// Se habilitan acentos en consola.
    /// NOTA: SI EXISTE DIFICULTAD EN COMPILAR EN
    /// SISTEMAS DIFERENTES DE WINDOWS, BORRE LAS
    /// SIGUIENTES DOS LÍNEAS.
    system("chcp 65001");
    system("cls");

    // Definición de variables.
    double decimal = 0.0;
    int base = 2;

    // Impresión de "interfaz de usuario".
    cout<<"\n═══════════════════════════════════════════════\n\n";
    cout<<"║ CONVERSIÓN EN SISTEMAS NUMÉRICOS ║";
    cout<<"\n\n * Cantidad decimal a convertir: ";
    cin>>decimal;
    do
    {
        cout<<" * Base numérica para convertir [2 - 9]: ";
        cin>>base;
    }
    while (base < 2 || base > 9);

    // Imprime la conversión realizada.
    cout<<"\n═══════════════════════════════════════════════\n";
    cout<<"\n"<<decimal<<" decimal == ";

    // CONVERSIÓN //
    decimalToBase(decimal, base);
    cout<<" base "<<base<<"\n\n═══════════════════════════════════════════════\n\n";

    system("pause");

    return 0;
}