#include <stdio.h>
#include "array.lib.c"

#define DMAX 1000
#define N 5

int abs(int x) {
    return (x > 0) ? x : -x;
}

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

void div(int *d, long *pn, int x) {
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

int nmax;
void maxEvenOdd(int *pemax, int *pomax, int x) {
    int d[DMAX];
    long n;
    div(d, &n, x);
//    print(d, n);

    if(n > nmax) {
        nmax = n;
    }

    *pemax = 0;
    *pomax = 0;
    for(int i = 0; i < n; i++) {
        int di = d[i];
        if(di % 2 == 0) {
            if(di > *pemax) {
                *pemax = di;   
            }

        } else {
            if(di > *pomax) {
                *pomax = di;
            }
        }
    }
}

int A(int x) {
    int emax, omax;
    maxEvenOdd(&emax, &omax, x);

    if(emax && omax) {
        return abs(emax - omax);
    } else {
        return 0;
    }
}


int main() {
    int n = 0;
    int i = 250156;

    while(n < N) {
        i++;

        int a = A(i);

        if(factor(a) == a && a % 10 == 9) {
            printf("%d %d\n", i, a);
            n++;
        }
    }

//    printf("%d\n", nmax);
}
