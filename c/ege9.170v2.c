#include <stdio.h>
#include "array.lib.c"

#define N 6
#define R1 4

int main() {
    FILE *f = fopen("ege9.170.txt", "r");
    int a[N];
    int b[N];
    int c[N];
    int n = 0;

    while(freadn(f, a, N) == N) {
        for(int i = 0; i < N; i++) {
            b[i] = count(a, N, a[i]);
            c[i] = (b[i] == 1) ? a[i] : 0;
        }

        if(count(b, N, 1) != R1) continue;

        int sNoRep = sum(c, N);
        int sRep = sum(a, N) - sNoRep;

        if(sNoRep <= sRep * 4) n++;
        
    }
    printf("%d\n", n);
}
