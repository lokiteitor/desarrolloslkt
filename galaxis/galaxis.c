#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#ifndef TAM
#define TAM 10
#endif

#ifndef UNIDADES
#define UNIDADES 9
#endif


char tplayer[24],tcpu[24];

char tablero[TAM];


void fijarpunto(char coo[],char flag){
    
    int tipe = (flag)?time(NULL):time(NULL)*2;
    srand(tipe);

    for (int i = 0; i < UNIDADES; ++i)
    {
        coo[i] = rand() % UNIDADES +1;
    }
}

char fijarDireccion(void){
    srand(time(NULL));

    num = rand() % 4 +1;

    return num
}
void vaciarTablero(void){
    /*llenar la matriz de espacios vacios*/





}

void llenarTarget(char tablero[]){
    // A = numeros = columnas , B = letras = filas
    char coordenadaA[UNIDADES],coordenadaB[UNIDADES],;
    char direccion;
    // 5 portaviones,3buques,1 lanchas ; total 9 elementos
    char espacios[] = {5,5,3,3,3,1,1,1,1,1}

    // llenar el array con el primer elemento de la coordenada
    fijarpunto(coordenadaB,0);
    fijarpunto(coordenadaA,1);

    // fijar direccion 

    for (int i = 0; i < UNIDADES; ++i)
    {
        direccion = fijarDireccion();
        // comprobar que la direccion esta vacia tantos espacios se necesitan
        



    }



    //convertir la segunda lista en letras
    for (int i = 0; i < UNIDADES; ++i)
    {
        coordenadaB[i] = coordenadaB[i] | (1 << 6);
        printf("%hhd\n",coordenadaB[i] );
    }
    printf("\n");

}

int main(int argc, char const *argv[])
{
    llenarTarget();
    return 0;
}
