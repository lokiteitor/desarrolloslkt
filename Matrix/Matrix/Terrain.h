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
 * File:   Terrain.h
 * Author: David Delgado Hernandez 150205@upslp.edu.mx
 *
 * Created on 21 de julio de 2017, 02:04 PM
 */

#ifndef TERRAIN_H
#define TERRAIN_H

#include "lib/FastNoise.h"
#include "Window.h"
#include <stdlib.h>

typedef struct chunk{
    float matriz[Window::WIDTH][Window::HEIGHT];    
};


class Terrain{
public:
    Terrain(int seed);
    ~Terrain();
    chunk getChunk();
private:
    int seed;
    float yoff = 0.01;
    float xoff = 0.02;
    FastNoise noise;
};
    

#endif /* TERRAIN_H */
