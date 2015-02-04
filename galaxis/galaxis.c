#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#ifndef TAM
#define TAM 110
#endif

#ifndef UNIDADES
#define UNIDADES 9
#endif

// contiene las coordenadas de cada una de las unidades
char tplayer[24],tcpu[24];

// contiene el tablero de cada uno de los jugadores 
char tableroplayer[TAM],tablerocpu[TAM];


void fijarpunto(char coo[]){
    
    srand(time(NULL));

    for (int i = 0; i < UNIDADES; ++i)
    {
        coo[i] = rand() % UNIDADES +1;
    }
}

char fijarDireccion(void){
    int num;
    srand(time(NULL));

    num = rand() % 4 +1;

    return num;
}

void llenarTablero(void){
    // llena el tablero a su estado inicial incluyendo los
    // saltos de linea
    char vacio = 'x';
    char contador = 0;

    for (char i = 0; i < TAM; ++i)
    {
        if (contador == 10) 
        {
            tableroplayer[i] = tablerocpu[i] = '\n';
            contador = 0;
        }
        else
        {
            tableroplayer[i] = tablerocpu[i] = vacio;
            contador++;
        }
    }

}

void revisarObjetivo(char coordenadaA,char coordenadaB){
    // coordenada A : fila Letra
    // coordenada B : columnna Numero

    // devolver 1 : objetivo encontrado
    //          0 : fallido

    // convertir numeros en letras
    if (coordenadaA >= 65 && coordenadaA <= 74)
    {
        coordenadaA = coordenadaA | (0 << 6);
    }


    if (coordenadaA > 0 && coordenadaA <= 10 && coordenadaB > 0 && coordenadaB <= 10)
    {
        char casilla = 
    }
    


}


void llenarTarget(char tablero[]){
    // A = Letras = fila , B = Numero = columnna
    char coordenadaA[UNIDADES],coordenadaB[UNIDADES];
    char direccion;
    // 5 portaviones,3buques,1 lanchas ; total 9 elementos
    char espacios[] = {5,5,3,3,3,1,1,1,1,1};

    // llenar el array con el primer elemento de la coordenada
    fijarpunto(coordenadaB);
    fijarpunto(coordenadaA);

    for (int i = 0; i < UNIDADES; ++i)
    {
        direccion = fijarDireccion();
        // comprobar que la direccion esta vacia tantos espacios se necesita

    }
}

int main(int argc, char const *argv[])
{
    llenarTablero();
    for (int i = 0; i < TAM; ++i)
    {
        printf("%c", tableroplayer[i]);
    }
}
