#include <stdio.h>
#include "array.lib.c"

int main() {
    FILE *f = fopen("ege9.144.txt", "r");
    int ax[4];
    int n = 0;

    while(freadn(f, ax, 4) == 4) {
        if(min(ax, 4) < 1 || max(ax, 4) > 8) continue;

        int ad[] = {ax[0] - ax[2], ax[1] - ax[3]};
        if(sumsqr(ad, 2) == 5) { 
            n++;
        }
    }
    printf("%d\n", n);
}
