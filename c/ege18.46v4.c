#include <stdio.h>
#include "array.lib.c"

#define N 1024
#define P 6

// 0 1 2 3 4 5
// a b c d e f
// b c d e f x
// c d e f x y

int main() {
    int ax[P] = {0};
    int k = 0;

    FILE *f = fopen("ege18.47.txt", "r");
    int x;
    while(fscanf(f, "%d", &x) != EOF) { 
//        print(ax, P);

        push(ax, P, x);

        for(int i = 0; i < P - 1; i++) {
            if(ax[i] == 0) continue;

            int s = ax[i] + x; 
            if(s < 1500 && s > 1000) {
                k++;
            }
        }
    }        

    printf("%d\n", k);
}

