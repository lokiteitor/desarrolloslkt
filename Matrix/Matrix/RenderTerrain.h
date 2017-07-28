/*
 * Copyright (C) 2017 David Delgado Hernandez 150205@upslp.edu.mx
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

/* 
 * File:   RenderTerrain.h
 * Author: David Delgado Hernandez 150205@upslp.edu.mx
 *
 * Created on 21 de julio de 2017, 02:32 PM
 */

#ifndef RENDERTERRAIN_H
#define RENDERTERRAIN_H

#include "Terrain.h"
#include <SDL2/SDL.h>


typedef struct listTexture{
    listTexture *left;
    listTexture *rigth;
    SDL_Color color;
    int xpos;
    int ypos;
    
};



/*A partir de la informacion del terreno genera las texturas y las renderiza*/
class RenderTerrain{
public:
    RenderTerrain(chunk data);
    ~RenderTerrain();
    void render(SDL_Renderer *render);
private:
    listTexture *head = NULL;
    listTexture *tail = NULL;
    int xoff = 800/255;
    int yoff = 600/255;
    void add(listTexture *texture);
    void pop();  
    float map(float value,float vmin,float vmax,float rmin,float rmax);
    
};

#endif /* RENDERTERRAIN_H */
