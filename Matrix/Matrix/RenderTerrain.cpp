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
 * File:   RenderTerrain.cpp
 * Author: David Delgado Hernandez 150205@upslp.edu.mx
 * 
 * Created on 21 de julio de 2017, 02:32 PM
 */

#include "RenderTerrain.h"
#include "Terrain.h"
#include "RenderTerrain.h"
#include "Window.h"
#include <stdio.h>
#include <math.h>

RenderTerrain::RenderTerrain(chunk data) {
    
    // con los datos obtenidos darle un color a cada punto dependiendo de la altura
    
    // asignar la altura de 0 a -1 es azul de 0 a 1 es cafe       
    
    for (int i = 0; i < Window::WIDTH; i++) {
        for (int x = 0; x < Window::HEIGHT; x++) {
            listTexture *nodo = (listTexture*)malloc(sizeof(listTexture));
/*            
            if (data.matriz[i][x] < 0){
                nodo->color.a = 0;
                nodo->color.b = 67;
                nodo->color.g = 255;
                nodo->color.r = 0;
            }
            else{
                nodo->color.a = 2;
                nodo->color.b = 142;
                nodo->color.g = 19;
                nodo->color.r = 0;                
            }
 */
            
            nodo->color.a = (int)map(data.matriz[i][x],-1,1,0,255);
            nodo->color.b = (int)map(data.matriz[i][x],-1,1,0,255);
            nodo->color.g = (int)map(data.matriz[i][x],-1,1,0,255);
            nodo->color.r = 0;
            
            nodo->xpos = i * xoff;
            nodo->ypos = x * yoff;
            this->add(nodo);
        }        
    }   
}

RenderTerrain::~RenderTerrain(){
    listTexture *aux = head;
    listTexture *tmp = NULL;

    while(aux != NULL ){
        tmp = aux->left;
        free(aux);
        aux = tmp;
    }
    head = NULL;
    tail = NULL;
    return;    
}

void RenderTerrain::add(listTexture *texture){
    
    if (this->tail ==  NULL){
        // lista nueva
        tail = texture;
        head = texture;
        texture->left = NULL;
        texture->rigth = NULL;
        
    }else{
        texture->rigth = tail;
        texture->left = NULL;
        tail->left = texture;
        tail = texture;
    }        
}


void RenderTerrain::pop(){
    listTexture *aux;
    if (this->head != NULL){
        aux = this->head;
        this->head = this->head->left;
        this->head->rigth = NULL;
        free(aux);
    }    
}

void RenderTerrain::render(SDL_Renderer *render){
    
    listTexture *aux = head;
    
    
    while(aux != NULL){
        SDL_Rect rect;
        rect.x = aux->xpos;
        rect.y = aux->ypos;
        rect.w = xoff;
        rect.h = yoff;
        
        SDL_SetRenderDrawColor(render,aux->color.a,aux->color.b,aux->color.g,aux->color.r);
        SDL_RenderFillRect(render,&rect);
        
        aux = aux->left;
                       
    }
    
}

float RenderTerrain::map(float value,float vmin,float vmax,float rmin,float rmax){
    float result = 0;
    
    if ((vmin < vmax) && (rmin < rmax) ){
        float range = abs(vmin - vmax);
        float rrange = abs(rmin - rmax);
        
        float tick = range / rrange;
        result = (abs(vmin - value) * rrange ) / range;
               
    }
    // lanzar excepsion en caso contrario
    
    return result;
}

