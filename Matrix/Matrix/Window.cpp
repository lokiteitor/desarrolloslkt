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
 * File:   Window.cpp
 * Author: David Delgado Hernandez 150205@upslp.edu.mx
 * 
 * Created on 21 de julio de 2017, 01:56 PM
 */

#include "Window.h"
#include <stdio.h>
#include <SDL2//SDL.h>


Window::Window()
{
    //ctor
    if(SDL_Init(SDL_INIT_VIDEO < 0 )){
        // ocurrio un error
        printf("SDL no pudo iniciarse error: %s",SDL_GetError());
    }
    else{
        // crear ventana
        gWindow  = SDL_CreateWindow("Sandbox",SDL_WINDOWPOS_UNDEFINED,SDL_WINDOWPOS_UNDEFINED,HEIGHT,WIDTH,SDL_WINDOW_SHOWN);
        if(gWindow == NULL){
            printf("Error al crear la ventana : %s",SDL_GetError());
        }
        else{
            // crear render
            wrenderer = SDL_CreateRenderer(gWindow,-1,SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC);
            if(wrenderer == NULL){
                printf("Error al crear el render %s",SDL_GetError());
            }

            else{
                // iniciar el color de fondo
                SDL_SetRenderDrawColor(wrenderer,0,0,0,0);
            }
        }
    }
}

Window::~Window()
{
    //dtor
    // Destruir la ventana y liberar recursos
    SDL_DestroyRenderer(wrenderer);
    SDL_DestroyWindow(gWindow);
    wrenderer = NULL;
    gWindow = NULL;
    SDL_Quit();
}

void Window::clearWindow(){
    SDL_SetRenderDrawColor(wrenderer,0,0,0,0);
    SDL_RenderClear(wrenderer);

}

void Window::update(){
    SDL_RenderPresent(wrenderer);
}

SDL_Renderer * Window::getRender(){
    return wrenderer;
}
