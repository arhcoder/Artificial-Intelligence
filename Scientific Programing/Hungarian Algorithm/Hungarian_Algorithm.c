#include <stdio.h>
#include <conio.h>
#define max 50

// DESARROLLADORES:

//		RAMOS HERRERA IVAN ALEJANDRO | @arhcoder.
//  	HERNANDEZ MAGALLANES JORGE ANTONIO.

// DESCRIPCIÓN:
/*
	ALGORITMO HÚNGARO: USADO PARA MINIMIZAR LOS COSTOS DE OPTIMIZACIÓN
	ANTE UN PROBLEMA EN EL QUE SE TIENEN X CANTIDAD DE TAREAS A REALIZAR
	Y X CANTIDAD DE TRABAJADORES CON UN COSTO PARA PODER REALIZARLAS.
	
	EL ALGORITMO ENCUENTRA; A PARTIR DE UNA TABLA EN LA QUE SE PLASMAN LOS
	DATOS ANTERIORMENTE MENCIONADOS, EL COSTE MÍNIMO AJUSTADO A LA COMBINACIÓN
	MÁS ÓPTIMA DE REPARTIR DICHAS X TAREAS ENTRE LOS DICHOS X TRABAJADORES.
*/

int nCl,nRe,size,dife,auv,numCruces;
int matCos[max][max];
//int aux[max][max]; //VALORES PARA SUMA
int matCosAux[max][max];
int cost[max][max];
int flag[max][max];
//AUXILIARES DE CRUCES
int rengC[max];
int colC[max];

int cross[max][max];
int RengZ[max];
int ColZ[max];

int valMenorRen[max];
int valMenorCo[max];

void priline();
int regMatriz();
int printMat();
int redux();

int main(){

	// Activa el paquete de códigos de Windows para tener tildes en consola.
	system("chcp 65001");
	system("cls");

	int opc;
	while(opc!=2){
		printf("\t\tCÁLCULOS DE MATRIZ POR ALGORITMO HUNGARIANO");
		priline();
		printf("\t\t\tMENU\n");
		printf("1: REGISTRAR MATRIZ Y APLICAR ALGORITMO\n2: SALIR\n");
		scanf("%d",&opc);
		switch(opc){
			case 1:
				regMatriz();
				printf("\nCÁLCULOS DE MATRIZ POR ALGORITMO HUNGARIANO");
				priline();
				printMat();
				getTaman();
				break;
			case 2:
				system("cls");
				printf("\n\n\t\t\t\tGRACIAS POR UTILIZAR NUESTRO PROGRAMA\n \t\t\t\t   DERECHOS RESERVADOS 2021 MMXXI\n");
				break;
		}
	}
	return 0;
}

int redux(){
	int i,j,numCruces=0;;
	for(i=0; i<size; i++){
		for(j=0; j<size; j++){
		matCosAux[i][j]=matCos[i][j];
			if(matCos[i][j]==0){
				RengZ[i]=RengZ[i]+1;
			}
			//aux[i][j]=matCos[i][j];
		}
	}
	
	int auxSize=size;
	
	if((size%2)>0){
		auv=(size+1)/2;
	}else{
		auv=size/2;
	}
	
	while(auxSize>=auv){
		for(i=0; i<size; i++){
			if(RengZ[i]==auxSize){
				for(j=0;j<size;j++){
					matCos[i][j]=-1;
					cross[i][j]=cross[i][j]+1;
				}
			}
		}
		auxSize--;
	}
	
	
	for(j=0; j<size; j++){
		for(i=0; i<size; i++){
			if(matCos[i][j]==0){
				ColZ[j]=ColZ[j]+1;
			}
		}
	}
	
	for(j=0;j<size;j++){
        if(ColZ[j]>=1){
            for(i=0;i<size;i++){
                matCos[i][j]=-1;
                cross[i][j]=cross[i][j]+1;
            }
        }
    }
	/*
	int rengC[i];
	int colC[i];*/
	
	for(i=0;i<size;i++){
		for(j=0;j<size;j++){
			if(matCos[i][j]==-1){
				rengC[i]=rengC[i]+1;
			}
			
			if(matCos[j][i]==-1){
				colC[i]=colC[i]+1;
			}
		}
	}
	
	
	
	for(i=0;i<size;i++){
		if(rengC[i]==size){
			numCruces+=1;
		}
	}
	
	if(numCruces!=size){
		for(i=0;i<size;i++){
			if(colC[i]==size){
				numCruces+=1;
			}
		}
	}
	
	
	
    printf("MATRIZ DE INTERSECCIONES");
    priline();
    
	for(i=0;i<size;i++){
		for(j=0;j<size;j++){
			cross[i][j]=cross[i][j]-1;
			printf("\t[%d]\t",cross[i][j]);
		}
		printf("\n");
	}
	
	
	int costoTotal=0,k;
	priline();
	printf("NÚMERO DE CRUCES %d \n",numCruces);
	if(numCruces==size){
		for(i=0; i<size; i++){
			for(j=0; j<size; j++){
				if((matCosAux[j][i]==0)&&(flag[j][i]==0)){
					printf("TAREA %d ASIGNADA A : %d \n", i+1,j+1);
					costoTotal=costoTotal+cost[j][i];
					for(k=0;k<size;k++){
						flag[j][k]=1;
					}
				}
			}
		}
		printf("COSTO TOTAL: %d",costoTotal);
	}
	
	if(numCruces!=size){
		printf("NUEVA MATRIZ FINAL REDUCIDA");
		priline();
		for(i=0;i<size;i++){
			for(j=0;j<size;j++){
				matCosAux[i][j]=(matCosAux[i][j]+cross[i][j]);
				printf("\t[%d]\t",matCosAux[i][j]);
				
			}
			printf("\n");
		}
		priline();
		int contador=0;
		costoTotal=0;
		for(i=0; i<size; i++){
			for(j=0; j<size; j++){
				if((matCosAux[j][i]==0)&&(flag[j][i]==0)){
					contador=contador+1;
					for(k=0;k<size;k++){
						flag[j][k]=1;
					}
					costoTotal=costoTotal+cost[contador-1][j];
					printf("TAREA %d ASIGNADA A : %d \n",contador,j+1);
				}
			}
		}
		printf("COSTO TOTAL: %d",costoTotal);
		priline();
	}
	
}


int getTaman(){
	int contador,i,j;
	//MENOR POR FILA
	priline();
	printf("MATRIZ MINIMO POR RENGLÓN\n");
	priline();
	for(i=0; i<nRe; i++){
	int menor = matCos[i][i];
		for(j=0; j<nCl; j++){
			int elem = matCos[i][j];
			if(elem<menor) menor = elem;
			valMenorRen[i] = menor;
		}
	}
	
	for(i=0; i<nRe; i++){
		for(j=0; j<nCl; j++){
			matCos[i][j]-=valMenorRen[i];
		}
	}
	printMat();
	
	priline();
	printf("MATRIZ MINIMO POR COLUMNA Y MATRIZ REDUCIDA");
	priline();
	
	//int valMenorCol[20];
	//MENOR POR COLUMNA

	int aux=0;
	int menor1;
	
	for(i=0;i<nCl;i++){
		int menor = matCos[0][i];
		for(j=0; j<nRe; j++){
			int elem = matCos[j][i];
			if(elem<menor) menor = elem;
		}
		valMenorCo[i]=menor;
	}
	
	
	aux=0;
	while(aux<nCl){
		for(i=0; i<nCl; i++){
			matCos[i][aux]-=valMenorCo[aux];
		}
		aux++;
	}
	
		
	printMat();
	priline();
	
	int r=nRe, c=nCl;
	
	if(r!=c){
		if(r>c){
			dife=r-c;
			while(dife!=0){
				c++; dife--;
			}
		}
		
		if(r<c){
			dife=r-c;
			while(dife!=0){
				r++; dife--;
			}
		}
	}
	
	if(r=c){
		size=r;
	}
	
	redux();
}

int regMatriz(){
	int i,j;
	printf("\t\tREGISTRO DEL TAMAÑO DE LA MATRIZ");
	priline();
	
	printf("INGRESE EL NÚMERO DE RENGLONES DE LA MATRIZ\n");
	scanf("%d",&nRe);
	printf("INGRESE EL NÚMERO DE COLUMNAS DE LA MATRIZ\n");
	scanf("%d",&nCl);
	
	for(i=0; i<nRe; i++){
		system("cls");
		printf("\t\tREGISTRO DEL TAMAÑO DE LA MATRIZ");
		priline();
		for(j=0; j<nCl; j++){
			printf("REGISTRE VALOR DE LA POSICIÓN [%i][%i] ",i+1,j+1);
			scanf("%d",&matCos[i][j]);
			flag[i][j]=0;
			cost[i][j]=matCos[i][j];
		}
	}
	system("cls");
}

void priline()
{
	printf("\n-------------------------------------------------------------\n");
}

int printMat(){
	int i,j;
	for(i=0; i<nRe; i++){
		printf("\n");
		for(j=0; j<nCl; j++){
			printf("\t[%i]\t",matCos[i][j]);
		}
	}
}