#include <stdio.h>
#include "array.lib.c"

int main() {
    FILE *f = fopen("ege9.99.txt", "r");
    int ax[3];
    int m;
    int smax = 0;
    int s;

    while(freadn(f, ax, 3) == 3) {
        m = max(ax, 3);
        if(sumsqr(ax, 3) == 2 * m * m) {
            s = sum(ax, 3) - m;
            if(s > smax) {
                smax = s;
            }
        }
    }

    printf("%d\n", smax);
}
