#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include "SDL.h"


#ifndef HEIGHT
#define HEIGHT 800
#endif

#ifndef WIDTH
#define WIDTH 600
#endif

#ifndef BPP
#define BPP 24
#endif

char tablero[HEIGHT][WIDTH];

SDL_Surface *screen;

int state = 1;

Uint32 ini_milisegundos;


void initVideo(void)
{
    
    // inicializar los componentes de sdl
    // preguntar sobre la disponibilidad del doublebuffer

    if (SDL_Init(SDL_INIT_VIDEO | SDL_INIT_TIMER) < 0)
    {
        printf("no se pudo iniciar %s\n", SDL_GetError);
    }

    // TODO : habilitar el uso de doublebuffer en caso de encontrarse disponible
    screen = SDL_SetVideoMode(WIDTH, HEIGHT,BPP,SDL_HWSURFACE | SDL_DOUBLEBUF);

    if (screen == NULL)
    {
        printf("error al iniciar surface %s\n", SDL_GetError);
    }

    atexit(SDL_Quit);
}

void llenarTablero(void){

    srand(time(NULL));

    for (int i = 0; i < HEIGHT; ++i)
    {
        for (int x = 0; x < WIDTH; ++x)
        {
            tablero[i][x] = rand() %2; 
        }
    }
}


SDL_Rect obtenerDireccion(int x,int y){

    SDL_Rect dest;

    dest.x = x;
    dest.y = y;
    dest.w = 1;
    dest.h = 1;

    return dest;

}


void comparar(int *alrededor,int x, int aux,int y){

    // aux es x + 1 en cada ciclo sumar y comparar que no sea mayor a
    // x + 1 del original

    while (aux <= x + 1){
        if (aux > -1 && y > -1)
        {    
            if (tablero[aux][y] == 1){
                *alrededor = *alrededor + 1;
            }
        }
        aux++;

    }
}

Uint32 soporteVida(int x, int y){

    Uint32 color;

    int alrededor = 0;

    int auxX = x,auxY = y;

    // primera linea

    auxX = x -1;
    auxY = y -1;

    comparar(&alrededor,x,auxX,auxY);

    // segunda linea
    auxY = y;
    auxX = x -1;

    comparar(&alrededor,x,auxX,auxY);

    // tercera linea

    auxX = x -1;
    auxY = y + 1;

    comparar(&alrededor,x,auxX,auxY);

    
    --alrededor;
    if (alrededor > 8)
    {
        printf("alerta casillas vivas %d\n", alrededor);
    }

    if (alrededor == 3 && tablero[x][y] == 0)
    {
        // casilla viva
        tablero[x][y] = 1;
        color = SDL_MapRGB(screen->format,255,0,0);
    }
    else if ((alrededor == 3 || alrededor == 2) && tablero[x][y] == 1)
    {
        tablero[x][y] = 1;
        color = SDL_MapRGB(screen->format,255,0,0);

    }
    
    else{
        // casilla muerta
        tablero[x][y] = 0;
        color = SDL_MapRGB(screen->format,219,219,219);
    }


    return color;


}


void Display(int x,int y){
    SDL_Rect dest;

    dest = obtenerDireccion(x,y);
    SDL_FillRect(screen,&dest,soporteVida(x,y));

}

void ResetTimeBase() {
    ini_milisegundos=SDL_GetTicks();
}
int CurrentTime() {
    Uint32 fin_milisegundos=SDL_GetTicks();
    return fin_milisegundos-ini_milisegundos;
}


int main(int argc, char const *argv[])
{
    int frametime;
    llenarTablero();

    initVideo();

    while(state){
        ResetTimeBase();
        for (int i = 0; i < HEIGHT; ++i)
        {
            for (int x = 0; x < WIDTH; ++x)
            {
                // printf("%hhd\n", tablero[i][x]);
                // printf("%d  %d\n",i,x);
                Display(i,x);
            }
        }
        SDL_Flip(screen);
        do {
            frametime=CurrentTime();
        } while (frametime<30);

    }






    return 0;
}