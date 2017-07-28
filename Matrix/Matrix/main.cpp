/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.cpp
 * Author: David Delgado Hernandez 150205@upslp.edu.mx
 *
 * Created on 21 de julio de 2017, 01:54 PM
 */

#include <cstdlib>
#include "Window.h"
#include "Terrain.h"
#include "RenderTerrain.h"
#include <SDL2/SDL.h>
#include <time.h>

using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {
    srand(time(NULL));
    Window window = Window();
    Terrain terrain = Terrain(rand());

    // loop

    bool quit = false;

    SDL_Event e;
    
    RenderTerrain tRender = RenderTerrain(terrain.getChunk());

    while(!quit){
        // recorrer los eventos generados
        while(SDL_PollEvent(&e)){
            // si se disparo el de salida
            if (e.type == SDL_QUIT)
                quit = true;
        }

        window.clearWindow();
        
        tRender.render(window.getRender());
        window.update();
    }
    return 0;
}

