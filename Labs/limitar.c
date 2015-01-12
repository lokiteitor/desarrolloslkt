/*limitar la cantidad de un numero aleatorio lanzado por rand*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char const *argv[])
{
    char numero[10];
    srand(time(NULL));

    for (int i = 0; i < 10; ++i)
    {
        numero[i] = rand() % 10 +1;
    }
    for (int i = 0; i < 10; ++i)
    {
        printf("%hhd\n", numero[i]);
    }



    return 0;
}

