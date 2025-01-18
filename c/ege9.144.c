#include <stdio.h>
#include "array.lib.c"

int sqr(int a) {
    return a * a;
}

int main() {
    FILE *f = fopen("ege9.144.txt", "r");
    int ax[4];
    int n = 0;

    while(freadn(f, ax, 4) == 4) {
        if(sqr(ax[0] - ax[2]) + sqr(ax[1] - ax[3]) == 5 && 
        ax[0] >= 1 && ax[1] >= 1 && ax[2] >= 1 && ax[3] >= 1 &&
        ax[0] <= 8 && ax[1] <= 8 && ax[2] <= 8 && ax[3] <= 8 &&
        ax[3] - ax[1] != 0 && ax[2] - ax[0] != 0) {
            n++;
        }
    }
    printf("%d\n", n);
}
