#include <stdio.h>
#include "array.lib.c"

#define NMAX 300000000
#define IMAX 5
#define UDN 5
#define DMAX 10000
#define UNIQUE 17

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

int unique(int x) {
    int s = 0;
    int j;
    while(x > 0) {
        j = x % 10;
        s += j;
        x /= 10;
    }

    return s == UNIQUE;
    
}

void filter(int *d, long k, int *ud, int *uk) {
    *uk = 0;
    for(long l = 0; l < k; l++) {
        if(unique(d[l])) {
            ud[(*uk)++] = d[l];
        }
    }
}

int D(int *ud, long uk) {
    return uk < 5 ? 0 : ud[uk - UDN];
}

int main() {
    int n = NMAX;
    int i = 0;

    int d[DMAX];
    long k = 0;

    int ud[DMAX];
    int uk = 0;

    int ae[IMAX];
    int auk[IMAX];

    while(i < IMAX) {
        n--;
        divs(n, d, &k);
        filter(d, k, ud, &uk);

        int e = D(ud, uk);

        if(e > 0) {
            ae[i] = e;
            auk[i] = uk;
            i++;
        }
    }

    for(int l = IMAX - 1; l >= 0; l--) {
        printf("%d %d\n", ae[l], auk[l]);
    }
}
