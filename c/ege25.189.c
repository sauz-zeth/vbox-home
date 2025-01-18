#include <stdio.h>
#include "array.lib.c"

#define DMAX 10000
#define IMIN 10000000


long factor(int x) {
    if(x < 2) return 0;

    int j = 2;
    while(j * j <= x) {
        if(x % j == 0) {
            return j;
        }
        j += (j > 2) ? 2 : 1;
    }

    return x;
}


void divs(int *d, long *pn, int x) {
    int d1[DMAX];
    int n1 = 0;

    int j = 2;
    *pn = 0;
    while(j * j < x) {
        if(x % j == 0) {
            int j1 = x / j;
            d[(*pn)++] = j;
            d1[n1++] = j1;
        }
        
        j++;
    }
    if(j * j == x) {
        d[(*pn)++] = j;
    }

    reverse(d1, n1);
    extend(d, pn, d1, n1);
}


#define C 3

int S(int x) {
    int d[DMAX];
    long n;

    divs(d, &n, x);

    return n < C ? 0 : sum(d + n - C, C);
}

#define K 5

int main() {
    int i = IMIN;
    int s = 0;
    int k = 0;

    while(k < K) {
        i++;

        int s = S(i);
        if(s == 0) continue;

        if(factor(s) == s) {
            printf("%d\n", s);
            k++;
        }
    }

}
