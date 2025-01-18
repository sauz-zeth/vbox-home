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
            int x = a[i];
            b[i] = count(a, N, x);

            if(b[i] == 1) {
                c[i] = a[i];
            }
            else {
                c[i] = 0;
            }

        }

        if(count(b, N, 1) != R1) continue;

        int SnoRep = sum(c, N);
        int Srep = sum(a, N) - SnoRep;
        float AvgNoRep = (float) SnoRep / R1;

        if(AvgNoRep <= Srep) n++;
        
    }
    printf("%d\n", n);
}
