#include <stdio.h>

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

void divMaxEvenOdd(int *pemax, int *pomax, int x) {
    *pemax = 0;
    *pomax = 0;
    int j = 2;
    while(j <= x / 2) {
        if(x % j == 0) {
            if(j % 2 == 0) {
                if(j > *pemax) {
                    *pemax = j;
                }
            } else {
                if(j > *pomax) {
                    *pomax = j;
                }
            }
        }
        j++;
    }
}

int A(int x) {
    int emax, omax;
    divMaxEvenOdd(&emax, &omax, x);

    if(emax && omax) {
        return abs(emax - omax);
    } else {
        return 0;
    }
}

#define N 5

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
}
