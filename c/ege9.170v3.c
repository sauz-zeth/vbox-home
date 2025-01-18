#include <stdio.h>
#include "array.lib.c"

#define N 6
#define R1 4

int main() {
    FILE *f = fopen("ege9.170.txt", "r");
    int a[N];
    int c[N];
    int n = 0;

    while(freadn(f, a, N) == N) {
        for(int i = 0; i < N; i++) {
            c[i] = count(a, N, a[i]);
        }

        if(count(c, N, 1) != R1) continue;

        int sRep = 0;
        int sNoRep = 0;

        for(int i = 0; i < N; i++) {
            if(c[i] == 1) {
                sNoRep += a[i];
            } else {
                sRep += a[i]; 
            }
        }

        if(sNoRep <= sRep * 4) n++;
        
    }
    printf("%d\n", n);
}

// a  d         c            cs
// 2  2         1            0 0 1 0 0 0 0  
// 3  2 3       1 1          0 0 1 1 0 0 0
// 6  2 3 6     1 1 1        0 0 1 1 0 0 1
// 4  2 3 6 4   1 1 1 1      0 0 1 1 1 0 1
// 6  2 3 6 4   1 1 2 1      0 0 1 1 1 0 2
// 3  2 3 6 4   1 2 2 1      0 0 1 2 1 0 2
// 2  2 3 6 4   2 2 2 1      0 0 2 2 1 0 2
