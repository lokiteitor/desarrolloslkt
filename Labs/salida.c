#include <stdio.h>
#include <time.h>

#ifndef MAXLON
#define MAXLON 100
#endif

// inservible
int main(int argc, char const *argv[])
{
    char cadena[MAXLON];
    int i=0;

    while(i < MAXLON ){
        printf("%d\n",i );


        i++;
    }
    fgets(cadena,MAXLON,stdout);
        

    for (int i = 0; i < MAXLON; ++i)
    {
        printf("%hhd\n",cadena[i] );
    }

    return 0;
}