#include <stdio.h>
#include "array.lib.c"

#define NMIN 200000000
#define IMAX 5
#define DMAX 10000


void divs(int x, int *d, long *pn) {
    int j = 2;
    *pn = 0;
    int d1[DMAX];
    int n1 = 0;

    while(j * j < x) {
        if(x % j == 0) {
            d[(*pn)++] = j;
            d1[n1++] = x / j;
        }

        j++;
    }

    if(j * j == x) {
        d[(*pn)++] = j;
    }

    reverse(d1, n1);
    extend(d, pn, d1, n1);
}

void odd(int *d, long k, int *o, long *pko) {
    *pko = 0;
    for(int i = 0; i < k; i++) {
        if(d[i] % 2 != 0) {
            o[(*pko)++] = d[i];
        }
    }
}

int D(int *o, long ko) {
    return ko >= 6 ? o[ko - 6] : 0;
}

int main() {
    int n = NMIN;
    int i = 0;

    int d[DMAX];
    long k = 0;

    int o[DMAX];
    long ko = 0;

    while(i < IMAX) {
        n++;

        divs(n, d, &k);
        odd(d, k, o, &ko);
        int e = D(o, ko);
        
        if(e > 0) {
            printf("%d %ld\n", e, ko);
            i++;
        }
    }
}
