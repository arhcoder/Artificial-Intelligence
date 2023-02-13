#include <stdio.h>
#include <conio.h>
#include <locale.h>
#include <stdbool.h>
#include <stdlib.h>
#define max 10

// DESARROLLADORES:

//		RAMOS HERRERA IVAN ALEJANDRO | @arhcoder.
//  	HERNANDEZ MAGALLANES JORGE ANTONIO.

// DESCRIPCIÓN:
	/*
		ALGORITMO POR MEDIO DEL REGISTRO DE UNA MATRIZ, EVALUA LAS CONEXIONES QUE PRESENTA CADA NODO, DE MANERA QUE 
		AL MOMENTO DE EXAMINARLA COMPRUEBE SI ES UN ARBOL O NO
	*/
//

int matr[max][max];
int nNodos;
bool flag1,flag2;

void reg();
void line();
void reg();
void view();
void comprobar();

int main(){
	int opc;
	do{
	setlocale(LC_CTYPE, "Spanish");
	printf("\t\t\t\tALGORITMO DE COMPROBACIÓN DE ARBOL\n");
	line();
	printf("PERMITE AL USUARIO, UNA VEZ REGISTRADO LAS CONEXIONES CON LOS NODOS, VALIDAR SI EL GRAFO ES UN ARBOL O NO\t\n");
	line();
	printf(" 1: Comprobar si el grafo es un arbol");
	printf("\n 2: Salir\n");
	scanf("%d",&opc);
	system("cls");
		switch(opc){
			case 1:
				reg();
				break;
			case 2:
				return 0;
				exit(-1);
				break;
			default: printf("\nOPCIÓN NO VALIDA");
		}
	}while(opc!=2);
	return 0;
}

void reg(){
	matr[max][max]=0;
	nNodos=0;
	do{
		line();
		printf("Registre el número de nodos (Recuerde que solo puede ingresar grafos menores a 10 nodos)\n");
		line();
		scanf("%d",&nNodos);
			if((nNodos>10)||(nNodos<1)){
				printf("\nRecuerde ingresar un grafo entre 1 y 10 nodos");
				system("pause");
				system("cls");
			}
	}while((nNodos>10)||(nNodos<1));
	
	int x,y;
	
	for(x=0;x<nNodos;x++){
		for(y=0;y<nNodos;y++){
			system("cls");
			printf("¿EXISTE UNA CONEXIÓN ENTRE EL NODO [%d] Y EL NODO [%d]?\n",x+1,y+1);
			line();
			printf("Para indicar que hay conexion presione (1), de lo contrario (0) para indicar desconexi�n\n");
			line();
			scanf("%d",&matr[x][y]);
			
			
			if(matr[y][y] == 1) {
				printf("\nEl grafo que intenta ingresar presenta un bucle\nPor lo tanto el grafo NO es arbol\n");
				system("pause");
				system("cls");
				return;
			}
		}
	}
	line();
	printf("\t\t\tMATRIZ RESULTANTE\t\n");
	line();
	
	view();
	comprobar();
	
	system("pause");
	system("cls");
} 

void comprobar(){
	int i, j;
	flag1=false;
	flag2=false;
	
	for(i=0;i<nNodos;i++){
		for(j=0; j<nNodos;j++){
			
			if(matr[i][j]==1){
				flag2=true;
				break;
			}
			
			if(matr[i][j]!=1 && matr[i][j]!=0){
				flag1=true;
				break;
			}	
		}
	}
	
	line();
	if(flag1||!flag2){
		printf("\t\nEl grafo dado NO ES un árbol\t");		
	}else{
		printf("\t\nEl grafo dado ES un árbol\t");	
	}
	
}


void view (){
	int i,j;
	
	for(i=0;i<nNodos;i++){
		for(j=0; j<nNodos;j++){
			printf("[%d]",matr[i][j]);
		}
		printf("\n");
	}
}

void line(){
	printf("--------------------------------------------------------------------------\n");
}