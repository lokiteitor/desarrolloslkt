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
 * File:   Window.h
 * Author: David Delgado Hernandez 150205@upslp.edu.mx
 *
 * Created on 21 de julio de 2017, 01:56 PM
 */

#include <SDL2/SDL.h>

#ifndef WINDOW_H
#define WINDOW_H

class Window
{
    public:
        Window();
        ~Window();
        void clearWindow();
        void update();
        SDL_Renderer * getRender();
        static const int HEIGHT = 1200;
        static const int WIDTH = 800;
    protected:

    private:
        // dimensiones de la pantalla

        // ventana y superficie
        SDL_Window *gWindow = NULL;
        SDL_Renderer *wrenderer = NULL;

};



#endif /* WINDOW_H */
