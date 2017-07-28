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
 * File:   Terrain.cpp
 * Author: David Delgado Hernandez 150205@upslp.edu.mx
 * 
 * Created on 21 de julio de 2017, 02:04 PM
 */

#include "Terrain.h"
#include "./lib/FastNoise.h"
#include "Window.h"
#include <math.h>
#include <stdio.h>

Terrain::Terrain(int Seed){    
    
    noise = FastNoise(Seed);
    noise.SetNoiseType(FastNoise::Perlin);   
    noise.SetFrequency(0.123);    
}

Terrain::~Terrain(){
    
}

chunk Terrain::getChunk(){
    chunk terrain;
    int xpos = 0;
    int ypos = 0;   
    
    for (int i = 0; i < Window::WIDTH; i++) {
        
        for (int x = 0; x < Window::HEIGHT; x++) {
            terrain.matriz[i][x] = noise.GetPerlin(i,x);            
        }
    }    
    return terrain;
}