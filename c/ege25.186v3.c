#include <stdio.h>
#include <stdlib.h>
#include "array.lib.c"

#define DMAX 10000
#define NMIN 500000000
#define IMAX 5

void divsa(int x, int **pd, long *pn) {
    int j = 2;
    *pd = malloc(DMAX * sizeof(int));
    *pn = 0;
    int d1[DMAX];
    int n1 = 0;

    while(j * j < x) {
        if(x % j == 0) {
            (*pd)[(*pn)++] = j;
            d1[n1++] = x / j;
        }

        j++;
    }

    if(j * j == x) {
        (*pd)[(*pn)++] = j;
    }

    reverse(d1, n1);
    extend(*pd, pn, d1, n1);
}

long P(int *d, int k) {
    return k < 5 ? 0 : prod(d, 5); 
     
}

int main() {
    int n = NMIN;
    int i = 0;
    int *d;
    long k = 0;

    while(i < IMAX) {
        n++;
        divsa(n, &d, &k);

        long p = P(d, k);
        int pdmax = p == 0 ? 0 : d[4];
        free(d);
        if(p <= n && p % 100 == 91) {
            printf("%ld %d\n", p, pdmax);
            i++;
        }
    }
}
