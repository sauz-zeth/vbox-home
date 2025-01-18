#include <stdio.h>
#include "array.lib.c"

#define NMIN 200000000
#define IMAX 5
#define DMAX 10000


void divsOdd(int x, int *d, long *pn) {
    int j = 2;
    *pn = 0;
    int d1[DMAX];
    int n1 = 0;

    while(j * j < x) {
        if(x % j == 0) {
            if(j % 2 != 0) {
                d[(*pn)++] = j;
            }

            int j1 = x / j;
            if(j1 % 2 != 0) {
                d1[n1++] = x / j;
            }
        }

        j++;
    }

    if(j * j == x) {
        if(j % 2 != 0) {
            d[(*pn)++] = j;
        }
    }

    reverse(d1, n1);
    extend(d, pn, d1, n1);
}


int D(int *d, long k) {
    return k >= 6 ? d[k - 6] : 0;
}

int main() {
    int n = NMIN;
    int i = 0;
    int d[DMAX];
    long k = 0;


    while(i < IMAX) {
        n++;
        divsOdd(n, d, &k);

        int e = D(d, k);
        
        if(e > 0) {
            printf("%d %ld\n", e, k);
            i++;
        }
    }
}
