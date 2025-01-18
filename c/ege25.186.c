#include <stdio.h>
#include "array.lib.c"

#define DMAX 10000
#define NMIN 500000000
#define IMAX 5

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

long P(int *d, int k) {
    return k < 5 ? 0 : prod(d, 5); 
     
}

int main() {
    int n = NMIN;
    int i = 0;
    int d[DMAX];
    long k = 0;

    while(i < IMAX) {
        n++;
        divs(n, d, &k);

        long p = P(d, k);
        int pdmax = p == 0 ? 0 : d[4];
        if(p <= n && p % 100 == 91) {
            printf("%ld %d\n", p, pdmax);
            i++;
        }
    }
}
