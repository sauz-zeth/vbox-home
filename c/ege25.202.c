#include <stdio.h>
#include "array.lib.c"

#define NMAX 300000000
#define IMAX 5
#define IMAX2 5
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

int D(int *d, long k) {
    int i = 0;
    int dl = 0;
    for(long l = k - 1; l >= 0; l--) {
        if(unique(d[l])) {
            i++;
            if(i == IMAX2) dl = d[l];
        }
    }

    return i < 5 ? 0 : dl;
}

int main() {
    int n = NMAX;
    int i = 0;
    int d[DMAX];
    long k = 0;

    while(i < IMAX) {
        n--;
        divs(n, d, &k);

        int e = D(d, k);

        if(e > 0) {
            i++;
            printf("%d\n", e);
        }
    }
}
