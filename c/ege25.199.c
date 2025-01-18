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

int D(int *d, int k, int *odd, int *o) {
    *o = 0;

    for(int i = k - 1; i >= 0; i--) {
        if(d[i] % 2 != 0) {
            odd[*o] = d[i];
            (*o)++;
        }
    }

    return *o >= 6 ? odd[5] : 0;
}

int main() {
    int n = NMIN;
    int i = 0;
    int d[DMAX];
    long k = 0;

    int odd[DMAX];
    int o = 0;

    while(i < IMAX) {
        n++;
        divs(n, d, &k);

        int e = D(d, k, odd, &o);
        
        if(e > 0) {
            printf("%d %d\n", e, o);
            i++;
        }
    }
}
